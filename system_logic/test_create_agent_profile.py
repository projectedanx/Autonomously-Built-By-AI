import os
import pytest
import shutil
from system_logic.create_agent_profile import create_agent

@pytest.fixture
def test_workspace(tmp_path):
    """Set up a temporary workspace for testing."""
    workspace = tmp_path / "workspace"
    workspace.mkdir()
    profiles_dir = workspace / "agent_profiles"
    profiles_dir.mkdir()

    # Change to the temporary workspace
    old_cwd = os.getcwd()
    os.chdir(workspace)
    yield workspace
    # Restore original working directory
    os.chdir(old_cwd)

def test_create_agent_normal(test_workspace):
    """Test normal agent creation."""
    create_agent(
        name="Normal Agent",
        designation="Tester",
        color="blue",
        specialty="Testing",
        when_to_use="When testing",
        primary_goal="Test",
        secondary_goal="Test more",
        forbidden="None",
        voice="Robotic",
        primary_mode="Testing",
        rules="Rule 1"
    )
    assert os.path.exists("agent_profiles/normal_agent/profile.yaml")

def test_create_agent_path_traversal_sanitized(test_workspace):
    """Test that path traversal characters are sanitized."""
    create_agent(
        name="Malicious Agent",
        designation="Tester",
        color="blue",
        specialty="Testing",
        when_to_use="When testing",
        primary_goal="Test",
        secondary_goal="Test more",
        forbidden="None",
        voice="Robotic",
        primary_mode="Testing",
        rules="Rule 1",
        folder_name="../../evil_agent"
    )
    # It should be sanitized to just 'evil_agent' under 'agent_profiles'
    assert os.path.exists("agent_profiles/evil_agent/profile.yaml")
    # And it should NOT be outside
    assert not os.path.exists("../evil_agent")

def test_create_agent_invalid_folder_names(test_workspace):
    """Test that invalid folder names raise ValueError."""
    with pytest.raises(ValueError) as exc_info:
        create_agent(
            name="Invalid Agent",
            designation="Tester",
            color="blue",
            specialty="Testing",
            when_to_use="When testing",
            primary_goal="Test",
            secondary_goal="Test more",
            forbidden="None",
            voice="Robotic",
            primary_mode="Testing",
            rules="Rule 1",
            folder_name=".."
        )
    assert "Invalid folder name" in str(exc_info.value)

    with pytest.raises(ValueError) as exc_info:
        create_agent(
            name="Invalid Agent",
            designation="Tester",
            color="blue",
            specialty="Testing",
            when_to_use="When testing",
            primary_goal="Test",
            secondary_goal="Test more",
            forbidden="None",
            voice="Robotic",
            primary_mode="Testing",
            rules="Rule 1",
            folder_name="/"
        )
    assert "Invalid folder name" in str(exc_info.value)
