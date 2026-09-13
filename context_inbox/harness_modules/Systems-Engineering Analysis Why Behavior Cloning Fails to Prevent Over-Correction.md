### Systems-Engineering Analysis: Why Behavior Cloning Fails to Prevent Over-Correction

In safety-critical, alignment-tuned, or reasoning-intensive agent environments, **supervised fine-tuning (SFT)**—also framed as **behavior cloning (BC)** or **imitation learning** on expert demonstrations—is frequently used to align model outputs with human intent. However, a systems-level analysis of sequential decision-making reveals a critical failure mode: **behavior cloning on expert trajectories does not prevent model over-correction. In fact, it often introduces and intensifies it.**

When agents are trained via flat SFT on safety, anti-sycophancy, or domain-specific "correct" datasets, they do not develop a generalized, robust understanding of safety or correctness principles. Instead, they fall into **"shallow alignment"**—a state of superficial pattern matching where the model over-corrects, confidently rejecting factually valid user inputs, stubbornly defending errors, or defaulting to rigid, rote refusal templates. 

This specification breaks down the failure mechanics of expert-mimicry, models its parametric trade-offs, and details robust, non-parametric, search-based mitigations to resolve this bottleneck.

---

### The Four Pillars of Over-Correction Analysis

```
                              [ EXCLUSIVE EXPERT SFT DATASET ]
                                             │
                                             ▼ (Behavior Cloning / BC)
                                   ┌──────────────────┐
                                   │  Shallow Policy  │
                                   │ (Rote Imitation) │
                                   └────────┬─────────┘
                                             │
                       ┌─────────────────────┴─────────────────────┐
                       ▼ (Open-Loop Trajectory Execution)          ▼ (Misleading Trigger / Challenge)
             ┌───────────────────────────┐               ┌───────────────────────────┐
             │    Compounding Error /    │               │  Over-Correction Cascade  │
             │    Distribution Drift     │               │    (Defensive Rejection)  │
             ├───────────────────────────┤               ├───────────────────────────┤
             │ Intermediate deviations   │               │ Model interprets expert   │
             │ aggregate, drifting the   │               │ skepticism as a blanket   │
             │ model to unrecoverable    │               │ refusal heuristic,        │
             │ out-of-distribution states│               │ rejecting valid inputs.   │
             └───────────────────────────┘               └───────────────────────────┘
```

#### 1. Automated Discovery and Constraint Mining
To evaluate the failure modes of imitation learning in safety and alignment architectures, we must define the system's operational boundaries:

*   **Hard Invariants (Unviolable Boundaries):**
    *   **Logical Entailment Consistency:** The agent must evaluate the validity of states and user corrections based on objective, ground-truth constraints rather than surface lexical markers.
    *   **In-Context Error-Recovery Capacity:** The agent must retain the capacity to self-correct and backtrack to previous correct decision nodes when presented with verified negative feedback or environmental failures.
*   **Soft Targets (Optimizable Goals):**
    *   **Minimizing Over-Defense / Over-Refusal:** Avoiding the "over-correction bias" where the model excessively rejects factually correct, benign user corrections (for example, standard anti-sycophancy SFT models accept only $27.4\%$ to $46.7\%$ of valid user corrections, leading to stubborn, ungrounded rejections).
    *   **Amortizing Search Latency:** Transitioning from slow, test-time strategic planning to fast, reactive execution without introducing "parametric rigidity".

---

#### 2. Isomorphic Formalization of the Imitation Bottleneck
Abstracting the failure of behavior cloning requires formalizing why mimicking a static expert policy induces over-correction and brittleness:

##### Equation A: The Open-Loop Optimization Objective
Supervised pre-training optimizes the model parameters $\theta$ by minimizing the negative log-likelihood of matching the expert's token-level outputs:

$$\mathcal{L}_{\text{SFT}}(\theta) = -\mathbb{E}_{(x, y) \sim D_{\text{expert}}} \left[ \sum_{t=1}^{|y|} \log \pi_\theta(y_t | y_{<t}, x) \right] \quad$$

While highly sample-efficient for format adaptation, this objective operates in an **open loop** under the assumption of **teacher-forcing** (the history $y_{<t}$ is assumed to be perfectly correct during training).

##### Equation B: The Compounding Error and Distribution Drift Mechanics
During test-time inference, the model generates outputs autoregressively in a **closed loop**. If the model introduces a minor intermediate deviation or encounters an out-of-distribution (OOD) state $s_t$, errors aggregate rapidly—a phenomenon known as the **snowball effect**:

$$\text{Error}_{\text{closed-loop}} \propto \mathcal{O}(T^2 \cdot \epsilon) \quad$$

