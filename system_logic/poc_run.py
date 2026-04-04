import os
from prp_forge import PRPForge
from task_dispatcher import TaskDispatcher
from state_manager import StateManager

def run_poc():
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
