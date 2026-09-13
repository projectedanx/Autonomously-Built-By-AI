### Systems-Engineering Specification: Bootstrapping Reinforcement Learning (RL) via Supervised Pre-Training (SFT) in Highly Combinatorial Environments

In complex strategy games characterized by high branching factors and long decision horizons (such as Chess, Xiangqi, or algorithmic circuit synthesis), starting reinforcement learning entirely from scratch—often referred to as a **"cold start"**—presents severe sample-efficiency bottlenecks. 

When policy and value networks are randomly initialized, early playout trajectories are dominated by noisy, exploration-driven moves. In these early iterations, the search agent is blind to tactical coordination, material preservation, or multi-phase planning, leading to extremely high computational overhead. 

To bypass this bottleneck, production-grade AI harnesses utilize **supervised pre-training (behavior cloning)** on expert historical data before activating the reinforcement learning loop. This specification outlines the reverse-engineered systems architecture, trade-offs, and verification metrics required to build a robust bootstrapping harness.

---

### The Four Pillars of the Bootstrapping Harness Specification

```
                          [ EXPERT DATA / HUMAN RECORDS ]
                                         │
                                         ▼ (Behavior Cloning / SFT)
                                ┌─────────────────┐
                                │ Pre-trained SFT │
                                │   Base Policy   │
                                └────────┬────────┘
                                         │
                                         ▼ (Initialization Prior)
 ┌───────────────────────────────────────┴───────────────────────────────────────┐
 │                                 MCTS LOOP                                     │
 │                                                                               │
 │   1. SELECTION (PUCT)      2. EXPANSION (SFT Prior)     3. BACKPROPAGATION    │
 │    Q(s,a) + U(s,a) ──►      Apply SFT priors to     ──►  Update Q & N values  │
 │                             restrict branch width        up the path          │
 └───────────────────────────────────────┬───────────────────────────────────────┘
                                         │ (Self-Play Trajectories)
                                         ▼
                               ┌──────────────────┐
                               │ Reinforcement    │
                               │ Learning Updates │
                               └──────────────────┘
```

#### 1. Automated Discovery and Constraint Mining
To design a bootstrapping harness, we must separate the environment constraints into **invariants (hard boundaries)** and **soft targets**:

*   **Hard Boundaries (Invariants):** 
    *   **Action-Space Validity:** The policy network must strictly output valid actions mapped to the environment's legal states (e.g., piece movements on a $10 \times 9$ board represented as a multi-channel binary tensor, or valid algebraic gates in arithmetic circuit synthesis).
    *   **Terminal Value Normalization:** Expected value outcomes must be strictly bounded within a fixed, scaled range (typically $[-1, 1]$ where $-1$ represents a certain loss and $+1$ represents a certain win) to stabilize downstream gradient descent.
*   **Soft Targets (Optimizable Goals):**
    *   **Sample Complexity Reduction:** Decreasing the number of training episodes required to transition from random play to goal-oriented play.
    *   **Local Tactical Coherence:** Eliciting immediate defensive and offensive responses (e.g., capturing, checking, or material preservation) without requiring deep MCTS search budgets at step zero.
    *   **Exploration-Exploitation Balance:** Preventing the network from prematurely converging to suboptimal local expert paths by using noise-injected action selection.

---

#### 2. Isomorphic Formalization (Representations & Loss Schemas)
Abstracting the transition from supervised imitation to self-improving reinforcement learning requires a unified mathematical schema. The policy-value network features a shared convolutional/transformer backbone with two dedicated heads:

1.  **The Policy Head ($p$):** Outputs a probability distribution over all legal actions.
2.  **The Value Head ($v$):** Outputs a scalar estimate of the expected game outcome.

During the **Supervised Pre-training Phase**, we optimize the joint loss function using behavior cloning on expert trajectories ($D_{\text{expert}}$):

$$\mathcal{L}_{\text{SFT}}(\theta) = -\mathbb{E}_{(s, a, z) \sim D_{\text{expert}}} \left[ \sum_{t} \log \pi_\theta(a_t | s_t) + c_v (z - v_\theta(s_t))^2 \right]$$