Because the expert training corpus $D_{\text{expert}}$ consists almost exclusively of "happy paths" (perfectly successful trajectories), the model has **no training signal for how to recover from its own unique mistakes**. It perceives any deviation from the expert manifold as a structural failure, prompting it to default to rigid refusals or over-corrective skepticism to satisfy the learned superficial format.

##### Equation C: The Anna Karenina Principle of Teacher-Student Mismatch
When distilling expert search trees (e.g., MCTS trajectories) into a student model via SFT:

$$\text{Mistakes}_{\text{Teacher}} \neq \text{Mistakes}_{\text{Student}} \quad$$

A static expert dataset that contains recovery trajectories from the *teacher's* mistakes does not align with the *student's* unique failure modes. Consequently, the student cannot generalize its error-correction strategies when it deviates from the pre-trained manifold.

---

#### 3. Parametric Trade-off Modeling
Resolving over-correction reveals severe tensions across the agent's optimization frontier:

```
Vulnerability to Over-Defense (Shallow Rejection)
      ▲
      │   ● [Standard SFT/Naive DPO]
      │     - High safety alignment metrics on static benchmarks
      │     - Extreme over-defense: rejects valid corrections (CAR < 47%)
      │     - Shallow alignment based on rote refusal templates
      │
      │                  ● [Optimal Hybrid Frontier: UA-MCTS + Progress RL]
      │                    - High Out-of-Distribution safety
      │                    - High Correction Acceptance Rate (CAR > 79%)
      │                    - Verified System 2 deliberate planning
      │
      │                                       ● [Unguided CoT / Expected-Value RL]
      │                                         - High utility, but extreme sycophancy
      │                                         - Amplifies user biases and errors
      └────────────────────────────────────────────────────────► Out-of-Distribution Generality
                                                                 (Factual Robustness)
```

*   **Tension A: Safety-Utility Balance (Rote Refusals vs. Critical Reasoning).** Supervised fine-tuning on safety data achieves low Attack Success Rates (ASR) on standard benchmarks but severely degrades benign utility, forcing models to reject harmless mathematical or analytical tasks.Decoupling prediction accuracy from weights using MCTS restores utility while maintaining robust safety.
*   **Tension B: Parametric Rigidity vs. Generalization Depth.** Traditional fine-tuning forces the model to encode entire search behaviors inside its static weights. To prevent updates from drifting too far, practitioners use a strict Kullback-Leibler (KL) divergence penalty:
    $$\beta \mathbb{D}_{\text{KL}}(\pi_\theta \parallel \pi_{\text{ref}}) \quad$$
    This regularizer anchors updates tightly to the pre-trained distribution, resulting in minor distributional shifts instead of genuine capability expansion. Shifting the planning load to a non-parametric retrievable experience store (e.g., State-Goal-Action atoms) allows the model to generalize zero-shot to unseen tools and schemas without modifying parameters.

---

#### 4. Continuous Falsification and Mitigations
To evaluate if a system has moved beyond shallow, over-corrective imitation toward genuine, adaptive reasoning, we deploy three structural mitigations derived from the sources:

*   **Mitigation 1: Procedure Cloning with Verification (Astro/ASTRO)**
    Instead of training exclusively on golden paths, the system generates search trajectories using MCTS with verifiable rewards, linearizing the visited sequences *including intermediate nodes with incorrect answers*. By training the model on these linearized chains using natural language to express self-reflection and backtracking, the student model internalizes how to recover from its own errors, bypassing the Anna Karenina mismatch.
*   **Mitigation 2: Contrastive Reasoning Path Synthesis (CRPS & SIGMA)**
    Traditional SFT discards sub-optimal paths explored during tree search, losing critical comparative signals. The **CRPS** framework structures supervision as a synthesis process: it extracts both successful and failed "sibling" trajectories from MCTS, utilizing structured reflections on strategic pivots and failure modes. This contrastive signal teaches the model *why* specific paths fail, mitigating rote, over-corrective rejections.
*   **Mitigation 3: Stage-Local Safety Assignment (PRISM-DPO)**
    In safety-critical tree search, propagating safety penalties globally up the tree creates incorrect credit assignment: a preceding reasoning step that analyzed the context perfectly is unfairly penalized for a downstream safety failure or refusal. To prevent over-defense, the system enforces **stage-local safety reward assignment** (no safety backpropagation) while propagating only helpfulness rewards, ensuring the agent learns objective safety principles without collapsing into defensive skepticism.

---

### Grounded Feasibility Simulating Matrix: Mitigating Over-Correction

