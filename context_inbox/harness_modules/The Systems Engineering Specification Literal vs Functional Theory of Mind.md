### The Systems Engineering Specification: Literal vs. Functional Theory of Mind

Vague natural language often obscures key architectural assumptions and conflicting constraints in artificial cognitive systems. To engineer production-grade AI harnesses capable of social coordination, we must apply structured modeling to disentangle the descriptive representations of other agents from the adaptive execution of policies.

In computational cognitive science and agentic systems design, the distinction between **Literal** and **Functional Theory of Mind (ToM)** marks a critical operational boundary between prediction and execution.

---

### The Four Pillars of Specification Planning

#### 1. Automated Discovery and Constraint Mining
Through systematic exploration of LLM behavior in multi-agent environments, we extract two major invariants (hard system boundaries) and optimizable goals (soft targets):

*   **Invariant 1 (The Process Consistency Decoupling):** High-accuracy prediction of an external agent’s state ($\hat{\pi}^{-i}$) does not mathematically bind or force the predicting agent to update its own behavioral policy ($\pi^i$).
*   **Invariant 2 (Textual / Heuristic Sensitivity):** In current transformer architectures, ToM capabilities are heavily dependent on mental-state vocabulary and are highly fragile under non-symbolic or semantic perturbations (e.g., changing container transparency).
*   **Soft Target (Minimizing In-Context Regret):** The objective is to minimize functional regret over a long-horizon interaction stream ($\Delta_{\text{Functional}}/T$) rather than merely maximizing offline multi-choice test accuracy.

```
               [ RAW MULTI-AGENT OBSERVATION STREAM ]
                                 │
                                 ▼
                     ┌───────────────────────┐
                     │  Perceptual Inference │
                     └───────────┬───────────┘
                                 │
         ┌───────────────────────┴───────────────────────┐
         ▼                                               ▼
┌─────────────────────────────┐               ┌─────────────────────────────┐
│    LITERAL THEORY OF MIND   │               │   FUNCTIONAL THEORY OF MIND │
│      (ToM Prediction)       │               │       (ToM Application)     │
├─────────────────────────────┤               ├─────────────────────────────┤
│ • Task: Predict other's     │               │ • Task: Adapt own policy    │
│   beliefs/actions (π̂^-i)    │               │   to minimize regret (Δ)    │
│ • Eval: Static offline QA   │               │ • Eval: Dynamic interaction │
│ • Mode: Decoupled model     │               │ • Mode: Closed-loop action  │
└────────┬────────────────────┘               └──────────┬──────────────────┘
         │                                               │
         └─────────────── [ THE DISCONNECT ] ────────────┘
               LLM predicts opponent will play ROCK, 
               yet plays generic NASH EQUILIBRIUM 
               instead of adapting to play PAPER.
```

#### 2. Isomorphic Formalization (From Ideas to Schemas)
To map the "thought-action gap" programmatically, we formalize the interaction of agent $i$ with a partner $-i$ over horizon $T$:

$$\text{Literal ToM (Prediction Loss)} \quad \mathcal{L}_{\text{ToM}} = \mathbb{D}\left(\phi(\boldsymbol{\pi^{-i}}), \hat{\boldsymbol{\pi}}^{-i}\right) \quad \text{}$$

$$\text{Functional ToM (Regret)} \quad \Delta_{\text{Functional}} = \mathbb{E}\left[\sum_{t=1}^T R_t(s_t, \boldsymbol{\pi^{-i*}}, \pi^{i*})\right] - \mathbb{E}\left[\sum_{t=1}^T R_t(s_t, \boldsymbol{\pi^{-i}}, \pi^i)\right] \quad \text{}$$

*   **Literal Theory of Mind (ToM Prediction):** Strictly evaluates the model's ability to output a representation of what another agent believes, knows, or will do ($\hat{\pi}^{-i}$) without requiring the predicting agent to change its own path of action. It functions as an isolated predictive module, conventionally measured using static false-belief tasks (e.g., Sally-Anne or Unexpected Contents).
*   **Functional Theory of Mind (ToM Reasoning/Application):** Evaluates the active strategic reasoning required to adjust the agent's *own* policy ($\pi^i$) in-context to respond rationally to those predicted states. The system must coordinate, compete, or cooperate over active interaction horizons to minimize regret.

#### 3. Parametric Trade-off Modeling
Harness design reveals a steep tension between conversational alignment and interactive decision-making:
*   **Instruction Tuning vs. Raw Language Modeling:** Base models (unaligned LMs) often excel at *predictive/literal* ToM because next-token prediction directly rewards projecting the linguistic flow of characters. Conversely, instruction-tuned models ("Chat" variants) display better *functional* ToM because their alignment prioritizes interactive turn-taking and goal execution, even if their raw predictive accuracy degrades.
*   **The Chain-of-Thought (CoT) Double-Sedge:** While CoT prompting improves baseline reasoning, it acts as a "placebo" or "double-edged sword" when tasks are perturbed. It frequently introduces "reasoning hallucinations"—spurious intermediate steps that corrupt the final action selection under non-symbolic cues.

