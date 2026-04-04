import sys
import os
from state_manager import StateManager

def main():
    manager = StateManager()
    role = manager.determine_session_role()

    print(f"--- SOVEREIGN CONTEXT ENGINEERING WORKSPACE ---")
    print(f"Session Waking Up.")
    print(f"Determined Role: {role}")
    print(f"-----------------------------------------------")

    if role == "SOVEREIGN":
        print("Executing SOVEREIGN Protocol (Session 0)...")
        unprocessed = manager.get_unprocessed_context()
        print(f"Found {len(unprocessed)} unprocessed context files.")
        print("Action required: Parse context, generate PRPs, and delegate tasks.")
        # Logic to call prp_forge.py and task_dispatcher.py will go here

    elif role == "WORKER":
        print("Executing WORKER Swarm Protocol (Session 1-N)...")
        tasks = manager.get_pending_tasks()
        print(f"Found {len(tasks)} pending tasks in /delegated_tasks/.")
        print("Action required: Claim task, execute strictly to PRP constraints, and commit artifact.")
        # Logic to claim and execute tasks will go here

    else:
        print("Workspace is IDLE. No pending tasks and no new context.")
        print("Action required: Wait for next scheduled run or ingest new context.")

if __name__ == "__main__":
    main()
