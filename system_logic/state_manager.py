import os
import json
import subprocess
from glob import glob

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
        self.completed_dir = os.path.join(self.root, "completed_artifacts")
        self.scar_archive_dir = os.path.join(self.root, "scar_archive")
        self.scars_file = os.path.join(self.scar_archive_dir, "scars.yaml")
        self.state_file = os.path.join(self.root, ".workspace_state.json")

        self._state = None
        self._processed_context_set = None

        self._ensure_dirs()

    def _ensure_dirs(self) -> None:
        """Creates the required workspace directories if they do not exist.

        Returns:
            None
        """
        for d in [self.inbox_dir, self.contracts_dir, self.tasks_dir, self.completed_dir, self.scar_archive_dir]:
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

    def mark_context_processed(self, filename: str) -> None:
        """Marks a given context file as processed in the workspace state.

        Args:
            filename: The name of the file to mark as processed.

        Returns:
            None
        """
        state = self._load_state()
        if "processed_context" not in state:
            state["processed_context"] = []

        if filename not in self._processed_context_set:
            state["processed_context"].append(filename)
            self._save_state(state)

    def get_pending_tasks(self) -> list:
        """Retrieves a list of pending task files.

        Returns:
            A list of file paths to pending tasks (JSON, YAML, or MD files).
        """
        all_tasks = glob(os.path.join(self.tasks_dir, "*.json")) + glob(os.path.join(self.tasks_dir, "*.yaml")) + glob(os.path.join(self.tasks_dir, "*.md"))
        return [t for t in all_tasks if os.path.isfile(t)]

    def claim_task(self, task_file: str) -> str:
        """Reads and returns the content of a task file.

        Args:
            task_file: The path to the task file to read.

        Returns:
            The raw string content of the task file.
        """
        with open(task_file, 'r') as f:
            content = f.read()
        return content

    def complete_task(self, task_file: str, artifact_content: str, artifact_name: str, commit: bool = True) -> None:
        """Saves a completed artifact, removes the task file, and commits the change.

        Args:
            task_file: The path to the completed task file, which will be removed.
            artifact_content: The generated content to save as the final artifact.
            artifact_name: The filename to use when saving the artifact.

        Returns:
            None
        """
        artifact_path = os.path.join(self.completed_dir, artifact_name)
        with open(artifact_path, 'w') as f:
            f.write(artifact_content)
        os.remove(task_file)
        if commit:
            self._git_commit(f"Completed task: {os.path.basename(task_file)} -> {artifact_name}")

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
        with open(self.state_file, 'w') as f:
            json.dump(state, f, indent=2)

    def record_scar(self, scar_data: dict) -> None:
        """Records a Symbolic Scar to scars.yaml, implementing Autophagic Debridement.

        Args:
            scar_data: The dictionary containing scar information (id, timestamp, etc.).
        """
        import yaml

        # Load existing scars
        scars = []
        if os.path.exists(self.scars_file):
            try:
                with open(self.scars_file, 'r') as f:
                    scars = yaml.safe_load(f) or []
            except Exception:
                scars = []

        # Append new scar
        scars.append(scar_data)

        # Autophagic Debridement: prune if > 40
        if len(scars) > 40:
            scars = scars[-40:]

        # Write back
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
