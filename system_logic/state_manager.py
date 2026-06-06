import os
import json
import subprocess
from glob import glob
import time
import threading
import tempfile
import atexit

try:
    from system_logic.vance_indexer import VanceLSPMapper
except ImportError:
    VanceLSPMapper = None

class StateManager:
    """Manages the state and filesystem interactions for the workspace.

    This class handles the creation and access to necessary directories,
    tracks processed context files, manages pending tasks, and provides
    mechanisms for Git integration to track completed artifacts.
    """
    def __init__(self, workspace_root: str = ".") -> None:
        """Initializes the StateManager and ensures necessary directories exist.

        Args:
            workspace_root: The root directory of the workspace. Defaults to ".".
        """
        self.root = workspace_root
        self.inbox_dir = os.path.join(self.root, "context_inbox")
        self.contracts_dir = os.path.join(self.root, "cognitive_contracts")
        self.tasks_dir = os.path.join(self.root, "delegated_tasks")
        self._scars_cache = None
        self.completed_dir = os.path.join(self.root, "completed_artifacts")
        self.escrow_dir = os.path.join(self.root, "epistemic_escrow")

        # Integrate VANCE LSP Mapper if available
        self.vance_mapper = VanceLSPMapper() if VanceLSPMapper else None
        self.scar_archive_dir = os.path.join(self.root, "scar_archive")
        self.scars_file = os.path.join(self.scar_archive_dir, "scars.yaml")
        self.state_file = os.path.join(self.root, ".workspace_state.json")

        self._state = None
        self._processed_context_set = None

        # Background writer thread variables
        self._dirty = False
        self._pending_state_json = None
        self._bg_writer = None
        self._writer_lock = threading.Lock()
        self._io_lock = threading.Lock()
        self._writer_stop_event = threading.Event()
        self._write_version = 0
        self._last_written_version = 0

        self._ensure_dirs()


    def _ensure_dirs(self) -> None:
        """Creates the required workspace directories if they do not exist.

        Returns:
            None
        """
        for d in (self.inbox_dir, self.contracts_dir, self.tasks_dir, self.completed_dir, self.scar_archive_dir, self.escrow_dir):
            os.makedirs(d, exist_ok=True)

    def get_unprocessed_context(self) -> list:
        """Retrieves a list of files in the inbox that have not been processed.

        Reads the workspace state to filter out files that are already marked as processed.

        Returns:
            A list of absolute file paths to unprocessed context files.
        """
        self._load_state()
        all_files = glob(os.path.join(self.inbox_dir, "*"))
        return [f for f in all_files if os.path.basename(f) not in self._processed_context_set and not os.path.basename(f).startswith('.') and os.path.isfile(f)]

    def mark_context_processed(self, filename: str, defer_save: bool = False) -> None:
        """Marks a given context file as processed in the workspace state.

        Args:
            filename: The name of the file to mark as processed.
            defer_save: If True, updates in-memory state but defers disk write.

        Returns:
            None
        """
        state = self._load_state()
        if "processed_context" not in state:
            state["processed_context"] = []

        if filename not in self._processed_context_set:
            state["processed_context"].append(filename)
            self._processed_context_set.add(filename)
            if not defer_save:
                self._save_state(state)

    def get_pending_tasks(self) -> list:
        """Retrieves a list of pending task files.

        Returns:
            A list of file paths to pending tasks (JSON, YAML, or MD files).
        """
        all_tasks = glob(os.path.join(self.tasks_dir, "*.json")) + glob(os.path.join(self.tasks_dir, "*.yaml")) + glob(os.path.join(self.tasks_dir, "*.md"))
        return [t for t in all_tasks if os.path.isfile(t) and not t.endswith(".claimed")]

    def claim_task(self, task_file: str) -> tuple[str, str]:
        """Atomically claims a task file and returns its content.

        Uses os.rename to prevent race conditions among concurrent workers.

        Args:
            task_file: The path to the task file to claim.

        Returns:
            A tuple containing the raw string content of the task file and the new claimed path.

        Raises:
            FileNotFoundError: If the task has already been claimed by another worker.
        """
        claimed_file = task_file + ".claimed"
        try:
            os.rename(task_file, claimed_file)
        except OSError:
            raise FileNotFoundError(f"Task {task_file} already claimed or does not exist.")

        with open(claimed_file, 'r') as f:
            content = f.read()
        return content, claimed_file

    def complete_task(self, task_file: str, artifact_content: str, artifact_name: str, commit: bool = True) -> None:
        # Notify VANCE of artifact change (Mock LSP update)
        if self.vance_mapper:
            mock_payload = {
                "jsonrpc": "2.0",
                "method": "textDocument/didChange",
                "params": {
                    "textDocument": {
                        "uri": f"file://{self.root}/completed_artifacts/{artifact_name}",
                        "version": int(time.time())
                    },
                    "contentChanges": [{"text": artifact_content}]
                }
            }
            self.vance_mapper.handle_did_change(mock_payload)

        """Saves a completed artifact, removes the task file, and commits the change.

        Args:
            task_file: The path to the completed task file, which will be removed.
            artifact_content: The generated content to save as the final artifact.
            artifact_name: The filename to use when saving the artifact.

        Returns:
            None
        """
        # Ensure artifact_name is just a filename to prevent path traversal
        safe_artifact_name = os.path.basename(artifact_name)
        if not safe_artifact_name or safe_artifact_name in (os.curdir, os.pardir):
            raise ValueError(f"Invalid artifact name: {artifact_name}")
        artifact_name = safe_artifact_name
        artifact_path = os.path.join(self.completed_dir, artifact_name)
        with open(artifact_path, 'w') as f:
            f.write(artifact_content)
        os.remove(task_file)
        if commit:
            self._git_commit(f"Completed task: {os.path.basename(task_file)} -> {artifact_name}")


    def escrow_task(self, task_file: str, cfdi_score: float, conflict_reason: str, is_cipher_task: bool = False) -> str:
        """
        Halts task execution, moves the task to epistemic_escrow, creates an Escrow Ticket,
        and automatically records a Symbolic Scar.

        Args:
            task_file: Path to the claimed task file.
            cfdi_score: The calculated Confidence-Fidelity Divergence Index.
            conflict_reason: Description of the contradictory schemas/beliefs.

        Returns:
            The path to the generated Escrow Ticket.
        """
        import datetime
        import uuid

        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        ticket_id = f"ESCROW-{timestamp}-{uuid.uuid4().hex[:6].upper()}"

        # Move the task file to escrow dir
        task_filename = os.path.basename(task_file)
        escrowed_task_path = os.path.join(self.escrow_dir, f"ESCROWED_{task_filename}")

        import shutil
        shutil.move(task_file, escrowed_task_path)

        # Create Escrow Ticket
        required_action = "Human Oracle or specialized agent intervention required to resolve contradiction before resuming."
        if is_cipher_task:
            required_action = "MANDATORY_HUMAN_REVIEW: EpistemicEscrow triggered for CIPHER security audit. Do not bypass without resolving structural ambiguity."

        ticket_data = {
            "ticket_id": ticket_id,
            "status": "QUARANTINED",
            "cfdi_score": cfdi_score,
            "conflict_reason": conflict_reason,
            "original_task": escrowed_task_path,
            "required_action": required_action,
            "is_cipher_task": is_cipher_task
        }

        ticket_path = os.path.join(self.escrow_dir, f"{ticket_id}.json")
        with open(ticket_path, 'w') as f:
            json.dump(ticket_data, f, indent=2)

        # Record a Symbolic Scar
        scar_data = {
            "id": f"SCAR-{timestamp}-{uuid.uuid4().hex[:6].upper()}",
            "timestamp": timestamp,
            "type": "EPISTEMIC_ESCROW_TRIGGERED",
            "trigger": "CFDI_THRESHOLD_EXCEEDED",
            "cfdi_score": cfdi_score,
            "description": conflict_reason,
            "related_ticket": ticket_id
        }
        self.record_scar(scar_data)

        self._git_commit(f"Task Escrowed: {ticket_id} (CFDI: {cfdi_score})")
        return ticket_path

    def _start_bg_writer_if_needed(self):
        with self._writer_lock:
            if self._bg_writer is None or not self._bg_writer.is_alive():
                self._writer_stop_event.clear()
                self._bg_writer = threading.Thread(target=self._writer_loop, daemon=True)
                self._bg_writer.start()
                # Ensure we only register the atexit handler once
                if not getattr(self, '_atexit_registered', False):
                    atexit.register(self._stop_bg_writer)
                    self._atexit_registered = True

    def _writer_loop(self):
        while not self._writer_stop_event.is_set():
            if self._writer_stop_event.wait(0.1):  # Write every 0.1s if dirty
                break
            self._flush_to_disk()

    def _flush_to_disk(self):
        state_data = None
        with self._writer_lock:
            if self._dirty and self._pending_state_json is not None:
                state_data = self._pending_state_json
                self._pending_state_json = None
                self._dirty = False

        if state_data is not None:
            version, state_to_serialize = state_data

            with self._io_lock:
                if version > self._last_written_version:
                    fd, temp_path = tempfile.mkstemp(dir=os.path.dirname(self.state_file), prefix=".tmp_state_")
                    try:
                        with os.fdopen(fd, 'w') as f:
                            f.write(state_to_serialize)
                        os.replace(temp_path, self.state_file)
                        self._last_written_version = version
                    except Exception:
                        if os.path.exists(temp_path):
                            os.remove(temp_path)
                        raise

    def _stop_bg_writer(self):
        self._writer_stop_event.set()
        bg_thread = None
        with self._writer_lock:
            bg_thread = self._bg_writer

        if bg_thread and bg_thread.is_alive():
            # Join with timeout to avoid interpreter shutdown deadlocks,
            # but give it a chance to finish its current write.
            bg_thread.join(timeout=1.0)

        self._flush_to_disk()
    def _load_state(self) -> dict:
        """Loads and caches the workspace state from the state file.

        Returns:
            A dictionary containing the parsed workspace state.
        """
        if self._state is not None:
            return self._state

        if os.path.exists(self.state_file):
            with open(self.state_file, 'r') as f:
                try:
                    self._state = json.load(f)
                except json.JSONDecodeError:
                    self._state = {}
        else:
            self._state = {}

        self._processed_context_set = set(self._state.get("processed_context", []))
        return self._state

    def _save_state(self, state: dict) -> None:
        """Saves and caches the provided state dictionary.

        Args:
            state: The dictionary representing the new workspace state.

        Returns:
            None
        """
        self._state = state
        self._processed_context_set = set(self._state.get("processed_context", []))

        # Serialize synchronously to avoid thread-safety issues with dict iteration
        state_json = json.dumps(state, indent=2)

        self._start_bg_writer_if_needed()
        with self._writer_lock:
            self._write_version += 1
            self._pending_state_json = (self._write_version, state_json)
            self._dirty = True


    def save_state(self) -> None:
        """Explicitly saves the current in-memory state to disk."""
        if self._state is not None:
            state_json = json.dumps(self._state, indent=2)

            with self._writer_lock:
                self._write_version += 1
                version = self._write_version
                self._dirty = False
                self._pending_state_json = None

            with self._io_lock:
                if version > self._last_written_version:
                    fd, temp_path = tempfile.mkstemp(dir=os.path.dirname(self.state_file), prefix=".tmp_state_")
                    try:
                        with os.fdopen(fd, 'w') as f:
                            f.write(state_json)
                        os.replace(temp_path, self.state_file)
                        self._last_written_version = version
                    except Exception:
                        if os.path.exists(temp_path):
                            os.remove(temp_path)
                        raise


    def record_scar(self, scar_data: dict) -> None:
        """Records a Symbolic Scar to scars.yaml, implementing Autophagic Debridement.
        Handles CIPHER-specific scar tracking like activation_count and false_positive_count.

        Args:
            scar_data: The dictionary containing scar information (id, timestamp, etc.).
        """
        import yaml

        # Load existing scars
        if self._scars_cache is not None:
            scars = self._scars_cache
        else:
            scars = []
            if os.path.exists(self.scars_file):
                try:
                    with open(self.scars_file, 'r') as f:
                        scars = yaml.safe_load(f) or []
                except Exception:
                    scars = []
            self._scars_cache = scars

        # Initialize CIPHER-specific counters if not present
        if "activation_count" not in scar_data:
            scar_data["activation_count"] = 0
        if "false_positive_count" not in scar_data:
            scar_data["false_positive_count"] = 0

        # Extract topology for FIPI rule generation
        if scar_data.get("type") == "FALSE_NEGATIVE":
            scar_data["fipi_rule"] = f"+++PetzoldSequence: Enforce check for topology {scar_data.get('ast_topology_fingerprint', 'UNKNOWN')} in future AUDIT phases."

        # Append new scar
        scars.append(scar_data)

        # Autophagic Debridement: prune if > 40
        if len(scars) > 40:
            scars = scars[-40:]

        # Write back
        self._scars_cache = scars
        with open(self.scars_file, 'w') as f:
            yaml.dump(scars, f, default_flow_style=False, sort_keys=False)

        self._git_commit(f"Recorded scar: {scar_data.get('id', 'UNKNOWN')}")

    def _git_commit(self, message: str) -> None:
        """Commits changes to the git repository with the given message.

        Adds all tracked and untracked changes, checks if there are changes
        to commit, and commits them. Suppresses stdout/stderr from git.

        Args:
            message: The commit message to use.

        Returns:
            None
        """
        try:
            # We don't want to fail if there's nothing to commit
            subprocess.run(["git", "add", "."], check=True, cwd=self.root, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            result = subprocess.run(["git", "status", "--porcelain"], check=True, cwd=self.root, capture_output=True, text=True)
            if result.stdout.strip():
                subprocess.run(["git", "commit", "-m", message], check=True, cwd=self.root, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError as e:
            print(f"Git commit failed: {e}")

    def resolve_scar(self, ticket_id: str, resolution_text: str, sic_id: str) -> None:
        """Updates an existing scar in scars.yaml with human resolution data.

        Args:
            ticket_id: The ID of the Escrow Ticket related to the scar.
            resolution_text: The human-provided resolution directive.
            sic_id: The generated Semantic Integrity Constraint ID.
        """
        import yaml
        import os

        if self._scars_cache is not None:
            scars = self._scars_cache
        else:
            if not os.path.exists(self.scars_file):
                return
            with open(self.scars_file, 'r') as f:
                try:
                    scars = yaml.safe_load(f) or []
                except Exception:
                    return
            self._scars_cache = scars

        updated = False
        for scar in scars:
            if scar.get("related_ticket") == ticket_id:
                scar["resolution"] = resolution_text
                scar["sic_id"] = sic_id
                scar["status"] = "RESOLVED"
                updated = True
                break

        if updated:
            self._scars_cache = scars
            with open(self.scars_file, 'w') as f:
                yaml.dump(scars, f, default_flow_style=False, sort_keys=False)
            self._git_commit(f"Updated scar related to {ticket_id} with SIC {sic_id}")

    def determine_session_role(self) -> str:
        """Determines the role of the current session based on workspace state.

        If there are pending tasks, the role is WORKER. If there is unprocessed
        context but no pending tasks, the role is SOVEREIGN. Otherwise, it is IDLE.

        Returns:
            A string indicating the role: "WORKER", "SOVEREIGN", or "IDLE".
        """
        pending_tasks = self.get_pending_tasks()
        if len(pending_tasks) > 0:
            return "WORKER"

        unprocessed = self.get_unprocessed_context()
        if len(unprocessed) > 0:
            return "SOVEREIGN"

        return "IDLE"

    def reingest_artifacts(self) -> None:
        """Copies completed artifacts back into context_inbox with a REINGESTED_ prefix.

        Prevents infinite loops by not re-ingesting artifacts that already have
        the REINGESTED_ prefix, or if they have already been processed.
        """
        import shutil
        from glob import glob

        all_artifacts = glob(os.path.join(self.completed_dir, "*.md"))
        count = 0

        self._load_state()

        for artifact_path in all_artifacts:
            filename = os.path.basename(artifact_path)

            # Prevent infinite loops
            if filename.startswith("REINGESTED_"):
                continue

            new_filename = f"REINGESTED_{filename}"
            if new_filename in self._processed_context_set:
                continue

            dst = os.path.join(self.inbox_dir, new_filename)
            if not os.path.exists(dst):
                shutil.copy2(artifact_path, dst)
                count += 1

        if count > 0:
            self._git_commit(f"Re-ingested {count} artifacts into context_inbox")
