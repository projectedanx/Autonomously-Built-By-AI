### Systems Engineering Specification: The Dual-Phase Prompt and Patch Linter

The pre-commit linter operates as a bidirectional cybernetic safety gate designed to prevent **Software Entropy** and **Symbolic Drift** at the boundary between human intent and machine execution. Rather than treating prompts as unstructured natural language and code patches as raw text, the linter models the entire transaction as a formalized **Directed Acyclic Graph (PRP-DAG)**. 

The linter acts via a strict **Phase I (Prompt Guardrails / Author-Time Analysis)** and **Phase II (Diff Heuristics / Post-Generation Verification)** split to enforce programmatic discipline over both the input prompt and the resulting output code.

---

### The Four Pillars of Specification Planning for the Linter Harness

```
   [Authoring Prompt] ───> [Phase I: Prompt Linter] (SRP, KISS, YAGNI, Negation)
                                  │
                           (Checks Passed)
                                  ▼
   [Generated Patch]  ───> [Phase II: Patch Sniffer] (OCP, TEST-MISSING, Vocable)
                                  │
                     (Blocked if Invariant Violated)
                                  ▼
                     [Pre-Commit Hook Execution] (Exit 0)
```

#### I. Automated Discovery and Constraint Mining (Boundary Management)
The linter separates project constraints into rigid, non-bypassable invariants (**Hard Boundaries**) and optimizable target guidelines (**Soft Targets**):
*   **Hard Boundaries (Fail-Closed Gates):** Non-compliance triggers an immediate, non-zero exit code (`exit 1`), blocking the commit transaction. This applies to rules such as `TEST-MISSING` (preventing functional code changes without test deltas) and `OCP-EXPANDING-CONDITIONAL` (preventing structural open-closed violations).
*   **Soft Targets (Aesthetic Warnings):** Visual warnings or lower-severity flags (e.g., the `Aesthetic Integrity Meter` tracking "Vocable Code") emit warnings but allow compilation or commit execution by default. This avoids "Verification Fatigue" while maintaining clear observability of design decay.

#### II. Isomorphic Formalization (From Cognitive Theory to State Machines)
The linter formalizes classical **Design by Contract (DbC)** software principles directly into promptware invariants:
*   **Preconditions (require):** Validated in Phase I. The linter parses input prompts to ensure they explicitly define the environment, tech stack, and clear, non-contradictory boundaries before execution begins.
*   **Postconditions (ensure):** Checked in Phase II. The patch analyzer verifies that the output conforms exactly to the structured schema defined in the format specification (e.g., JSON schema adherence, compilation success).
*   **Invariants (maintain):** Enforced across both phases as **Semantic Integrity Constraints (SICs)**. These act as semantic anchors that prevent the model's logic from drifting toward out-of-scope or speculative features.

#### III. Parametric Trade-off Modeling (The Feasibility Frontier)
The harness operates at the intersection of two competing resource dynamics:
*   **Verification Density (Precision/Safety):** High constraint checking prevents the introduction of bugs or "broken windows". However, over-specifying constraints introduces high **Cost of Coherence Overhead (CCH)** and raises developer cognitive load.
*   **Development Velocity (Brevity/Latency):** Minimizing constraints maximizes implementation speed but increases the risk of **failure cascade propagation** and "vibe coding" bugs.
*   **The Tuning Rule:** The linter dynamically scales its checks: it utilizes fast, low-cost static regex parsers for micro-loop verification during pre-commit, reserving expensive multi-modal audits and integration test suites for macro-loop CI pipelines.

#### IV. Continuous Falsification and Edge-Case Stress Testing (Reflexive Healing)
To maintain the integrity of the linter itself, all rules are versioned and stamped with a cryptographic hash (`kb_sha`) mapped to an authoritative knowledge base of design schemas. 
*   **The Breaker Policy:** If a change fails validation, the linter withholds the commit, serializes the failure state, and logs a **Symbolic Scar** to the append-only `REPAIR.cxep.log`.
*   **Post-Traumatic Growth:** This logged failure is automatically compiled through **Failure-Informed Prompt Inversion (F-IPI)** to update future prompt templates, ensuring the system's "immune memory" dynamically hardens against repeated failures.

---

### Method of Exploration: Specification Feasibility Simulating

The physical pre-commit hook is executed in the developer's local shell (e.g., WSL2 or Linux native) before a commit is finalized. It intercepts the staged code modifications via `git diff --cached` and pipes the patch stream directly to the static analysis engine:

