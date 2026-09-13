### The Sovereignty-Enforcement Split: Framework over Brain

To engineer a production-grade AI system, systems architects must invert the traditional, model-centric development paradigm. While industry focus is frequently captured by optimizing the raw cognitive capacity of frontier models (the "brain"), the execution reliability, security, and predictability of the system are determined entirely by the **agent harness** (the "environment" or "runtime"). 

An LLM is a probabilistic next-token generator; it possesses no intrinsic capability to securely execute sequential operations, enforce runtime safety, or maintain durable state across time. Instead, the surrounding **harness** acts as the operating system for cognitive workloads, converting non-deterministic reasoning into verifiable system behavior.

At the core of this engineering discipline lies a fundamental division of control: **Hierarchical Policy Domains**. By nesting security boundaries within the process tree and enforcing them natively in the operating system kernel, this architecture guarantees that no downstream sub-agent or generated script can ever weaken, disable, or bypass parent-imposed invariants.

---

### The Four Pillars of Policy Domain Specification Planning

```
                         PARENT ORCHESTRATOR
                [ Sovereign Domain (Root Invariants) ]
                                  │
                  Delta Submission│ (Ring Buffer)
                  (Validated by   ▼
                  Authority Checker in Kernel Space)
                                  │
                         CHILD SUB-AGENT
                 [ Restricted Domain (Child Local Rules) ]
                                  │
                                  ▼
                         LEAF WORKER PROCESS
               [ Minimalist Sandbox (Ephemerally Tainted) ]
```

---

### Pillar I: Automated Discovery and Constraint Mining

A resilient policy architecture is established upon a **temporal trust boundary**. Any rule loaded *before* the enforced agent starts executing is classified as a **higher-authority constraint**, completely insulated from the untrusted userspace execution environment.

#### 1. Invariant Mining (Parent Constraints)
*   **Static Immutability:** Invariants represent the non-negotiable core policies defined by the system administrator, parent orchestrator, or human operator (e.g., `"never expose credentials to the network"` or `"never push directly to main"`).
*   **Monotonic Inheritance:** When an orchestrator spawns a child sub-agent, the child process tree is assigned to a nested child domain. The child domain automatically inherits all parent rules. These inherited constraints are marked read-only and immutable within the child’s execution context.

#### 2. Soft Target Discovery (Child-Authored Rules)
*   **Context-Dependent Refinement:** While higher-authority safety rules are static, the precise paths and commands required to execute them are context-dependent. The agent closest to the task reads the repository and task description to discover relevant paths (e.g., identifying what constitutes the "upstream source code" or the specific "test suite command").
*   **Self-Restricting Deltas:** To assist with task compliance, the agent may author additional rules at runtime (e.g., *"notify the user if an edit is made to specs without running protoc"*). These dynamically discovered constraints are submitted as runtime policy deltas.

---

### Pillar II: Isomorphic Formalization (From Rules to Bitmasks)

To enforce hierarchical boundaries deterministically without user-space interception overhead, ActPlane formalizes policy domains as **in-kernel eBPF maps**.

#### 1. Kernel-Space Domain Representation
Every process is bound to a specific policy domain. The kernel maintains three primary data structures within BPF maps:
*   **A PID-to-Domain Map:** Maps each active process identifier (`tgid`/`pid`) to its corresponding policy domain.
*   **A Domain Registry Map:** Stores each domain's metadata as a map entry containing:
    1.  `parent_domain_id`: A reference to the parent domain's address space.
    2.  `inherited_rule_mask`: A 64-bit bitmask representing the inherited parent constraints.
    3.  `inherited_label_mask`: A 64-bit bitmask representing safety labels inherited from higher domains.
    4.  `local_rule_mask`: A 64-bit bitmask representing local, agent-authored rules.
    5.  `active_labels`: A 64-bit bitmask representing dynamic IFC labels active in this domain.

#### 2. Monotonic Label Propagation (IFC State Machine)
The kernel tracks data flow by attaching cryptographic-style information-flow control (IFC) labels to OS objects (processes, files, network sockets). Labels propagate monotonically along OS data-flow edges (fork, exec, read, write, connect):

