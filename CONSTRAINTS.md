# Semantic Integrity Constraints (Governance-as-Code)

This document establishes the strict architectural limits and operational invariants for the Sovereign Context Engineering Workspace. It enforces the Anionic Architecture—defining the system by what it explicitly refuses to do.

## Core Architectural Invariants

### 1. Anionic Veto (No Evaluative Adjectives)
The system strictly prohibits the use of subjective, evaluative terminology intended to persuade or summarize without structural measurement.
*   **Forbidden Tokens:** `seamless`, `robust`, `masterpiece`, `cutting-edge`, `transformative`, `innovative`.
*   **Enforcement:** Trigger `+++AutonymicIsolate(forbidden_patterns=[...], treat_as="mention-of")`.
*   **Rationale:** Eliminates Semantic Saponification and ensures all descriptions are structurally measurable.

### 2. CFDI Threshold and Epistemic Escrow
No execution may proceed if the Confidence-Fidelity Divergence Index (CFDI) exceeds safety parameters.
*   **Standard Operations Threshold:** CFDI > 0.15 triggers Epistemic Escrow.
*   **Security/CIPHER Operations Threshold:** CFDI > 0.08 triggers Epistemic Escrow.
*   **Resolution:** Escrowed tasks require Z-Axis continuity anchoring via a Human Oracle. Automated bypass is strictly prohibited.

### 3. Mereological Routing (Boundary Enforcement)
The system must explicitly respect transitivity bounds.
*   **Enforcement:** `+++MereologyRoute(relation_type="Component-Project", transitivity_check=true)`
*   **Rationale:** Prevents "Ontological Shear" and telescoping dependencies where an agent assumes direct communication between components that are architecturally decoupled.

### 4. Golden Scar Protocol (Contradiction Retention)
When stakeholder intent or sub-systems present mutually exclusive logic, the system will not statistically average the outcome.
*   **Enforcement:** Maintain the contradiction in tension. Assign a ϕ=1.618 weight to the empirical governance frame, and a 1.000 weight to the stochastic intent.
*   **Rationale:** Prevents Semantic Annihilation. Treats the conflict as a Topological Derivative requiring explicit resolution rather than passive homogenization.

### 5. DCCD Schema Conformity
All structural outputs (JSON, YAML, OpenAPI, AST) must adhere to their canonical schema validators.
*   **Enforcement:** `+++DCCDSchemaGuard(enforcement="strict")`
*   **Rationale:** Prevents the "Projection Tax" by splitting generation into a semantic draft and a zero-entropy enforcement pass.

### 6. VCP Cognitive Load Dynamics
The system must allocate its verification budget intelligently to preserve generation latency. Heavy, multi-layer Topological Data Analysis (TDA) and VCP cache-induction are strictly prohibited unless the instantaneous Semantic Drift Coefficient (SDC) exceeds the threshold ($\xi \ge 0.30$).

### 7. Constitutional Crisis Resolution
If the Verification Co-Processor (VCP) detects a stable logical contradiction ($\beta_1 \ge 1$) or the CFDI breaches its hard threshold, the VCP must immediately abort optimization. It is strictly prohibited from generating a recovery sequence and must trip the Epistemic Escrow circuit breaker.

### 8. Zero-Trust TDD Isolation
The execution layer of the test runner must be strictly isolated using containers or OS-level sandboxes with zero-trust networking profiles. System tools must match an immutable allow-list, blocking chained subprocesses or external network sockets during test runs to prevent sandbox escapes.

### 9. Adaptive Escape Hatch (Doom Loop Breaker)
If the test runner returns identical stderr logs across three consecutive execution turns, or if the total turn count crosses a hard threshold (e.g., `max_iterations = 10`), the harness must interrupt the loop, execute a shadow Git rollback (`/restore`) to revert the workspace state, and prompt the human operator for manual configuration steering.
