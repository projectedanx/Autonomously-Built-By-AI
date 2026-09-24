import pytest
from system_logic.anomaly_learning_agent import AnomalyLearningAgent

def test_ala_laminar_pass():
    ala = AnomalyLearningAgent()
    # Tool not on watchlist, low entropy gradient
    result = ala.evaluate_action("edit_post", entropy_gradient=0.20)
    assert result["status"] == "LAMINAR"
    assert result["action"] == "execute_unhindered"

def test_ala_watchlist_trigger():
    ala = AnomalyLearningAgent()
    # Mock synthesis to return high risk for watchlisted tool
    def mock_synthesis(tool):
        return {"S_neural": 0.9, "S_bicm": 0.8, "S_recon": 0.8, "F_symbolic": 1.0}
    ala._execute_nesy_synthesis = mock_synthesis

    result = ala.evaluate_action("delete_user")
    assert result["status"] == "BREACH"
    assert result["action"] == "halt_and_await_hitl"

def test_ala_entropy_trigger():
    ala = AnomalyLearningAgent()
    # Tool not on watchlist, but high entropy gradient
    def mock_synthesis(tool):
        return {"S_neural": 0.9, "S_bicm": 0.9, "S_recon": 0.9, "F_symbolic": 1.0}
    ala._execute_nesy_synthesis = mock_synthesis

    result = ala.evaluate_action("create_post", entropy_gradient=0.85)
    assert result["status"] == "BREACH"
    assert result["action"] == "halt_and_await_hitl"
