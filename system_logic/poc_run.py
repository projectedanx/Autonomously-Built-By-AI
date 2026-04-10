import os
from orchestrator import Orchestrator

def run_poc() -> None:
    """Executes a Proof of Concept (POC) run of the Sovereign workflow.

    This function simulates the role of the Sovereign Node. It reads the
    first unprocessed context file from the inbox, generates a Cognitive
    Contract (PRP) from it using the PRPForge, dispatches a task based on
    that PRP, and finally marks the context file as processed.

    Returns:
        None
    """
    orchestrator = Orchestrator()

    # 1. Get unprocessed context
    unprocessed = orchestrator.manager.get_unprocessed_context()
    if not unprocessed:
        print("No unprocessed context found.")
        return

    # Pick the first one for the POC
    target_file = unprocessed[0]
    # 2-4. Process context, generate PRP, dispatch task, mark processed
    orchestrator.process_context_file(target_file)

if __name__ == "__main__":
    run_poc()
