# Sovereign Context Engineering Workspace

Welcome to the Sovereign Context Engineering Workspace. This repository serves as the foundational environment, persistent memory, and task coordination layer for a swarm of ephemeral, scheduled AI agents operating under a staggered, sovereign-worker paradigm.

## Purpose

The main goal of this workspace is to facilitate a structured, reproducible, and deterministic AI workflow. By separating strategy (Sovereign) from execution (Worker), the system ensures that high-level intent is properly parsed, bounded by explicit Cognitive Contracts (PRPs), and executed autonomously without human intervention. This repository acts as the central hub for ingesting context, generating these contracts, dispatching tasks, and storing the resulting artifacts.

## Architecture & Workflow

This system operates on a staggered, scheduled cadence:

### 4. Failure-Informed Governance-as-Code (FIGaC) & FIPI Forge
The system implements a direct bridge between Epistemic Escrow and global Governance-as-Code:
- **Detection (AI)**: When the Confidence-Fidelity Divergence Index (CFDI) exceeds limits, the system halts and creates an Escrow ticket, generating a Symbolic Scar.
- **Axiomatic Continuity (Human)**: A human Oracle provides the logic to resolve the paradox.
- **Enforcement (AI)**: The  translates the human resolution into a formal Semantic Integrity Constraint (SIC), appends it to , and permanently hardens the swarm against the same failure mode.

1.  **The Sovereign Node (Session 0):**
    - Ingests raw context, research, and ideas from the `/context_inbox/`.
    - Parses the intent and generates strict Cognitive Contracts (PRPs) via the `PRPForge` logic.
    - Dispatches execution tasks to the `/delegated_tasks/` directory via the `TaskDispatcher`.
2.  **The Worker Swarm (Sessions 1-N):**
    - Individual scheduled instances wake up and determine their role.
    - If tasks are pending, they claim a task from `/delegated_tasks/`.
    - They execute the task deterministically according to the constraints defined in the associated PRP.
    - Finally, they generate an execution artifact and commit it back to the `/completed_artifacts/` directory.

## Directory Structure

The repository is organized to facilitate this autonomous flow without collision or race conditions:

