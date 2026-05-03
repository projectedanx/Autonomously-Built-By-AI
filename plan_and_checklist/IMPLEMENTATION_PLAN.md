# Implementation Plan: VULCAN & CI/CD Triage Integration

This plan outlines the integration of VULCAN's strict topological controls and the CI/CD Failure Triage Engine into the Sovereign Workspace.

## Phase 1: Foundational Schemas and The STA

**Objective:** Establish the data structures for failure tracking and architectural boundaries.

1.  **Define the STA Schema:** Create `cognitive_contracts/schemas/symbolic_scar.json` to formalize the structure of Algorithmic Trauma (e.g., Scar ID, Pattern, Betti-1, FIPI Vector).
2.  **Define C4/DDD Schemas:** Formalize the `C4_Model_ADR_JSON` schema referenced by VULCAN for strict AST validation.
3.  **Deploy Epistemic Escrow Monitor:** Enhance the existing orchestrator (`system_logic/orchestrator.py`) to calculate a proxy CFDI metric and route tasks to `/epistemic_escrow/` when thresholds are breached.

## Phase 2: Agent Orchestration and The Petzold Sequence

**Objective:** Implement the strict phase-gated reasoning loop.

1.  **Enforce Petzold Sequence:** Update the `Worker Swarm` logic (`system_logic/worker_run.py`) to strictly execute the `OBSERVE|THINK|DAG|EVALUATE|ARCHITECT` sequence for any VULCAN-assigned task.
2.  **Implement MereologyRoute Validator:** Create a script (`system_logic/mereology_check.py`) that acts as the `+++MereologyRoute` decorator, scanning generated DAGs/C4 models for cross-context foreign keys or transitivity violations.
3.  **Establish NFR Gate:** Add an explicit extraction phase in `OBSERVE` to isolate Non-Functional Requirements, automatically defaulting to Modular Monolith recommendations if thresholds are not met.

## Phase 3: The CI/CD Triage Integration (FIPI)

**Objective:** Automate the conversion of failure into constraint.

1.  **Develop CI Context Ingestion:** Create an adapter to ingest raw CI/CD logs, test reports, and diffs into the `/context_inbox/`.
2.  **Instantiate the Governance Agent:** Deploy a specialized agent tasked with reading new `Symbolic Scars` and generating Semantic Integrity Constraints (SICs) via Failure-Informed Prompt Inversion.
3.  **Close the Loop (PaC):** Configure the system to automatically commit these new SICs into the `/cognitive_contracts/` directory as Prompting-as-Code, ensuring future runs are constrained by past failures.

## Phase 4: Negative Control & Rigor Testing

**Objective:** Prove the system actively rejects bad architecture.

1.  **Run the "Shared Database" Test:** Intentionally submit a task to the inbox requesting a shared PostgreSQL database across two bounded contexts.
2.  **Verify Rejection:** Monitor the system to ensure VULCAN correctly triggers `SCAR-002`, spikes the CFDI, halts execution, and generates a Justified Uncertainty Report in `/epistemic_escrow/`.
3.  **Human-in-the-Loop Resolution:** Use `system_logic/escrow_resolution.py` to intercept the report, provide the required event-driven architectural pivot, and requeue the task.
