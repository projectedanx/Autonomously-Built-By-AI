import pytest
from lattice_breaker import LatticeBreakerHarness

def test_laminar_flow():
    harness = LatticeBreakerHarness()
    result = harness.evaluate_action_vector("agent_123", [0.1, 0.1, 0.1, 0.1, 0.1], ["Plugin", "Func"])
    assert result["status"] == "LAMINAR_HOMEOSTASIS"
    assert result["action"] == "execute_unhindered"

def test_lattice_breach():
    harness = LatticeBreakerHarness()
    # Distance will be > 0.8
    result = harness.evaluate_action_vector("agent_456", [1.0, 1.0, 0.9, 0.9, 0.8], ["MaliciousPlugin", "Exec"])
    assert result["status"] == "LATTICE_BREAKER_BREACH"
    assert result["action"] == "gated_checkpoint_halt"
    assert "breach_record" in result
    assert result["breach_record"]["triage_verdict"] == "PENDING"
    assert result["misuse_score"] >= 0.8

def test_triage_verdict_apply():
    harness = LatticeBreakerHarness()
    result = harness.evaluate_action_vector("agent_789", [1.0, 1.0, 0.9, 0.9, 0.8], ["MaliciousPlugin", "Exec"])
    record = result["breach_record"]
    updated = harness.apply_triage_verdict(record, "QUARANTINE")
    assert updated["triage_verdict"] == "QUARANTINE"

    with pytest.raises(ValueError):
        harness.apply_triage_verdict(record, "INVALID")
