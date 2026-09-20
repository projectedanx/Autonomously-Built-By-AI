# ADR 003: Self-Healing Multimodal UI Verification Harness via Agent-Driven Playwright Replay Loops

## 1. Introduction and Goals
Design an automated, self-healing visual testing harness using a multimodal agent to execute end-to-end UI verification loops.

## 2. Architecture Constraints
- Test-Driven Visual Spec execution.
- Automated Layout Grading & Code Repair.
- Verification and Checkpointing.

## 3. System Scope and Context
Containerized browser (Chrome DevTools / Playwright MCP) interacting with a vision-enabled model.

## 4. Solution Strategy
Translate multimodal assets (hand-drawn UI sketch, PDF) into type-safe Playwright testing scripts, execute to record baseline failure, and iteratively self-heal code.

## 5. Building Block View
- **Multimodal Agent**: Parses visual constraints.
- **Playwright MCP**: Executes UI tests and captures screenshots/console logs.
- **Healing Loop**: Grades layout delta and applies CSS/HTML modifications.

## 6. Runtime View
1. Parse design spec into Playwright script.
2. Execute test; record baseline failure.
3. Capture high-res screenshots and live console.log streams.
4. Model analyzes screenshots against specs and generates fixes.
5. Validate resolution.

## 7. Deployment View
Containerized browser environment with atomic filesystem snapshots for rollback functionality.

## 8. Cross-cutting Concepts
Rollback capability (`/restore` command) to previous checkpoints if style drift occurs.

## 9. Architecture Decisions
- Use JSON-RPC tool definitions for Playwright MCP integration.
- Rely on semantic tokens for visual repairs (no direct color classes).

## 10. Quality Requirements
High fidelity in visual match; zero regression introduced during healing.

## 11. Risks and Technical Debt
High compute cost for continuous high-resolution screenshot analysis.
