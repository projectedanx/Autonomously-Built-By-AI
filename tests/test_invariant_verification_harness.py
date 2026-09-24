import pytest
import numpy as np
from system_logic.invariant_verification_harness import InvariantVerificationHarness

def test_anomaly_mining():
    ivh = InvariantVerificationHarness(anomaly_threshold=3.0)
    data = [1.0, 1.1, 0.9, 1.0, 1.2, 10.0] # 10.0 is an anomaly
    preds = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

    anomalies = ivh.mine_anomalies(data, preds)
    assert 5 in anomalies
    assert 0 not in anomalies

def test_isomorphic_formalization():
    ivh = InvariantVerificationHarness()

    good_schema = ivh.formalize_isomorphism("Force equals mass times acceleration")
    assert good_schema["status"] == "compiled"

    bad_schema = ivh.formalize_isomorphism("It's a vague generalization about stuff moving")
    assert bad_schema["status"] == "rejected"

def test_calculate_bic():
    ivh = InvariantVerificationHarness()

    # Model A: High parameters, low RSS
    bic_a = ivh.calculate_bic(num_params=20, num_data_points=100, residual_sum_squares=10.0)

    # Model B: Low parameters, slightly higher RSS
    bic_b = ivh.calculate_bic(num_params=2, num_data_points=100, residual_sum_squares=12.0)

    # In this scenario, Model B should be preferred (lower BIC)
    assert bic_b < bic_a

def test_boundary_audit():
    ivh = InvariantVerificationHarness()

    schema = {"description": "Newtonian Kinematics"}

    report = ivh.execute_boundary_audit(schema, "v -> c")
    assert report["result"] == "model_broken"
    assert report["drift_sigma"] > 3.0
