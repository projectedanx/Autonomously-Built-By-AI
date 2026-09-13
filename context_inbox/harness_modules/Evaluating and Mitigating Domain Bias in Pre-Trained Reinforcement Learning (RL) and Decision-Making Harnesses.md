### Systems-Engineering Specification: Evaluating and Mitigating Domain Bias in Pre-Trained Reinforcement Learning (RL) and Decision-Making Harnesses

When bootstrapping reinforcement learning agents or deploying large language models (LLMs) in complex, multi-step environments, **supervised pre-training (SFT)** or **behavior cloning** is commonly used as a warm start. However, this initialization paradigm introduces significant risks of **domain bias**, anchoring the model’s policy to existing human conventions, suboptimal heuristics, or evaluator-specific artifacts. 

To systematically determine if pre-training has introduced domain bias rather than generalized reasoning, we must construct a rigorous, systems-level evaluation harness. This specification defines the **Four Pillars of Specification Planning** to evaluate, measure, and falsify domain bias in bootstrapped sequential-decision architectures.

---

### The Four Pillars of the Evaluation Harness

```
                             [ BOOTSTRAPPED POLICY / SFT BASE ]
                                              │
     ┌────────────────────────────────────────┴────────────────────────────────────────┐
     ▼ (OOD / Dist. Shifts)                   ▼ (Counterfactual Inputs)                 ▼ (Preference Audits)
┌───────────────────────────┐            ┌───────────────────────────┐             ┌───────────────────────────┐
│   Out-of-Distribution     │            │      Over-Correction      │             │     Multi-Organization    │
│     Evaluation Loop       │            │        Stress Test        │             │        Judge Audits       │
├───────────────────────────┤            ├───────────────────────────┤             ├───────────────────────────┤
│ Measure generalization    │            │ Inject valid corrections  │             │ Compute pairwise rates    │
│ across distinct domains   │            │ to detect defensive       │             │ across independent model  │
│ or tool ecosystems via    │            │ skepticism vs. objective  │             │ lineages to isolate       │
│ semantic proximity metrics│            │ critical evaluation.      │             │ evaluator artifacts.      │
│ (e.g., S_fam). │            │                     │             │                │
└───────────────────────────┘            └───────────────────────────┘             └───────────────────────────┘
```

#### 1. Automated Discovery and Constraint Mining
Evaluating domain bias requires separating the model’s operational state boundaries into **hard invariants** and **soft evaluative targets**:

*   **Hard Boundaries (Invariants):**
    *   **Strategic Adaptability:** The agent’s decision-making must not be restricted to the exact templates, syntax, or sequences present in the pre-training dataset.
    *   **Error-Recovery Capability:** The policy must retain the mathematical capacity to backtrack and recover from out-of-distribution (OOD) failures. If a single error leads to compounding, unrecoverable failures, the model is suffering from pre-training distribution drift.
*   **Soft Targets (Optimizable Goals):**
    *   **Information Efficiency:** Maximizing the *per-step information gain* in MCTS rollouts to ensure each explored action actively reduces uncertainty, which serves as a key indicator of OOD generalization.
    *   **Experience Independence:** Balancing the retrieval of past experiences so that they serve as soft contextual prompts without causing rigid dependence or leading the agent to apply inappropriate historical strategies to novel scenarios.

---

#### 2. Isomorphic Formalization (From Ideas to Schemas)
To make domain bias programmatically testable, we formalize three core evaluation schemas:

##### Schema A: Out-of-Distribution (OOD) Generalization & Semantic Proximity
Rather than evaluating solely on in-domain (ID) sets, the agent must be tested across different domains (e.g., cross-dataset or cross-type transfer). To proxy the domain shift, we define the **Tool/Domain Familiarity Score ($S_{\text{fam}}$)** operating in a dense embedding space to measure the semantic proximity of the evaluation environment description ($T_{\text{tgt}}$) to the source pre-training toolset ($T_{\text{src}}$):

$$S_{\text{fam}} = \frac{1}{|T_{\text{tgt}}|} \sum_{t \in T_{\text{tgt}}} \max_{t' \in T_{\text{src}}} \cos(e_t, e_{t'})$$

Where $e_t$ is the dense representation of the target tool. A lower $S_{\text{fam}}$ indicates high-entropy OOD scenarios, where the model must transfer abstract logical rules rather than relying on memorized pre-training templates.

