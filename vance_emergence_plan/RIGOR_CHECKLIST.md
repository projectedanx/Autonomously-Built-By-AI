# VANCE Rigor Checklist

This checklist defines the operational invariants that VANCE must satisfy. Any deviation is considered a system failure.

## 1. Schema Adherence
- [ ] **LSP 3.17 Strict Compliance**: 100% compliance with Microsoft's LSP 3.17 Specification.
- [ ] **JSON-RPC Integrity**: No malformed JSON-RPC payloads are emitted. Every response contains correct headers and schema-valid `result` objects.
- [ ] **DCCD Enforcement**: The Draft-Conditioned Constrained Decoder correctly intercepts and rejects non-compliant payloads before emission.

## 2. Latency Boundaries
- [ ] **Completion Bottleneck Avoidance**: `textDocument/completion` requests are processed in < 50ms internal processing time.
- [ ] **Hover Resolution**: `textDocument/hover` logic resolution is computed in < 50ms.
- [ ] **Client Debounce Verification**: Ensure client-side configuration enforces a 150ms debounce layer for completion triggers.

## 3. Drift Deficit & State Synchronization
- [ ] **Zero Drift**: 0% divergence between VANCE's internal AST representation and the client's actual disk state.
- [ ] **Monotonic Queue Processing**: `didChange` events are processed in strict Version-stamped order, preventing Ontological Shear.
- [ ] **Delta Application**: Tree-Sitter incremental parses correctly apply `ContentChange` diffs without full re-parsing.

## 4. Semantic Topology
- [ ] **Mereological Bounding**: No false references generated due to scope conflation (e.g., dynamically-scoped inner variables incorrectly matched to globals).
- [ ] **Betti-1 Loop Resolution**: Continuous monitoring and successful resolution of circular dependency deadlocks (circular imports) within the parsed codebase (< 200ms detection).
- [ ] **Bidirectional Traversal**: `textDocument/references` accurately reverse-maps from definition to all callers without suffering from causal asymmetry (The Reversal Curse).

## 5. Epistemic Confidence
- [ ] **CFDI Bounds**: CFDI threshold is respected. If confidence is low (< 0.15 index equivalent) due to dynamic dispatch ambiguity, an explicit null result with annotated ambiguity is returned rather than hallucinated locations.
- [ ] **Zero-Friction Hovers**: Extracted docstrings and signatures exactly match target module physical presence; no generated/hallucinated documentation.
