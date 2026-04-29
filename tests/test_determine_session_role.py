from unittest.mock import patch
from system_logic.state_manager import StateManager

def test_determine_session_role_worker(tmp_path):
    manager = StateManager(workspace_root=str(tmp_path))

    with patch.object(StateManager, 'get_pending_tasks', return_value=["task1.json"]):
        assert manager.determine_session_role() == "WORKER"

def test_determine_session_role_sovereign(tmp_path):
    manager = StateManager(workspace_root=str(tmp_path))

    with patch.object(StateManager, 'get_pending_tasks', return_value=[]):
        with patch.object(StateManager, 'get_unprocessed_context', return_value=["file1.txt"]):
            assert manager.determine_session_role() == "SOVEREIGN"

def test_determine_session_role_idle(tmp_path):
    manager = StateManager(workspace_root=str(tmp_path))

    with patch.object(StateManager, 'get_pending_tasks', return_value=[]):
        with patch.object(StateManager, 'get_unprocessed_context', return_value=[]):
            assert manager.determine_session_role() == "IDLE"
