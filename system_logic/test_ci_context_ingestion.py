import pytest
import os
import json
from system_logic.ci_context_ingestion import CIContextAdapter

def test_ingest_algorithmic_trauma(tmp_path):
    adapter = CIContextAdapter(workspace_root=str(tmp_path))

    # Mock CI Log
    raw_log = "Error: ConnectionRefusedError: [Errno 111] Connection refused. Service B is unreachable from Service A."
    job_metadata = {
        "job_id": "job-87123",
        "stage": "integration_test",
        "services": ["ServiceA", "ServiceB"]
    }

    ingested_file_path = adapter.ingest_failure(raw_log, job_metadata)

    assert os.path.exists(ingested_file_path)

    with open(ingested_file_path, 'r') as f:
        data = json.load(f)

    assert data["type"] == "ALGORITHMIC_TRAUMA"
    assert data["metadata"]["job_id"] == "job-87123"
    assert "ConnectionRefusedError" in data["raw_log"]
    assert "Betti-1" in data["topological_implication"]

def test_generate_symbolic_scar(tmp_path):
    adapter = CIContextAdapter(workspace_root=str(tmp_path))
    # Test FIPI preparation from trauma
    trauma_data = {
         "type": "ALGORITHMIC_TRAUMA",
         "metadata": {"job_id": "job-87123"},
         "raw_log": "Error: ConnectionRefusedError: [Errno 111] Connection refused. Service B is unreachable from Service A."
    }

    scar = adapter.transform_to_scar(trauma_data)

    assert scar["type"] == "CI_PIPELINE_FAILURE"
    assert scar["trigger"] == "ConnectionRefusedError"
    assert "Service B" in scar["description"]
