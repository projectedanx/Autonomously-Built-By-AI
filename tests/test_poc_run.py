import pytest
from unittest.mock import patch, MagicMock

from system_logic.poc_run import run_poc

@patch("orchestrator.TaskDispatcher")
@patch("orchestrator.PRPForge")
@patch("orchestrator.StateManager")
def test_run_poc_no_unprocessed_context(mock_state_manager, mock_prp_forge, mock_task_dispatcher, capsys):
    mock_manager_instance = mock_state_manager.return_value
    mock_manager_instance.get_unprocessed_context.return_value = []

    run_poc()

    captured = capsys.readouterr()
    assert "No unprocessed context found." in captured.out

@patch("orchestrator.TaskDispatcher")
@patch("orchestrator.PRPForge")
@patch("orchestrator.StateManager")
def test_run_poc_with_unprocessed_context(mock_state_manager, mock_prp_forge, mock_task_dispatcher):
    mock_manager_instance = mock_state_manager.return_value
    mock_forge_instance = mock_prp_forge.return_value
    mock_dispatcher_instance = mock_task_dispatcher.return_value

    # Setup mocks
    mock_manager_instance.get_unprocessed_context.return_value = ["file1.txt", "file2.txt"]
    mock_forge_instance.extract_intent.return_value = "intent"
    mock_forge_instance.generate_prp.return_value = ({"prp": "data"}, "prp_id")
    mock_forge_instance.save_prp.return_value = "/path/to/prp"
    mock_dispatcher_instance.dispatch_task.return_value = "/path/to/task"

    run_poc()

    # Verify StateManager usage
    mock_manager_instance.get_unprocessed_context.assert_called_once()
    mock_manager_instance.mark_context_processed.assert_called_once_with("file1.txt", defer_save=False)

    # Verify PRPForge usage
    mock_forge_instance.extract_intent.assert_called_once_with("file1.txt")
    mock_forge_instance.generate_prp.assert_called_once_with("intent", "file1.txt")
    mock_forge_instance.save_prp.assert_called_once_with({"prp": "data"}, "prp_id")

    # Verify TaskDispatcher usage
    mock_dispatcher_instance.dispatch_task.assert_called_once_with("/path/to/prp")

import runpy
import sys

def test_poc_run_main():
    mock_orchestrator_module = MagicMock()
    mock_orch_instance = mock_orchestrator_module.Orchestrator.return_value
    mock_orch_instance.manager.get_unprocessed_context.return_value = []

    with patch.dict(sys.modules, {"orchestrator": mock_orchestrator_module}):
        runpy.run_path("system_logic/poc_run.py", run_name="__main__")

    mock_orchestrator_module.Orchestrator.assert_called_once()
    mock_orch_instance.manager.get_unprocessed_context.assert_called_once()
