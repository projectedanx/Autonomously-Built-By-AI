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
