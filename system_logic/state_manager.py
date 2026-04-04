import os
import json
import subprocess
from glob import glob

class StateManager:
    def __init__(self, workspace_root="."):
        self.root = workspace_root
        self.inbox_dir = os.path.join(self.root, "context_inbox")
        self.contracts_dir = os.path.join(self.root, "cognitive_contracts")
        self.tasks_dir = os.path.join(self.root, "delegated_tasks")
        self.completed_dir = os.path.join(self.root, "completed_artifacts")
        self.state_file = os.path.join(self.root, ".workspace_state.json")

        self._ensure_dirs()

    def _ensure_dirs(self):
        for d in [self.inbox_dir, self.contracts_dir, self.tasks_dir, self.completed_dir]:
            os.makedirs(d, exist_ok=True)

    def get_unprocessed_context(self):
        state = self._load_state()
        processed = state.get("processed_context", [])
        all_files = glob(os.path.join(self.inbox_dir, "*"))
        return [f for f in all_files if os.path.basename(f) not in processed and not os.path.basename(f).startswith('.') and os.path.isfile(f)]

    def mark_context_processed(self, filename):
        state = self._load_state()
        if "processed_context" not in state:
            state["processed_context"] = []
        if filename not in state["processed_context"]:
            state["processed_context"].append(filename)
        self._save_state(state)

    def get_pending_tasks(self):
        all_tasks = glob(os.path.join(self.tasks_dir, "*.json")) + glob(os.path.join(self.tasks_dir, "*.yaml")) + glob(os.path.join(self.tasks_dir, "*.md"))
        return [t for t in all_tasks if os.path.isfile(t)]

    def claim_task(self, task_file):
        with open(task_file, 'r') as f:
            content = f.read()
        return content

    def complete_task(self, task_file, artifact_content, artifact_name):
        artifact_path = os.path.join(self.completed_dir, artifact_name)
        with open(artifact_path, 'w') as f:
            f.write(artifact_content)
        os.remove(task_file)
        self._git_commit(f"Completed task: {os.path.basename(task_file)} -> {artifact_name}")

    def _load_state(self):
        if os.path.exists(self.state_file):
            with open(self.state_file, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return {}
        return {}

    def _save_state(self, state):
        with open(self.state_file, 'w') as f:
            json.dump(state, f, indent=2)

    def _git_commit(self, message):
        try:
            # We don't want to fail if there's nothing to commit
            subprocess.run(["git", "add", "."], check=True, cwd=self.root, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            result = subprocess.run(["git", "status", "--porcelain"], check=True, cwd=self.root, capture_output=True, text=True)
            if result.stdout.strip():
                subprocess.run(["git", "commit", "-m", message], check=True, cwd=self.root, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError as e:
            print(f"Git commit failed: {e}")

    def determine_session_role(self):
        """
        Determines if the current session should act as a Sovereign (Planner)
        or a Worker (Executor) based on the workspace state.
        """
        pending_tasks = self.get_pending_tasks()
        if len(pending_tasks) > 0:
            return "WORKER"

        unprocessed = self.get_unprocessed_context()
        if len(unprocessed) > 0:
            return "SOVEREIGN"

        return "IDLE"
