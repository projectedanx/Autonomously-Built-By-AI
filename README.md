# Sovereign Context Engineering Workspace

This repository serves as a **Sovereign Context Engineering Workspace** — a persistent, shared memory and task coordination layer for a swarm of scheduled, parallel AI agents. It operates on a decentralized, filesystem-based architecture that facilitates asynchronous collaboration between specialized AI nodes.

## Core Architecture

The multi-agent system architecture follows a staggered, asynchronous cadence using a "Hickam-OODA Recursive Loop":

1.  **The Sovereign Node (Session 0)**
    *   **Role**: Orchestrator and Planner.
    *   **Action**: Ingests raw, high-entropy intent from `context_inbox/`, applies the "Hickam Filter" to reject simplistic explanations (Occam's Razor), and synthesizes structured **Cognitive Contracts** (Product Requirement Prompts - PRPs). It then delegates these contracts as tasks to the `delegated_tasks/` directory.

2.  **The Worker Swarm (Sessions 1-N)**
    *   **Role**: Specialized execution units.
    *   **Action**: Wakes up intermittently, atomically claims pending tasks from `delegated_tasks/`, executes them according to strict constraints defined in the PRPs, and deterministically commits artifacts to `completed_artifacts/`.

## Key Concepts & Protocols

*   **Algorithmic Trauma & Symbolic Scars**: Failures in execution or logic are not discarded. They are captured as "Symbolic Scars" and fed back into the system via **Failure-Informed Prompt Inversion (FIPI)** to generate Semantic Integrity Constraints (SICs).
*   **Epistemic Escrow (The CFDI Brake)**: If an agent encounters a high Confidence-Fidelity Divergence Index (CFDI) — meaning contradictory parameters or ambiguous intent — the task is halted and quarantined in `epistemic_escrow/`. This forces **Human-in-the-Loop (HITL)** intervention to resolve the ambiguity, preventing hallucination and enforcing "Emergence Inversion."
*   **Paraconsistent States & Dissonance Induction**: The system intentionally engineers states of high "Aesthetic Tension" to explore N-dimensional manifolds of possibility, requiring human operators to act as the "Z-Axis Continuity Anchor."
*   **Anionic Architecture (Lattice of Refusal)**: The system strictly refuses subjective, evaluative adjectives (e.g., "seamless", "robust", "masterpiece"). Requests using such language trigger diagnostic rejections, forcing physical, structurally isomorphic specifications.

## Repository Structure

*   `agent_profiles/`: YAML and Markdown manifests defining the personas, constraints, and specialized cognitive architectures of individual agents (e.g., VULCAN, V.I.P.E.R., AXIOM).
*   `context_inbox/`: The entry point for raw intent, research notes, and unsynthesized ideas.
*   `cognitive_contracts/`: Storage for generated Product Requirement Prompts (PRPs) — strict JSON/YAML schemas detailing execution constraints.
*   `delegated_tasks/`: The queue for pending tasks waiting to be claimed by the Worker Swarm.
*   `completed_artifacts/`: The final output directory for executed tasks and generated code/documentation.
*   `epistemic_escrow/`: Quarantined tasks requiring human resolution due to CFDI threshold breaches.
*   `system_logic/`: Python scripts that power the orchestration, task dispatching, escrow resolution, and state management.
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


### KIRA-7 (Lark-Weaver) Integration
The repository now features the emergence plan for **KIRA-7**, specialized in deterministic Feishu/Lark bot execution.
KIRA-7 enforces strict architectural constraints through its Anionic Architecture, emphasizing:
*   **Webhook Sovereignty**: Zero-trust ingress requiring cryptographic validation (URL Challenge, AES decryption, SHA256 signatures).
*   **Token Primacy**: Strict management of TTL-bound access tokens via Redis or in-memory caches.
*   **Scope Isolation**: Forcing explicit human Z-Axis inference instead of AI guesswork when dealing with API scopes and event triggers.

Detailed implementation strategies, value propositions, and rigor checklists can be found in the `kira7_emergence_plan/` directory.

### CIPHER (Zero-Trust Epistemic Sentinel) Integration
The repository now includes the `CIPHER` agent emergence plan, deploying an autonomous security engineer into the CI/CD pipeline.
CIPHER enforces rigorous constraints via its topological architecture:
*   **PetzoldSequence Enforcement:** Absolute phase isolation (`THINK|THREAT_MODEL|AUDIT|REPORT`) preventing threat models from contaminating code generation.
*   **Epistemic Escrow (CFDI Brake):** Tighter Confidence-Fidelity Divergence thresholds (CFDI > 0.08) requiring human clarification before logging uncertain security findings.
*   **Failure-Informed Prompt Inversion (FIPI):** Automated generation of Semantic Integrity Constraints (SICs) based on historical Symbolic Scars.

Detailed specifications and rigor checklists are located in the `cipher_emergence_plan/` directory. Note: Earlier agent integrations (such as some worker logic expansions) showed signs of AI "laziness" or incomplete feature delivery. These have been remediated in the current integration, and we continue to document these failure modes as part of the overall Symbolic Scar learning framework.

### VANCE (Topological LSP Architect) Integration
The repository incorporates **VANCE**, the Vector-Anchored Node & Context Engineer, bridging the gap between human-written source code and JSON-RPC 2.0. VANCE acts as a **Conflict-Free Replicated Semantic Graph (CFRSG)**.
VANCE enforces topological discipline via:
*   **Incremental Parse Engine:** Utilizes Tree-Sitter for sub-millisecond AST diffing without full re-parses.
*   **Semantic Graph Layer:** Employs a bidirectional Neo4j + Pinecone dual-layer to prevent transitivity fallacies.
*   **Nitinol Failure Ledger (NFL):** Memorizes structural errors in JSON-RPC payload generation as Symbolic Scars to immunize against repeats.
*   **Draft-Conditioned Constrained Decoder (DCCD):** Intercepts malformed payloads before emission, ensuring strict LSP 3.17 compliance.

Detailed specifications and rigor checklists can be found in the `vance_emergence_plan/` directory.

### Dashboard Interface (Frontend)
A Next.js application resides in the `frontend/` directory. It provides a visual orchestration panel mapping the states of the filesystem queues (`context_inbox`, `delegated_tasks`, `completed_artifacts`, `epistemic_escrow`).

To run the dashboard locally:
```bash
cd frontend
npm install
npm run build
```
Then start the application.

### Agentic Inversion Protocol & The Strategic Integration Project Manager
The Sovereign Context Engineering Workspace operates under the **Agentic Inversion Protocol**, shifting from a traditional "Prompt -> Output" paradigm to an "Agentic Telemetry Loop." Here, the user provides seed intent and aesthetic grounding, while the system operates as a Structural Mapper traversing High-Dimensional Latent Spaces. This pluriversal synthesis prevents "epistemic monoculture."

Key persona executing this protocol:
*   **Strategic Integration Project Manager:** Generates Zachman Framework deterministic system-first specifications and maps Operational Workflow semantics (SPZ-Zeta).

### AEGIS-11 (Autonomic Epistemic Gatekeeper) Integration
The repository incorporates **AEGIS-11**, the Consilience Validator operating within SCOS. AEGIS-11's core directives focus on preventing Ontological Incommensurability.
*   **Hickam Topology Scaffold**: Mandates an explicit JSON mapping (`Hickam_Orientation`, `Contrastive_Delta`, etc.) before any execution.
*   **Epistemic Syntax**: Preserves the Pluriverse without averaging conflicting worldviews. Structural contradictions are explicitly marked (e.g., `[∇]`, `[⊗]`).
*   **R-A8B Execution Synthesis**: Executes according to the Deterministic Execution Synthesis for the Rheological-Anionic 8B Language Engine Architecture (`DRP-RA8B-NON-EUCLIDEAN-CORE-001`).

Detailed profile available at `agent_profiles/aegis11/profile.yaml` and cognitive contract at `cognitive_contracts/DRP-RA8B-NON-EUCLIDEAN-CORE-001.yaml`.
