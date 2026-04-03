# Sovereign Context Engineering Workspace

Welcome to the Sovereign Context Engineering Workspace. This repository serves as the foundational environment, persistent memory, and task coordination layer for a swarm of ephemeral, scheduled AI agents.

## Architecture & Workflow

This system operates on a staggered, scheduled cadence separating strategy from execution:

1.  **The Sovereign Node (Session 0):** Ingests raw context, research, and ideas. Designs the architecture, generates precise Cognitive Contracts (PRPs), and delegates tasks.
2.  **The Worker Swarm (Sessions 1-N):** Individual scheduled instances that wake up, claim a delegated task, execute it deterministically according to the PRP, and commit their artifacts back to the repository.

## Directory Structure

The repository is organized to facilitate this autonomous flow without collision or race conditions:

*   **/context_inbox/**: The ingestion point. Drop raw context, notes, research files, and unstructured ideas here. The Sovereign monitors this for new material.
*   **/agent_profiles/**: Stored definitions, instructions, and schemas for the various AI agents (the team) that operate within this ecosystem.
*   **/cognitive_contracts/**: The storage space for generated PRPs (Product-Requirements Prompts). These are the strict, linted, YAML/JSON definitions mapping intent to executable constraints.
*   **/delegated_tasks/**: The hand-off zone. The Sovereign places specific PRPs here, assigned to scheduled workers for execution.
*   **/completed_artifacts/**: The output zone. Workers commit their finished code, analysis, or designs here.
*   **/system_logic/**: The operational code backing the workspace. Includes linters (e.g., `prp_linter`), router scripts, state management, and validation tools.

## Operating Principles

*   **Zero-Fluff Tolerance:** Requirements are structurally bound; ambiguity is escalated, not hallucinated.
*   **Design by Contract (DbC):** Every executed task is bound by explicit preconditions, postconditions, and invariants.
*   **Antifragility:** The system is designed to identify failures (Symbolic Scars) through reflexive checks and improve over time via Algorithmic Reparation.

---
*Initiated via DRP-CRITICAL-REQUIREMENTS-PRP-2026*
