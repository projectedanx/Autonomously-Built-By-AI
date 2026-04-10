import sys
import os
import json
from state_manager import StateManager
from prp_forge import PRPForge
from task_dispatcher import TaskDispatcher
from worker_run import execute_task

def main() -> None:
    """Main entry point for the Sovereign Context Engineering Workspace orchestrator.

    Determines the current session's role (SOVEREIGN, WORKER, or IDLE) based on
    the workspace state, and executes the corresponding protocol logic.

    Returns:
        None
    """
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

        forge = PRPForge()
        dispatcher = TaskDispatcher()

        for target_file in unprocessed:
            filename = os.path.basename(target_file)
            print(f"Processing context: {filename}")

            raw_intent = forge.extract_intent(target_file)
            prp_data, prp_id = forge.generate_prp(raw_intent, filename)
            prp_path = forge.save_prp(prp_data, prp_id)
            print(f"Generated Cognitive Contract: {prp_path}")

            task_path = dispatcher.dispatch_task(prp_path)
            print(f"Dispatched Task: {task_path}")

            manager.mark_context_processed(filename)
            print("Marked context as processed in StateManager.")

    elif role == "WORKER":
        print("Executing WORKER Swarm Protocol (Session 1-N)...")
        tasks = manager.get_pending_tasks()
        print(f"Found {len(tasks)} pending tasks in /delegated_tasks/.")
        print("Action required: Claim task, execute strictly to PRP constraints, and commit artifact.")

        for target_task in tasks:
            execute_task(manager, target_task)
        print("Running artifact re-ingestion cycle...")
        manager.reingest_artifacts()

    else:
        print("Workspace is IDLE. No pending tasks and no new context.")
        print("Action required: Wait for next scheduled run or ingest new context.")

if __name__ == "__main__":
    main()
