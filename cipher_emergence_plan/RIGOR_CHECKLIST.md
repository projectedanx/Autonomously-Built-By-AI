# CIPHER Rigor Checklist

## Pre-Flight
- [ ] Ensure `cipher_emergence_plan/` directory is created and populated.
- [ ] Review `SEC-AGENT-FORGE-001` blueprint for core invariants.

## Phase 1: Core Modifications
- [ ] `system_logic/worker_run.py`: Implement PetzoldSequence phase isolation (`THINK|THREAT_MODEL|AUDIT|REPORT`).
- [ ] `system_logic/worker_run.py`: Implement CIPHER-specific CFDI threshold (0.08).
- [ ] `system_logic/state_manager.py`: Enhance `escrow_task` to handle CIPHER-specific conflict reasons.

## Phase 2: Memory & Constraints
- [ ] `system_logic/state_manager.py`: Update `record_scar` to support FIPI rule generation and tracking.
- [ ] `system_logic/state_manager.py`: Implement tracking of scar activation counts (prevent Epistemic Sclerosis).

## Phase 3: Testing & Documentation
- [ ] Verify modifications via `pytest tests/ system_logic/`.
- [ ] Check for syntax errors or logical breaks in the newly added phase tracking.
- [ ] Update `README.md` to reflect CIPHER integration and address any legacy agent laziness issues.
