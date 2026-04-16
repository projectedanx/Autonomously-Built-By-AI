import os
from unittest.mock import patch

import pytest

from system_logic.state_manager import StateManager

def test_complete_task(tmp_path):
    # Initialize StateManager with a temporary workspace
    manager = StateManager(workspace_root=str(tmp_path))

    # Create a dummy task file
    task_filename = "dummy_task.json"
    task_file_path = os.path.join(manager.tasks_dir, task_filename)
    with open(task_file_path, "w") as f:
        f.write('{"task": "do something"}')

    # Define artifact details
    artifact_content = "This is the generated artifact."
    artifact_name = "dummy_artifact.md"

    with patch.object(StateManager, '_git_commit') as mock_git_commit:
        manager.complete_task(task_file_path, artifact_content, artifact_name)

        # Verify the artifact was saved correctly
        expected_artifact_path = os.path.join(manager.completed_dir, artifact_name)
        assert os.path.exists(expected_artifact_path), "Artifact file should have been created"
        with open(expected_artifact_path, "r") as f:
            content = f.read()
        assert content == artifact_content, "Artifact content should match the provided content"

        # Verify the task file was deleted
        assert not os.path.exists(task_file_path), "Task file should have been removed"

        # Verify _git_commit was called with the correct message
        expected_message = f"Completed task: {task_filename} -> {artifact_name}"
        mock_git_commit.assert_called_once_with(expected_message)

def test_claim_task(tmp_path):
    # Initialize StateManager with a temporary workspace
    manager = StateManager(workspace_root=str(tmp_path))

    # Create a dummy task file
    task_filename = "dummy_task2.json"
    task_file_path = os.path.join(manager.tasks_dir, task_filename)
    expected_content = '{"task": "do something else"}'
    with open(task_file_path, "w") as f:
        f.write(expected_content)

    # Call claim_task
    actual_content, claimed_path = manager.claim_task(task_file_path)

    # Verify the content matches
    assert actual_content == expected_content, "The returned content should match the file content"
    assert claimed_path == task_file_path + ".claimed", "The claimed path should have .claimed suffix"
    assert os.path.exists(claimed_path), "Claimed task file should exist"
    assert not os.path.exists(task_file_path), "Original task file should be renamed"

def test_claim_task_not_found(tmp_path):
    # Initialize StateManager with a temporary workspace
    manager = StateManager(workspace_root=str(tmp_path))

    # Define a missing task file path
    task_file_path = os.path.join(manager.tasks_dir, "missing_task.json")

    # Verify that a FileNotFoundError is raised
    with pytest.raises(FileNotFoundError):
        manager.claim_task(task_file_path)

def test_complete_task_missing_file(tmp_path):
    # Initialize StateManager with a temporary workspace
    manager = StateManager(workspace_root=str(tmp_path))

    # Define a missing task file path
    task_file_path = os.path.join(manager.tasks_dir, "missing_task.json")

    artifact_content = "This is the generated artifact."
    artifact_name = "dummy_artifact.md"

    with patch.object(StateManager, '_git_commit') as mock_git_commit:
        with pytest.raises(FileNotFoundError):
            manager.complete_task(task_file_path, artifact_content, artifact_name)

        # Verify that _git_commit was NOT called because removing the non-existent task file raised an error
        mock_git_commit.assert_not_called()
