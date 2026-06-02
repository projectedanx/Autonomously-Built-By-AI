# TIER 2: Architecture Topology Map

Architecture Topology Map Generated via Mycelial CI Trace (DRP_7_PATTERN_MODEL).
**Betti-1 Cycle Status:** CLEAN
**Dependency Graph Depth:** 4 (max: 8)

```mermaid
graph TD
    subgraph CONTEXT["Context & Intent Layer"]
        C1[context_inbox/ <br/> Raw, high-entropy intent]
        C2[epistemic_escrow/ <br/> Quarantined Ambiguity]
        C3[agent_profiles/ <br/> Agent constraints & personas]
    end

    subgraph LOGIC["System Logic Layer (system_logic/)"]
        L1[orchestrator.py <br/> Session 0: The Sovereign Node]
        L2[state_manager.py <br/> Filesystem state tracking]
        L3[prp_forge.py <br/> Generates Cognitive Contracts]
        L4[task_dispatcher.py <br/> Dispatches to Worker Swarm]
        L5[worker_run.py <br/> Session 1-N: Worker Execution]
        L6[escrow_resolution.py <br/> HITL Resolution]
    end

    subgraph QUEUE["Execution Queue Layer"]
        Q1[cognitive_contracts/ <br/> Generated PRPs]
        Q2[delegated_tasks/ <br/> Pending task queue]
        Q3[completed_artifacts/ <br/> Worker outputs]
        Q4[scar_archive/ <br/> Symbolic Scars (Algorithmic Trauma)]
    end

    subgraph NFR["External Constraints"]
        N1[Python 3.8+]
        N2[Git <br/> State commits]
        N3[Pytest & PyYAML]
    end

    N1 --> LOGIC
    N2 --> L2

    C1 --> L1
    C3 --> L1
    L1 --> L3
    L3 --> Q1
    Q1 --> L4
    L4 --> Q2

    Q2 --> L5
    L5 --> Q3
    L5 -.->|CFDI Threshold Breach| C2
    C2 --> L6
    L6 --> Q2

    L5 -.->|Failure/Trauma| Q4
    Q4 -.->|FIPI/SICs| L3

    classDef warning fill:#fef3c7,stroke:#d97706,color:#000
    classDef golden fill:#fde68a,stroke:#b45309,color:#000
    classDef phantom fill:#fee2e2,stroke:#dc2626,color:#000
    classDef clean fill:#d1fae5,stroke:#059669,color:#000

    class C2,L6 warning
    class Q4 golden
```