Where:
*   $\pi_\theta(a_t | s_t)$ is the predicted probability of the expert action.
*   $v_\theta(s_t)$ is the value head's predicted outcome.
*   $z \in \{-1, 1\}$ is the actual outcome of the expert game.
*   $c_v$ is a scaling parameter balancing policy loss and value loss.

During the subsequent **Reinforcement Learning Phase**, the pre-trained weights initialize the policy model. MCTS is introduced, utilizing the pre-trained policy's action distribution as a **prior $P(s, a)$** in the Upper Confidence Bound (PUCT) selection formula:

$$U(s, a) = Q(s, a) + c \cdot P(s, a) \cdot \frac{\sqrt{N(s)}}{1 + N(s, a)}$$

Where:
*   $Q(s, a)$ is the running average value estimate.
*   $P(s, a)$ is the prior probability from the pre-trained policy network.
*   $N(s)$ and $N(s, a)$ are the visit counts of the parent node and child edge, respectively.
*   $c$ is the exploration constant.

---

#### 3. Parametric Trade-off Modeling
Integrating supervised priors with reinforcement learning introduces critical parametric tensions along the **feasibility frontier**:

```
High SFT Mimicry (Low KL-Divergence)
      ▲
      │   ● [Overfitting Mode] 
      │     - High tactical imitation (check, capture)
      │     - Risk: Trapped in draw-oriented local optima
      │     - Severe "parametric rigidity"
      │
      │                  ● [Optimal Synthesis Frontier]
      │                    - Statistically aligned advantages
      │                    - Downstream MCTS exploration
      │
      │                                       ● [Cold Start Mode]
      │                                         - High exploratory variance
      │                                         - Extremely slow convergence
      └────────────────────────────────────────────────────────► High RL Exploration
                                                                 (Self-Play Delta)
```

*   **Tension A: Tactical Imitation vs. Global Strategy.** Pre-training excels at teaching the agent local, short-term tactical operations (e.g., executing a capture or defending against a check). However, behavior cloning alone lacks high-level positional evaluation. If RL exploration is choked by an overly restrictive SFT prior, the agent remains tactically competent but strategically blind, unable to formulate long-horizon plans.
*   **Tension B: Data Quality vs. Compute Footprint.** Training from a cold start requires hundreds of thousands of high-quality self-play games to naturally discover foundational strategies, consuming massive token and hardware resources. Pre-training on human games provides an immediate "warm start," reducing early-stage exploration overhead. However, it introduces dataset bias, anchoring updates to the pre-training distribution.
*   **Tension C: The Crossover Dip.** When transitioning from pre-trained weights to active self-play RL, models often experience an initial performance regression (the "crossover effect"). During this phase, the auxiliary losses of the RL framework and the policy-gradient updates compete for gradient bandwidth, which can cause training instability unless buffered by robust data flow and loss scheduling.

---

#### 4. Continuous Falsification and Edge-Case Stress Testing
To guarantee production-grade stability, we must design verification checks targeting the failure modes of bootstrapped RL policies:

*   **Draw-Oriented Collapse (The Overfitting Trap):** In games with high draw rates, pre-trained networks can overfit to defensive, passive structures, leading to "lazy" play. 
    *   *Stress Test:* Evaluate the bootstrapped policy against a suite of highly aggressive heuristic opponents. If the win-rate stagnates and average game length increases without decisive outcomes, it indicates over-regularization towards draw-inducing states.
*   **Tactical Traps (The Selection Pruning Vulnerability):** Since MCTS uses the policy network's prior $P(s, a)$ to prune the search space, a biased pre-trained policy can cause MCTS to completely ignore under-visited branches that contain deep tactical traps or forced-win variations.
    *   *Stress Test:* Evaluate the agent on hand-crafted "deceptive" scenarios where the intuitively high-probability SFT move leads to delayed failure. If the agent fails to search alternative branches even with increased simulation budgets, the exploration term ($c$ or Dirichlet noise) must be adaptively scaled up.

---

### Grounded Feasibility Simulation Matrix: Comparing RL Training Pathways