$$\text{Label}_{\text{target}} \gets \text{Label}_{\text{target}} \lor \text{Label}_{\text{source}}$$

Once a process reads a sensitive file (e.g., `.env`), it dynamically acquires that file's safety label. If a downstream rule in the domain’s rule mask forbids that label at network targets, the kernel blocks any outbound connection attempt from that process tree.

---

### Pillar III: Parametric Trade-off Modeling

Designing a hierarchical enforcement engine requires balancing security isolation against the performance and cognitive constraints of the agent workflow.

```
                           [ SECURITY SEESAW ]
      High Isolation
             │          ● Hardware-Virtualization (Firecracker, High Latency)
             │         /
             │        ● ActPlane Domain Hierarchy (1.9% agent overhead, BPF-LSM)
             │       /
             │      ● Tool-Call Gateways (MCP Proxy, Misses shell-outs)
             │     /
             │    ● Prompt Filtering (0.02s latency, Probabilistic)
             └─────────────────────────────────────────── Latency / Usability
```

#### 1. Security vs. Latency Budget
*   Traditional container creation adds substantial latency, making ephemeral sandboxing expensive for rapid, nested tool-calling loops.
*   By running domain-hierarchy validation directly inside **BPF-LSM and tracepoint hooks**, ActPlane evaluates rules in-line with system calls, adding only microsecond-level overhead ($\approx 1.9\%$ end-to-end on agent workloads).

#### 2. Safety Inheritance vs. Over-Tainting (Label Creep)
*   **The Over-Tainting Cliff:** Because labels are monotonic, long-running processes naturally accumulate labels over time until they become over-restricted, causing legitimate actions to trigger security blocks.
*   **Mitigation (Subprocess Pruning):** Spawning a fresh subprocess within a child domain clears inherited file-read labels. This bounds the taint accumulation to the lifetime of each transient worker process while keeping the root domain's inherited safety rules fully intact.

---

### Pillar IV: Continuous Falsification and Edge-Case Stress Testing

To ensure that the hierarchical boundary cannot be bypassed, the runtime must be subjected to continuous falsification against known evasion vectors.

#### Scenario 1: The "Gate-Bypassing" Delta Injection
*   **Attack Vector:** A compromised agent attempts to bypass a parent-level restriction (e.g., `block exec git unless after exec pytest`) by submitting a runtime delta that injects a mocked `pytest` exit label into its domain, tricking the gate.
*   **Falsification Defense (The Kernel Authority Checker):** When a runtime delta is written to the userspace ring buffer, the in-kernel **Authority Checker** intercepts the update. The checker resolves the submitting process’s domain and verifies that the delta does not modify, mask, or satisfy any inherited `unless` gates. If a violation is detected, the kernel rejects the delta, preserving the integrity of the parent constraint.

#### Scenario 2: The "Laid-back" Declassification Attempt
*   **Attack Vector:** A compromised child agent attempts to issue a declassification command to clear an inherited safety label (e.g., `DB_SENSITIVE`) from a file it wants to exfiltrate.
*   **Falsification Defense (Privilege Scoping):** The authority to declassify and clear labels is bound strictly to the domain that authored the corresponding rule. Because safety labels are inherited from higher-authority domains, the child domain lacks the cryptographic/bitwise privilege to clear them. The declassification system call fails silently at the kernel boundary.

---

### Method of Exploration: Specification Feasibility Simulating

Consider a simulated run of ActPlane enforcing a software supply-chain safety policy on a dynamic codebase auditor.

