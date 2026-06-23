import json
import concurrent.futures
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

    def _load_ticket_and_task(self, ticket_path: str):
        with open(ticket_path, 'r') as f:
            ticket_data = json.load(f)

        escrowed_task_path = ticket_data.get("original_task")
        if not escrowed_task_path or not os.path.exists(escrowed_task_path):
            print(f"Error: Original task file {escrowed_task_path} not found.")
            return None, None, None

        with open(escrowed_task_path, 'r') as f:
            task_data = json.load(f)

        return ticket_data, task_data, escrowed_task_path

    def _load_prp_data(self, task_data: dict):
        prp_ref = task_data.get("prp_reference")
        if not prp_ref:
            print("Error: Missing prp_reference in task data.")
            return None, None

        abs_prp_ref = os.path.realpath(os.path.join(self.root, prp_ref))
        root_dir = os.path.realpath(self.root)
        if os.path.commonpath([abs_prp_ref, root_dir]) != root_dir:
            raise PermissionError(f"Access denied: {prp_ref} is outside the allowed workspace directory.")

        if abs_prp_ref in self._prp_cache:
            prp_data = self._prp_cache[abs_prp_ref]
        else:
            with open(abs_prp_ref, 'r') as f:
                prp_data = json.load(f)
            self._prp_cache[abs_prp_ref] = prp_data

        return prp_data, abs_prp_ref

    def _update_prp_with_resolution(self, prp_data: dict, abs_prp_ref: str, ticket_id: str, human_resolution: str):
        if "constraints_and_invariants" not in prp_data:
            prp_data["constraints_and_invariants"] = {}
        if "human_resolution_blocks" not in prp_data["constraints_and_invariants"]:
            prp_data["constraints_and_invariants"]["human_resolution_blocks"] = []

        # --- FIPI & FIGaC Integration ---
        sic_id = self.fipi_forge.generate_sic(human_resolution, ticket_id)
        self.state_manager.resolve_scar(ticket_id, human_resolution, sic_id)
        # --------------------------------

        prp_data["constraints_and_invariants"]["human_resolution_blocks"].append({
            "resolved_ticket": ticket_id,
            "resolution_directive": human_resolution
        })

        with open(abs_prp_ref, 'w') as f:
            json.dump(prp_data, f, indent=2)
        self._prp_cache[abs_prp_ref] = prp_data

    def _requeue_task(self, escrowed_task_path: str, ticket_path: str, task_data: dict):
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

    def resolve_ticket(self, ticket_path: str, human_resolution: str):
        """Resolves an escrow ticket with human input and requeues the task.

        Args:
            ticket_path (str): The path to the escrow ticket file.
            human_resolution (str): The resolution provided by the human oracle.
        """
        ticket_data, task_data, escrowed_task_path = self._load_ticket_and_task(ticket_path)
        if ticket_data is None:
            return

        prp_data, abs_prp_ref = self._load_prp_data(task_data)
        if prp_data is None:
            return

        self._update_prp_with_resolution(prp_data, abs_prp_ref, ticket_data.get("ticket_id"), human_resolution)
        self._requeue_task(escrowed_task_path, ticket_path, task_data)



def _load_ticket_data(ticket_path):
    with open(ticket_path, 'r') as f:
        return json.load(f)

def main():
    """Main entry point for the interactive escrow resolution CLI."""
    resolver = EscrowResolver()
    tickets = resolver.get_pending_tickets()

    if not tickets:
        print("No pending escrow tickets found.")
        return

    print(f"Found {len(tickets)} pending escrow tickets.")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        ticket_data_list = list(executor.map(_load_ticket_data, tickets))

    for idx, data in enumerate(ticket_data_list):
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
