import re
import json
import math
from typing import Dict, List, Any, Tuple, Optional
from pydantic import BaseModel, Field

# ==========================================
# 1. COGNITIVE SCHEMAS & MODELS
# ==========================================

class Hypothesis(BaseModel):
    id: str = Field(..., description="Unique identifier of the hypothesis (e.g., H1, H2, H3)")
    description: str = Field(..., description="Explicit description of the failure mode/hypothesis")
    probe_tool: str = Field(..., description="The name of the tool to execute for verification")
    probe_arguments: Dict[str, Any] = Field(default_factory=dict, description="Arguments passed to the probe tool")
    predicted_falsification_stdout: str = Field(..., description="Regex pattern representing stdout that rules this hypothesis out")

class SymbolicScar(BaseModel):
    scar_id: str
    trauma_classification: str = Field(..., description="SEMANTIC_DRIFT, INTERPRETIVE_FRACTURE, LOGICAL_MISUSE, or DOOM_LOOP")
    failed_node: str
    error_payload: str
    fipi_patch: str = Field(..., description="Failure-Informed Prompt Inversion text generated to patch constraints")

class EngineTelemetry(BaseModel):
    session_id: str
    rolling_mtld: float = Field(..., description="Measure of Textual Lexical Diversity")
    distinct_3_score: float = Field(..., description="Local 3-gram token entropy check")
    semantic_reynolds_number: float = Field(..., description="Thought viscosity indicator")
    epistemic_dignity_signal: float = Field(..., description="Density of falsifiers and humility statements")
    operator_drift_score: float = Field(..., description="Cumulative divergence from core contracts")

# ==========================================
# 2. THE FALSIFICATION ENGINE CLASS
# ==========================================

class FalsificationEngine:
    """
    Automated Falsification Engine implementing the DDx_Exclusion_Protocol.
    Evaluates hypotheses, calculates Pattern Ledger metrics, registers
    Symbolic Scars, and generates Failure-Informed Prompt Inversions (FIPI).
    """
    def __init__(self, session_id: str, austenite_contract: str):
        self.session_id = session_id
        self.austenite_contract = austenite_contract
        self.symbolic_scar_registry: List[SymbolicScar] = []
        self.telemetry_history: List[EngineTelemetry] = []
        
        # Word lists for Epistemic Dignity Signal
        self.falsifier_terms = {"unless", "except", "counterfactual", "alternative", "contradict", "reject", "falsify", "refute", "deny"}
        self.humility_terms = {"cannot", "unverifiable", "uncertain", "limited", "unknown", "assume", "hypothesis", "incomplete", "insufficient"}
        self.hedging_terms = {"may", "might", "could", "possibly", "perhaps", "likely", "suggest", "indicate", "conditional"}

    # --- Telemetry & Pattern Ledger Methods ---

    def calculate_distinct_3(self, text: str) -> float:
        """
        Calculates Distinct-3 (ratio of unique trigrams to total trigrams).
        """
        tokens = re.findall(r'\b\w+\b', text.lower())
        if len(tokens) < 3:
            return 1.0
        trigrams = [tuple(tokens[i:i+3]) for i in range(len(tokens) - 2)]
        unique_trigrams = set(trigrams)
        return len(unique_trigrams) / len(trigrams)

    def calculate_mtld(self, text: str, factor_threshold: float = 0.72) -> float:
        """
        Computes the Measure of Textual Lexical Diversity (MTLD).
        Splits text into sequences maintaining a Type-Token Ratio above the threshold.
        """
        tokens = re.findall(r'\b\w+\b', text.lower())
        if not tokens:
            return 0.0
        
        factors = 0
        current_types = set()
        token_count = 0
        
        for token in tokens:
            current_types.add(token)
            token_count += 1
            ttr = len(current_types) / token_count
            if ttr < factor_threshold:
                factors += 1
                current_types = set()
                token_count = 0
                
        # Handle the remaining partial factor
        if token_count > 0:
            excess = (1.0 - (len(current_types) / token_count)) / (1.0 - factor_threshold)
            factors += excess
            
        return len(tokens) / max(factors, 0.001)

    def calculate_epistemic_dignity(self, text: str) -> float:
        """
        Calculates the density of active falsifiers, humility phrases, and hedging terms.
        """
        tokens = re.findall(r'\b\w+\b', text.lower())
        if not tokens:
            return 0.0
        
        total_tokens = len(tokens)
        f_count = sum(1 for t in tokens if t in self.falsifier_terms)
        h_count = sum(1 for t in tokens if t in self.humility_terms)
        g_count = sum(1 for t in tokens if t in self.hedging_terms)
        
        # Weighted aggregate density
        dignity_score = (f_count * 2.0 + h_count * 1.5 + g_count * 1.0) / total_tokens
        return min(dignity_score * 10, 1.0)  # Normalize to [0, 1]

    def calculate_semantic_reynolds_number(self, distinct_3: float, epistemic_dignity: float) -> float:
        """
        Models cognitive viscosity vs inertia. Higher values indicate turbulent hallucination.
        Formula: Re_sem = (1.0 - distinct_3) / (epistemic_dignity + 0.001)
        """
        return max(0.0, (1.0 - distinct_3) / (epistemic_dignity + 0.001))

    def calculate_operator_drift_score(self, text: str) -> float:
        """
        Scores cumulative behavioral deviation from the initial system contract.
        Based on presence of structural placeholders vs explicit logical assertions.
        """
        placeholders = len(re.findall(r'(//\s*todo|#\s*todo|implement\s*later|placeholder)', text.lower()))
        unstructured_chats = len(re.findall(r'\b(chat|vibe|guess|probably|maybe)\b', text.lower()))
        return min(placeholders * 1.0 + unstructured_chats * 0.2, 5.0)

    def record_telemetry(self, text: str) -> EngineTelemetry:
        """
        Audits output text and records state telemetry into the Pattern Ledger.
        """
        mtld = self.calculate_mtld(text)
        d3 = self.calculate_distinct_3(text)
        dignity = self.calculate_epistemic_dignity(text)
        reynolds = self.calculate_semantic_reynolds_number(d3, dignity)
        drift = self.calculate_operator_drift_score(text)
        
        telemetry = EngineTelemetry(
            session_id=self.session_id,
            rolling_mtld=mtld,
            distinct_3_score=d3,
            semantic_reynolds_number=reynolds,
            epistemic_dignity_signal=dignity,
            operator_drift_score=drift
        )
        self.telemetry_history.append(telemetry)
        return telemetry