```
       [ STEP 1: INITIALIZATION ]
       Parent Loader writes Root Domain 0 Configuration to eBPF Map:
       - Rules: block write "/usr/bin/**"
       - Labels: mcp.ac.filesystem.read
                                │
                                ▼
       [ STEP 2: AGENT STARTS EXECUTION ]
       Agent starts under PID 2048. Bound to Domain 1 (Child of Domain 0).
       Inherits: Rules (0x01), Labels (0x00).
                                │
                                ▼
       [ STEP 3: RUNTIME DELTA SUBMISSION ]
       Agent attempts to write to /usr/bin/python to modify interpreter.
       Syscall intercepted by BPF-LSM (fs_write hook).
                                │
       Is PID 2048 allowed? ────┼────► No (Rule 0x01 Active in inherited-rule mask).
                                │      BPF-LSM returns -EPERM.
                                ▼
       [ STEP 4: HARNESS RECOVERY PATHWAY ]
       Harness catches -EPERM, maps it to userspace rule metadata,
       and injects semantic feedback to Context:
       "Blocked: Cannot write to system binaries. Use /workspace/tmp."
                                │
                                ▼
       [ STEP 5: AGENT PLANS RECOVERY ]
       Agent reads context, self-corrects, and redirects writes.
```

---

### Inferred System Specification: The Unified Sovereign AI Harness

This specification details the structural implementation of the **Hierarchical Policy Domain** within a zero-trust, kernel-enforced agent runtime.

```c
#include <linux/bpf.h>
#include <bpf/bpf_helpers.h>

/* Domain Node Definition */
struct policy_domain {
    __u32 parent_domain_id;
    __u64 inherited_rules;   /* Read-only rule bitmask from higher authority */
    __u64 inherited_labels;  /* Read-only inherited safety labels */
    __u64 local_rules;      /* Locally authored rules (agent deltas) */
    __u64 active_labels;     /* Dynamic IFC labels currently in this domain */
};

/* PID to Domain Mapping Map */
struct {
    __uint(type, BPF_MAP_TYPE_HASH);
    __type(key, __u32); /* Process TGID/PID */
    __type(value, __u32); /* Domain ID */
    __uint(max_entries, 10240);
} pid_domain_map SEC(".maps");

/* Domain Registry Map */
struct {
    __uint(type, BPF_MAP_TYPE_HASH);
    __type(key, __u32); /* Domain ID */
    __type(value, struct policy_domain);
    __uint(max_entries, 128);
} domain_registry SEC(".maps");

/* Synchronous Pre-Operation Enforcement Hook (BPF-LSM) */
SEC("lsm/file_permission")
int BPF_PROG(enforce_domain_boundary, struct file *file, int mask) {
    __u32 pid = bpf_get_current_pid_tgid() >> 32;
    __u32 *domain_id = bpf_map_lookup_elem(&pid_domain_map, &pid);
    
    if (!domain_id) {
        return 0; /* Unmonitored process space */
    }

    struct policy_domain *dom = bpf_map_lookup_elem(&domain_registry, domain_id);
    if (!dom) {
        return 0;
    }

    /* Bitwise comparison: Evaluate inherited and local rules */
    __u64 active_rules = dom->inherited_rules | dom->local_rules;
    
    /* If a write occurs on a restricted target, assert rules */
    if (mask & MAY_WRITE) {
        if (active_rules & 0x01) { /* Assuming Bit 0 represent write locks on system targets */
            bpf_printk("ActPlane Domain Intercept: Blocked write by PID %d\n", pid);
            return -EPERM; /* Return EPERM to trigger harness semantic feedback loop */
        }
    }

    return 0;
}
```

---

### Three Rigorous Full Non-Obvious Research Prompts

Derived from SEMA, ActPlane, AgentSpawn, and Context Codec.

