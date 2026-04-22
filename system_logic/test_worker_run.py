import pytest
from unittest.mock import patch, MagicMock

from system_logic.worker_run import run_worker

@patch("system_logic.worker_run.StateManager")
@patch("system_logic.worker_run.execute_task")
def test_run_worker_no_tasks(mock_execute_task, mock_state_manager, capsys):
    mock_manager_instance = mock_state_manager.return_value
    mock_manager_instance.get_pending_tasks.return_value = []

    run_worker()

    captured = capsys.readouterr()
    assert "No pending tasks." in captured.out
    mock_execute_task.assert_not_called()

@patch("system_logic.worker_run.StateManager")
@patch("system_logic.worker_run.execute_task")
def test_run_worker_with_tasks(mock_execute_task, mock_state_manager):
    mock_manager_instance = mock_state_manager.return_value
    mock_manager_instance.get_pending_tasks.return_value = ["task_1"]

    run_worker()

    mock_execute_task.assert_called_once_with(mock_manager_instance, "task_1")
