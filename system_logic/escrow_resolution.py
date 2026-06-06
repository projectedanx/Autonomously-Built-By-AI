import json
import os
import shutil
from glob import glob
from system_logic.fipi_forge import FIPIForge
from system_logic.state_manager import StateManager

class EscrowResolver:
    """Resolves tasks that have been placed in Epistemic Escrow due to high CFDI."""
    def __init__(self, workspace_root: str = "."):
        """Initializes the EscrowResolver.

        Args:
            workspace_root (str): The root directory of the workspace. Defaults to ".".
        """
        self.root = workspace_root
        self.escrow_dir = os.path.join(self.root, "epistemic_escrow")
        self.tasks_dir = os.path.join(self.root, "delegated_tasks")
        self.contracts_dir = os.path.join(self.root, "cognitive_contracts")
        self.fipi_forge = FIPIForge(workspace_root)
        self.state_manager = StateManager(workspace_root)
        self._prp_cache = {}

    def get_pending_tickets(self):
        """Retrieves a list of pending escrow tickets.

        Returns:
            list: A list of file paths to pending escrow tickets.
        """
        return glob(os.path.join(self.escrow_dir, "ESCROW-*.json"))

    def resolve_ticket(self, ticket_path: str, human_resolution: str):
        """Resolves an escrow ticket with human input and requeues the task.

        Args:
            ticket_path (str): The path to the escrow ticket file.
            human_resolution (str): The resolution provided by the human oracle.
        """
        with open(ticket_path, 'r') as f:
            ticket_data = json.load(f)

        escrowed_task_path = ticket_data.get("original_task")
        if not escrowed_task_path or not os.path.exists(escrowed_task_path):
            print(f"Error: Original task file {escrowed_task_path} not found.")
            return

        with open(escrowed_task_path, 'r') as f:
            task_data = json.load(f)

        prp_ref = task_data.get("prp_reference")
        abs_prp_ref = os.path.realpath(os.path.join(self.root, prp_ref))

        if abs_prp_ref in self._prp_cache:
            prp_data = self._prp_cache[abs_prp_ref]
        else:
            with open(abs_prp_ref, 'r') as f:
                prp_data = json.load(f)
            self._prp_cache[abs_prp_ref] = prp_data

        if "constraints_and_invariants" not in prp_data:
            prp_data["constraints_and_invariants"] = {}
        if "human_resolution_blocks" not in prp_data["constraints_and_invariants"]:
            prp_data["constraints_and_invariants"]["human_resolution_blocks"] = []


        # --- FIPI & FIGaC Integration ---
        sic_id = self.fipi_forge.generate_sic(human_resolution, ticket_data.get("ticket_id"))
        self.state_manager.resolve_scar(ticket_data.get("ticket_id"), human_resolution, sic_id)
        # --------------------------------
        prp_data["constraints_and_invariants"]["human_resolution_blocks"].append({
            "resolved_ticket": ticket_data.get("ticket_id"),
            "resolution_directive": human_resolution
        })

        with open(abs_prp_ref, 'w') as f:
            json.dump(prp_data, f, indent=2)
        self._prp_cache[abs_prp_ref] = prp_data

        task_filename = os.path.basename(escrowed_task_path)
        if task_filename.startswith("ESCROWED_"):
            task_filename = task_filename[len("ESCROWED_"):]
        if task_filename.endswith(".claimed"):
            task_filename = task_filename[:-len(".claimed")]

        task_data["status"] = "PENDING"

        requeued_task_path = os.path.join(self.tasks_dir, task_filename)
        with open(requeued_task_path, 'w') as f:
            json.dump(task_data, f, indent=2)

        os.remove(escrowed_task_path)
        os.remove(ticket_path)
        print(f"Successfully resolved and requeued task {task_filename}")

def main():
    """Main entry point for the interactive escrow resolution CLI."""
    resolver = EscrowResolver()
    tickets = resolver.get_pending_tickets()

    if not tickets:
        print("No pending escrow tickets found.")
        return

    print(f"Found {len(tickets)} pending escrow tickets.")
    for idx, ticket in enumerate(tickets):
        with open(ticket, 'r') as f:
            data = json.load(f)
            print(f"[{idx}] Ticket: {data.get('ticket_id')} - CFDI: {data.get('cfdi_score')}")
            print(f"    Conflict: {data.get('conflict_reason')}")

    try:
        choice = int(input("Select a ticket to resolve (index): "))
        if choice < 0 or choice >= len(tickets):
            print("Invalid choice.")
            return
    except ValueError:
        print("Invalid input.")
        return

    selected_ticket = tickets[choice]
    print(f"\nResolving {selected_ticket}...")
    resolution = input("Enter human oracle resolution (FIPI patch / structural directive):\n> ")

    if not resolution.strip():
        print("Resolution cannot be empty. Aborting.")
        return

    resolver.resolve_ticket(selected_ticket, resolution)

if __name__ == "__main__":
    main()
