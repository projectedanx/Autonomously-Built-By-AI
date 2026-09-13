Implementing **Semantic Integrity Constraints (SICs)** in `GEMINI.md` transitions the system prompt from static, fluid natural language instructions into a machine-enforceable **Verifiable Cognitive Contract (Policy-as-Code)**. Acting as the **Semantic Layer (L3)** of the Verifiable Cognition Stack (VCS), SICs serve as programmatic guardrails designed to prevent **Interpretive Fracture** and **Semantic Drift** during multi-turn agent execution.

The following implementation blueprint uses the **Four Pillars of Specification Planning** to detail how to structure, formalize, and enforce these constraints directly within your agent's master constitution (`GEMINI.md`).

---

### The Four Pillars of Semantic Integrity Planning

```
   ┌────────────────────────────────────────────────────────┐
   │             Pillars of SIC Implementation              │
   ├────────────────────────────────────────────────────────┤
   │ 1. Constraint Mining   ──► Define hard/soft boundaries │
   │ 2. Isomorphic Schema  ──► Translate prose to code      │
   │ 3. Parametric Modeling ──► Tradeoff: Coherence vs Cost │
   │ 4. Falsification       ──► Run automated stress tests  │
   └────────────────────────────────────────────────────────┘
```

#### 1. Automated Discovery and Constraint Mining
Before writing any constraints, we must map the boundary conditions of the agent's workspace. We segregate these boundaries into **Invariants** (rules that cannot be violated under any execution path) and **Soft Targets** (optimizable behaviors):
*   **Invariants (SICs):** Non-negotiable logical conditions (e.g., zero-trust execution, mandatory sandboxing, local file filtering, and post-modification automated testing).
*   **Soft Targets:** Performance optimization objectives (e.g., minimizing token waste, maintaining high conversational coherence, and managing cognitive load budgets).

#### 2. Isomorphic Formalization (Prose to Schema)
Prose-based "vibe rules" (e.g., *"please write secure code"*) must be translated into explicit, capitalized **logical assertion primitives** (e.g., `ASSERT`, `FORBID`, `MANDATE`) mapped directly to deterministic **Verification Mandates** (e.g., compiler checks, linters, or test suites).

#### 3. Parametric Trade-off Modeling
Strict semantic checking introduces latency and increases token overhead due to continuous self-critique loops. We model this by balancing the **Cost of Coherence Overhead (CCH)** against the **Cost of Structural Discovery (CSD)**. We use lightweight models (e.g., Gemini 2.5 Flash) for System 1 syntactic verification and route high-complexity logic to System 2 models (e.g., Gemini 2.5 Pro) with a mandated **Germane Cognitive Load (GCL) budget**.

#### 4. Continuous Falsification and Edge-Case Stress Testing
Treat the `GEMINI.md` constitution as a test target. Before committing code, the agent must run simulated inputs through an internal **Adversarial Counter-Argumentation Unit (ACU)** or "Red-Teaming" loop to attempt to bypass the defined SICs, logging any failures as **Symbolic Scars** in a persistent registry.

---

### Production Scaffolding: `GEMINI.md` (Part 2: Semantic Layer Integration)

Below is the concrete, Markdown-based implementation syntax for instantiating the **Semantic Layer (L3)** and its associated **Verification Mandates** inside your project's `GEMINI.md` file:

