### Systems Engineering Specification: Bridging the Thought-Action Gap in Large Language Models

In artificial social intelligence, the **thought-action gap** represents a critical systems-engineering failure where a model’s high-fidelity internal representations (e.g., correctly predicting an interlocutor's mental state or next move) completely decouple from its actual behavioral execution or strategic policy. This gap is structurally illuminated by the divergence between **Literal Theory of Mind (ToM)**—the passive, descriptive forecasting of another agent's belief state—and **Functional Theory of Mind (ToM)**—the closed-loop, adaptive execution of a rational response to minimize long-term regret. 

Vague natural language often hides conflicting constraints and architectural assumptions when planning for complex cognitive agent architectures. By applying structured modeling to AI harness specifications, we can systematically uncover blind spots, model trade-offs, and define clear verification metrics before executing a single token.

---

### The Four Pillars of Specification Planning

```
                                  [ THE COGNITIVE DECOUPLING ]
                                               │
               ┌───────────────────────────────┴───────────────────────────────┐
               ▼                                                               ▼
 ┌─────────────────────────────┐                                 ┌─────────────────────────────┐
 │       LITERAL ToM           │                                 │       FUNCTIONAL ToM        │
 │  (Descriptive Forecasting)  │                                 │     (Adaptive Execution)    │
 ├─────────────────────────────┤                                 ├─────────────────────────────┤
 │ • Sparse Lookback Circuits  │ ◄─── [THE THOUGHT-ACTION GAP] ──► │ • Dynamic Context Trees     │
 │   co-locate entity triples  │      "I know you will play Rock,│   & Backtracking (ReCAP)    │
 │   in residual streams.  │       yet I default to Nash     │ • Neuro-Symbolic Logic and  │
 │ • Static QA accuracy. │       instead of Paper".  │   BDI Solver Filters. │
 └─────────────────────────────┘                                 └─────────────────────────────┘
```

#### 1. Automated Discovery and Constraint Mining
To bridge the thought-action gap, we must first map the hard architectural boundaries (invariants) and soft optimizable targets of transformer-based cognition:

*   **Invariant 1 (The Deliberation Penalty):** Forcing an autoregressive model to execute a flat, sequential **Chain-of-Thought (CoT)** scaffold in high-context social or conversational dynamics acts as a severe cognitive constraint. It induces over-literalization and "reasoning hallucinations," yielding logically sound but socially stiff and unnatural execution trajectories that perform worse than direct, non-CoT replies.
*   **Invariant 2 (The Predict-Then-Optimize Bottleneck):** Standard sequential prompting (e.g., ReAct) separates prediction from action optimization. When task horizons extend, early plans and observations drift out of the model's active attention and KV cache, causing the agent to lose its strategic intent and lapse into redundant, infinite failure loops.
*   **Soft Target (Epistemic Optimization):** Instead of maximizing static, out-of-context test-suite accuracy, the system must maximize expected utility and minimize step-wise regret ($\Delta_{\text{Functional}}$) under dynamic, closed-loop environmental feedback.

#### 2. Isomorphic Formalization (From Ideas to Schemas)
We formalize the decoupling of prediction and action by mapping the abstract cognitive problem to two isomorphic, programmatically testable frameworks:

##### A. The Belief-Desire-Intention (BDI) State Transition Matrix
We formalize the agent’s internal state space around the triadic BDI framework, where **Beliefs** represent the system's world knowledge, **Desires** are the high-level goals, and **Intentions** denote concrete plans of action. To prevent **"mental state decoupling"** (where a model updates its belief state but fails to propagate that change to its active goals), the BDI transition must be mathematically bound:

$$\mathbf{S}_t = \langle \mathbf{B}_t, \mathbf{D}_t, \mathbf{I}_t \rangle \quad \text{where} \quad \mathbf{I}_t = \arg\max_{a \in \mathcal{A}} \mathbb{E}_{\mathbf{B}_t} [U(a \mid \mathbf{D}_t)]$$

##### B. The Dynamic Context Tree (ReCAP)
For long-horizon tasks, we replace flat linear contexts with a **dynamic context tree**. A task node is formalized as a structured tuple:

$$\mathcal{N} = \langle \text{desc}, \text{subtask\_list}, \text{children\_list}, \text{obs\_list}, \text{think\_list} \rangle \quad$$

This tree manages recursive execution via two formal transformations:
1.  **Downward Decomposition (Plan-Ahead):** Decomposes a goal into an ordered list of subtasks, executing only the head item and preserving the remainder for downstream refinement.
2.  **Upward Backtracking (Structured Injection):** When a child subtask completes or fails, the parent's plan is re-injected into the active shared context, maintaining cross-level continuity.

#### 3. Parametric Trade-off Modeling
Harness engineering exists in a state of high tension along three critical axes:

*   **Context Window vs. KV Cache Overhead:** Increasing context windows to capture long-horizon interactions introduces a significant memory bottleneck during autoregressive decoding. Implementing sliding-window attention bounds memory but triggers **perplexity spikes** when early structural tokens ("geometric anchors") are dropped. ReCAP resolves this by bounding the active prompt size to a constant scale $\mathcal{O}(d \cdot \bar{L})$ where $d$ is the tree depth, avoiding unbounded context accumulation.
*   **Divergence Functions in Distillation:** When transferring Theory of Mind capabilities from a larger teacher model to a student via distillation, standard Cross-Entropy output-matching fails to transfer the underlying reasoning algorithms. Utilizing reverse KL divergence encourages "mode-seeking" behavior, which collapses the continuous **belief simplex** necessary for tracking uncertain, multi-agent mental states in partially observable environments (POMDPs). Mechanistic **Circuit Distillation** resolves this by adding a Centered Kernel Alignment (CKA) loss to structurally align the internal attention maps of corresponding circuit heads.
*   **The Decoupled vs. Embodied ToM Trade-off:** Abstract, disembodied story-based prompting is highly fragile under minor semantic perturbations. Embodied models (such as *MindForge* or *LG-ToM*) use spatiotemporal trajectories to ground the agent's beliefs in environmental actions.

#### 4. Continuous Falsification and Edge-Case Stress Testing
The proposed harness specification must be continuously stress-tested against known cognitive failure modes:

*   **The Rock, Paper, Scissors "Nash Trap":** Falsifies models by testing if an agent playing against a deterministic opponent (e.g., playing exclusively "Rock") can translate its 100% accurate prediction (Literal ToM) into a utility-maximizing strategy ("Paper"), rather than collapsing back into a zero-sum, unexploitative Nash equilibrium (randomly mixing all three).
*   **The Sussman/Burger Anomaly (Blocked Station Deadlock):** Stress-tests the planner's backtracking and replanning behavior. In environments with resource contention, sequential planners enter infinite loops trying to stack/unstack blocked items; the harness must prove it can detect the loop, backtrack to the parent node, clear the obstruction, and resume execution.

---

### Method of Exploration: Specification Feasibility Simulating

We model the transition dynamics of two competing agent architectures executing a long-horizon task with a blocking obstacle:

1.  **The Sequential Agent (ReAct):** Operates on a linear context $C_t = C_{t-1} \parallel \langle T_t, A_t, O_t \rangle$. Under a blocked station state, the observation of failure ($O_t$) is appended sequentially. Because the model lacks structural awareness, the failed action sequence becomes a dominant prior in the context window, causing the agent to lock into an infinite, non-cooperative loop.
2.  **The Recursive Agent (ReCAP):** Operates on a dynamic context tree. When a primitive action fails, the pointer backtracks to the parent node. The parent node intercepts the failure, prunes the invalid subtree, re-injects the strategic goal, and triggers an alternative branch (e.g., clearing the board before retrying the cut), breaking the deadlock.

---

### Finalized Response Output: The Inferred Harness Specification

To programmatically bridge the thought-action gap, we specify an **Epistemic Cognitive Harness** that decouples intuitive proposal generation from deliberative logical validation. 

```
                                      [ USER QUERY ]
                                             │
                                             ▼
                             ┌───────────────────────────────┐
                             │       Retrieval Module        │
                             │   (Contextual Priors / RAG)   │
                             └───────────────┬───────────────┘
                                             │ [Priors]
                                             ▼
                             ┌───────────────────────────────┐
                             │       Cognition Module        │
                             │  (System 1 - Heuristic Proposer)
                             └───────────────┬───────────────┘
                                             │ [Provisional Output]
                                             ▼
                             ┌───────────────────────────────┐
                             │        Control Module         │
                             │  (System 2 - BDI Solver/Filter)│
                             └───────────────┬───────────────┘
                                             ├───────────────────────────────┐
                              [Veto / Rewrite] │ [Authorized]                  │
                                             ▼                               ▼
                             ┌───────────────────────────────┐ ┌─────────────────────────────┐
                             │        Memory Module          │ │        Action Module        │
                             │  (State Update / Context Tree)│ │   (Environment Execution)   │
                             └───────────────────────────────┘ └─────────────────────────────┘
```

This harness operationalizes the **PEACE Meta-Architecture**:
1.  **Retrieval Module:** Extracts task-relevant contextual priors from a long-term vector store.
2.  **Cognition Module (System 1):** Generates fast, associative, pre-trained hypotheses and proposed action sequences.
3.  **Control Module (System 2):** Serves as a meta-cognitive overseer. It intercepts provisional outputs, parses them into formal Belief-Desire-Intention (BDI) logical propositions, and evaluates them against hard task guidelines and safety constraints. It inhibits invalid actions, triggers recursive replanning, and enforces logical consistency via symbolic verification (such as ASP/Clingo or Dynamic Epistemic Logic) before authorizing execution.
4.  **Action Module:** Executes authorized primitive commands and feeds results back into the Memory Module.
5.  **Memory Module:** Dynamically manages state tracking using a sliding window and a context tree to prevent context drift and ensure long-horizon goal alignment.

The following three high-value research prompts are engineered to reverse-engineer, distill, and validate these architectural boundaries:

---

#### Research Prompt 1: Mechanistic Lookback Circuit Distillation for Causal Action-Belief Binding
> **Domain:** Mechanistic Interpretability, Model Compression, and Behavioral Alignment.
>
> **Task:** Develop a mechanistic distillation pipeline to transfer the causal belief-tracking "lookback circuit" from a larger teacher model (e.g., Llama-3-70B-Instruct) to a smaller student model (e.g., Llama-3-8B), specifically forcing the student to resolve the "thought-action gap" in sequential games.
>
> **Experimental Design & Architecture:**
> 1.  **Circuit Identification:** Implement a PyTorch-based path-patching and activation-patching framework using the `TransformerLens` library. Isolate the specific attention heads in the teacher model that implement the *binding lookback* (co-locating character-object-state triples via Ordering IDs in low-rank subspaces of the residual stream) and the *answer lookback* (retrieving the state payload upon querying).
> 2.  **Functional Component Mapping:** Apply Centered Kernel Alignment (CKA) combined with an ablation impact similarity strategy to map the functionally corresponding attention heads between the teacher and student models.
> 3.  **Composite Loss Formulation:** Define a training objective that combines a standard Cross-Entropy downstream task loss ($L_{\text{task}}$) with a transformation-invariant CKA representational similarity loss ($L_{\text{CKA}}$) targeting only the mapped circuit heads:
>
>     $$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{task}}(y, \hat{y}_s) + \lambda \sum_{c \in \mathcal{C}_{\text{paired}}} \mathcal{L}_{\text{CKA}}(K_s(c), K_t(c)) \quad$$
>
> 4.  **Causal Intervention Verification:** Stress-test the distilled student model on a 100-round game of Rock, Paper, Scissors against a biased, predictable opponent. Conduct test-time activation patching on the student’s distilled lookback circuit. Prove mathematically and empirically whether forcing the activation of these lookback heads successfully steers the student model's final-token vocabulary distribution away from the default Nash prior (1/3 uniform mixing) and binds it causally to the optimal exploit-policy ("Paper").