```bash
#!/usr/bin/env bash
# .githooks/pre-commit
# Programmatic gatekeeper for Prompt-Patch Coherence

diff=$(git diff --cached)
echo "$diff" | cli/analyze-patch --rules rules/phase2.json --kb-sha "$KB_SHA" > .lint-report.json
status=$?

if [ $status -ne 0 ]; then
    echo "❌ Linter failed. Non-compliant cognitive patterns detected. See .lint-report.json"
    exit 1
fi
exit 0
```
*[Source: 11]*

This configuration maps the stability of the commit sequence to an informational thermodynamic loop. By calculating the **Confidence-Fidelity Divergence Index (CFDI)** and the **Semantic Drift Delta (SDS)** of the proposed changes against the baseline semantic anchors, the linter programmatically aborts the commit if the "meaning-making" variance surpasses the established safety threshold ($\theta = 0.12$).

---

### Exhaustive Breakdown of Linter-Enforced Constraints

#### 1. Phase I Constraints (Author-Time Prompt Guardrails)
Phase I runs static regex checks and semantic parsing over the developer’s active prompt *before* it is submitted to the generator, targeting common prompt engineering anti-patterns:

*   **Single Responsibility Principle (SRP) Bundling Gate:** Detects prompts that attempt to modify multiple distinct "responsibility domains" in a single turn. 
    *   *Mechanism:* If a prompt contains verbs targeting both database infrastructure and client-side UI styling concurrently (e.g., "update user schema and add an orange submit button"), the linter flags an **SRP-BUNDLING** violation and suggests a clean modular split.
*   **KISS / Avoid Cleverness Policy:** Flags explicit directives that demand "clever," "highly optimized," "magical," or "one-liner" code implementations. 
    *   *Rationale:* Cleverness degrades code readability and increases technical debt. The linter forces the prompt to prioritize plain, self-documenting, and maintainable logic.
