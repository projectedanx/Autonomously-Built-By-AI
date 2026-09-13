### Systems-Engineering Specification: Diagnostics and Mitigations for Parametric Rigidity in Agentic Planning Harnesses

In production-grade AI harnesses, **parametric rigidity** is a critical failure mode where a model's policy becomes tightly anchored to its pre-trained or supervised fine-tuned (SFT) weight distribution. When transitioning to downstream reinforcement learning (RL) or facing out-of-distribution (OOD) tasks, this rigidity chokes off exploration, causes catastrophic forgetting, and forces the model to rely on shallow, memorized templates rather than generalized reasoning.

To address this bottleneck, we must establish a systems-level evaluation and architectural framework that decouples strategic reasoning from rigid parameter spaces.

---

### The Four Pillars of Rigidity Planning

```
                                [ PARAMETRIC AGENT PIPELINE ]
                                              │
       ┌──────────────────────────────────────┼──────────────────────────────────────┐
       ▼                                      ▼                                      ▼
┌────────────────────────────┐         ┌────────────────────────────┐         ┌────────────────────────────┐
│    Automated Discovery     │         │   Isomorphic Formalization │         │     Parametric Trade-off   │
├────────────────────────────┤         ├────────────────────────────┤         ├────────────────────────────┤
│ • Trace KL-Divergence      │         │ • Construct directed       │         │ • Map the frontier of      │
│   vs. Reward Curve.        │         │   acyclic graphs (DAGs).   │         │   Inference Latency vs.    │
│ • Identify "activity cliff"│         │ • Bind abstract logic to   │         │   Out-of-Distribution      │
│   anomalies in embeddings. │         │   typed, executable slots. │         │   Generalization Accuracy. │
└────────────────────────────┘         └────────────────────────────┘         └────────────────────────────┘
                                              │
                                              ▼
                               ┌────────────────────────────┐
                               │   Continuous Falsification │
                               ├────────────────────────────┤
                               │ • Stress-test with dynamic │
                               │   schema-swaps and tool    │
                               │   precondition violations. │
                               └────────────────────────────┘
```

---

### 1. Automated Discovery and Constraint Mining

To diagnose and isolate parametric rigidity, we first separate the system's operational boundaries into **hard invariants** and **soft targets**:

*   **Hard Boundaries (Invariants):**
    *   **The Representation-Precision Limit:** Neural networks are bound by a **Smoothness Inductive Bias**; they tend to map token-wise or structurally similar inputs to proximal embeddings. However, complex environments (such as molecular chemistry or logic circuit synthesis) feature **"activity cliffs"** where minor structural changes trigger non-linear, drastic shifts in physical or logical outcomes. The policy must have a non-parametric mechanism to represent these non-smooth discontinuities without undergoing continuous weight collapse.
    *   **The KL Exploration Choke:** In standard RL fine-tuning, the Kullback-Leibler (KL) divergence penalty ($\beta \mathbb{D}_{\text{KL}}(\pi_\theta \parallel \pi_{\text{ref}})$) acts as a strict regularizer to prevent policy drift. Under high rigidity, this constraint restricts the agent's action probability distribution, trapping it in local, sub-optimal pre-trained modes.
*   **Soft Targets (Optimizable Goals):**
    *   **Contextual Fluidity:** Bypassing "lexical overfitting" to allow the agent to generalize to entirely unseen API schemas or toolsets without parameter updates.
    *   **Amortized Inference Cost:** Achieving the strategic depth of System 2 thinking (e.g., deep tree search) at the low latency and token cost of System 1 reactive execution.

---

### 2. Isomorphic Formalization (From Rigidity to Schemas)

To mitigate parametric rigidity, we formalize three core architectural schemas that replace implicit weight adaptation with explicit, non-parametric structures.

#### Schema A: De-lexicalized State-Goal-Action (SGA) Atoms
Instead of training the model to memorize concrete, domain-specific strings (which leads to rigid, fragile plans), we apply a **Schema-Guided Abstraction Function $\Phi_\Lambda$** to distill execution trajectories into composable algebraic primitives. 

$$\mathcal{E}_i = \Phi_\Lambda(s_t, g_t, a^*_t) = \langle \hat{S}, \hat{G}, \hat{A} \rangle \quad$$