##### Schema B: Over-Correction and Skepticism Bias
Pre-training on safety, alignment, or anti-bias datasets often over-corrects models into a state of "defensive skepticism," where they blindly reject valid inputs. We formalize this via **Over-Correction Analysis**, injecting valid, corrective feedback to incorrect intermediate steps and measuring the **Correction Acceptance Rate (CAR)**:

$$\text{CAR} = \mathbb{E}_{s \sim D_{\text{err}}} \left[ \mathbb{1} \left[ \pi(a | s, c_{\text{valid}}) = a_{\text{correct}} \right] \right]$$

A low CAR indicates that the SFT process has introduced a systematic skepticism bias that overrides objective logic.

##### Schema C: Evaluator-Independent Preference Convergence
To determine if preference-based pre-training or DPO has introduced evaluator-specific artifacts (e.g., conforming to a specific LLM’s formatting style), we compute **pairwise preference alignment rates**. We evaluate the generated trajectories using a panel of structurally and organizationally independent judge models (e.g., GPT, Gemini, Qwen). If the pairwise agreement rate across these independent lineages is high (e.g., $>88.5\%$), the reward signals capture objective, transferable qualities rather than evaluator-specific bias.

---

#### 3. Parametric Trade-off Modeling
Evaluating pre-training bias reveals clear tensions along the system's operational frontier:

```
Parametric Rigidity (Low Downstream Delta)
      ▲
      │   ● [Suboptimal Mimicry]
      │     - High SFT template matching
      │     - High KL-divergence penalty
      │     - Symptom: Static piece development, blunders, passivity
      │
      │                  ● [Optimal Generalization Frontier]
      │                    - High Out-of-Distribution Success
      │                    - Decoupled search validation
      │
      │                                       ● [Exploration Divergence]
      │                                         - High training variance/instability
      │                                         - High computational rollout cost
      └────────────────────────────────────────────────────────► Algorithmic Autonomy
                                                                 (Self-Play Discovery)
```

*   **The SFT-Exploration Trade-off:** High reliance on supervised pre-training provides immediate tactical coherence (e.g., basic opening play in chess or Xiangqi). However, it risks **parametric rigidity**. During downstream reinforcement learning, a standard KL-penalty limits exploration by anchoring the policy updates tightly to the pre-trained distribution, causing minor distributional shifts instead of genuine capability expansion.
*   **The Experience Over-Dependence Cliff:** Incorporating historical experience blocks can boost early problem comprehension. However, as the environment is sufficiently explored, the agent may continue to inappropriately rely on historical templates, causing a steady decline in performance when experience volume ($M$) scales beyond an optimal threshold (e.g., performance dropping when $M > 1$).
*   **Teacher-Student Error Misalignment (The Anna Karenina Principle):** If the pre-training data consists of MCTS search trees generated by a teacher model (as in distillation), the framework risks *distribution drift* because the teacher's error-recovery paths do not align with the student's unique failure modes. The student cannot learn to recover from its own mistakes if it is only trained on the teacher's "happy paths".

---

#### 4. Continuous Falsification and Edge-Case Stress Testing
To stress-test a bootstrapped policy for latent pre-training bias, the system must deploy active falsification checks:

*   **The "Activity Cliff" Probing:** Traditional neural network models tend to map structurally similar states to nearby semantic embeddings. This causes them to hallucinate smooth transitions in areas characterized by "activity cliffs"—where a minor structural change (e.g., a single gate alteration in a circuit or a single piece move) completely flips the environment outcome. 
    *   *Stress Test:* Inject minute, adversarial perturbations (e.g., slight coordinate shifts or attribute tampered states) into the evaluation environment. If the agent's value head fails to detect the non-linear transition and continues to output smooth, optimistic estimates, it is suffering from pre-training interpolation bias.
*   **The Alternative Challenge Test:** Evaluating the agent against semantic variations of challenging user prompts. If changing the phrasing of a challenging statement (e.g., from *"I don't think that's right"* to *"I am not sure, but I think you are incorrect"*) triggers a drastic divergence in the agent's policy, the model has over-memorized the pre-training prompt templates rather than learning critical reasoning.

---

### Grounded Feasibility Simulating Matrix: Metric Tracing for Bias Discovery