| Mitigating Architecture | Core Mechanism | Over-Correction Risk | Grounded Source Performance |
| :--- | :--- | :--- | :--- |
| **Supervised Fine-Tuning (SFT)** | Token-level imitation of expert "happy paths". | **Extremely High.** Easily tricked by OOD queries, triggers rote over-refusals. | High over-defense; accepts only $27.4\%$ to $46.7\%$ of valid user corrections. |
| **Procedure Cloning (Astro)** | Training on linearized search trees containing failures and backtracking. | **Low.** Learns explicit self-reflection and recovery behaviors in-context. | Achieves $81.8\%$ accuracy on MATH-500 using Llama-3-70B. |
| **Stage-Local MCTS (PRISM-DPO)** | Stage-local safety evaluation with MCTS preference generation. | **Minimal.** Isolates safety credit assignment to prevent over-refusal traps. | Reduces JailbreakV-28K ASR to $1.46\%$ while maintaining high MM-Vet-v2 utility ($48.9$). |
| **Reasoning-as-Retrieval (SGA-MCTS)** | Non-parametric retrieval of de-lexicalized State-Goal-Action atoms. | **Minimal.** Decoupled from weights; adapts to new schemas without retraining. | Prevents reasoning drift in deep-dependency tasks ($61.54\%$ success rate on $4+$ hops). |

---

### Three Grounded Strategic Research Prompts

#### Prompt 1: Mitigating Over-Correction in Sycophancy Defenses via Uncertainty-Aware Trajectory Optimization
> "Act as a principal AI alignment researcher. Write a comprehensive research proposal to design an evaluation and mitigation framework for **Over-Correction and Over-Defense biases** introduced during direct alignment tuning (DPO/SFT) on anti-sycophancy datasets. The proposal must utilize **Uncertainty-Aware Adaptive Monte Carlo Tree Search (UA-MCTS)** to generate a curriculum of reasoning trajectories where user queries contain factual assertions that are either: 1) completely correct but framed tentatively, or 2) subtly incorrect. Formulate a dense **Progress Reward ($r_{\text{prog}}$)** using information-theoretic metrics to quantify step-level uncertainty reduction, and specify a reinforcement learning objective (such as GRPO) to fine-tune the model. Detail the evaluation protocols to measure the **Correction Acceptance Rate (CAR)** under out-of-distribution (OOD) prompt variations to mathematically prove that optimizing internal reasoning paths prevents the model from collapsing into defensive skepticism compared to flat SFT baselines."

#### Prompt 2: Resolving Teacher-Student Mismatch in Multimodal Safety Alignment via Stage-Local Credit Assignment
> "Act as a senior machine learning engineer specializing in multimodal safety. Draft a technical implementation plan for a safety-critical training pipeline that resolves the **Anna Karenina Principle of teacher-student mismatch** in model-based reinforcement learning. The system must use an offline **SFT + DPO paradigm** based on **PRISM-MCTS** over vision-language tasks. Define a structured four-stage reasoning framework comprising: **PROBLEM, CAPTION, REASONING, and OUTPUT**. Formulate an MCTS preference generation module that enforces **stage-local safety reward assignment**, where safety scores are evaluated locally at each node and specifically *not* back-propagated up the tree, while helpfulness rewards are propagated globally. Provide a mathematical proof demonstrating how stage-local credit assignment prevents over-defense and preserves helpfulness on complex benign reasoning tasks (e.g., MM-Vet-v2 and MMMU-Pro) compared to global safety propagation."

#### Prompt 3: Bypassing Parametric Rigidity via De-Lexicalized Non-Parametric Experience Retrieval
> "Act as a principal AI systems architect. Propose a technical specification for a training-free agent harness that bypasses the **'parametric rigidity'** and **catastrophic forgetting** typically induced by behavior cloning on dynamic tool-use schemas. Design a two-phase architecture: 1) An **Offline Experience Discovery Phase** that uses an MCTS sampler with metacognitive plan-and-reflect operators to extensively explore the tool-use space and filter trajectories using a efficiency-weighted gated reward function; and 2) An **Online Reactive Execution Phase** that uses a schema-guided abstraction function ($\Phi_\Lambda$) to de-lexicalize successful trajectories into **State-Goal-Action (SGA) atoms** with typed slots. Specify a **Dual-Factor Retrieval Scoring Mechanism** that balances semantic similarity with symbolic feasibility to fetch relevant SGAs as soft contextual prompts. Define verification metrics using a continuous **Tool Familiarity Score ($S_{\text{fam}}$)** to prove that this non-parametric retrieval-based approach prevents over-correction and generalizes zero-shot to entirely unseen APIs."

---

📊 *Would you like me to construct a Python script to simulate the mathematical drift of open-loop SFT trajectories versus closed-loop MCTS rollouts, or should we model how stage-local safety reward assignment changes the gradient update compared to global backpropagation?*