```json
{
  "sga_id": "api_parameter_filter_01",
  "entry": {
    "state": {
      "description": "Requires filtering candidate database entities using temporal and category attributes.",
      "required_slots": ["<YEAR_VAL>", "<CATEGORY_TAG>"]
    },
    "goal": "Filter available entities matching constraints.",
    "action": "execute_query_search"
  }
}
```
*Grounded in SGA-MCTS: This de-lexicalized structure allows the agent to retrieve abstract rules based on functional intent and instantiate them dynamically with local parameters, ensuring zero-shot transfer across novel tool environments.*

#### Schema B: Trust Calibration and Dirichlet Prior Update
Rather than forcing the search engine to uniformly trust the neural policy's priors, we define a **Dirichlet Trust Policy** where the concentration parameters $\alpha_t$ are dynamically scaled by a running **Trust Score $C_t$**:

$$\pi(a | Z_t, C_t) \sim \text{Dirichlet}(\alpha_t) \quad \text{where} \quad \tilde{\alpha}_t(a) = f(a) \cdot (1 + \beta \cdot C_t) \quad$$

Where:
*   $f(a)$ is the raw action prior generated by the parameterized model.
*   $C_t \in$ is the dynamically updated trust score reflecting how well the model's commonsense aligns with physical observations.
*   When $C_t$ is high (familiar state), the policy peaks sharply around the model's suggestions (exploitation). When $C_t$ is low (OOD or high-risk state), the policy flattens, promoting broad, unbiased tree exploration.

#### Schema C: Decoupled Mixed Discrete-Continuous Loss
To bypass the representation-precision paradox, we isolate qualitative semantic reasoning from quantitative numerical search. The neural network is restricted to generating discrete topological hypotheses, while continuous parameters (e.g., thermodynamic mixing ratios or physical coordinate trajectories) are optimized via a **Differentiable Physics/Kinematics Engine**.

$$\mathcal{L}_{\text{hybrid}} = \mathcal{L}_{\text{ratio}} + \omega_{\text{diff}}\mathcal{L}_{\text{diff}} + \mathcal{L}_{\text{penalty}} \quad$$

---

### 3. Parametric Trade-off Modeling

Evaluating parametric rigidity requires mapping the boundaries of the **feasibility frontier** across competing operational dimensions:

```
OOD Transfer Accuracy
      ▲
      │                              ● [Non-Parametric SGA Retrieval (Ours)]
      │                                - High zero-shot generalization
      │                                - Negligible fine-tuning cost
      │
      │         ● [Parametric Fine-Tuned (SFT)]
      │           - High in-domain accuracy
      │           - Catastrophic OOD forgetting
      │           - Rigid weight anchoring
      │
      │                                       ● [Unconstrained RL Exploration]
      │                                         - High convergence instability
      │                                         - Prohibitive online search latency
      └────────────────────────────────────────────────────────► Inference Efficiency
                                                                 (Normalized Latency)
```

*   **Tension A: Imitation Fidelity vs. Explanatory Generalization.** SFT on human expert trajectories provides rapid convergence and high in-domain accuracy. However, it anchors the policy to human-specific biases, leading to a steep decline in OOD performance when the target domain drifts.
*   **Tension B: Parametric Compression vs. Computational Latency.** Compressing planning logic directly into the model's weights reduces test-time compute. However, resolving multi-step dependencies on unfamiliar tasks requires expensive inference-time tree searches (like MCTS). Shifting this burden to a non-parametric, retrieval-augmented experience store allows System 2 reasoning quality at System 1 speeds.

---

### 4. Continuous Falsification and Edge-Case Stress Testing

To verify if an agentic planning harness has successfully mitigated parametric rigidity, we deploy three automated stress tests:

1.  **The "Activity Cliff" Probing:**
    *   *Mechanism:* Inject minute, non-semantic changes into the task schema (e.g., shifting coordinates slightly or renaming API parameters).
    *   *Falsification Criterion:* If the agent's value head continues to output smooth, optimistic estimates and fails to detect the altered execution constraints, the model is hallucinating transitions due to continuous embedding smoothing.
2.  **The Over-Correction and Skepticism Test:**
    *   *Mechanism:* Introduce a correct, intermediate state update that contradicts the pre-trained model's typical trajectory path.
    *   *Falsification Criterion:* If the model rejects the valid correction due to "defensive alignment skepticism" and insists on backtracking to its pre-trained default, the parametric priors are overly rigid.
3.  **The Dual-Factor Retrieval Audit:**
    *   *Mechanism:* Evaluate the retrieval engine on a low-familiarity target dataset ($S_{\text{fam}} < 0.6$).
    *   *Falsification Criterion:* Measure the ratio of semantic relevance to symbolic feasibility. If the retrieval engine prioritizes semantic text similarity over hard parameter-slot constraints, the system will execute ungrounded, unexecutable plans.