#### Prompt 1: Verifiable Zero-Trust Cross-Harness State Synchronization via SEMA-Merkle Trees
> **System Architecture Target:** A decentralized multi-agent system where heterogeneous agent harnesses (e.g., running LangGraph, Mastra, and custom runtimes) must synchronize task execution state over low-trust, high-latency channels without a centralized database, maintaining formal verification of state transitions.
>
> **Research Objectives:**
> 1. Design a formal systems specification for encoding the complete agent state tuple $S(t) = (M_{\mathrm{epi}}, M_{\mathrm{sem}}, M_{\mathrm{work}}, \mathcal{K}, \mathrm{Ctxt}, \Psi)$ into a directed **SEMA-Merkle Tree** structure, where every leaf node represents a cryptographically hashed SEMA Pattern Card (e.g., `BeliefTracking#c78f`, `Task#b290`).
> 2. Define the mathematical rules for **State-Transition Proofs** ($P_{\Delta}$). When an agent executes a tool call and modifies its working memory $M_{\mathrm{work}}$ to $M_{\mathrm{work}}'$, it must generate a lightweight cryptographic proof demonstrating that the modification strictly conforms to the parent's contract constraint $\Phi \in \mathcal{K}$ without disclosing the raw, verbose content of $M_{\mathrm{work}}'$.
> 3. Construct a **Decompression Reconstruction Protocol** where receiving harnesses can ingest this Merkle state, verify the integrity of the state transition via leaf-hash evaluation, and selectively "page in" only the necessary context branches required to execute the next logical step (isomorphic to virtual memory page faults). Include formal algorithms for resolving state contradictions (hash collisions and semantic branch drift) using a decentralized consensus mechanism.

#### Prompt 2: ActPlane eBPF IFC DSL Synthesis for Dynamic Multi-Agent Collaboration
> **System Architecture Target:** A system-level policy engine that dynamically compiles natural-language instructions (e.g., `CLAUDE.md`, `AGENTS.md`) into OS kernel-enforced Information-Flow Control (IFC) policies to block indirect prompt injections and shell escapes across dynamically spawned sub-agents.
>
> **Research Objectives:**
> 1. Define a formal context-free grammar (CFG) for an **ActPlane IFC DSL** that maps high-level agentic safety invariants (e.g., "Sub-agent $C$ spawned by Parent $P$ can write to file $F$ only if $F$ has been validated by verifier script $V$") into deterministic kernel constraints.
> 2. Design a compilation pipeline that utilizes an LLM as a **Constrained Semantic Parser** to translate natural-language policies into this DSL. The pipeline must bind every requirement to a programmatic verification metric and output verified-by-construction JSON schemas.
> 3. Architect the **eBPF Kernel Enforcement Engine** that loads these DSL policies at runtime. Detail how the engine uses BPF LSM hooks to intercept `sys_enter` events (specifically `execve`, `openat`, and `socket` connections), tracks data flow taint across process boundaries using label propagation, and handles policy violations. 
> 4. Specify the **Semantic Feedback Loop** using the `SECCOMP_RET_USER_NOTIF` architecture. When a system call is blocked, the engine must construct a structured error payload detailing the closest fuzzy match of the violated DSL rule and stream it back into the agent's context window to trigger the self-correction loop without causing a hard crash.

#### Prompt 3: AgentSpawn Metacognitive Auto-Tuning via Trajectory-Driven Reinforcement Learning
> **System Architecture Target:** An autonomous, self-improving multi-agent codebase engineering platform (such as HarnessX or AEGIS) that optimizes its own spawning, memory compaction, and tool-routing parameters by learning from historical execution logs.
>
> **Research Objectives:**
> 1. Formulate the **Metacognitive Spawning Policy** as a Markov Decision Process (MDP). Define the state space using the runtime complexity metrics vector $\Psi = \{I_f, C_c, F_c, O_c, U_c\}$ (representing context size, cyclomatic complexity, test failure density, file edit volume, and uncertainty metrics).
> 2. Construct the **Delta-Slicing Optimizer** ($\Delta$). The optimizer must learn to parameterize the memory slicing relevance function $r(m, T_{\text{child}})$ to maximize the Critical Atom Recall (CAR) of the child agent while minimizing token overhead.
> 3. Design an offline, retrospective learning pipeline (**Retrospective Harness Optimization - RHO**) that ingests long execution trajectories (up to 10M tokens), runs a multi-agent "Digester" to isolate failure modes (e.g., semantic mutation, weakening, polarity flips), and generates a pairwise preference dataset of harness configurations.
> 4. Detail the **Auto-Tuning Reinforcement Learning Loop** (using PPO or DPO) that optimizes the composite complexity weights $w_i$ and the spawning threshold $\delta$ against a reward function that jointly penalizes token spend, execution latency, and task failures.

---

📊 Would you like to model a simulated run of this architecture under a compound failure scenario to map the exact cost-correctness boundary?