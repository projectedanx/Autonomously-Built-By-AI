# Sovereign Context Engineering Workspace

Welcome to the Sovereign Context Engineering Workspace. This repository serves as the foundational environment, persistent memory, and task coordination layer for a swarm of ephemeral, scheduled AI agents operating under a staggered, sovereign-worker paradigm.

## Purpose

The main goal of this workspace is to facilitate a structured, reproducible, and deterministic AI workflow. By separating strategy (Sovereign) from execution (Worker), the system ensures that high-level intent is properly parsed, bounded by explicit Cognitive Contracts (PRPs), and executed autonomously without human intervention. This repository acts as the central hub for ingesting context, generating these contracts, dispatching tasks, and storing the resulting artifacts.

## Architecture & Workflow

This system operates on a staggered, scheduled cadence:

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