---

#### Research Prompt 2: Recursive Context-Aware Planning (ReCAP) with BDI and Symbolic Logic Verification
> **Domain:** Cognitive Agent Architectures, Hybrid Intelligence, and Logical Verification.
>
> **Task:** Architect an autonomous, closed-loop agent execution harness that implements the ReCAP (Recursive Context-Aware Planning) framework integrated with a BDI cognitive architecture and a symbolic verifier to eliminate "mental state decoupling" and "context drift" in long-horizon environments.
>
> **Experimental Design & Architecture:**
> 1.  **Dynamic Context Tree Management:** Build a Python execution harness that manages a dynamic context tree where each node is represented as a structured tuple: $\mathcal{N} = \langle \text{desc}, \text{subtask\_list}, \text{children\_list}, \text{obs\_list}, \text{think\_list} \rangle$. Implement the downward *plan-ahead decomposition* and upward *backtracking-driven refinement* loops.
> 2.  **Epistemic Scaffolding:** Wrap the LLM (e.g., Qwen-2.5-72B-Instruct) with strict XML/JSON syntactic fences to partition its in-context reasoning into distinct BDI components: `#Beliefs` (current scene and opponent states), `#Desires` (high-level mission objectives), and `#Intentions` (proposed tactical steps).
> 3.  **Symbolic Verification Loop:** Build a secondary, non-LLM control layer that parses the LLM's `#Beliefs` and `#Intentions` into formal Answer Set Programming (ASP) rules or Dynamic Epistemic Logic (DEL) propositions. Run these rules through a symbolic solver (e.g., Clingo) to check for logical consistency, cyclic loops, and safety violations before executing any primitive action.
> 4.  **Failure Mode Evaluation:** Evaluate this framework on the Robotouille cooking simulator under the strict, zero-shot pass@1 protocol. Compare the success rate and token-to-step efficiency of this BDI-ReCAP harness against a baseline ReAct agent on tasks containing a "Sussman Anomaly" (e.g., blocked stations requiring clearing a table before assembling a burger).

