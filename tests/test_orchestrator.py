import os
from unittest.mock import patch, MagicMock
from system_logic.orchestrator import Orchestrator

@patch("system_logic.orchestrator.StateManager")
@patch("system_logic.orchestrator.PRPForge")
@patch("system_logic.orchestrator.TaskDispatcher")
def test_process_context_file(mock_task_dispatcher_class, mock_prp_forge_class, mock_state_manager_class):
    # Setup mocks
    mock_manager = MagicMock()
    mock_state_manager_class.return_value = mock_manager

    mock_forge = MagicMock()
    mock_prp_forge_class.return_value = mock_forge
    mock_forge.extract_intent.return_value = "mock_raw_intent"
    mock_forge.generate_prp.return_value = ({"mock": "data"}, "mock_prp_id")
    mock_forge.save_prp.return_value = "/mock/path/prp.json"

    mock_dispatcher = MagicMock()
    mock_task_dispatcher_class.return_value = mock_dispatcher
    mock_dispatcher.dispatch_task.return_value = "/mock/path/task.json"

    # Instantiate Orchestrator
    orchestrator = Orchestrator()

    # Call the method under test
    target_file = "/some/dir/test_context.md"
    orchestrator.process_context_file(target_file)

    # Assertions
    filename = "test_context.md"
    mock_forge.extract_intent.assert_called_once_with(target_file)
    mock_forge.generate_prp.assert_called_once_with("mock_raw_intent", filename)
    mock_forge.save_prp.assert_called_once_with({"mock": "data"}, "mock_prp_id")
    mock_dispatcher.dispatch_task.assert_called_once_with("/mock/path/prp.json")
    mock_manager.mark_context_processed.assert_called_once_with(filename, defer_save=False)
