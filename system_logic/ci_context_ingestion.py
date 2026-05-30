import os
import json
import uuid
import datetime
from typing import Dict, Any

class CIContextAdapter:
    """
    Ingests unstructured CI/CD failure logs and translates them into
    structured 'Algorithmic Trauma' payloads for the Sovereign Workspace.
    """
    def __init__(self, workspace_root: str = "."):
        self.root = workspace_root
        self.inbox_dir = os.path.join(self.root, "context_inbox")
        os.makedirs(self.inbox_dir, exist_ok=True)

    def ingest_failure(self, raw_log: str, job_metadata: Dict[str, Any]) -> str:
        """
        Parses a raw log, determines topological implication, and writes it to the inbox.
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        trauma_id = f"TRAUMA-{timestamp}-{uuid.uuid4().hex[:6].upper()}"

        # Simple heuristic for topological implication (mocking the Betti-1 mapping)
        topological_implication = "Unknown Deformation"
        if "ConnectionRefusedError" in raw_log or "Timeout" in raw_log:
             topological_implication = "Potential Betti-1 Loop: Network boundary isolation or deadlocked transitivity."

        payload = {
            "id": trauma_id,
            "type": "ALGORITHMIC_TRAUMA",
            "timestamp": timestamp,
            "metadata": job_metadata,
            "raw_log": raw_log,
            "topological_implication": topological_implication,
            "requires_fipi": True
        }

        file_path = os.path.join(self.inbox_dir, f"{trauma_id}.json")
        with open(file_path, 'w') as f:
            json.dump(payload, f, indent=2)

        return file_path

    def transform_to_scar(self, trauma_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Transforms Algorithmic Trauma into a structured Symbolic Scar for the STA.
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        scar_id = f"SCAR-{timestamp}-{uuid.uuid4().hex[:6].upper()}"

        # Extremely basic log parsing logic
        trigger = "UNKNOWN_ERROR"
        if "ConnectionRefusedError" in trauma_data.get("raw_log", ""):
            trigger = "ConnectionRefusedError"

        scar = {
            "id": scar_id,
            "timestamp": timestamp,
            "type": "CI_PIPELINE_FAILURE",
            "trigger": trigger,
            "description": f"Failure derived from {trauma_data.get('metadata', {}).get('job_id')}. {trauma_data.get('raw_log', '')[:100]}...",
            "cfdi_score": 0.20, # Assume CI failures introduce high uncertainty initially
            "related_ticket": "NONE"
        }
        return scar