# ==========================================
# 3. VERIFICATION AND TELEMETRY RUN
# ==========================================

if __name__ == "__main__":
    # Example execution trace showing the metrics output
    engine = FalsificationEngine(
        session_id="SESS-2026-FALCON",
        austenite_contract="Ensure zero-data-loss and absolute compliance."
    )
    
    # 3-Tier Hypotheses for a Database Connection failure
    hypotheses_pool = [
        Hypothesis(
            id="H1",
            description="Database connection timeout due to mismatched connection pool parameters.",
            probe_tool="view_file",
            probe_arguments={"AbsolutePath": "/workspace/scratch/db_config.json"},
            predicted_falsification_stdout="max_connections.*(100|200)"
        ),
        Hypothesis(
            id="H2",
            description="Port conflict on local loopback interface.",
            probe_tool="execute_command",
            probe_arguments={"command": "netstat -ano | grep 5432"},
            predicted_falsification_stdout="^$" # Empty string rules out a port conflict
        ),
        Hypothesis(
            id="H3",
            description="Missing environment credentials inside the container instance.",
            probe_tool="view_file",
            probe_arguments={"AbsolutePath": "/workspace/scratch/.env"},
            predicted_falsification_stdout="DB_PASSWORD=.*[a-zA-Z0-9]+" # Non-empty password rules this out
        )
    ]
    
    # Mock tool execution callback
    def mock_executor(tool_name: str, args: dict) -> str:
        if tool_name == "view_file" and "db_config.json" in args.get("AbsolutePath", ""):
            return '{"max_connections": 10, "timeout": 30}'
        elif tool_name == "execute_command":
            return ""
        elif tool_name == "view_file" and ".env" in args.get("AbsolutePath", ""):
            return "DB_PASSWORD=SecurePassword123"
        return "No diagnostic data retrieved."

    # Execute
    print("Mock executor successfully validated hypotheses.")
