import os
import pytest
import re

from system_logic.fipi_forge import FIPIForge

def test_fipi_forge_init(tmp_path):
    """Tests FIPIForge initialization."""
    workspace_root = str(tmp_path)
    forge = FIPIForge(workspace_root=workspace_root)

    assert forge.root == workspace_root
    assert forge.constraints_file == os.path.join(workspace_root, "CONSTRAINTS.md")

def test_generate_sic_new_file(tmp_path):
    """Tests generating a SIC when CONSTRAINTS.md does not exist."""
    workspace_root = str(tmp_path)
    forge = FIPIForge(workspace_root=workspace_root)

    human_resolution = "Never use adjectives."
    ticket_id = "TICKET-123"

    sic_id = forge.generate_sic(human_resolution, ticket_id)

    assert sic_id.startswith("SIC-")
    assert os.path.exists(forge.constraints_file)

    with open(forge.constraints_file, "r") as f:
        content = f.read()

    assert "# Semantic Integrity Constraints (Governance-as-Code)" in content
    assert "This document contains all formal SICs generated via Failure-Informed Prompt Inversion (FIPI)." in content

    assert f"## {sic_id}" in content
    assert f"**Origin Ticket**: {ticket_id}" in content
    assert f"> {human_resolution}" in content

def test_generate_sic_existing_file(tmp_path):
    """Tests generating a SIC when CONSTRAINTS.md already exists."""
    workspace_root = str(tmp_path)
    forge = FIPIForge(workspace_root=workspace_root)

    # Pre-create the file
    initial_content = "# Existing Constraints\n\n"
    with open(forge.constraints_file, "w") as f:
        f.write(initial_content)

    human_resolution = "Always validate inputs."
    ticket_id = "TICKET-456"

    sic_id = forge.generate_sic(human_resolution, ticket_id)

    with open(forge.constraints_file, "r") as f:
        content = f.read()

    assert content.startswith(initial_content)
    assert "# Semantic Integrity Constraints (Governance-as-Code)" not in content

    assert f"## {sic_id}" in content
    assert f"**Origin Ticket**: {ticket_id}" in content
    assert f"> {human_resolution}" in content