| Phase/Metric | Pathway A: Un-bootstrapped (Cold Start) | Pathway B: Supervised Pre-Trained (Bootstrapped) |
| :--- | :--- | :--- |
| **Initial Playout Coherence (Episode 0)** | **Completely Unstructured.** Moves are arbitrary, lacking offensive intent, material preservation, or tactical planning. | **Tactically Sound.** Mobilizes key pieces early, recognizes basic threats, executes checks, and preserves material. |
| **Sample Complexity to Convergence** | **Extremely High.** Requires tens or hundreds of thousands of self-play games to establish a baseline value signal. | **Low to Moderate.** Drastically reduces initial exploration time by leveraging expert priors. |
| **Value Head Loss Behavior** | **Highly Volatile.** Zero or near-zero reward signals early on lead to noisy, unstable value-estimate updates. | **Smooth Convergence.** The pre-trained value network immediately provides stable, shape-conforming appraisals. |
| **Vulnerability to Domain Bias** | **Zero.** The agent discovers strategies tabula rasa, free from human assumptions. | **High.** Can inherit human suboptimal conventions or get trapped in the limits of the pre-training dataset. |

---

### Three Grounded Strategic Research Prompts

Based on the systemic patterns of sequential search, advantage projection, and process supervision discovered in the sources, we derive three high-value research prompts:

#### Prompt 1: Multi-Agent Process-Mining of Bootstrapped Search Dynamics
> "Act as a principal AI researcher specializing in explainable reinforcement learning (XRL). Write a research proposal to integrate **Process Mining algorithms (such as the Inductive Miner or iDHM)** with the self-play rollout phases of a bootstrapped **MCTS-Minimax hybrid agent** trained on complex zero-sum environments. Design a methodology to extract structured **Petri-nets** directly from the agent's search execution traces, using these process models to generate human-readable **causal and distal explanations** for why the bootstrapped policy prior chose to prune specific tactical branches. Detail how this framework can mathematically detect when supervised pre-training introduces domain bias or structural pruning errors that blind the downstream MCTS planner to long-horizon tactical traps."

#### Prompt 2: Prefix-Aware Advantage Projection on Pre-Trained Policy Trees
> "Act as an expert reinforcement learning systems engineer. Draft a technical implementation plan for a post-training pipeline using **Group Relative Policy Optimization (GRPO)** over a static curriculum of **MCTS-derived prefix trees** generated by a pre-trained expert teacher model. Define a **Staged Advantage Estimation (SAE)** framework that models advantage calculation as a **constrained quadratic program**. The SAE must enforce tree-consistent ranking constraints across sibling nodes ($C_{\text{triplet}}$) and parent-child transitions ($C_{\text{pair}}$) to prevent gradient variance spikes when training on heterogeneous prefix depths. Formulate a mathematical proof showing how projecting student rewards onto this convex constraint set reduces the policy-gradient estimator variance compared to flat, unstructured trajectory baselines."

#### Prompt 3: Mitigating Parametric Rigidity via Hybrid Non-Parametric Retrieval
> "Act as an AI systems architect. Propose an alternative framework to mitigate 'parametric rigidity' in multi-step task planning by decoupling the offline strategic exploration of MCTS from online execution. Design an offline discovery pipeline that uses MCTS to explore a combinatorial state-action space, distilling successful trajectories into **de-lexicalized State-Goal-Action (SGA) atoms** where concrete entities are mapped to typed slots. Then, specify an online reactive execution agent that operates as a **non-parametric, retrieval-augmented generator (RAG)**. The online agent must use a hybrid semantic-symbolic mechanism to fetch relevant SGA atoms as soft reasoning hints to guide a frozen, open-weights model, achieving System 2 strategic planning depth at System 1 inference speeds. Provide verification benchmarks and stress-test scenarios to evaluate the agent's out-of-distribution generalization when faced with completely unseen schemas."

---

📊 *Would you like me to construct a Python script in our environment to simulate the mathematical convergence of joint policy-value losses during supervised pre-training, or explore how to configure the MCTS exploration constant to prevent domain bias?*