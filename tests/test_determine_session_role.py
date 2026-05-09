from unittest.mock import patch
from system_logic.state_manager import StateManager

def test_determine_session_role_worker(tmp_path):
    """Tests that the session role is WORKER when tasks are pending.

    Args:
        tmp_path: Pytest fixture for a temporary directory.
    """
    manager = StateManager(workspace_root=str(tmp_path))

    with patch.object(StateManager, 'get_pending_tasks', return_value=["task1.json"]):
        assert manager.determine_session_role() == "WORKER"

def test_determine_session_role_sovereign(tmp_path):
    """Tests that the session role is SOVEREIGN when context is unprocessed and no tasks are pending.

    Args:
        tmp_path: Pytest fixture for a temporary directory.
    """
    manager = StateManager(workspace_root=str(tmp_path))

    with patch.object(StateManager, 'get_pending_tasks', return_value=[]):
        with patch.object(StateManager, 'get_unprocessed_context', return_value=["file1.txt"]):
            assert manager.determine_session_role() == "SOVEREIGN"

def test_determine_session_role_idle(tmp_path):
    """Tests that the session role is IDLE when there are no tasks and no unprocessed context.

    Args:
        tmp_path: Pytest fixture for a temporary directory.
    """
    manager = StateManager(workspace_root=str(tmp_path))

    with patch.object(StateManager, 'get_pending_tasks', return_value=[]):
        with patch.object(StateManager, 'get_unprocessed_context', return_value=[]):
            assert manager.determine_session_role() == "IDLE"
