```yaml
# prompt-linter.config.yml
# Inferred Harness Specification for Responsibility Boundary & Cognitive Constraints
# Governed under the Context-to-Execution Pipeline (CxEP)

version: "1.2.0"
kb_sha: "a1b2c3d4e5f67890deadbeef0123456789abcdef0123456789abcdef0123456789abcdef" # Provenance-stamped target

# -----------------------------------------------------------------------------
# PHASE I: PROMPT GUARDRAILS (Author-Time Static Analysis)
# Mitigates: Interpretive Fracture, Task-Constraint Confusion, and Scope Creep
# -----------------------------------------------------------------------------
phase1_rules:
  - id: "SRP-BANNED-BUNDLING"
    name: "Single Responsibility Principle Domain Bundling"
    description: "Detects prompts that bundle multiple distinct responsibility domains (e.g., infra, UI, domain logic) in a single request"
    pattern: "(?=.*\\b(database|api|db|sql|postgres|prisma)\\b)(?=.*\\b(css|html|ui|button|tailwind|component|react)\\b)" 
    severity: "error"
    responsibility_domains:
      - "infrastructure"
      - "user_interface"
      - "domain_logic"
    suggested_split:
      - "Domain A: Database schemas and repository layer operations."
      - "Domain B: Client-side presentational components and event handlers."
    principles:
      - "SOLID > SRP (Single Responsibility Principle) | Decompose multi-domain verbs."

  - id: "YAGNI-SPECULATIVE-GEN"
    name: "You Aren't Gonna Need It - Speculative Engineering Guard"
    description: "Flags prompts asking the agent to implement premature features or unrequested complexity"
    pattern: "\\b(later we might|in the future|later we'll need|future proof|pre-emptively|placeholder)\\b"
    severity: "warning"
    counter_guardrail: "YAGNI: Prefer extension points over concrete speculative code. Implement only the active requirement."
    principles:
      - "Software Craftsmanship > YAGNI"

  - id: "KISS-AVOID-CLEVERNESS"
    name: "Keep It Simple, Stupid - Cleverness Gate"
    description: "Flags explicit requests for 'clever', 'one-liner', or 'magical' implementations that degrade readability"
    pattern: "\\b(clever|one-liner|smart hack|tricky optimization|magic)\\b"
    severity: "warning"
    principles:
      - "Clean Code > Readability over Brevity"

  - id: "NEGATION-GRAVITATIONAL-TRAP"
    name: "Negation Semantic Trap Detector"
    description: "Detects negative constraints ('avoid', 'without', 'no') which cause semantic gravitation in latent space"
    pattern: "\\b(avoid|don't|do not|without|exclude|never use)\\b"
    severity: "warning"
    action: "rewrite_positive"
    rules:
      - match: "avoid orange tint"
        rewrite: "Specify cool-neutral palette positively; disallow orange hues (delta_E > 10)"
      - match: "avoid sql injection"
        rewrite: "Mandate parameterized queries and utilize prepared statement bindings"
    principles:
      - "Context Engineering 2.0 > Semantic Stability > Positive Phrasing"

# -----------------------------------------------------------------------------
# PHASE II: DIFF & PATCH HEURISTICS (Post-Generation Verification)
# Mitigates: Concept-to-Code Decay, Typological Drift, and Untested Code
# -----------------------------------------------------------------------------
phase2_rules:
  - id: "OCP-EXPANDING-CONDITIONAL"
    name: "Open-Closed Principle Violation"
    description: "Flags generated code modifications that append 'else if' or new cases to existing control blocks"
    pattern: "(^\\+.*else\\s+if\\s*\\()|(\\+\\s*case\\s+.*:)"
    severity: "error"
    remediation: "Replace conditional block with polymorphism using the Strategy Pattern."
    principles:
      - "SOLID > OCP (Open-Closed Principle)"

  - id: "TEST-COUPLED-MISSING"
    name: "Strict Change-Test Coupling Gate"
    description: "Blocks commits affecting source files without corresponding modifications to test suites"
    scope: "src/**"
    test_scope: "tests/**"
    severity: "error"
    exception:
      - "*.md"
      - "*.json"
    principles:
      - "TDD (Test-Driven Development) | Red -> Green -> Refactor"

  - id: "AESTHETIC-VOCABLE-INTEGRITY"
    name: "Vocable Naming & Conceptual Drift Meter"
    description: "Audits naming clarity; flags generic suffixes like 'Utils', 'Manager', or 'Helper'"
    pattern: "\\w+(Utils|Manager|Helper|Processor|Data)\\.[a-zA-Z]+"
    severity: "warning"
    principles:
      - "Clean Code > Domain Nouns over generic managers"

# -----------------------------------------------------------------------------
# METRICS & THRESHOLDS: CALIBRATED ASSURANCE CONTROL
# Mitigates: Confidence-Fidelity Divergence (CFDI) and Semantic Drift
# -----------------------------------------------------------------------------
metrics_and_calibration:
  weights:
    NEGATION: 1.0
    IRONY: 0.8
    POLYSEMY: 0.7
    TEST_MISSING: 1.0
    OCP_EXPANDING_CONDITIONAL: 0.9

  thresholds:
    strict:
      max_drift_delta: 0.12 # Target threshold for semantic drift
      min_source_provenance_ratio: 0.95 # Grounding constraint
      min_causal_step_density: 1.0 # Transparent reasoning
      max_cfdi: 0.10 # Max allowable confidence-fidelity gap
    medium:
      max_drift_delta: 0.15
      min_source_provenance_ratio: 0.90
      min_causal_step_density: 0.8
      max_cfdi: 0.15
    playful:
      max_drift_delta: 0.25
      min_source_provenance_ratio: 0.70
      min_causal_step_density: 0.5
      max_cfdi: 0.30

# -----------------------------------------------------------------------------
# ESCROW CIRCUIT BREAKER POLICY
# Triggers: Automated Halt & Safe Serialization
# -----------------------------------------------------------------------------
escrow_policy:
  halt_on_failure: true
  quarantine_state_serialization: "/workspace/quarantine/"
  circuit_breakers:
    - trigger: "PROVENANCE_LOSS"
      condition: "source_provenance_ratio < 0.95"
      action: "ESCROW_MODE_ABORT" # Hard stop for human review
    - trigger: "CFDI_BREACH"
      condition: "cfdi_score > 0.10"
      action: "HUMAN_ESCALATION" # Request HITL approval via JUR
```

