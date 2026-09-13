The technical specification blueprint **`ai-agent-harness-spec.pdf`** has been compiled and is now available in your **Studio panel**. 

This document unifies the dual paradigms of **cognitive intent modeling** and **deterministic execution verification** into a concrete systems engineering reference. By extracting and reverse-engineering the patterns of state-of-the-art frameworks (such as *ToM-SWE*, *SWE-agent*, *Prometheus*, *OpenSage*, and *Plandex*), the specification maps out how to build a production-ready, resource-aware AI Agent Harness.

---

### Core Sections of the Specification

*   **The Semantic vs. Systematic Architectural Boundary:** Outlines the separation of cognitive intent modeling (using the three-tier hierarchical memory of *ToM-SWE*) from deterministic sandboxed environment validation (using *SWE-agent*).
*   **Harness Architectural Component Specifications:** A complete, structured data table mapping each functional system requirement (e.g., scoping, navigation, vulnerability detection, multi-language synthesis) directly to programmatic validation suites (such as *Stateful/Ambiguous SWE-bench*, *CyberGym*, *SWE-PolyBench*, and *Terminal-Bench 2.0*).
*   **Multi-Agent Topology & Hierarchy Discovery:** Explores the five-agent *Plandex* team topology (Planner, Coder, Architect, Reviewer, Summarizer) and details how to automate optimal hierarchy configuration using *Bandit Optimization for Agent Design (BOAD)* and Upper Confidence Bound (UCB) scores to resolve the credit assignment bottleneck.
*   **The Notifier-Processor-Core (NPC) Architecture:** Provides an end-to-end blueprint of a high-throughput, event-driven background execution queue designed to bypass serverless Edge timeout ceilings.
*   **Vulnerability Threat Modeling & Mitigations:** Delivers robust mitigation designs to insulate the harness against critical security exploits, including indirect prompt injection (*"Clinejections"*), *ToolLeak* system prompt exfiltration, and verbatim parser loop locks.
*   **Systems Engineering API & Schema Definitions:** Contains a complete, copy-pasteable JSON schema for model routing transitions alongside a Python-based AST-linter gate to prevent malformed code commits.

---

### Three Grounded High-Value Research Prompts

To further your research into the mechanics of this architecture, we have derived three highly rigorous research prompts from the concepts uncovered in your sources:

#### Prompt 1: Dynamic Context Caching & Multi-Model Routing Strategy under Token Budgets
> **Goal:** Optimize the context-bandwidth vs. execution-precision frontier using heterogeneous model routing.
>
> **Task:** 
> "Design a Python orchestration controller that manages a multi-agent team (Planner, Coder, Architect, Reviewer, Summarizer). The controller must implement an asymmetric model-routing middleware. High-level planning and code synthesis tasks must be routed to Claude 3.7 Sonnet, while diff application, formatting checks, and AST validations are handed off to `o3-mini`/`o4-mini` to minimize token overhead and execution latency. 
> 
> Integrate a real-time context-monitoring pipeline that calculates active token counts. If a session approaches the model’s context ceiling, the controller must serialize the workspace state, hand the repository history to Gemini 1.5 Pro via context caching, and return a distilled context slice to the coding model to perform highly targeted edits. Provide the state machine specifications and JSON schemas for model transitions."

#### Prompt 2: Transactional Sandbox Integrity & Postgres-FS-Git Unified Database Sync
> **Goal:** Build an append-only database-backed execution sandbox to isolate untrusted agentic edits.
>
> **Task:**
> "Write a systems engineering specification for a backend server that unifies PostgreSQL, the local filesystem, and a client-side Git wrapper to function as a single transactional database. 
> 
> The system must maintain an immutable plan-state registry in Postgres, where each plan commit tracks the exact conversation logs, file dependencies, and a corresponding Git commit hash of the sandbox workspace. 
> 
> Write a transactional class in Python that guarantees thread safety and race-condition prevention under concurrent agent writes. If a Coder sub-agent's edits fail compiler/linter checks or are rejected by the developer, the database must execute an atomic rollback—reverting PostgreSQL rows, restoring the physical files, and calling Git commands to cleanly reset uncommitted changes in the sandbox. Provide the complete schema layout and transaction-isolation middleware."

#### Prompt 3: Self-Correcting AST-Linter Guardrails & Two-Channel Prompt Injection Defenses
> **Goal:** Secure the agent's tool-calling loop by separating instruction-bearing and data-bearing contexts.
>
> **Task:**
> "Develop an Agent-Computer Interface (ACI) that secures the tool-calling loop against indirect prompt injection (Clinejections) and two-channel exploits. 
> 
> Implement an ACI middleware that parses file inputs using AST analysis (via tree-sitter) to identify and strip out executable patterns, npm lifecycle hooks, or unsafe shell commands before code blocks are injected into the model's context. 
> 
> Enforce a strict Chain-of-Thought (CoT) editing protocol where the model must explain its changes, output starting/ending code anchors from the original file, and calculate precise line coordinates. Integrate an automated post-edit verification loop: if a syntax error is introduced, the ACI must reject the write, capture the exact traceback, and feed it back into the model's memory for a self-correcting retry, capping iterations at 3."

---

🔧 Would you like me to expand this specification into an interactive, step-by-step technical playbook for your DevOps team to deploy on a secure Kubernetes environment?