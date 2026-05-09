import os
import unittest
from unittest.mock import patch

from system_logic.state_manager import StateManager

class TestStateManager(unittest.TestCase):
    """Tests for the StateManager class, ensuring correct context processing and security."""
    @patch('system_logic.state_manager.glob')
    @patch('system_logic.state_manager.os.path.isfile')
    def test_get_unprocessed_context(self, mock_isfile, mock_glob):
        """Tests that get_unprocessed_context correctly filters processed and hidden files.

        Args:
            mock_isfile: Mock for os.path.isfile.
            mock_glob: Mock for glob.glob.
        """
        # Setup mocks
        mock_glob.return_value = [
            "context_inbox/file1.txt",
            "context_inbox/processed.txt",
            "context_inbox/.hidden.txt",
            "context_inbox/directory"
        ]

        # isfile returns True for everything except the directory
        def isfile_side_effect(path):
            """Side effect to simulate os.path.isfile behavior.

            Args:
                path (str): The path to check.

            Returns:
                bool: True if the path is considered a file, False otherwise.
            """
            return path != "context_inbox/directory"
        mock_isfile.side_effect = isfile_side_effect

        # Initialize StateManager (need to mock _ensure_dirs so it doesn't create real dirs)
        with patch.object(StateManager, '_ensure_dirs'):
            manager = StateManager()
            manager._state = {"processed_context": ["processed.txt"]}
            manager._processed_context_set = {"processed.txt"}

            # Execute
            unprocessed = manager.get_unprocessed_context()

            # Verify
            self.assertEqual(len(unprocessed), 1)
            self.assertEqual(unprocessed[0], "context_inbox/file1.txt")

    def test_complete_task_security(self):
        """Tests that completing a task with a malicious path prevents directory traversal."""
        import tempfile

        with tempfile.TemporaryDirectory() as test_root:
            manager = StateManager(test_root)
            task_file = os.path.join(manager.tasks_dir, "task.json")
            with open(task_file, "w") as f:
                f.write("{}")

            malicious_name = "../../malicious.txt"
            manager.complete_task(task_file, "content", malicious_name, commit=False)

            # Ensure it didn't escape to the test root (where it would have landed with ../../)
            traversed_path = os.path.join(test_root, "malicious.txt")
            self.assertFalse(os.path.exists(traversed_path))

            # Ensure it was saved safely inside completed_artifacts
            safe_path = os.path.join(manager.completed_dir, "malicious.txt")
            self.assertTrue(os.path.exists(safe_path))

if __name__ == '__main__':
    unittest.main()
