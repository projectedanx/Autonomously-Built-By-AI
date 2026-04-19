import os
import unittest
from unittest.mock import patch

from system_logic.state_manager import StateManager

class TestStateManager(unittest.TestCase):
    @patch('system_logic.state_manager.glob')
    @patch('system_logic.state_manager.os.path.isfile')
    def test_get_unprocessed_context(self, mock_isfile, mock_glob):
        # Setup mocks
        mock_glob.return_value = [
            "context_inbox/file1.txt",
            "context_inbox/processed.txt",
            "context_inbox/.hidden.txt",
            "context_inbox/directory"
        ]

        # isfile returns True for everything except the directory
        def isfile_side_effect(path):
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

if __name__ == '__main__':
    unittest.main()
