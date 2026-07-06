# Sovereign Context Engineering Workspace

This repository serves as a **Sovereign Context Engineering Workspace** — a persistent, shared memory and task coordination layer for a swarm of scheduled, parallel AI agents. It operates on a decentralized, filesystem-based architecture that facilitates asynchronous collaboration between specialized AI nodes.

> **0xCARTO Notice:** This repository has been mapped by 0xCARTO — The Pluriversal Repository Cartographer (DRP-2026-CARTO-0.0.1). Its topography, entropy, and cultural artifacts are preserved in the `docs/0xCARTO/` directory.

## Intent & Problem Space

Modern AI coding assistants assist with local edits but collapse under real-world software engineering complexities: multi-service architectures, evolving requirements, and long-lived codebases. They treat hallucinations, broken builds, and incident regressions as one-off bugs instead of feeding them into an antifragile learning loop.

**Core Problem:** There is no cognitive engine for software engineering that combines multi-branch reasoning (CoT/ToT/GoT), multi-agent orchestration, context engineering over real repos and systems, and antifragile failure learning into a single, governed platform.

**Core Solution:** This workspace acts as a Cognitive Software Engineering Engine (CSEE). It orchestrates planning, coding, reviewing, and operations as a multi-agent workflow. It uses **Symbolic Scars** from failures to generate new tests and policies via **Failure-Informed Prompt Inversion (FIPI)** and enforces them via **Prompting-as-Code (PaC)**.

## Core Architecture

The multi-agent system architecture follows a staggered, asynchronous cadence using a "Hickam-OODA Recursive Loop":