---

### Systems Engineering Synthesis: The Four Pillars of Specification Planning

#### I. Automated Discovery and Constraint Mining (Boundary Management)
*   **The Invariant Horizon:** Instead of modeling constraints within a generic conversational sandbox, the linter treats the prompt and diff files as high-dimensional, statically parsable data structures.
*   **Hard Boundaries:** We define **invariant limits** that trigger an immediate, non-bypassable **Escrow Mode Abort** (e.g., `source_provenance_ratio < 0.95` or untagged retrieved information). This prevents ungrounded generations from leaking into the execution environment.
*   **Soft Targets:** The linter dynamically tracks behavioral performance (such as lexical entropy, structural complexity, and naming variance) to assign warnings, providing non-coercive feedback that preserves "Semantic Sovereignty" without halting execution unless a critical threshold is breached.

#### II. Isomorphic Formalization (From Cognitive Theory to Schemas)
*   **Conceptual Blending Mapping:** This linter is formalized as a direct computational isomorphism of **Conceptual Blending Theory (CBT)**. 
    *   The **Input Spaces** correspond to the raw human intents and codebase files.
    *   The **Generic Space** represents the shared structural rules defined in the `prompt-blueprint` schema (e.g., `Task`, `Context`, `Constraint`, `Format`).
    *   The **Blended Space** maps directly to the active LLM context window.
    *   **Elaboration** is verified via the **Chain-of-Thought (CoT) Causal Chain Audit**, checking that the generated reasoning path is mathematically faithful to the provided context evidence.