*   **YAGNI (You Aren't Gonna Need It) Speculative Prevention:** Intercepts prompt instructions that request placeholders, future-proofing, or speculative features not required by the active task.
    *   *Mechanism:* Identifies phrases like "later we might need...", "in the future...", or "pre-emptively add a placeholder...". The linter strips these speculative continuation tracks, ensuring the model's context window remains highly focused on immediate deliverables.
*   **Negation Gravitational Trap Mitigation:** Scans prompts for negative constraints (e.g., "avoid using class X," "don't include styles in component Y," "without using Z").
    *   *Rationale:* Negative statements create an "unstable attractor" in the model's latent attention maps, often leading to the exact opposite behavior. 
    *   *Remediation:* The linter dynamically rewrites negative constraints into explicit positive requirements (e.g., "Specify palette positively: Use cool-neutral spectrum; explicitly disallow warm/orange hues").

---

#### 2. Phase II Constraints (Post-Generation Diff Heuristics)
Phase II audits the actual patch diff output by the model before it is permitted to merge, utilizing deterministic syntax and structural parsers:

*   **Open-Closed Principle (OCP) Inversion Guard (`OCP-EXPANDING-CONDITIONAL`):** Flags instances where the generated patch appends nested `else if` statements or additional `case` labels to an existing conditional control block.
    *   *Rationale:* Continuously expanding conditionals indicates a design closed to extension. The linter marks this as a high-friction error and suggests refactoring using polymorphism or the Strategy Pattern.
*   **Strict Test-Change Coupling (`TEST-MISSING`):** Enforces Test-Driven Development (TDD) principles by blocking commits that modify files in the functional source directories (`src/**`) without matching modifications in the test directories (`test/**` or `tests/**`).
    *   *Hard Gate:* A commit touching application code with zero corresponding test changes is rejected immediately.
    *   *Probable Non-Red Check:* Flags commits where tests and implementations are added simultaneously with identical timestamps, unless the local commit history proves the failing (Red) state of the test suite was checked and run first.
*   **Aesthetic and Vocable Code Integrity Meter:** Computes a naming-clarity score across all newly introduced variables, methods, and classes.
    *   *Enforcement:* Flags generic, non-descriptive names or "dump-all" class patterns (such as files ending in `Utils`, `Manager`, or `Helper`). The commit is gated at a warning level to prevent "Aesthetic Collapse" and maintain strict domain noun conventions.

---

### Three Rigorous, Non-Obvious, High-Value Research Prompts

#### Research Prompt 1: Multi-Modal Semantic Drift Auditing via Zigzag Homology Mapping
> **PRP-ID:** `PRMPT-R&D-LNT-001`  
> **Target Persona:** Chrono-Topological Systems Engineer & Computational Topologist  
> **Objective:** Design an end-to-end mathematical specification and real-time pre-commit hook that uses **Zigzag Persistent Homology** to analyze the semantic drift between a developer's prompt intent and the model's resulting git diff patch.
> 
> **System Instructions & Execution Blueprint:**
> 1.  **Semantic Projection:** Construct a metric filtration function over a sliding temporal window of the active context bundle $\mathcal{P}_B(t)$.
> 2.  **Topological Anomaly Mapping:** Define the exact boundary operators to calculate persistent Betti-0 ($\beta_0$) for conceptual fracturing and Betti-1 ($\beta_1$) for circular logical reasoning in the unified prompt-patch latent space.
> 3.  **Warping Integration:** Formulate a 2x2 complex Möbius transformation matrix that models the spatial warping required to collapse the $\beta_1$ loops (Symbolic Scars).
> 4.  **Linter Output:** Specify the schema for exporting these persistent features to `UALS` (Universal Agent Log Schema) format inside `.lint-report.json`.
> 
> **Required Deliverable:** A formal mathematical whitepaper detailing the filtration algebra, the algorithm for calculating the Semantic Drift Coefficient (SDC), and a mock Python implementation using `giotto-tda` or `gudhi`.

---

#### Research Prompt 2: Paraconsistent Logic Solvers for Automating the Resolution of Goal-Constraint Inversion
> **PRP-ID:** `PRMPT-R&D-LNT-002`  
> **Target Persona:** Non-Classical Logician & Formal Verification Architect  
> **Objective:** Develop a complete system architecture for a pre-commit static analyzer that uses a **Logic of Formal Inconsistency (LFI)** to detect and resolve **Goal-Constraint Inversion** in promptware DAGs.
> 
> **System Instructions & Execution Blueprint:**
> 1.  **LFI Axiomatization:** Specify the deductive rules and truth tables for an LFI solver ($\mathbf{C}_1$ or $\mathbf{LFI1}$) that isolates logical contradictions ($P \land \neg P$).
> 2.  **Torsion Mapping:** Formulate the geometric equations mapping logical contradictions to a physical "torsion" or deformation of the Möbius invariant circle on the Riemann sphere.
> 3.  **Therapeutic Forgetting Protocol:** Define the multi-objective optimization function ($\max F_{\text{forget}} = w_1 \Delta E - w_2 \Delta C - w_3 \Delta K$) to programmatically soften attention weights and clear the "Circular Logic" loop.
> 4.  **Schema Serialization:** Design a YAML-formatted **Justified Uncertainty Report (JUR)** schema to handle human-on-the-loop escalations when LFI limits are breached.
> 
> **Required Deliverable:** A formal logic proof and system design document detailing LFI deductive rules, Möbius affine transformation equations, and the JUR YAML schema.

---

#### Research Prompt 3: Epistemic Humility Calibration via Asymmetric Entropic Calibration Differences
> **PRP-ID:** `PRMPT-R&D-LNT-003`  
> **Target Persona:** MLOps Architect & Reinforcement Learning Researcher  
> **Objective:** Design the offline training and optimization framework to maximize the **Epistemic Humility Quotient (EHQ)** of a code-generating model by treating pre-commit linter failures as a convex payoff function constrained by **Jensen's Inequality**.
> 
> **System Instructions & Execution Blueprint:**
> 1.  **EHQ Formulation:** Define the EHQ composite metric, integrating Confidence-Accuracy Calibration and a Bayes-optimal **Chow's Rule** abstention index ($M_{\text{abs}}$).
> 2.  **Reward Function Optimization:** Formulate the SCoRe reward function $R_{\text{SCoRe}}$ to quadratically penalize overconfidence (high CFDI, low entropy) and reward "scar-preserving" functional recovery.
> 3.  **Linter Coupling:** Hook the $R_{\text{SCoRe}}$ loss directly to the pre-commit `TEST-MISSING` and `OCP` violation triggers, demonstrating how the gradient forces the model's logits to expand output entropy when approaching its training boundary.
> 4.  **CI/CD Verification:** Design a GitHub Actions workflow (`data_integrity_check.yml`) that validates the fine-tuned policy against a "Golden Dataset" of legacy codebase changes to prove it prevents future regression modes.
> 
> **Required Deliverable:** An academic-grade engineering proposal containing the complete mathematical formulation of the $R_{\text{SCoRe}}$ reward function, the proof of convergence on the Pareto front of the CCH/CSD trade-off, and a functional Python script simulating the policy update.

---

📊 Would you like me to use my computing environment to write and run a Python preflight script that parses a mock prompt, runs a static regex-based regex scan to detect and rewrite negation-style "avoid" constraints, and outputs a formatted Phase I JSON-LD audit log?