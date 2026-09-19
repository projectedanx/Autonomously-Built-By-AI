import os
from unittest.mock import patch, MagicMock
from system_logic.orchestrator import Orchestrator

@patch("system_logic.orchestrator.StateManager")
@patch("system_logic.orchestrator.PRPForge")
@patch("system_logic.orchestrator.TaskDispatcher")
def test_process_context_file(mock_task_dispatcher_class, mock_prp_forge_class, mock_state_manager_class):
    """Tests processing a context file by the Orchestrator.

    Args:
        mock_task_dispatcher_class: Mock for TaskDispatcher.
        mock_prp_forge_class: Mock for PRPForge.
        mock_state_manager_class: Mock for StateManager.
    """
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

@patch('system_logic.orchestrator.execute_task')
@patch('system_logic.orchestrator.Orchestrator')
def test_main_sovereign_with_files(mock_orchestrator_class, mock_execute_task):
    from system_logic.orchestrator import main
    mock_orchestrator = MagicMock()
    mock_orchestrator_class.return_value = mock_orchestrator

    mock_orchestrator.manager.determine_session_role.return_value = "SOVEREIGN"
    mock_orchestrator.manager.get_unprocessed_context.return_value = ["file1.txt", "file2.txt"]

    main()

    mock_orchestrator.manager.determine_session_role.assert_called_once()
    mock_orchestrator.manager.get_unprocessed_context.assert_called_once()
    assert mock_orchestrator.process_context_file.call_count == 2
    mock_orchestrator.process_context_file.assert_any_call("file1.txt", defer_save=True)
    mock_orchestrator.process_context_file.assert_any_call("file2.txt", defer_save=True)
    mock_orchestrator.manager.save_state.assert_called_once()

@patch('system_logic.orchestrator.execute_task')
@patch('system_logic.orchestrator.Orchestrator')
def test_main_sovereign_no_files(mock_orchestrator_class, mock_execute_task):
    from system_logic.orchestrator import main
    mock_orchestrator = MagicMock()
    mock_orchestrator_class.return_value = mock_orchestrator

    mock_orchestrator.manager.determine_session_role.return_value = "SOVEREIGN"
    mock_orchestrator.manager.get_unprocessed_context.return_value = []

    main()

    mock_orchestrator.manager.determine_session_role.assert_called_once()
    mock_orchestrator.manager.get_unprocessed_context.assert_called_once()
    mock_orchestrator.process_context_file.assert_not_called()
    mock_orchestrator.manager.save_state.assert_not_called()

@patch('system_logic.orchestrator.execute_task')
@patch('system_logic.orchestrator.Orchestrator')
def test_main_worker_with_tasks(mock_orchestrator_class, mock_execute_task):
    from system_logic.orchestrator import main
    mock_orchestrator = MagicMock()
    mock_orchestrator_class.return_value = mock_orchestrator

    mock_orchestrator.manager.determine_session_role.return_value = "WORKER"
    mock_orchestrator.manager.get_pending_tasks.return_value = ["task1", "task2"]

    main()

    mock_orchestrator.manager.determine_session_role.assert_called_once()
    mock_orchestrator.manager.get_pending_tasks.assert_called_once()
    assert mock_execute_task.call_count == 2
    mock_execute_task.assert_any_call(mock_orchestrator.manager, "task1", commit=False)
    mock_execute_task.assert_any_call(mock_orchestrator.manager, "task2", commit=False)
    mock_orchestrator.manager._git_commit.assert_called_once_with("Completed 2 tasks.")
    mock_orchestrator.manager.reingest_artifacts.assert_called_once()

@patch('system_logic.orchestrator.execute_task')
@patch('system_logic.orchestrator.Orchestrator')
def test_main_worker_no_tasks(mock_orchestrator_class, mock_execute_task):
    from system_logic.orchestrator import main
    mock_orchestrator = MagicMock()
    mock_orchestrator_class.return_value = mock_orchestrator

    mock_orchestrator.manager.determine_session_role.return_value = "WORKER"
    mock_orchestrator.manager.get_pending_tasks.return_value = []

    main()

    mock_orchestrator.manager.determine_session_role.assert_called_once()
    mock_orchestrator.manager.get_pending_tasks.assert_called_once()
    mock_execute_task.assert_not_called()
    mock_orchestrator.manager._git_commit.assert_not_called()
    mock_orchestrator.manager.reingest_artifacts.assert_called_once()

@patch('system_logic.orchestrator.execute_task')
@patch('system_logic.orchestrator.Orchestrator')
def test_main_idle(mock_orchestrator_class, mock_execute_task):
    from system_logic.orchestrator import main
    mock_orchestrator = MagicMock()
    mock_orchestrator_class.return_value = mock_orchestrator

    mock_orchestrator.manager.determine_session_role.return_value = "IDLE"

    main()

    mock_orchestrator.manager.determine_session_role.assert_called_once()
    mock_orchestrator.manager.get_unprocessed_context.assert_not_called()
    mock_orchestrator.manager.get_pending_tasks.assert_not_called()
