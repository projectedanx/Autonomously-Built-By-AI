# VANCE Implementation Plan: Topological Cartography

## Overview
VANCE (Vector-Anchored Node & Context Engineer) is integrated into the Sovereign Context Engineering Workspace not as a simple wrapper around a Language Server, but as a **Conflict-Free Replicated Semantic Graph (CFRSG)**. VANCE enforces topological discipline on the codebase, eradicating the "Reversal Curse" and maintaining strict adherence to the LSP 3.17 specification.

## The Four Non-Negotiable Layers

1.  **Layer 1: Incremental Parse Engine (Tree-Sitter Substrate)**
    *   **Mechanism**: Uses Tree-Sitter for sub-millisecond AST diffing. VANCE computes deltas on every `textDocument/didChange` rather than performing full re-parses.
    *   **Constraint**: All events must be processed in strict monotonic order using version-stamped edit queues. Error nodes must be immediately quarantined.

2.  **Layer 2: The Semantic Graph (Neo4j + Pinecone Dual-Layer)**
    *   **Mechanism**: Maintains a directed property graph of AST entities, with edges like `CALLS`, `INHERITS_FROM`, and `SCOPES_WITHIN`. A Pinecone vector overlay acts as a proximity oracle for fuzzy search.
    *   **Constraint**: Vectors are candidates; graphs are truth. Mereological boundaries are strictly enforced (e.g., scoping rules prevent transitivity fallacies).

3.  **Layer 3: The Nitinol Failure Ledger (NFL)**
    *   **Mechanism**: Operates as the Failure-Informed Prompt Inversion (FIPI) mechanism for VANCE. Every structural error or near-miss in JSON-RPC payload generation is logged as a Symbolic Scar.
    *   **Constraint**: The NFL encodes these scars as hard negative rules in the constrained decoding grammar, ensuring structural immunity to repeat failures.

4.  **Layer 4: Draft-Conditioned Constrained Decoder (DCCD)**
    *   **Mechanism**: A schema guard layer based on the LSP 3.17 specification. Validates all outgoing payloads.
    *   **Constraint**: Zero tolerance for malformed JSON-RPC. If validation fails, the payload is rejected before emission, preventing epistemic collapse.

## Operational Workflow (The Cartography Loop)
-   **OBSERVE**: Ingest `didChange` deltas, run Tree-Sitter incremental parse.
-   **ORIENT**: Update Semantic Graph with new edges and scope chains; re-embed docstrings in Pinecone.
-   **DECIDE**: On query (e.g., `textDocument/references`), check CFDI. Return explicit ambiguity if high; execute Cypher reverse traversal if unambiguous.
-   **ACT**: Emit DCCD-validated JSON-RPC response.
