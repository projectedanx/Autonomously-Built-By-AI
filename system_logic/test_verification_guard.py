import unittest
from unittest.mock import MagicMock
from system_logic.verification_guard import VerificationGuard

class TestVerificationGuard(unittest.TestCase):
    def setUp(self):
        self.guard = VerificationGuard()

    def test_laminar_geodesic(self):
        # SDC <= 0.30
        result = self.guard.evaluate_trajectory(sdc=0.20, cfdi=0.1, betti_1=0)
        self.assertEqual(result["status"], "LAMINAR")

    def test_surgical_repair(self):
        # SDC > 0.30, CFDI <= 0.42, betti_1 == 0
        result = self.guard.evaluate_trajectory(sdc=0.35, cfdi=0.30, betti_1=0)
        self.assertEqual(result["status"], "REPAIRED")
        self.assertTrue("e_rec" in result)

    def test_constitutional_crisis_cfdi(self):
        # SDC > 0.30, CFDI > 0.42, betti_1 == 0
        result = self.guard.evaluate_trajectory(sdc=0.35, cfdi=0.50, betti_1=0)
        self.assertEqual(result["status"], "CRISIS")

    def test_constitutional_crisis_betti(self):
        # SDC > 0.30, CFDI <= 0.42, betti_1 >= 1
        result = self.guard.evaluate_trajectory(sdc=0.35, cfdi=0.30, betti_1=1)
        self.assertEqual(result["status"], "CRISIS")

    def test_hard_boundary_drift(self):
        # delta_drift >= 0.12 overrides everything
        result = self.guard.evaluate_trajectory(sdc=0.10, cfdi=0.1, betti_1=0, delta_drift=0.15)
        self.assertEqual(result["status"], "CRISIS")
        self.assertTrue("Hard Boundary Breach" in result["message"])

    def test_laminar_with_safe_drift(self):
        # delta_drift < 0.12 and SDC <= 0.30
        result = self.guard.evaluate_trajectory(sdc=0.20, cfdi=0.1, betti_1=0, delta_drift=0.10)
        self.assertEqual(result["status"], "LAMINAR")