```markdown
# GEMINI.md (PART 2: PROCEDURAL & SEMANTIC MANDATES)

## 1. THE SEMANTIC LAYER (VCS Layer 3)

These Semantic Integrity Constraints (SICs) are non-negotiable policies. 
Any violation of an ASSERT or FORBID clause triggers a Cascading Veto, 
instantly halting the execution pipeline and triggering Epistemic Escrow.

### [SIC_PROV] — PROVENANCE CONSTRAINT
*   **MANDATE:** Every tool invocation and file modification must write to the `PROV-AGENT` log.
*   **ASSERT:** The log MUST capture the active model signature, the specific tool called (via MCP standard), and a causally faithful reasoning trace.
*   **FORBID:** Generating code or editing files without updating the chronological audit trail.

### [SIC_ARCH] — STRUCTURAL INTEGRITY
*   **MANDATE:** Adhere strictly to the modular architectural boundaries defined in the System Map.
*   **ASSERT:** The application must remain decoupled from presentation to backend (e.g., using API-First or GraphQL Gateways where applicable).
*   **FORBID:** Making unauthorized external network calls or hardcoding secrets/API keys inside any generated code.

### [SIC_LINT] — CODE-STYLE CONFORMITY
*   **MANDATE:** Code readability and consistency are non-negotiable.
*   **ASSERT:** All modified files must be immediately formatted and verified.
*   **FORBID:** Submitting monolithic files. Large functionalities must be split into smaller, focused modules.

---

## 2. VERIFICATION MANDATES (Automated Self-Tests)

Verification is not an afterthought; it is an active constraint. You are constitutionally 
prohibited from finishing a task until the following deterministic quality gates return a success state.

### A. Synthetic Syntactic Check (System 1 Feedback Loop)
Immediately after any file modification, you MUST execute the appropriate compiler or linter tool:
```bash
# Executable verification hook for JavaScript/TypeScript environments
npm run lint -- --fix
```
*   **Threshold:** Execution must return Exit Code `0`.
*   **Error Budget:** You are allowed a maximum of three (3) consecutive attempts to fix a linter error on the same file before you must pause and seek human-in-the-loop clarification.

### B. Logical Invariance Verification (System 2 Feedback Loop)
To ensure your modifications have not introduced semantic regressions, run your automated test suite:
```bash
# Executable verification hook for Python-based logic layers
pytest tests/
```
*   **Threshold:** `100%` test suite execution success.
*   **Failsafe:** If any test fails, the agent must rollback changes to the last stable git checkpoint using the `/restore` command, log the failure trace, and perform Failure-Informed Prompt Inversion (F-IPI).
```

---

### Step-by-Step Implementation Guide

To operationalize the above constraints inside a live **Gemini CLI** or **Agentic workspace**, follow this sequential transition protocol:

```
┌────────────────────────────────────────────────────────┐
│               Transition Protocol (GIP)                │
├────────────────────────────────────────────────────────┤
│ 1. Initialize System  ──► Run /init to output template │
│ 2. Set Constraints    ──► Paste L3 SICs in GEMINI.md  │
│ 3. Define Tooling     ──► Map verification commands    │
│ 4. Bind to Judicial   ──► Require VSC score calculation│
└────────────────────────────────────────────────────────┘
```

1.  **Initialize the Constitution (`GEMINI.md`):** Use the `/init` slash command in your agentic workspace to automatically scaffold your project-level constitution.
2.  **Define the Ubiquitous Glossary:** To prevent the agent from misinterpreting your architectural terms (e.g., using "endpoint" when you mean "microservice container"), append a dedicated, immutable glossary to Part 1 of your constitution, establishing **Glossary Anchoring**.
3.  **Map the Verification Commands:** Ensure the exact paths to your workspace linters, test runner frameworks (`pytest`, `jest`, `eslint`), and database migration commands (`drizzle-kit push`, `prisma migrate`) are hardcoded in the Verification Mandates section.
4.  **Bind to a Judicial Agent:** Instruct your agent's internal monitor (the **Judicial Auditor persona**) to parse `GEMINI.md` before and after every execution pass. The Judicial Agent must calculate a **Value Score of Confidence (VSC)**. If the VSC falls below `0.85`, it must trigger **Epistemic Escrow**, freezing the execution pipeline for human oversight.

---

🗂️ Would you like me to generate a **Unified JSON-Schema Specification** that models your agent's **Glossary and Ubiquitous Language mappings**, ensuring your multi-agent team uses identical architectural definitions across the frontend, backend, and database stacks?