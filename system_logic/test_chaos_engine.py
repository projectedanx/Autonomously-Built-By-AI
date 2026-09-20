import unittest
from chaos_engine import ChaosEngine

class TestChaosEngine(unittest.TestCase):
    def setUp(self):
        self.engine = ChaosEngine()

    def test_evaluate_cfdi_high(self):
        result = self.engine.evaluate_cfdi(0.45)
        self.assertEqual(result, "trigger_+++PositiveFriction_and_EpistemicEscrow")

    def test_evaluate_cfdi_low(self):
        result = self.engine.evaluate_cfdi(0.3)
        self.assertEqual(result, "Laminar Flow")

if __name__ == '__main__':
    unittest.main()