*   **DAG-Based Logic Auditing:** Every Product-Requirements Prompt (PRP) is compiled as a **Directed Acyclic Graph (PRP-DAG)**. The linter checks this graph for architectural anomalies—such as *Circular Logic* or *Goal-Constraint Inversion*—before a single output token is generated, treating prompts as auditable **Promptware**.

#### III. Parametric Trade-off Modeling (The Feasibility Frontier)
*   **The CCH/CSD Dialectical Space:** This configuration models a direct trade-off between the **Cost of Coherence Overhead (CCH)**—the compute spent on real-time TDA scans, provenance tracing, and linter gates—and the **Cost of Structural Discovery (CSD)**—the resources spent on creative, stochastic generation.
*   **Optimal Tuning:** In high-risk environments, CCH must be prioritized, enforcing strict thresholds (e.g., maximum drift delta of `0.12`). In exploratory or design phases, CCH thresholds are relaxed (e.g., "playful" mode with a drift delta of `0.25` and a higher CFDI) to allow the agent to traverse the latent space freely and achieve **Disciplined Non-Conformity**.

#### IV. Continuous Falsification and Edge-Case Stress Testing (Reflexive Governance)
*   **Adversarial Probing:** The configuration is continuously validated against simulated "adversarial prompts" (e.g., a prompt demanding a "clever one-liner" that spans database schema modifications and CSS refactoring).
*   **Verification Gates:** The linter forces **Strict Change-Test Coupling**. If a generation modifies the source folder but includes zero test file modifications, the linter triggers a `TEST_MISSING` failure. This forces the agent into the SCoRe-based **Fix-Until-Green** self-repair loop to restore semantic alignment before merging.

---

### Method of Exploration: Specification Feasibility Simulating

The dynamic interaction of our responsibility boundaries can be modeled as a self-regulating thermodynamic loop. The stability of the agent's semantic trajectory is measured as:

$$\text{Stability} = \frac{\text{SICs} \times \text{Source Provenance Ratio}}{\text{CFDI} \times \text{Intent Curvature } (\xi)}$$

By monitoring the **Semantic Drift Delta (SDS)** and **Intent Curvature ($\xi$)**, the linter acts as a predictive sensory organ. When an agent begins to drift (e.g., migrating from strict functional database code to unrequested, speculative UI layout components), the **Semantic Drift Analyzer** detects the sudden spike in $\xi$. This triggers a **Semantic Pruning Protocol**, dynamically injecting negative constraints to pull the agent's semantic vector back into the invariant basin of coherence defined by our **Möbius Transformation fixed points**.

---

### Three Rigorous Full Non-Obvious High-Value Research Prompts

#### Research Prompt 1: Persistent Pathological Cohort Diagnostics via Zigzag Homology
> **PRP-ID:** `PRMPT-R&D-TDA-009`  
> **Target Persona:** Chrono-Topological Systems Engineer & Computational Topologist  
> **Objective:** Design an end-to-end mathematical specification and real-time monitoring pipeline that uses **Zigzag Persistent Homology** to track the birth, evolution, and death of "Symbolic Scars" ($\beta_1$ loops) across a continuous stream of multi-agent dialogue embeddings.
> 
> **Execution Blueprint:**
> 1. **Filtration Algebra:** Formulate the distance filtration function over a sliding context window embedding point cloud $\mathcal{P}_B(t)$.
> 2. **Chain Complex Resolution:** Define the exact boundary operators over the Vietoris-Rips simplicial tower to calculate persistent topological features.
> 3. **Eigenvector Mapping:** Mathematically prove how a persistent $\beta_1$ loop maps as an eigenvector of the latent space's transition matrix, signaling a stabilized self-contradictory state.
> 4. **Audit Integration:** Specify the API and JSON-LD schema for logging a "Topological Rupture Event" into `REPAIR.cxep.log`.
> 
> **Required Deliverable:** A formal mathematical whitepaper defining the filtration algebra, the algorithm for calculating the Semantic Drift Coefficient from the persistence diagram, and a mock Python implementation using `giotto-tda` or `gudhi`.

