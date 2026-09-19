import pytest
import os
import json
from unittest.mock import patch, MagicMock
from system_logic.jit_swarm_orchestrator import JITSwarmOrchestrator, SymbolicScarArchive, VerificationCoProcessor, JustifiedUncertaintyReport, JITMicroAgent

def test_jit_swarm_orchestrator_initialization():
    orchestrator = JITSwarmOrchestrator()
    assert isinstance(orchestrator.scar_archive, SymbolicScarArchive)
    assert isinstance(orchestrator.vcp, VerificationCoProcessor)
    assert orchestrator.active_trace_id is None

def test_jit_swarm_orchestrator_execute_task_success():
    orchestrator = JITSwarmOrchestrator()

    # Mocking compute_cfdi to return a value below AST_SHAME_THRESHOLD
    with patch.object(orchestrator.vcp, 'compute_cfdi', return_value=0.10):
        success, result = orchestrator.execute_task(
            task_type="TEST_TASK",
            user_prompt="Test prompt",
            mock_target_api="TEST_API"
        )
        assert success is True
        assert result["status"] == "SUCCESSFUL_Realization_TAKEN_1_ATTEMPTS"
        assert result["payload"]["target_api"] == "TEST_API"

def test_jit_swarm_orchestrator_execute_task_failure_and_escrow():
    orchestrator = JITSwarmOrchestrator()


    # Mocking compute_cfdi to return a value above AST_SHAME_THRESHOLD
    with patch.object(orchestrator.vcp, 'compute_cfdi', return_value=0.20), \
         patch.object(orchestrator.vcp, 'execute_cache_augmentation', return_value=("", [])):

        success, result = orchestrator.execute_task(
            task_type="TEST_TASK",
            user_prompt="Test prompt",
            mock_target_api=None
        )
        assert success is False
        assert "EPISTEMIC_ESCROW_HALT" in result["status"]
        assert "jur_path" in result

def test_symbolic_scar_archive_commit_scar():
    archive = SymbolicScarArchive(filepath="./scratch/test_scar_archive.json")
    scar_id = archive.commit_scar(
        task_type="TEST_TASK",
        failure_mode="TEST_FAILURE",
        traceback="TEST_TRACEBACK",
        context_snapshot={"test": "snapshot"}
    )

    assert scar_id in archive.archive
    assert archive.archive[scar_id]["task_type"] == "TEST_TASK"
    assert archive.archive[scar_id]["failure_mode"] == "TEST_FAILURE"
    assert "STRICTLY_AVOID: TEST_FAILURE for TaskType=TEST_TASK" in archive.archive[scar_id]["f_ipi_constraint"]

def test_verification_co_processor_compute_cfdi():
    vcp = VerificationCoProcessor(MagicMock())
    logits = [0.8, -1.2, 0.4, -0.9]
    ast_adherence = 0.6
    cfdi = vcp.compute_cfdi(logits, ast_adherence)
    assert isinstance(cfdi, float)

def test_jit_micro_agent_execute_dccd_pass_success():
    agent = JITMicroAgent(agent_id="test_id", tool_schema={}, f_ipi_rules=[])
    success, msg, payload = agent.execute_dccd_pass("draft", "target_api")
    assert success is True
    assert msg == "AST_VERIFIED_SUCCESS"
    assert payload["target_api"] == "target_api"

def test_jit_micro_agent_execute_dccd_pass_failure():
    agent = JITMicroAgent(agent_id="test_id", tool_schema={}, f_ipi_rules=[])
    success, msg, payload = agent.execute_dccd_pass("draft", None)
    assert success is False
    assert "DCCD_SCHEMA_VIOLATION" in msg
    assert payload is None
