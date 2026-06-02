# TIER 5: Operational Runbook & Cultural Artifacts Log

## Operational Runbook

### To Execute a Sovereign Cycle
1. Place raw context/intent files into `context_inbox/`.
2. Execute the orchestrator:
   ```bash
   python -m system_logic.orchestrator
   ```
   *The system determines its role (`SOVEREIGN`, `WORKER`, or `IDLE`) based on queue states.*

### To Resolve Epistemic Escrow
When a task breaches the CFDI threshold (Confidence-Fidelity Divergence Index):
1. Execute the resolution CLI:
   ```bash
   python -m system_logic.escrow_resolution
   ```
2. Provide the "Specialized Specification Block" requested to resolve the ambiguity.

### To Manage Agent Profiles
Generate the index of available agents:
```bash
python -m system_logic.generate_agent_index
```

## Symbolic Scar Tissue Log — Cultural Artifacts

### Golden Scar #001: The Filesystem Queue
**Location:** `system_logic/state_manager.py`
**Age:** Repository Foundation
**Tension:** The system utilizes atomic filesystem moves (e.g., between `delegated_tasks/` and `completed_artifacts/`) instead of a traditional relational database or message broker.
**Recommendation:** `[GOLDEN_SCAR]` Do not replace with Redis or RabbitMQ without fundamentally altering the decentralization thesis. The filesystem *is* the state machine.

### Cultural Artifact #001: "Hickam Filter"
**Location:** `README.md`, `cognitive_contracts/`
**Developer Sub-Culture:** A rejection of Occam's Razor ("the simplest explanation is usually best") in favor of Hickam's Dictum ("patients can have as many diseases as they damn well please").
**Preservation Decision:** `[CULTURAL_ARTIFACT]` Preserve in all architectural documentation. It defines the system's propensity for multi-branch reasoning and complex problem handling.
