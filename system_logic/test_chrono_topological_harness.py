import pytest
from chrono_topological_harness import ChronoTopologicalHarness

def test_evaluate_betti_1_persistence():
    harness = ChronoTopologicalHarness(tau_p=1.0)
    assert harness.evaluate_betti_1_persistence(0.5) == "Laminar Flow"
    assert harness.evaluate_betti_1_persistence(1.5) == "trigger_EpistemicEscrow_and_RTA"

def test_compute_ssi():
    harness = ChronoTopologicalHarness()
    assert harness.compute_ssi(10.0, 2.0) == 0.8
    assert harness.compute_ssi(0.0, 2.0) == 1.0
