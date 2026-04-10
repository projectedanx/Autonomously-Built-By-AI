import pytest
import os
import json
from state_manager import StateManager
from worker_run import execute_task

def test_path_traversal_prevention(tmp_path):
    """Test that path traversal attempts raise a PermissionError."""
    # Set up dummy environment
    manager = StateManager(workspace_root=str(tmp_path))

    # Create an invalid file we want to try to access (outside of contracts_dir)
    secret_file = tmp_path / "secret.txt"
    secret_file.write_text("SUPER_SECRET_DATA")

    # Create a task file that tries to access the secret file
    task_file = manager.tasks_dir + "/TASK_malicious.json"
    with open(task_file, 'w') as f:
        json.dump({
            "task_id": "malicious",
            "prp_reference": str(secret_file)
        }, f)

    # Executing the task should raise PermissionError
    with pytest.raises(PermissionError) as exc_info:
        execute_task(manager, task_file)

    assert "Access denied" in str(exc_info.value)

def test_missing_prp_reference(tmp_path):
    """Test that missing prp_reference raises ValueError."""
    manager = StateManager(workspace_root=str(tmp_path))

    # Create a task file without prp_reference
    task_file = manager.tasks_dir + "/TASK_missing.json"
    with open(task_file, 'w') as f:
        json.dump({
            "task_id": "missing",
        }, f)

    # Executing the task should raise ValueError
    with pytest.raises(ValueError) as exc_info:
        execute_task(manager, task_file)

    assert "Missing prp_reference" in str(exc_info.value)
