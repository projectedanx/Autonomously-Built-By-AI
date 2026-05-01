import os
import uuid
import datetime

class FIPIForge:
    """Failure-Informed Prompt Inversion (FIPI) Forge.

    Translates a human resolution from an Epistemic Escrow ticket into a
    Semantic Integrity Constraint (SIC) and appends it to CONSTRAINTS.md
    as Governance-as-Code.
    """
    def __init__(self, workspace_root: str = "."):
        self.root = workspace_root
        self.constraints_file = os.path.join(self.root, "CONSTRAINTS.md")

    def generate_sic(self, human_resolution: str, ticket_id: str) -> str:
        """Generates a SIC from human resolution and appends to CONSTRAINTS.md."""
        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        sic_id = f"SIC-{timestamp}-{uuid.uuid4().hex[:6].upper()}"

        sic_block = (
            f"## {sic_id}\n"
            f"**Origin Ticket**: {ticket_id}\n"
            f"**Timestamp**: {timestamp}\n"
            f"**Constraint Directive**:\n"
            f"> {human_resolution}\n\n"
        )

        # Ensure CONSTRAINTS.md exists
        if not os.path.exists(self.constraints_file):
            with open(self.constraints_file, 'w') as f:
                f.write("# Semantic Integrity Constraints (Governance-as-Code)\n\n")
                f.write("This document contains all formal SICs generated via Failure-Informed Prompt Inversion (FIPI).\n\n")

        with open(self.constraints_file, 'a') as f:
            f.write(sic_block)

        return sic_id
