import yaml
import os

class InsightGapHarness:
    def __init__(self, config_path="cognitive_contracts/scos_insight_gap_harness.yaml"):
        # [∇] Assuming the file exists and is well-formed
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)['SCOS_INSIGHT_GAP_HARNESS_SPEC']['epistemic_telemetry']['metrics']

    def evaluate_telemetry(self, cd: float, ssi: float, cfdi: float) -> str:
        if cd >= self.config['interpretive_fracture_cd']['critical_hazard_threshold']:
            return self.config['interpretive_fracture_cd']['action_on_violation']
        if ssi >= self.config['semantic_saponification_index']['critical_hazard_threshold']:
            return self.config['semantic_saponification_index']['action_on_violation']
        if cfdi >= self.config['confidence_fidelity_divergence']['critical_hazard_threshold']:
            return self.config['confidence_fidelity_divergence']['action_on_violation']
        return None
