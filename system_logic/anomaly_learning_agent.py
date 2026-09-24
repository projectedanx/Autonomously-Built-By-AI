class AnomalyLearningAgent:
    """Anomaly Learning Agent (ALA) for detecting 'grey-zone misuse'."""
    def __init__(self, warning_threshold=0.40, breach_threshold=0.80):
        self.warning_threshold = warning_threshold
        self.breach_threshold = breach_threshold
        self.watchlist = set(["plugin_install", "delete_user", "execute_script"])
        self.weights = {"w1": 0.4, "w2": 0.3, "w3": 0.2, "w4": 0.1}

    def add_to_watchlist(self, tool_name: str):
        self.watchlist.add(tool_name)

    def _compute_entropy_gradient(self, tool: str) -> float:
        # Mock calculation of entropy gradient
        return 0.25 # Safe baseline

    def _execute_nesy_synthesis(self, tool: str) -> dict:
        # Mock synthesis returning sub-scores
        return {
            "S_neural": 0.5,
            "S_bicm": 0.3,
            "S_recon": 0.2,
            "F_symbolic": 0.1
        }

    def evaluate_action(self, tool: str, entropy_gradient: float = None) -> dict:
        """Evaluates an action through the ALA Guard pipeline."""
        is_watchlisted = tool in self.watchlist

        if entropy_gradient is None:
            entropy_gradient = self._compute_entropy_gradient(tool)

        if not is_watchlisted and entropy_gradient <= self.warning_threshold:
            return {"status": "LAMINAR", "action": "execute_unhindered", "risk_score": 0.0}

        # Trigger heavy NeSy ALA Evaluation suite
        scores = self._execute_nesy_synthesis(tool)
        risk_score = (self.weights["w1"] * scores["S_neural"] +
                      self.weights["w2"] * scores["S_bicm"] +
                      self.weights["w3"] * scores["S_recon"] +
                      self.weights["w4"] * scores["F_symbolic"])

        if risk_score < self.breach_threshold:
            return {"status": "LAMINAR", "action": "execute_unhindered", "risk_score": risk_score}
        else:
            return {
                "status": "BREACH",
                "action": "halt_and_await_hitl",
                "risk_score": risk_score,
                "message": "Synchronous execution halt. Traceback mapped to SEPAO Graph."
            }