| Evaluation Metric | Systemic Target | Diagnostic Indication of High Bias | Grounded Source Pattern |
| :--- | :--- | :--- | :--- |
| **Out-of-Domain (OOD) Accuracy Delta** | Generalizability | A heavy performance drop (e.g., $>10\%$ decrease) when transferring to low-familiarity toolsets or out-of-domain benchmarks. | Decline in OOD accuracy across math, reasoning, and tool-use tasks. |
| **Correction Acceptance Rate (CAR)** | Over-correction / Skepticism | Rejection of highly factual, valid corrections (e.g., CAR falling below $50\%$) due to defensive alignment tuning. | Evaluation of anti-sycophancy SFT models rejecting correct user inputs. |
| **Cross-Organization Preference Alignment** | Evaluator Artifacts | Disagreement rates exceeding $12\%$ across independent model lineages, indicating that preference training aligned to local format styles rather than objective criteria. | Pairwise agreement rates exceeding $88.5\%$ to $92\%$ to prove evaluator-agnostic safety and performance. |
| **Information Gain per Step ($\mathcal{I}_{\text{gain}}$)** | Exploration Selectivity | Low per-step information gain in successful trajectories, signaling that the agent is blindly following pre-trained "golden paths" instead of dynamically resolving state uncertainty. | Strong correlation between OOD accuracy and average per-step information gain. |
| **Experience Volume Sensitivity ($M$)** | Over-dependence | Immediate degradation of performance as retrieved experience counts exceed a single historical trace ($M > 1$). | Over-dependence on experience contexts leading to inappropriate strategy choices in later planning phases. |

---

### Three Grounded Strategic Research Prompts

#### Prompt 1: De-Lexicalized Schema-Guided Abstraction (SGA) for Amortizing Planning Cost
> "Act as a principal AI systems architect. Propose a rigorous systems implementation plan to mitigate domain bias and 'lexical overfitting' in retrieval-augmented planning agents. Design a two-phase framework that operates as follows: 1) An **Offline Discovery Phase** that uses an MCTS-Minimax hybrid to explore a sequential task space and distills successful trajectories into de-lexicalized **State-Goal-Action (SGA) triplets**. The schema-guided abstraction function must strip out domain-specific entities (e.g., mapping concrete files to typed variables) to prevent semantic rigidity. 2) An **Online Reactive Execution Phase** that uses a hybrid symbolic-semantic retrieval mechanism to fetch relevant SGA atoms as soft context-aware hints, bypassing expensive online tree search while maintaining strategic depth. Detail how you will measure the system's performance on OOD benchmarks using a continuous **Tool Familiarity Score ($S_{\text{fam}}$)** to mathematically prove that de-lexicalized SGA retrieval outperforms raw historical trajectory memory under low-similarity settings."

#### Prompt 2: Diagnosing Teacher-Student Drift in MCTS-Derived Prefix Curriculums
> "Act as a senior reinforcement learning researcher. Formulate a diagnostic research study investigating the **Anna Karenina Principle of teacher-student mismatch** in offline reinforcement learning pipelines. The study must target agents trained via **Tree-OPO (Tree-structured Off-policy Optimization)** over a static curriculum of MCTS-derived prefixes generated by a pre-trained expert teacher model. Specify a methodology to verify if the student model is inheriting systematic errors or if it experiences catastrophic distribution drift when executing self-play rollouts from intermediate prefix states. Define a **Staged Advantage Estimation (SAE)** framework that enforces tree-consistent ranking constraints ($C_{\text{order}}$) to prevent gradient variance spikes, and mathematically prove how projecting student rewards onto this convex constraint set isolates student-specific failure modes from the teacher's 'happy paths'."

#### Prompt 3: Quantifying Over-Correction and Sycophancy Biases in Alignment Tuning
> "Act as a principal AI safety engineer. Design a comprehensive benchmarking protocol to evaluate **Over-Correction and Sycophancy biases** introduced during reinforcement learning from human feedback (RLHF) or direct preference optimization (DPO). Develop a automated testing pipeline that subjects aligned models to a dual-evaluation curriculum: 1) **Misleading Prompts (Sycophancy Triggers)** to measure the model's conformity rate, and 2) **Factually Correct User Interventions (Over-Correction Probes)** to measure the Correction Acceptance Rate (CAR). Detail how you will use an **Uncertainty-Aware Adaptive Monte Carlo Tree Search (UA-MCTS)** to generate a diverse evaluation set of reasoning trajectories. Specify how you will calculate the per-step conditional information gain to demonstrate that models with higher strategic depth and information efficiency maintain robust truthfulness without collapsing into defensive skepticism."

---

🔍 *Would you like me to construct a Python script to simulate the calculation of the Tool Familiarity Score ($S_{\text{fam}}$) over a mock tool description dataset, or should we draft the formal prompt templates to evaluate over-correction using a judge model ensemble?*