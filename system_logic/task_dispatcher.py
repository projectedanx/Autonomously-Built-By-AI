import json
import os
import shutil

class TaskDispatcher:
    """
    Handles the staggered cadence by taking compiled PRPs and creating explicit
    assignments in /delegated_tasks/ for the Worker Swarm to claim.
    """
    def __init__(self, workspace_root="."):
        self.root = workspace_root
        self.contracts_dir = os.path.join(self.root, "cognitive_contracts")
        self.tasks_dir = os.path.join(self.root, "delegated_tasks")

    def dispatch_task(self, prp_filepath, agent_role="WORKER"):
        """
        Creates a delegated task package pointing to the PRP.
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