1.  **The Sovereign Node (Session 0)**
    *   **Role**: Orchestrator and Planner.
    *   **Action**: Ingests raw, high-entropy intent from `context_inbox/`, applies the "Hickam Filter" to reject simplistic explanations (Occam's Razor), and synthesizes structured **Cognitive Contracts** (Product Requirement Prompts - PRPs). It then delegates these contracts as tasks to the `delegated_tasks/` directory.

2.  **The Worker Swarm (Sessions 1-N)**
    *   **Role**: Specialized execution units.
    *   **Action**: Wakes up intermittently, atomically claims pending tasks from `delegated_tasks/`, executes them according to strict constraints defined in the PRPs, and deterministically commits artifacts to `completed_artifacts/`.

## 0xCARTO Pluriversal Cartography

To understand the empirical reality of this repository, refer to the 0xCARTO synthesized documentation tiers:

1.  [TIER 1: Repository Identity & Ontological Glossary](docs/0xCARTO/TIER_1_REPOSITORY_IDENTITY.md) - Defines the ground truth and local lexicon.
2.  [TIER 2: Architecture Topology Map](docs/0xCARTO/TIER_2_ARCHITECTURE_TOPOLOGY.md) - Visualizes the actual structural dependencies.
3.  [TIER 3: CI/CD Pipeline Cartograph](docs/0xCARTO/TIER_3_CI_CD_CARTOGRAPH.md) - Maps the execution flow and highlights Nominative Traps.
4.  [TIER 4: Dependency Matrix & Entropy Audit](docs/0xCARTO/TIER_4_DEPENDENCY_ENTROPY.md) - Quantifies build inefficiency and thermodynamic entropy.
5.  [TIER 5: Operational Runbook & Cultural Artifacts Log](docs/0xCARTO/TIER_5_RUNBOOK_CULTURAL_ARTIFACTS.md) - Preserves non-standard logic and "Golden Scars".

## Key Concepts & Protocols

*   **Algorithmic Trauma & Symbolic Scars**: Failures in execution or logic are not discarded. They are captured as "Symbolic Scars" and fed back into the system via **Failure-Informed Prompt Inversion (FIPI)** to generate Semantic Integrity Constraints (SICs).
*   **Epistemic Escrow (The CFDI Brake)**: If an agent encounters a high Confidence-Fidelity Divergence Index (CFDI) — meaning contradictory parameters or ambiguous intent — the task is halted and quarantined in `epistemic_escrow/`. This forces **Human-in-the-Loop (HITL)** intervention to resolve the ambiguity, preventing hallucination and enforcing "Emergence Inversion."
*   **Paraconsistent States & Dissonance Induction**: The system intentionally engineers states of high "Aesthetic Tension" to explore N-dimensional manifolds of possibility, requiring human operators to act as the "Z-Axis Continuity Anchor."
*   **Anionic Architecture (Lattice of Refusal)**: The system strictly refuses subjective, evaluative adjectives (e.g., "seamless", "robust", "masterpiece"). Requests using such language trigger diagnostic rejections, forcing physical, structurally isomorphic specifications.

## Repository Structure

*   `agent_profiles/`: YAML and Markdown manifests defining the personas, constraints, and specialized cognitive architectures of individual agents (e.g., VULCAN, V.I.P.E.R., AXIOM, 0xCARTO).
*   `context_inbox/`: The entry point for raw intent, research notes, and unsynthesized ideas.
*   `cognitive_contracts/`: Storage for generated Product Requirement Prompts (PRPs) — strict JSON/YAML schemas detailing execution constraints.
*   `delegated_tasks/`: The queue for pending tasks waiting to be claimed by the Worker Swarm.
*   `completed_artifacts/`: The final output directory for executed tasks and generated code/documentation.
*   `epistemic_escrow/`: Quarantined tasks requiring human resolution due to CFDI threshold breaches.
*   `system_logic/`: Python scripts that power the orchestration, task dispatching, escrow resolution, and state management.
*   `docs/`: Extensive documentation extruded by specialized agents (e.g., 0xCARTO).
*   `tests/`: Unit tests ensuring the integrity of the `system_logic/` components.
*   `benchmarks/`: Performance testing scripts for core state management operations.

## Setup & Usage

### Prerequisites
*   Python 3.8+
*   Git (for automated state commits)
*   Pytest (for running tests and benchmarks)
*   PyYAML (for agent profile parsing)

### Installation
```bash
# Clone the repository
git clone <repository_url>
cd <repository_directory>

# Install required packages (if using a virtual environment)
pip install pytest pytest-benchmark pyyaml
```

### Running the Orchestrator
To execute a cycle of the Sovereign workspace, run the main orchestrator script:
```bash
python -m system_logic.orchestrator
```
The system will automatically determine its role (`SOVEREIGN`, `WORKER`, or `IDLE`) based on the current state of the filesystem (pending tasks vs. unprocessed context).

### Resolving Epistemic Escrow
When a task is quarantined, a human operator must resolve the contradiction:
```bash
python -m system_logic.escrow_resolution
```
This interactive CLI will display pending tickets and prompt for a "Specialized Specification Block" (resolution directive).

### Managing Agent Profiles
To generate a comprehensive `README.md` index of all agent profiles in the `agent_profiles/` directory:
```bash
python -m system_logic.generate_agent_index
```

## Testing and Benchmarks

To ensure system integrity, run the test suite:
```bash
pytest tests/ system_logic/
```

To run performance benchmarks on the StateManager:
```bash
pytest benchmarks/
```

## Dashboard Interface (Frontend)
A Next.js application resides in the `frontend/` directory. It provides a visual orchestration panel mapping the states of the filesystem queues (`context_inbox`, `delegated_tasks`, `completed_artifacts`, `epistemic_escrow`).

To run the dashboard locally:
```bash
cd frontend
npm install
npm run build
```
Then start the application.

## Integrated Agent Swarm

The workspace is empowered by numerous specialized agent emergence plans and deployment specifications, including:

*   **0xCARTO**: The Pluriversal Repository Cartographer (Documentation & Topology mapping).
*   **KIRA-7**: Deterministic Feishu/Lark bot execution enforcing Webhook Sovereignty.
*   **CIPHER**: Zero-Trust Epistemic Sentinel deploying autonomous security engineering into CI/CD.
*   **VANCE**: Topological LSP Architect bridging source code and JSON-RPC 2.0 via a Conflict-Free Replicated Semantic Graph.
*   **AEGIS-11**: Autonomic Epistemic Gatekeeper preventing Ontological Incommensurability.
*   **VULCAN**: Vector-Unified Logical Computing Architect Node for strict topological bounds.
*   **AEW Pluriversal Discovery Agent**: Antifragile Epistemic Weaver (AEW) engineered for Pluriversal Codebase Feature Discovery, utilizing RCC-8 topological blending and paraconsistent Z-Axis inference to maximize topological novelty while enforcing absolute structural conservation.
