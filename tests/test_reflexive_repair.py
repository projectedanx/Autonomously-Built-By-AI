import pytest
from unittest.mock import MagicMock
from system_logic.reflexive_repair import ReflexiveRepairLoop
from system_logic.state_manager import StateManager

def test_reflexive_repair_success():
    manager = MagicMock(spec=StateManager)
    loop = ReflexiveRepairLoop(manager, max_attempts=3)

    # Fails once, succeeds on second attempt
    def mock_generator(prp, constraints):
        return {"attempt": len(constraints) + 1}

    def mock_verifier(candidate):
        if candidate["attempt"] < 2:
            return False, "Error", {"error_code": 1}
        return True, "", {}

    result = loop.execute("task.json", {}, mock_generator, mock_verifier)
    assert result is not None
    assert result["attempt"] == 2
    manager.escrow_task.assert_not_called()
    manager.record_scar.assert_not_called()

def test_reflexive_repair_exhaustion():
    manager = MagicMock(spec=StateManager)
    loop = ReflexiveRepairLoop(manager, max_attempts=3)

    def mock_generator(prp, constraints):
        return {"attempt": len(constraints) + 1}

    def mock_verifier(candidate):
        return False, "Persistent Error", {"error_code": 2}

    result = loop.execute("task.json", {}, mock_generator, mock_verifier)
    assert result is None
    manager.escrow_task.assert_called_once()
    manager.record_scar.assert_called_once()
