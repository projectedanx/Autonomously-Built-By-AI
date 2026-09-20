# ADR 12: Epistemic Mechanics of the Insight Gap

## Context
The Insight Gap represents the discrepancy between an operator's mental model and the LLM's emergent output. We need a formalized harness to measure and correct this via variable viscosity prompting, epistemic telemetry, and failure-informed prompt inversion.

## Decision
We will implement the `InsightGapHarness` to actively monitor three primary telemetry metrics:
1. Interpretive Fracture ($C_d$ Cosine Distance)
2. Semantic Saponification Index (SSI via KL Divergence)
3. Confidence-Fidelity Divergence Index (CFDI)

We also instantiate specific agent profiles (Lead Interpretability Engineer, Principal Mathematician, Chief Quantum-Isomorphic Logic Architect) to conduct structural audits on residual streams, manifold tearing, and non-separable attention.

## Consequences
- **Positive:** Enhances deterministic output fidelity by converting silent hallucinations into measurable, trappable exceptions (e.g. Epistemic Escrow).
- **Negative:** Introduces latency per-token evaluation in the `InsightGapHarness`.

## Lessons Learned
- Moving from 'Instruction-Follower' idealized models to probabilistic evaluation loops is necessary for production-grade reliability.
- Epistemic Scars and Epistemic Escrow must be utilized to maintain alignment when system conditions decay.