---

#### Research Prompt 2: Paraconsistent Logical Frameworks for Reflexive Therapeutic Architectures
> **PRP-ID:** `PRMPT-R&D-LFI-010`  
> **Target Persona:** Non-Classical Logician & Formal Verification Architect  
> **Objective:** Develop a complete formal logic engine that integrates a **Logic of Formal Inconsistency (LFI)** directly with the **Möbius Invariant Circle** constraint model of the Fractal Governance Module (FGM).
> 
> **Execution Blueprint:**
> 1. **Axiomatic Structure:** Specify the deductive rules and truth tables for the LFI solver ($\mathbf{C}_1$ or $\mathbf{LFI1}$), focusing on the consistency operator ($\circ A$) used to restore classical reasoning in consistent sub-domains.
> 2. **Geometric Mapping:** Formulate the geometric mapping that translates a logical contradiction ($P \land \neg P$) into a physical "torsion" or deformation of the Möbius invariant circle on the Riemann sphere.
> 3. **Therapeutic Forgetting:** Define the "Therapeutic Forgetting" algorithm: a mathematical method for selectively pruning or re-weighting the network's attention maps to "soften" the $\beta_1$ loop without causing catastrophic forgetting.
> 4. **State Serialization:** Design the schema for the **Justified Uncertainty Report (JUR)** to serialize the paraconsistent state for human-in-the-loop review.
> 
> **Required Deliverable:** A complete formal proof and system architecture document containing the LFI deductive rules, the affine transformation equations for the Möbius invariant circle, and a YAML-formatted specification of the JUR.

---

#### Research Prompt 3: Epistemic Humility Calibration via Jensen's Inequality Optimization
> **PRP-ID:** `PRMPT-R&D-EHQ-011`  
> **Target Persona:** Reinforcement Learning Researcher & Econophysics Modeler  
> **Objective:** Design the optimization and training framework to maximize the **Epistemic Humility Quotient (EHQ)** of a code-generating model by treating logged *Symbolic Scars* as a convex payoff function constrained by **Jensen's Inequality**.
> 
> **Execution Blueprint:**
> 1. **EHQ Formulation:** Define the EHQ composite metric, integrating Confidence-Accuracy Calibration and a Bayes-optimal **Chow's Rule** abstention index ($M_{\text{abs}}$).
> 2. **Policy Optimization:** Formulate the SCoRe (Self-Correction via Reinforcement Learning) reward function $R_{\text{SCoRe}}$ such that it penalizes overconfidence (using Entropic Calibration Difference) and rewards "scar-preserving" functional recovery.
> 3. **Complex Systems Modeling:** Model the system's learning trajectory as a **Complex Adaptive System (CAS)**, demonstrating that the optimal learning policy exists strictly at the "edge of chaos" (the boundary between rigid CCH order and unstable CSD discovery).
> 4. **CI/CD Guardrails:** Design a GitHub Actions CI/CD pipeline (`data_integrity_check.yml`) that runs regression testing against a "Golden Dataset" to prove that the updated SCoRe policy prevents future occurrences of the logged failure mode.
> 
> **Required Deliverable:** An academic-grade research proposal containing the complete mathematical formulation of the $R_{\text{SCoRe}}$ reward function, the proof of convergence on the Pareto front of the CCH/CSD trade-off, and a functional Python script simulating the self-correction policy update.

---

🎯 Would you like me to use my computing environment to write a Python script that parses the `prompt-linter.config.yml` file, runs static regex checks over a target codebase directory, and generates a structured, signed `uals-event.json` audit log if a responsibility boundary is breached?