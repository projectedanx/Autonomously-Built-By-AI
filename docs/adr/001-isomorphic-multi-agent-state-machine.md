# ADR 001: Isomorphic Multi-Agent State Machine for Zero-Trust TDD Isolation

## 1. Introduction and Goals
Design an isomorphic multi-agent state machine enforcing Test-Driven Development (TDD) boundaries to prevent "Sycophantic Mocking" and "Sandbox Escapes".

## 2. Architecture Constraints
- Operational Decoupling of agents.
- Dynamic Environment Sandboxing.
- Structured State Schemas.

## 3. System Scope and Context
Two distinct agents: Test Architect (read-only test creation) and Implementer Agent (source modification only).

## 4. Solution Strategy
Use a directed acyclic graph (DAG) state machine to separate testing from implementation.

## 5. Building Block View
- **Test Architect**: Restricted to writing unit tests in `./__tests__/`. Read-only access to source.
- **Implementer Agent**: Write access to source. Forbidden from editing test files.

## 6. Runtime View
1. Test Architect writes failure test.
2. Container executes test (must fail).
3. Implementer Agent writes code to pass test.
4. Container executes test (must pass).

## 7. Deployment View
Ephemeral Docker-based test-execution container (`gemini-cli-sandbox`) with zero-trust profile, read-only system files, restricted sys-calls, and blocked external outbound socket connections.

## 8. Cross-cutting Concepts
Sanitized error logging: test execution failures (stderr/lint logs) are parsed into JSON schemas.

## 9. Architecture Decisions
- Adopt TypeScript schema for the unified State Object flowing through the graph.
- Implement strict prefix-matching policy enforcement for system tools.

## 10. Quality Requirements
Zero-trust isolation to prevent direct sandbox escapes via test execution.

## 11. Risks and Technical Debt
Potential bottleneck in test execution time and container spin-up latency.