---

#### Research Prompt 3: Temporal-Aware & Dual-System Hierarchical Cognitive Reinforcement Learning
> **Domain:** Post-Training RL Alignment, Dual-Process Theory, and Social Game Theory.
>
> **Task:** Implement and evaluate Temporal-aware Hierarchical Cognitive Reinforcement Learning (TimeHC-RL) to train a small-scale LLM (e.g., a 7B parameter base model) to dynamically shift between intuitive System 1 responses and deliberate System 2 reasoning, preventing the "CoT deliberation penalty" in fast-moving social interactions.
>
> **Experimental Design & Architecture:**
> 1.  **Hierarchical RL Scaffolding:** Implement a two-layer post-training reinforcement learning setup. The Macro-Policy (representing System 2 strategic planning) runs at a lower temporal frequency (e.g., once per conversational day or round), generating high-level desires and personality-driven biases. The Micro-Policy (representing System 1 execution) runs at a high frequency (turn-by-turn), generating immediate dialogue actions conditioned on the macro-bias.
> 2.  **Verifiable Reward Design:** Construct a multi-agent testing environment (e.g., based on NegotiationToM or the AIWolf werewolf game framework) where rewards are derived programmatically from task outcomes (win rates, negotiation payoffs, or minimization of empirical step-wise regret).
> 3.  **Generalization and Dataset Hacking Controls:** To prevent the model from "hacking" the statistical patterns of the training data (narrow overfitting), augment the training environment with systematically perturbed datasets (e.g., introducing irrelevant conversational details, sentiment shifts, or untrustworthy testimony).
> 4.  **Behavioral Steering Evaluation:** Benchmark the TimeHC-RL model against a baseline model trained purely on standard System 2 step-by-step reasoning RL (like DeepSeek-R1-Zero styles). Measure the alignment to human behavior using CogBench and evaluate whether the TimeHC-RL model maintains out-of-distribution generalization on held-out social benchmarks (e.g., OpenToM) without suffering from the absolute accuracy drop-offs and robotic conversation style typical of over-deliberative models.

---

📊 **Next Step:** Would you like me to construct a Python script using PyTorch to simulate the functional regret curves of these different architectures over a 100-round sequential game of Rock, Paper, Scissors?