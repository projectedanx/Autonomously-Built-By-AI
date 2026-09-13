### The "Burger Anomaly": A Formal Specification of Planning and Backtracking Failures

In the engineering of autonomous social agents, the **Burger Anomaly** is a specialized instantiation of the classic **Sussman Anomaly** modeled within the *Robotouille* cooking simulator. It serves as a rigorous testing ground to evaluate whether an agent's cognitive architecture can handle **interleaving subgoals** and **irreversible environmental constraints** without falling into infinite, token-consuming deadlocks.

---

### 1. Formal System Specification

The Burger Anomaly is defined over a discrete, partially observable state-space consisting of spatial coordinates, container capacities, and stack topologies.

```
[ INITIAL STATE ]
table1 : [ bottombun1 (bottom) | topbun1 (top) ]  <-- Stacked
table2 : [ (empty) ]
table3 : [ patty1 ]
robot1 : at table1, holding: nothing

[ TARGET GOAL STATE ]
Assemble: bottombun1 ➔ patty1 ➔ topbun1 (stacked in exact sequence on a table)
```

#### The Destructive Subgoal Interaction
To achieve the goal, the agent must satisfy two primary subgoals:
1.  $\text{Stack}(\text{patty1 on bottombun1})$
2.  $\text{Stack}(\text{topbun1 on patty1})$

In isolation, these subgoals interact destructively. To assemble the base of the burger, the agent must first **unstack** `topbun1` to access `bottombun1`. However, `table2` is the only empty table. If the agent clears `topbun1` by placing it on `table2`, that table becomes occupied. If the agent then attempts to move `bottombun1` to `table2` to stack it, the action fails because the simulator prohibits placing two unstacked items side-by-side on the same workspace.

---

### 2. The Linear Failure Mode (The ReAct Deadlock)

When evaluated under a standard linear execution model (like `ReAct`), the agent is forced to process its environment as a flat, sequential history: $C_t = C_{t-1} \parallel \langle T_t, A_t, O_t \rangle$. 

```
Linear Planner (ReAct) Execution Trace:
1. Thought: "I need to unstack topbun1 and then move bottombun1."
2. Act: Unstack topbun1 from bottombun1 ➔ Place on table2. (Success)
3. Act: Move to table1 ➔ Pick up bottombun1 ➔ Move to table2.
4. Act: Attempt to place bottombun1 on table2.
   ➔ ❌ Fail: table2 is occupied by topbun1!
```

At this juncture, a flat, sequential agent experiences **predictive-behavioral decoupling** or **context drift**. The failure observation is appended to the linear context window, pushing early strategic plans further away from the active attention head. 

Because the model lacks a hierarchical representation of its goals, the failed attempt to place the bun on the occupied table becomes an "attention sink". The model enters an **infinite unstack/stack loop**—repeatedly picking up, placing, and moving the same ingredients back and forth between `table1` and `table2` without ever resolving the underlying obstruction.

---

### 3. The Recursive Solution (ReCAP Backtracking and Refinement)

The Recursive Context-Aware Planning (**ReCAP**) framework bypasses this failure by modeling the execution space as a **dynamic context tree**.

```
               [ Parent Node: Prepare Burger ]
                             │
              ┌──────────────┴──────────────┐
              ▼                             ▼
       [ Subtask 1 ]                 [ Subtask 2 ]
    Unstack topbun1               Assemble Base & Patty
     (Leaves table1)              (Pruned & Refined on Fail)
              │                             │
              ▼                             ▼
       [ Table2 Occupied ] ➔➔➔➔➔ Backtrack to Parent Node
```

#### Step-by-Step Recovery Trace:
1.  **Downward Decomposition:** ReCAP decomposes the parent task into an initial subtask list $S$:
    1.  `Unstack topbun1 from bottombun1`
    2.  `Move bottombun1 to table2` (Suboptimal step)
    3.  `Move patty1 and stack on bottombun1`
    4.  `Stack topbun1 on patty1`
2.  **Primitive Execution:** The agent executes the first subtask. `robot1` unstacks `topbun1` and places it on `table2`. 
3.  **The Backtrack Trigger:** The moment this subtask terminates, ReCAP **backtracks** to the parent node. Rather than blindly proceeding with the original plan, the parent node observes the updated environment state and evaluates the viability of the remaining subtasks.
4.  **Plan Refinement and Node Pruning:** The refinement function $\rho$ triggers. Since `table2` is now occupied by `topbun1`, the agent identifies that the original Step 2 (`Move bottombun1 to table2`) is invalid. The unexecuted, suboptimal subtasks are immediately **pruned and removed** from the active context tree.
5.  **Dynamic Replanning:** The agent constructs a fresh, logically consistent branch to route around the blockage:
    *   **Move** back to `table1` and **Place** `bottombun1` back down to serve as the stable assembly base on `table1`.
    *   **Go** to `table3`, **Pick up** `patty1`, and **Stack** it directly onto `bottombun1` on `table1`.
    *   **Go** to `table2`, **Pick up** `topbun1`, and **Stack** it on top of the patty on `table1`.

