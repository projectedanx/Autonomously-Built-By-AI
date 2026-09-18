import pytest
from project_manager_persona import StrategicIntegrationProjectManager, State

def test_golden_scar_protocol():
    pm = StrategicIntegrationProjectManager()
    # Test contradiction mapping
    result = pm.evaluate_dissonance(stochastic_score=0.9, empirical_score=0.2)
    assert result['state'] == State.GOLDEN_SCAR
    assert round(result['tension_weight'], 3) == round((0.2 * 1.618) + (0.9 * 1.000), 3)
