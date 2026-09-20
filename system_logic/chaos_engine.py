class ChaosEngine:
    def __init__(self, cfdi_threshold=0.42):
        self.cfdi_threshold = cfdi_threshold

    def evaluate_cfdi(self, cfdi: float) -> str:
        if cfdi > self.cfdi_threshold:
            return "trigger_+++PositiveFriction_and_EpistemicEscrow"
        return "Laminar Flow"
