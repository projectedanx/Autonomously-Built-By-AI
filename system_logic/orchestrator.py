import sys
import os
import json
from system_logic.state_manager import StateManager
from system_logic.prp_forge import PRPForge
from system_logic.task_dispatcher import TaskDispatcher
from system_logic.worker_run import execute_task

class Orchestrator:
    """Core class that orchestrates the workflow components."""

    def __init__(self):
        self.manager = StateManager()
        self.forge = PRPForge()
        self.dispatcher = TaskDispatcher()

    def process_context_file(self, target_file: str) -> None:
        """Processes a single context file: generates a PRP, dispatches a task, and marks as processed."""
        filename = os.path.basename(target_file)
        print(f"Processing context: {filename}")

        raw_intent = self.forge.extract_intent(target_file)
        prp_data, prp_id = self.forge.generate_prp(raw_intent, filename)
        prp_path = self.forge.save_prp(prp_data, prp_id)
        print(f"Generated Cognitive Contract: {prp_path}")

        task_path = self.dispatcher.dispatch_task(prp_path)
        print(f"Dispatched Task: {task_path}")

        self.manager.mark_context_processed(filename)
        print("Marked context as processed in StateManager.")

def main() -> None:
    """Main entry point for the Sovereign Context Engineering Workspace orchestrator.

    Determines the current session's role (SOVEREIGN, WORKER, or IDLE) based on
    the workspace state, and executes the corresponding protocol logic.

    Returns:
        None
    """
    orchestrator = Orchestrator()
    role = orchestrator.manager.determine_session_role()

    print(f"--- SOVEREIGN CONTEXT ENGINEERING WORKSPACE ---")
    print(f"Session Waking Up.")
    print(f"Determined Role: {role}")
    print(f"-----------------------------------------------")

    if role == "SOVEREIGN":
        print("Executing SOVEREIGN Protocol (Session 0)...")
        unprocessed = orchestrator.manager.get_unprocessed_context()
        print(f"Found {len(unprocessed)} unprocessed context files.")
        print("Action required: Parse context, generate PRPs, and delegate tasks.")

        for target_file in unprocessed:
            orchestrator.process_context_file(target_file)

    elif role == "WORKER":
        print("Executing WORKER Swarm Protocol (Session 1-N)...")
        tasks = orchestrator.manager.get_pending_tasks()
        print(f"Found {len(tasks)} pending tasks in /delegated_tasks/.")
        print("Action required: Claim task, execute strictly to PRP constraints, and commit artifact.")

        for target_task in tasks:
            execute_task(orchestrator.manager, target_task)
        print("Running artifact re-ingestion cycle...")
        orchestrator.manager.reingest_artifacts()

    else:
        print("Workspace is IDLE. No pending tasks and no new context.")
        print("Action required: Wait for next scheduled run or ingest new context.")

if __name__ == "__main__":
    main()
