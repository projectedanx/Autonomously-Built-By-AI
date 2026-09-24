from typing import Dict, Any, List

class Action:
    def __init__(self, name: str, preconditions: Dict[str, Any], effects: Dict[str, Any]):
        self.name = name
        self.preconditions = preconditions
        self.effects = effects

class SystemAssuranceAgent:
    def __init__(self, cpi_threshold: float = 0.95):
        self.cpi_threshold = cpi_threshold

    def calculate_cpi(self, states: List[Dict[str, Any]], actions: List[Action]) -> float:
        if len(states) < 2 or len(actions) != len(states) - 1:
            return 1.0

        N = len(states)
        valid_transitions = 0

        for k in range(N - 1):
            s_k = states[k]
            s_k1 = states[k + 1]
            a_k = actions[k]

            pre_met = all(s_k.get(key) == v for key, v in a_k.preconditions.items())
            eff_met = all(s_k1.get(key) == v for key, v in a_k.effects.items())

            frame_met = True
            for key in s_k.keys():
                if key not in a_k.effects:
                    if s_k.get(key) != s_k1.get(key):
                        frame_met = False
                        break

            if pre_met and eff_met and frame_met:
                valid_transitions += 1

        return valid_transitions / (N - 1)

class TemporalBlendingEngine:
    def __init__(self):
        self.saa = SystemAssuranceAgent()

    def process_trace(self, states: List[Dict[str, Any]], actions: List[Action]) -> str:
        # [∇] Assuming that when trace is very short we still use >= 0.95 threshold
        cpi = self.saa.calculate_cpi(states, actions)
        if cpi >= self.saa.cpi_threshold:
            return "Release State"
        else:
            return "Epistemic Escrow / Reflexive Repair"