By nesting these plans inside a self-correcting loop, the agent successfully assembles the burger on `table1` while maintaining absolute goal consistency across high-to-low-level transitions.

---

### Inferred Harness Specification & High-Value Research Prompts

To systematically diagnose and align planning capabilities under dynamic constraints, we formalize the following reverse-engineered specifications and experimental prompts:

```
[ EPISTEMIC PLANNING VERIFIER HARNESS ]
                  │
                  ├──► Input: PDDL Initial State s_0 & Goal State G
                  ├──► Monitor: Step-wise Plan Pruning Rate ρ_prune
                  └──► Metric: Loop Detection Latency & Step-wise Regret
```

#### Research Prompt 1: Topological Cache Pruning for Recursive Backtracking Recovery
> **Domain:** Low-Level Transformer Memory, Topological Data Analysis (TDA), and Agentic Backtracking.
>
> **Task:** Design a PyTorch-based memory management scheduler that applies Topological Data Analysis to prune a sliding-window KV cache during recursive backtracking in high-depth planning tasks (e.g., $N$-order Sussman Anomalies).
>
> **Architecture & Implementation Requirements:**
> 1. Write a pipeline using `Dionysus` or `Gudhi` to track the persistent homology of token embeddings in the residual stream during multi-step planning. 
> 2. Model the active parent-child nodes of a ReCAP tree as a high-dimensional point cloud. Extract connected components ($H_0$) representing persistent, high-level goals and identify redundant loops ($H_1$) representing failed action sequences.
> 3. Implement a dynamic KV cache controller: When the agent backtracks, evict the tokens corresponding to $H_1$ loops (outdated observations and failed actions) to prevent "context rot", while strictly protecting the $H_0$ components (global goal anchors) to avoid perplexity spikes.
> 4. Verify the performance across 100 Robotouille traces, measuring the reduction in step-wise regret and total token consumption compared to standard sliding-window baselines.

#### Research Prompt 2: Neuro-Symbolic BDI Scaffolding to Mitigate Plan-Space Degeneracy
> **Domain:** Cognitive Agent Architectures, Answer Set Programming (ASP), and Robust Planning.
>
> **Task:** Architect a hybrid neuro-symbolic execution harness that wraps a frontier LLM (e.g., Qwen-2.5-72B-Instruct) inside a formal Belief-Desire-Intention (BDI) engine to eliminate unstack/stack deadlocks under zero-shot pass@1 protocols.
>
> **Architecture & Implementation Requirements:**
> 1. Construct an XML-enforced parser that partitions the LLM's in-context reasoning into explicit, structured blocks: `#Beliefs` (PDDL state fluents), `#Desires` (hierarchical goals), and `#Intentions` (proposed action paths).
> 2. Build a symbolic compilation layer in Python that translates these parsed text blocks into formal Answer Set Programming (ASP) rules. 
> 3. Run the compiled rules through a symbolic solver (e.g., `Clingo`) at every step to verify that the proposed intention is logically consistent with the current belief state. If the solver detects an environmental constraint violation (such as attempting to place an item on an occupied table), the symbolic layer must veto the token generation, inject a "Precondition Blocked" error into the active memory, and force a recursive context-aware replanning call (ReCAP).
> 4. Benchmark this neuro-symbolic harness against vanilla ReAct on the Robotouille burger assembly task, evaluating the strict pass@1 success rate under a 64-message limit.

#### Research Prompt 3: Quantifying the Expectation-Realization Gap under Group-Feasible Action Space Constraints
> **Domain:** Multi-Agent Coordination, Game Theory, and Empirical Evaluation.
>
> **Task:** Implement a multi-agent evaluation framework to measure the "expectation-realization gap" of hierarchical planning agents operating in resource-constrained, cooperative-competitive (mixed-motive) environments.
>
> **Architecture & Implementation Requirements:**
> 1. Build an interactive simulator based on *Robotouille* or *Colored Trails* where multiple agents must coordinate to access shared, limited resources (e.g., cutting boards, knives, and tables).
> 2. Implement the **Group Feasible Action-Space Reduction (group FeAR)** metric to quantify collective causal responsibility: measure how much a group of agents restricts the available actions of others.
> 3. Compare two population configurations:
>    *   *Configuration A:* A flat hierarchy where agents communicate unconstrained plans peer-to-peer.
>    *   *Configuration B:* A hierarchical coordination model where a designated manager agent decomposes tasks and allocates subtasks via a Contract Net Protocol.
> 4. Analyze the emergence of deadlocks and coordination overhead ($O(N^2)$ vs. $O(N)$ messages). Measure whether the introduction of recursive Theory of Mind (ToM) beliefs allows agents to bypass physical resource contention and minimize group-level regret.

---
📊 Would you like me to construct a Python script using matplotlib to plot the success rates and average token costs of ReAct vs. ReCAP across different plan depths to visualize how the "planning gap" scales?