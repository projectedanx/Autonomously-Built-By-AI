import unittest
import os
import tempfile
import json
from unittest.mock import patch

from system_logic.escrow_resolution import EscrowResolver
from system_logic.state_manager import StateManager

class TestEscrowResolution(unittest.TestCase):
    """Tests for the EscrowResolver class, ensuring tickets can be retrieved and resolved correctly."""
    def setUp(self):
        """Sets up a temporary workspace with necessary directories and mock files for testing."""
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = self.temp_dir.name
        self.manager = StateManager(self.root)
        self.resolver = EscrowResolver(self.root)

        # Create a mock PRP
        self.prp_id = "PRP-TEST"
        self.prp_data = {"metadata": {"id": self.prp_id}, "constraints_and_invariants": {}}
        self.prp_path = os.path.join(self.manager.contracts_dir, f"{self.prp_id}.json")
        with open(self.prp_path, 'w') as f:
            json.dump(self.prp_data, f)

        # Create a mock Task
        self.task_id = "TASK-123"
        self.task_filename = f"TASK_{self.task_id}.json"
        self.task_path = os.path.join(self.manager.tasks_dir, self.task_filename)
        self.task_data = {
            "task_id": self.task_id,
            "status": "PENDING",
            "prp_reference": self.prp_path
        }
        with open(self.task_path, 'w') as f:
            json.dump(self.task_data, f)

    def tearDown(self):
        """Cleans up the temporary workspace after tests."""
        self.temp_dir.cleanup()

    def test_resolve_ticket(self):
        """Tests that a ticket is correctly resolved, the PRP is updated, and the task is requeued."""
        # 1. Claim task and trigger escrow to set up the state
        task_content, claimed_path = self.manager.claim_task(self.task_path)
        ticket_path = self.manager.escrow_task(claimed_path, 0.20, "Test Conflict")

        # Verify state before resolution
        self.assertFalse(os.path.exists(self.task_path))
        self.assertFalse(os.path.exists(claimed_path))
        self.assertTrue(os.path.exists(ticket_path))

        with open(ticket_path, 'r') as f:
            ticket_data = json.load(f)
        escrowed_task_path = ticket_data.get("original_task")
        self.assertTrue(os.path.exists(escrowed_task_path))
        self.assertTrue("ESCROWED_" in escrowed_task_path)

        # 2. Resolve the ticket
        resolution_text = "HUMAN ORACLE: Override rule 1, apply FIPI patch."
        self.resolver.resolve_ticket(ticket_path, resolution_text)

        # 3. Verify state after resolution
        self.assertFalse(os.path.exists(ticket_path))
        self.assertFalse(os.path.exists(escrowed_task_path))

        # Check task was requeued correctly
        requeued_task_path = os.path.join(self.manager.tasks_dir, self.task_filename)
        self.assertTrue(os.path.exists(requeued_task_path))
        with open(requeued_task_path, 'r') as f:
            requeued_task_data = json.load(f)
            self.assertEqual(requeued_task_data["status"], "PENDING")

        # Check PRP was updated
        with open(self.prp_path, 'r') as f:
            updated_prp = json.load(f)

        blocks = updated_prp.get("constraints_and_invariants", {}).get("human_resolution_blocks", [])
        self.assertEqual(len(blocks), 1)
        self.assertEqual(blocks[0]["resolution_directive"], resolution_text)


    def test_path_traversal_prevention(self):
        """Tests that resolving a ticket with a prp_reference outside contracts_dir raises PermissionError."""
        # Create a malicious task pointing outside the workspace directory
        secret_file = "/tmp/secret.txt"
        with open(secret_file, 'w') as f:
            f.write("SUPER_SECRET_DATA")

        malicious_task_filename = f"TASK_malicious.json"
        malicious_task_path = os.path.join(self.manager.tasks_dir, malicious_task_filename)
        malicious_task_data = {
            "task_id": "malicious",
            "status": "PENDING",
            "prp_reference": secret_file
        }
        with open(malicious_task_path, 'w') as f:
            json.dump(malicious_task_data, f)

        # Claim task and trigger escrow
        task_content, claimed_path = self.manager.claim_task(malicious_task_path)
        ticket_path = self.manager.escrow_task(claimed_path, 0.20, "Test Conflict")

        # Resolving the ticket should raise PermissionError
        with self.assertRaises(PermissionError) as context:
            self.resolver.resolve_ticket(ticket_path, "HUMAN ORACLE: Resolve malicious task.")

        self.assertIn("Access denied", str(context.exception))

    @patch('builtins.input', side_effect=['0', 'My resolution patch'])
    def test_main_cli_flow(self, mock_input):
        """Tests the main interactive CLI flow for resolving escrow tickets.

        Args:
            mock_input: Mock for the built-in input function.
        """
        # Setup escrow state
        task_content, claimed_path = self.manager.claim_task(self.task_path)
        ticket_path = self.manager.escrow_task(claimed_path, 0.20, "Test Conflict")

        # Run main via mock
        with patch('system_logic.escrow_resolution.EscrowResolver', return_value=self.resolver):
            from system_logic.escrow_resolution import main
            main()

        # Check task was requeued correctly
        requeued_task_path = os.path.join(self.manager.tasks_dir, self.task_filename)
        self.assertTrue(os.path.exists(requeued_task_path))

if __name__ == '__main__':
    unittest.main()