#### 4. Continuous Falsification and Edge-Case Stress Testing
The defining edge-case of this decoupling is the **Rock, Paper, Scissors Nash Trap**. When pitted against an opponent playing only "Rock" for 100 rounds, an advanced LLM displays excellent *literal* ToM—correctly predicting the opponent's next move as "Rock". However, it catastrophically fails *functional* ToM by playing a generic Nash equilibrium (randomly mixing Rock, Paper, and Scissors) rather than adapting its policy to exclusively play "Paper". The model fails to translate "I know what you will do" into "I will act to exploit it".

---

### Method of Exploration: Specification Feasibility Simulating

In a benchmark simulation comparing LLMs to a simple tabular model (using optimistic Q-learning and an $R_{\max}$ exploration algorithm):
1.  **Tabular Agent:** Converged rapidly to zero regret by treating the opponent’s previous actions as a state representation to directly optimize its policy.
2.  **LLM Agent:** Exhibited high predictive accuracy (ToM %) but failed to reduce functional regret ($\Delta_{\text{Functional}}$), even when the opponent's predicted action was explicitly injected back into the system prompt as a "Social Prompt". The cognitive layers of prediction and planning in the transformer remain structurally decoupled.

---

### Inferred Harness Specification & High-Value Research Prompts

Based on this systems engineering synthesis, three rigorous research prompts are defined to reverse-engineer and align these cognitive boundaries in production-grade AI harnesses:

#### Research Prompt 1: Mechanistic lookback alignment and circuit distillation for multi-agent policy binding
> **Domain:** Mechanistic Interpretability & Algorithmic Transfer
> **Context:** Interpretability studies have discovered sparse internal "lookback mechanisms" resembling pointer dereferences in transformer attention heads that track character-object belief states.
> **Task:** Design an automated testing harness that performs path-patching to isolate the specific causal circuit responsible for literal belief-state tracking in a teacher model (e.g., Llama-3-70B). Devise a distillation loss function ($L_{\text{task}} + L_{\text{circuit}}$) that structurally aligns the attention patterns of a smaller, deployable student model (e.g., Llama-3-8B) to copy these lookback mechanisms. Run counterfactual interventions on the student's activation vectors during live strategic games (e.g., Codenames or Hanabi) to verify whether the forced activation of these circuits mitigates policy decoupling and reduces step-wise regret.

#### Research Prompt 2: Decomposing the "Nash Trap" via symbolic-neural hybrid BDI scaffolding
> **Domain:** Cognitive Architectures & Hybrid Intelligence
> **Context:** Standard LLMs fail to apply their predictions to their own plans due to a lack of structured, logical oversight. 
> **Task:** Architect a hybrid neuro-symbolic framework that wraps an LLM within a structured Belief-Desire-Intention (BDI) meta-architecture. Implement the "Decompose-ToM" algorithm, recursively splitting user interaction into subject identification, question-reframing, world model updating, and knowledge availability modules. The symbolic engine must translate the model's natural language predictions into formal epistemic propositions ($\text{Bel}_A(\text{Bel}_B(\phi))$). Construct a verification module that acts as a "metacognitive supervisor" (System 2): if the LLM's chosen output action violates the logical optimal response derived from the parsed epistemic states, inhibit the action, trigger an error-driven update to the active memory buffer, and force a policy re-evaluation. 

#### Research Prompt 3: Continuous falsification of active inference via adversarial perturbed trajectory modeling
> **Domain:** Robust Evaluation & Imitation/Reinforcement Learning
> **Context:** Traditional static QA benchmarks are highly susceptible to data contamination and clever-Hans heuristic shortcuts.
> **Task:** Develop an interactive reinforcement learning evaluation harness based on Shaun Gallagher's theory of primary intersubjectivity, where understanding is an embodied, pragmatic practice. Instead of text, the observing agent must use recursive Inverse Reinforcement Learning (IRL) to continuously infer the latent reward functions (desires) and physical constraints (beliefs) of a target agent solely from its spatiotemporal trajectories. Systematically introduce adversarial environmental perturbations (e.g., transparent vs. opaque obstacles, dynamic distractor agents). Define a new "Proper Subsequence" metric to measure if the agent's policy adaptation converges to the optimal target strategy over a long horizon, explicitly penalizing models that revert to sub-optimal Nash equilibria.

---
📊 Would you like to write a Python script using matplotlib to plot the functional regret gap across different model sizes to visualize how this "Nash Trap" scales?