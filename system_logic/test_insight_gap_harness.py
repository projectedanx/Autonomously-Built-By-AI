import unittest
from insight_gap_harness import InsightGapHarness

class TestInsightGapHarness(unittest.TestCase):
    def setUp(self):
        self.harness = InsightGapHarness()

    def test_interpretive_fracture(self):
        action = self.harness.evaluate_telemetry(cd=0.45, ssi=0.01, cfdi=0.05)
        self.assertEqual(action, "activate_+++SilentReasoning(depth='deep')")

    def test_semantic_saponification(self):
        action = self.harness.evaluate_telemetry(cd=0.1, ssi=0.05, cfdi=0.05)
        self.assertEqual(action, "execute_+++ContextLock(refresh_interval=2048)")

    def test_confidence_fidelity_divergence(self):
        action = self.harness.evaluate_telemetry(cd=0.1, ssi=0.01, cfdi=0.20)
        self.assertEqual(action, "quarantine_to_+++EpistemicEscrow")

    def test_no_violation(self):
        action = self.harness.evaluate_telemetry(cd=0.1, ssi=0.01, cfdi=0.05)
        self.assertIsNone(action)

if __name__ == '__main__':
    unittest.main()