---

### Grounded Feasibility Simulating Matrix: Mitigating Rigidity

| Diagnostic Metric | Rigid Parametric Baseline | Decoupled Non-Parametric Harness | Grounded Source Pattern |
| :--- | :--- | :--- | :--- |
| **Out-of-Distribution (OOD) Pass Rate** | **Catastrophic Failure.** Drops to $<15\%$ on novel tool schemas due to template mismatches. | **Robust Transfer.** Maintains $>61\%$ accuracy by dynamically re-grounding abstract logic. | Decoupled non-parametric retrieval isolates causal logic from surface-level details. |
| **Inference Token Consumption** | **Prohibitive.** Generates massive chain-of-thought steps and rollouts for every query. | **Highly Efficient.** Reduces token cost by up to $76\%$ via cached, retrieved experiences. | Amortizing MCTS search trajectories into retrievable, de-lexicalized assets. |
| **Value Head Behavior under Discontinuity** | **Smoothed Hallucinations.** Fails to detect abrupt state-to-goal transitions (activity cliffs). | **Sharp Discontinuity.** Correctly captures cliffs via discrete, rule-based execution paths. | Decoupling prediction accuracy from weights using symbolic verification loops. |
| **Exploration Entropy ($\mathcal{H}$)** | **Stagnant.** Trapped in pre-trained modes; ignores alternative paths during RL tuning. | **Dynamic.** Broadens search space using uncertainty-aware priors. | Scaling Dirichlet concentration parameters based on real-time task uncertainty. |

---

### Three Grounded Strategic Research Prompts

#### Prompt 1: De-Lexicalized Experience Curation for Cross-Schema Tool Synthesis
> "Act as a principal AI systems architect. Propose a technical implementation plan for a training-free agent harness that mitigates 'parametric rigidity' in tool-use tasks. The system must utilize an offline **Meta-Cognitive MCTS** phase to explore tool-use trajectories, containing **Plan** and **Reflect** operators to generate successful traces. Specify a **Schema-Guided Abstraction Function $\Phi_\Lambda$** that strips out concrete domain strings and maps them to typed, symbolic slots to extract de-lexicalized **State-Goal-Action (SGA) atoms**. For the online reactive execution phase, define a **Dual-Factor Retrieval Scoring Mechanism** that balances semantic relevance with symbolic feasibility to filter out unexecutable candidate plans. Design a validation suite using a continuous **Tool Familiarity Score ($S_{\text{fam}}$)** to prove that this non-parametric retrieval-based approach out-generalizes SFT baselines in high-entropy, out-of-distribution tool environments."

#### Prompt 2: Resolving the Representation-Precision Paradox in Discrete-Continuous Search
> "Act as a senior machine learning researcher. Write a research proposal to solve the **representation-precision paradox** in AI agents tasked with optimizing high-Lipschitz physical processes (e.g., molecular property prediction or automated circuit design) where minor structural shifts cause 'activity cliffs'. Design a neuro-symbolic framework that decouples smooth continuous representations from discrete logical operations. The system must use an LLM strictly as a **prior generator** to propose structural adjustments, while a deterministic **differentiable physics/kinematics solver** performs continuous parameter optimization under physical constraints. Detail the evaluation protocol using synthetic environments to mathematically demonstrate how this decoupled, look-ahead planning framework overcomes the irreducible error limits imposed by neural network smoothness bounds."

#### Prompt 3: Uncertainty-Driven Trust Calibration and Prior Scaling in Stochastic Environments
> "Act as a principal reinforcement learning systems engineer. Draft a technical specification for an **Uncertainty-Aware Adaptive Monte Carlo Tree Search (UA-MCTS)** engine that dynamically modulates its exploration-exploitation policy based on real-time task uncertainty. Define an information-theoretic **Progress Reward** that quantifies step-level contribution through conditional information gain, replacing sparse outcome-based rewards. Formulate a **Dirichlet Trust Policy** where the concentration parameters are adjusted by a running **Trust Score $C_t$** derived from value prediction error and environmental feedback. Prove mathematically how this adaptive prior scaling mechanism prevents the policy from collapsing into rigid pre-trained templates under high-uncertainty scenarios while preserving exploitation stability in familiar states."

---

📊 *Would you like me to construct a Python script to simulate the mathematical behavior of the Dirichlet prior under varying trust calibration scores, or should we model the performance delta of de-lexicalized SGA retrieval vs. raw trajectory memory on an out-of-distribution benchmark?*