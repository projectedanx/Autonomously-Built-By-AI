import json
import os
import shutil

class TaskDispatcher:
    """Handles the assignment of compiled PRPs to the Worker Swarm.

    This class supports the staggered execution cadence by taking compiled
    Cognitive Contracts (PRPs) and creating explicit task assignment files
    in the `/delegated_tasks/` directory, which can later be claimed by workers.
    """
    def __init__(self, workspace_root: str = ".") -> None:
        """Initializes the TaskDispatcher with the specified workspace root.

        Args:
            workspace_root: The root directory of the workspace. Defaults to ".".
        """
        self.root = workspace_root
        self.contracts_dir = os.path.join(self.root, "cognitive_contracts")
        self.tasks_dir = os.path.join(self.root, "delegated_tasks")

    def dispatch_task(self, prp_filepath: str, agent_role: str = "WORKER") -> str:
        """Creates a delegated task package pointing to a specific PRP.

        Reads the filename from the given PRP path, constructs a task payload
        with a pending status and the specified agent role, and writes it to
        a new JSON file in the delegated tasks directory.

        Args:
            prp_filepath: The absolute or relative path to the compiled PRP file.
            agent_role: The role required to execute the task. Defaults to "WORKER".

        Returns:
            The file path to the newly created delegated task JSON file.
        """
        filename = os.path.basename(prp_filepath)
        task_id = filename.replace(".json", "")

        task_payload = {
            "task_id": task_id,
            "status": "PENDING",
            "assigned_role": agent_role,
            "prp_reference": prp_filepath,
            "instructions": "Execute strictly according to the referenced Cognitive Contract (PRP)."
        }

        task_filepath = os.path.join(self.tasks_dir, f"TASK_{task_id}.json")
        with open(task_filepath, 'w') as f:
            json.dump(task_payload, f, indent=2)

        return task_filepath

if __name__ == "__main__":
    dispatcher = TaskDispatcher()
    print("TaskDispatcher initialized.")
