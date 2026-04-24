import os
import json
import pytest

from system_logic.task_dispatcher import TaskDispatcher

def test_task_dispatcher_init(tmp_path):
    workspace = str(tmp_path)
    dispatcher = TaskDispatcher(workspace_root=workspace)

    assert dispatcher.root == workspace
    assert dispatcher.contracts_dir == os.path.join(workspace, "cognitive_contracts")
    assert dispatcher.tasks_dir == os.path.join(workspace, "delegated_tasks")

def test_dispatch_task_default_role(tmp_path):
    workspace = str(tmp_path)
    # Ensure the delegated_tasks directory exists
    os.makedirs(os.path.join(workspace, "delegated_tasks"), exist_ok=True)

    dispatcher = TaskDispatcher(workspace_root=workspace)
    prp_filepath = os.path.join(workspace, "cognitive_contracts", "test_contract.json")

    task_filepath = dispatcher.dispatch_task(prp_filepath)

    expected_filename = "TASK_test_contract.json"
    expected_task_filepath = os.path.join(dispatcher.tasks_dir, expected_filename)

    assert task_filepath == expected_task_filepath
    assert os.path.exists(task_filepath)

    with open(task_filepath, "r") as f:
        data = json.load(f)

    assert data["task_id"] == "test_contract"
    assert data["status"] == "PENDING"
    assert data["assigned_role"] == "WORKER"
    assert data["prp_reference"] == prp_filepath
    assert data["instructions"] == "Execute strictly according to the referenced Cognitive Contract (PRP)."

def test_dispatch_task_custom_role(tmp_path):
    workspace = str(tmp_path)
    os.makedirs(os.path.join(workspace, "delegated_tasks"), exist_ok=True)

    dispatcher = TaskDispatcher(workspace_root=workspace)
    prp_filepath = "/some/absolute/path/another_contract.json"

    task_filepath = dispatcher.dispatch_task(prp_filepath, agent_role="REVIEWER")

    expected_filename = "TASK_another_contract.json"
    expected_task_filepath = os.path.join(dispatcher.tasks_dir, expected_filename)

    assert task_filepath == expected_task_filepath
    assert os.path.exists(task_filepath)

    with open(task_filepath, "r") as f:
        data = json.load(f)

    assert data["task_id"] == "another_contract"
    assert data["status"] == "PENDING"
    assert data["assigned_role"] == "REVIEWER"
    assert data["prp_reference"] == prp_filepath
    assert data["instructions"] == "Execute strictly according to the referenced Cognitive Contract (PRP)."
