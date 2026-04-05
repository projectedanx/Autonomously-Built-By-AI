import os
from prp_forge import PRPForge
from task_dispatcher import TaskDispatcher
from state_manager import StateManager

def run_poc() -> None:
    """Executes a Proof of Concept (POC) run of the Sovereign workflow.

    This function simulates the role of the Sovereign Node. It reads the
    first unprocessed context file from the inbox, generates a Cognitive
    Contract (PRP) from it using the PRPForge, dispatches a task based on
    that PRP, and finally marks the context file as processed.

    Returns:
        None
    """
    manager = StateManager()
    forge = PRPForge()
    dispatcher = TaskDispatcher()

    # 1. Get unprocessed context
    unprocessed = manager.get_unprocessed_context()
    if not unprocessed:
        print("No unprocessed context found.")
        return

    # Pick the first one for the POC
    target_file = unprocessed[0]
    filename = os.path.basename(target_file)
    print(f"Processing context: {filename}")

    # 2. Extract intent and generate PRP
    raw_intent = forge.extract_intent(target_file)
    prp_data, prp_id = forge.generate_prp(raw_intent, filename)
    prp_path = forge.save_prp(prp_data, prp_id)
    print(f"Generated Cognitive Contract: {prp_path}")

    # 3. Dispatch Task
    task_path = dispatcher.dispatch_task(prp_path)
    print(f"Dispatched Task: {task_path}")

    # 4. Mark as processed
    manager.mark_context_processed(filename)
    print("Marked context as processed in StateManager.")

if __name__ == "__main__":
    run_poc()