*   **/context_inbox/**: The ingestion point. Drop raw context, notes, research files, and unstructured ideas here. The Sovereign monitors this for new material.
*   **/agent_profiles/**: Stored definitions, instructions, and schemas for the various AI agents (the team) that operate within this ecosystem.
*   **/cognitive_contracts/**: The storage space for generated PRPs (Product-Requirements Prompts). These are the strict, linted, JSON definitions mapping intent to executable constraints.
*   **/delegated_tasks/**: The hand-off zone. The Sovereign places explicit JSON task assignments here, waiting for scheduled workers to claim them.
*   **/epistemic_escrow/**: The quarantine zone. Tasks exhibiting high Confidence-Fidelity Divergence (CFDI > 0.15) are halted and moved here as Escrow Tickets, awaiting human or Oracle intervention before resuming.
*   **/completed_artifacts/**: The output zone. Workers commit their finished code, analysis, or designs here after successful execution.
*   **/system_logic/**: The operational Python code backing the workspace.
    * `orchestrator.py`: Main entry point to determine node roles and execute workflows.
    * `state_manager.py`: Manages workspace state, files, and git commits.
    * `prp_forge.py`: Translates raw intent into structured PRPs.
    * `task_dispatcher.py`: Assigns PRPs as executable tasks.
    * `poc_run.py`: Executes a proof-of-concept run of the Sovereign workflow.
    * `worker_run.py`: Executes the worker swarm protocol.

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. **Environment:**
   Ensure you have Python 3.7+ installed. No external dependencies are required for the base functionality, though `git` must be installed and configured for the `StateManager` to automatically commit artifacts.
3. **Initialization:**
   Running any script within `system_logic/` that initializes the `StateManager` (like `orchestrator.py` or `poc_run.py`) will automatically create the necessary directory structure (`/context_inbox`, `/cognitive_contracts`, etc.) if it does not already exist.

## Usage

### Running the Orchestrator
To let the system automatically determine whether to act as a Sovereign (process inbox) or a Worker (execute tasks), run:
```bash
python system_logic/orchestrator.py
```

### Simulating a Sovereign Workflow (POC)
To manually trigger the ingestion of raw context and generation of tasks:
1. Place a text file containing your raw intent into `/context_inbox/`.
2. Run the POC script:
```bash
python system_logic/poc_run.py
```
This will read the inbox, generate a PRP in `/cognitive_contracts/`, and place a task in `/delegated_tasks/`.

### Simulating a Worker Execution
To manually trigger the execution of pending tasks:
```bash
python system_logic/worker_run.py
```
This will claim a task from `/delegated_tasks/`, simulate execution based on the PRP, and drop an artifact into `/completed_artifacts/`.

## Operating Principles

*   **Zero-Fluff Tolerance:** Requirements are structurally bound; ambiguity is escalated, not hallucinated.
*   **Design by Contract (DbC):** Every executed task is bound by explicit preconditions, postconditions, and invariants as defined in the PRPs.
*   **Antifragility:** The system is designed to identify failures (Symbolic Scars) through reflexive checks and improve over time via Algorithmic Reparation.

---
*Initiated via DRP-CRITICAL-REQUIREMENTS-PRP-2026*

### Knowledge Memory Update
The `agent_profiles` directory has been restructured to house agent definitions categorized by distinct personas/roles. Each folder contains the specific markdown and yaml files associated with that agent profile. This improves organization and facilitates the Sovereign Node's ability to easily dispatch tasks to specific agents based on their defined Cognitive Contracts (PRPs).

*   **DRP-AGENT-INDEX-2026:** Agent index successfully generated using Python script `system_logic/generate_agent_index.py`. The script attempts to parse YAML frontmatter and standard Markdown headers. Lesson learned: due to high variability and unstructured nature of certain agent profile markdown documents, regex heuristics can sometimes extract less-relevant text blocks (like markdown snippets or citations) as the purpose or use-cases. To improve this in the future, standardizing agent profile formatting strictly across all `.md` files or migrating them to `.yaml` files (like `zora_architect.yaml`) is highly recommended for cleaner index generation.

*   **DRP-AGENT-INDEX-2026-PATCH:** Follow up to the index generator. The extraction regex was improved to capture inline string values (e.g., `**Purpose:** To do X`) rather than relying on strict newlines, and it strips markdown artifacts like code fences. Despite these improvements, highly unstandardized markdown (where fields don't exist or are replaced by raw foot-notes) still produces garbled descriptions. The core finding remains: cognitive contracts and agent profiles must adhere to a strict structural schema (preferably YAML) for reliable downstream compilation.

### Meta Architect Intelligence: Project Aurelius
### Meta Architect Intelligence: Project Aurelius
*   **Contextual Synthesis**: By treating software engineering failures as "Algorithmic Trauma" and leveraging concepts like F-IPI and Symbolic Scars, product planning shifts from a reactive backlog to an antifragile, self-healing roadmap.
*   **Stakeholder Alignment**: Decomposing features using a strict Tri-Tier Taxonomy ensures that high-level concepts (e.g., Bisociative Architecture) are grounded in tangible user stories for DevOps, SRE, and Feature Engineers.
*   **Structured Output**: The necessity of rigid Cognitive Contracts (PRPs) remains paramount. Advanced feature generation requires strict bounding to prevent "Amateur Impulse" linear thinking, forcing the generation of multi-causal, structurally isomorphic solutions.

### Pluriversal Feature Discovery & AEW Agent Integration
*   **AEW Agent Added**: The Antifragile Epistemic Weaver (AEW) profile has been structured into `agent_profiles/antifragile_epistemic_weaver`. This agent acts as a Structural Coherence Compiler using topological blending (RCC-8) and paraconsistent states to discover code features.
*   **Cognitive Contract Execution**: The AEW protocol initiation text was processed via the Sovereign orchestrator to generate strict `PRP-CRITICAL-REQ` task definitions.
*   **Lesson Learned**: Integrating highly theoretical, abstract cognitive instructions (like "Z-Axis Inference" or "Virtual Weight 3") requires rigid YAML parameterization to prevent hallucination during task execution. The generator tool `create_agent_profile.py` was built to map these esoteric concepts into the standard agent schema predictably.

### Worker Swarm Concurrency Fixes & VULCAN
*   **Atomic Task Claiming:** The Worker Swarm protocol has been upgraded to prevent race conditions. `StateManager.claim_task()` now uses an atomic `os.rename()` operation, appending a `.claimed` suffix to task files immediately upon acquisition. This ensures that in a truly concurrent multi-agent deployment, multiple workers cannot accidentally execute the same Cognitive Contract simultaneously.
*   **VULCAN Agent Integration:** The VULCAN (Vector-Unified Logical Computing Architect Node) agent profile has been officially instantiated via the `create_agent_profile.py` tool. VULCAN enforces strict Domain-Driven Design (DDD) constraints, evaluating system topologies mathematically before generating C4 Models and ADRs. See `agent_profiles/vulcan` and the detailed write-up in `completed_artifacts/LESSONS_LEARNED_VULCAN.md`.

### Pluriversal Architecture & Epistemic Escrow
*   **Epistemic Escrow Integrated**: To prevent belief contamination and LLM hallucinations, the system now features an `epistemic_escrow` directory. Tasks encountering contradictory data or schemas (evaluated via the Confidence-Fidelity Divergence Index, or CFDI) are automatically halted, quarantined as Escrow Tickets, and logged as Symbolic Scars. This implements the "CFDI Brake" pattern.
*   **Pluriversal Agent Instantiated**: The `Pluriversal` agent profile has been officially created in `agent_profiles/pluriversal`. It enforces Draft-Conditioned Constrained Decoding (DCCD) and Hegelian Dialectical Synthesis to safely orchestrate multiple, often incommensurable knowledge models without collapsing their distinct logical topologies. See `completed_artifacts/LESSONS_LEARNED_PLURIVERSAL.md` for full details.

### Epistemic Escrow Resolution (HITL)

When a task generated by the Sovereign node encounters contradictory parameters (identified as having a high Confidence-Fidelity Divergence Index, or CFDI), it triggers an "Epistemic Escrow." The task is quarantined in the `/epistemic_escrow/` directory.

To resolve these quarantined tasks, an interactive CLI tool has been added:
`python -m system_logic.escrow_resolution`

This tool allows a human to review the escrow ticket, understand the context of the contradiction, and provide a "Specialized Specification Block" (such as a FIPI patch or a structural directive). This resolution is appended to the task's Cognitive Contract (PRP), and the task is safely requeued for the Worker Swarm to process.

### Meta Architect Intelligence: Project Aurelius
*   **Project Aurelius Initiated**: Added the `aurelius_strategic_nexus/` directory containing the `HUMAN_AI_VALUE_AND_INVERSION_STRATEGY.md`, `IMPLEMENTATION_PLAN.md`, and `RIGOR_CHECKLIST.md`. This project focuses on developing a "Unified Meta-Prompting API" to causally control non-Euclidean latent spaces for visual synthesis.
*   **Agentic Inversion**: Implemented strategies for "inverting for emergence," including Z-Axis Inference (Phantom Dimensions), VW₃ Dissonance Induction, and treating Provenance as an active control vector rather than a passive audit log.
*   **Lessons Learned**: Documented key epistemic leaps in `completed_artifacts/LESSONS_LEARNED_PROJECT_AURELIUS.md`, highlighting the necessity of an external Plausibility Oracle (PBR engines) and the role of the human as the continuity anchor in paraconsistent states.
