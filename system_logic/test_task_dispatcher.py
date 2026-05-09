import os
import json
import unittest
from unittest.mock import patch, mock_open

from system_logic.task_dispatcher import TaskDispatcher

class TestTaskDispatcher(unittest.TestCase):
    """Tests for the TaskDispatcher class to ensure task payload creation is correct."""

    def test_init(self):
        """Test path assignments on initialization."""
        dispatcher = TaskDispatcher("/test/workspace")
        self.assertEqual(dispatcher.root, "/test/workspace")
        self.assertEqual(dispatcher.contracts_dir, os.path.join("/test/workspace", "cognitive_contracts"))
        self.assertEqual(dispatcher.tasks_dir, os.path.join("/test/workspace", "delegated_tasks"))

        dispatcher_default = TaskDispatcher()
        self.assertEqual(dispatcher_default.root, ".")
        self.assertEqual(dispatcher_default.contracts_dir, os.path.join(".", "cognitive_contracts"))
        self.assertEqual(dispatcher_default.tasks_dir, os.path.join(".", "delegated_tasks"))

    @patch('builtins.open', new_callable=mock_open)
    @patch('json.dump')
    def test_dispatch_task_success(self, mock_json_dump, mock_file):
        """Test dispatching a task with the default agent role."""
        dispatcher = TaskDispatcher("/test/workspace")
        prp_filepath = "/test/workspace/cognitive_contracts/PRP_001.json"

        expected_task_id = "PRP_001"
        expected_filepath = os.path.join("/test/workspace", "delegated_tasks", f"TASK_{expected_task_id}.json")

        expected_payload = {
            "task_id": expected_task_id,
            "status": "PENDING",
            "assigned_role": "WORKER",
            "prp_reference": prp_filepath,
            "instructions": "Execute strictly according to the referenced Cognitive Contract (PRP)."
        }

        # Execute
        task_filepath = dispatcher.dispatch_task(prp_filepath)

        # Verify
        self.assertEqual(task_filepath, expected_filepath)
        mock_file.assert_called_once_with(expected_filepath, 'w')
        mock_json_dump.assert_called_once_with(expected_payload, mock_file(), indent=2)

    @patch('builtins.open', new_callable=mock_open)
    @patch('json.dump')
    def test_dispatch_task_custom_role(self, mock_json_dump, mock_file):
        """Test dispatching a task with a custom agent role."""
        dispatcher = TaskDispatcher("/test/workspace")
        prp_filepath = "PRP_002.json"
        custom_role = "REVIEWER"

        expected_task_id = "PRP_002"
        expected_filepath = os.path.join("/test/workspace", "delegated_tasks", f"TASK_{expected_task_id}.json")

        expected_payload = {
            "task_id": expected_task_id,
            "status": "PENDING",
            "assigned_role": custom_role,
            "prp_reference": prp_filepath,
            "instructions": "Execute strictly according to the referenced Cognitive Contract (PRP)."
        }

        # Execute
        task_filepath = dispatcher.dispatch_task(prp_filepath, agent_role=custom_role)

        # Verify
        self.assertEqual(task_filepath, expected_filepath)
        mock_file.assert_called_once_with(expected_filepath, 'w')
        mock_json_dump.assert_called_once_with(expected_payload, mock_file(), indent=2)

if __name__ == '__main__':
    unittest.main()
