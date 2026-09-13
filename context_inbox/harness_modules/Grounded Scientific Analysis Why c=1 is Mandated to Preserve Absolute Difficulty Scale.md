### Grounded Scientific Analysis: Why c=1 is Mandated to Preserve Absolute Difficulty Scale

In standard reinforcement learning algorithms (such as GRPO or PPO), it is conventional to normalize advantages across a batch or group by subtracting the mean and dividing by the standard deviation ($z$-scoring). This is equivalent to applying an affine transformation:
$$A'_k = \frac{A_k - b}{c}$$
where $b = \mathbb{E}[A]$ is the mean-centering baseline and $c = \sigma$ is the standard deviation. 

However, in **Tree-structured Off-policy Optimization (Tree-OPO)**—where the student policy is optimized using a curriculum of off-policy, teacher-vetted prefixes of varying lengths—this standardization protocol catastrophically collapses. Enforcing $c = 1$ (refusing scale normalization) is mathematically necessary to preserve the **absolute difficulty scale** of the prefix curriculum. 

---

#### 1. The Pathology of Heterogeneous Prefix Batches
In traditional on-policy RL, all completions in a group share a single, uniform prompt, meaning their true expected returns $V^\pi(p)$ are identical. Under those conditions, flat group-wise standardization is unbiased. 

In Tree-OPO, however, a single training batch contains completions sampled from **heterogeneous prefixes** $\{p_k\}$ originating from diverse depths of the search tree. These prefixes represent subproblems of fundamentally disparate difficulty levels and expected returns:
*   **Deep Prefixes (Easy)**: Located close to the terminal state, possessing a high base success probability $V(p) \to 1.0$.
*   **Shallow Prefixes (Hard)**: Located close to the root, representing highly uncertain, multi-step decision frontiers where $V(p) \to 0.1$ or $0.2$.

Applying a standardizing divisor ($c = \sigma_{group}$ or $c \neq 1$) rescales the advantages **inconsistently** across different prefixes. If a batch contains mostly easy prefixes with one hard prefix, dividing by the group variance artificially inflates or compresses the learning signal, destroying the relative physical meaning of the rewards.

---

#### 2. Absolute Scale as a Carrier of Semantic Information
In tree-structured reasoning, the absolute magnitude of the advantage carries vital semantic information about **prefix difficulty**. 
When we compute raw prefix-aware advantages using Staged Advantage Estimation (SAE):
$$a'_i = r_i - \alpha V(p_i)$$
the baseline $V(p_i)$ acts as a local centering force (where $V(p) = \mathbb{E}[r \mid p]$ is the conditional success probability). This local centering ensures that the advantage strictly measures the *local surprise* of the completion relative to its starting state. 

If we preserve $c=1$, the magnitude of the advantage $a'_i$ remains directly anchored to the **true difficulty boundary** of that prefix:
*   A correct completion ($r_i = 1$) from a highly difficult, low-probability prefix ($V(p) = 0.1$) yields a massive positive advantage: $a'_i = 1 - 0.1 = +0.9$. This signals an enormous policy breakthrough.
*   A correct completion ($r_i = 1$) from an easy, near-terminal prefix ($V(p) = 0.9$) yields a tiny positive advantage: $a'_i = 1 - 0.9 = +0.1$.

If standard deviation normalization ($c \neq 1$) is applied, these absolute magnitudes are crushed. The highly informative $+0.9$ breakthrough is squashed down to the same normalized scale as the $+0.1$ trivial completion. This **Prefix-Difficulty Saponification** blinds the policy gradient to the structural geometry of the tree, causing easy, deep prefixes to overshadow hard, shallow prefixes in credit assignment.

---

#### 3. Mathematical Redundancy and Learning Rate Absorption
Formally, the policy gradient estimator $\hat{g}$ under an affine transformation scales linearly with $1/c$:
$$\hat{g} = \frac{1}{K} \sum_{k=1}^K \left(\frac{A_k - b}{c}\right) \nabla_\theta \log \pi_\theta(a_k \mid s_k)$$
The variance of this estimator scales as $1/c^2$. 

Because $c$ is a constant scalar across the batch, its presence in the denominator does not alter the direction of the gradient step—it only scales its magnitude. This global scale adjustment is **completely redundant** because it can be entirely absorbed by adjusting the learning rate ($\eta$) of the optimizer. 

Thus, simple mean-centering (setting $b = \mathbb{E}[A]$ and $c = 1$) provides the **variance-optimal shift** while avoiding the semantic distortion and training instability introduced by scaling standardizations.

---

### Systems Engineering Synthesis: The Four Pillars of Specification Planning for Tree-OPO Advantage Preservation

To construct a production-grade AI training harness that leverages off-policy tree structures without suffering from scale distortion, we establish a formal systems engineering specification:

```
               [HETEROGENEOUS OFFLINE PREFIXES (p_k)]
                                 │
                                 ▼
         ┌────────────────────────────────────────────────┐
         │ 1. AUTOMATED DISCOVERY & CONSTRAINT MINING     │
         │    • Enforces c = 1 invariant                  │
         │    • Maps learning rate absorption limits      │
         └────────────────────────────────────────────────┘
                                 │
                                 ▼
         ┌────────────────────────────────────────────────┐
         │ 2. ISOMORPHIC FORMALIZATION                    │
         │    • Projects raw rewards onto C_order         │
         │    • Binds advantages to local surprise values │
         └────────────────────────────────────────────────┘
                                 │
                                 ▼
         ┌────────────────────────────────────────────────┐
         │ 3. PARAMETRIC TRADE-OFF MODELING               │
         │    • Quantifies Local Variance vs.             │
         │      Global Scale Preservation (c = 1)         │
         └────────────────────────────────────────────────┘
                                 │
                                 ▼
         ┌────────────────────────────────────────────────┐
         │ 4. CONTINUOUS FALSIFICATION                    │
         │    • Stress-tests baseline variance drift      │
         │    • Prunes non-convex scale collapses         │
         └────────────────────────────────────────────────┘
                                 │
                                 ▼
                  [OPTIMIZED POLICY GRADIENT (g)]
```

#### 1. Automated Discovery and Constraint Mining
*   **Hard Boundaries (Invariants)**: The advantage divisor must satisfy the invariant $c = 1$. Group-wide division by standard deviation ($\sigma$) is strictly prohibited during multi-prefix optimization batches to prevent the loss of absolute difficulty characteristics.
*   **Soft Targets (Optimizable Goals)**: The advantage baseline weight $\alpha \in$ scales the baseline subtraction. Empirically, the optimal balance between gradient variance reduction and reward alignment is achieved at **$\alpha = 0.5$**.

#### 2. Isomorphic Formalization (From Ideas to Schemas)
*   The raw advantages are structured as a Directed Acyclic Graph (DAG) corresponding to the hierarchical prefix tree. We formalize the **Staged Advantage Estimation (SAE)** as a convex projection of centered rewards $r_0$ onto a closed, convex set $F_0$ that respects tree-consistency constraints ($C_{order}$):
    $$\min_{a \in \mathbb{R}^N} \|a - r_0\|^2 \quad \text{s.t.} \quad \mathbf{1}^\top a = 0, \quad \|a\|_2 \le N, \quad a_i + \delta_{ij} \le a_j \quad \forall (i, j) \in C_{order}$$
    This projection mathematically guarantees that the variance of the adjusted advantages is strictly bounded by the variance of the raw centered rewards ($Var[a^*] \le Var[r_0]$) while enforcing perfect prefix-consistent ranking.

#### 3. Parametric Trade-off Modeling
*   **The Feasibility Frontier**: Pushing for ultra-high local variance reduction via aggressive subtree pooling (e.g., using subtree success rates $V_E(p)$ as the baseline) introduces a non-zero estimation bias. 
*   Conversely, using the unbiased global mean $V_{GRPO}$ keeps bias at zero but causes extreme gradient variance when prefixes are heterogeneous. 
*   By modeling this relationship parametrically, the harness utilizes the **Empirical Expectation ($V_E$) baseline** combined with **$c = 1$** to achieve the optimal trade-off—minimizing overall Mean Squared Error ($MSE = \text{Bias}^2 + \text{Variance}$) while preserving absolute scale.

#### 4. Continuous Falsification and Edge-Case Stress Testing
*   **The Stressor**: We pass a pathological training batch containing a 50/50 mix of extremely easy prefixes ($V(p) = 0.99$) and extremely hard prefixes ($V(p) = 0.01$). 
*   **The Failure Criterion**: If the relative advantage difference between a successful completion at a hard prefix and an easy prefix drops below the theoretical margin ($\delta_{ij} = 0.01$), the standard-deviation normalizer is flagged as active, and the iteration is aborted. 
*   The system must prove that the expectation-based baseline combined with $c=1$ maintains a **Constraint Satisfaction rate of $\ge 95\%$** on $C_{order}$ throughout non-stationary training steps.

---

### Three Rigorous, Non-Obvious Research Prompts

These prompts are designed to reverse-engineer and stress-test the boundary limits of search-augmented reinforcement learning and advantage estimation.

#### Research Prompt 1: Parametric Scale-Invariant Alignment of Multi-Prefix Advantages under Non-Stationary Task Distributions
> **System Objective**: Build and evaluate an adaptive, prefix-conditioned advantage optimization harness in Python that preserves absolute difficulty scales without relying on standard-deviation normalization ($c = 1$), dynamically adjusting the baseline weight $\alpha$ to match the local Shannon entropy of the student policy's completions.
>
> **Task Instructions**:
> 1. **Mathematical Formalization**: Define a dual-scale baseline modifier where the baseline weight $\alpha(t)$ is mapped dynamically to the rolling completion entropy $H(\pi_\theta \mid p_i)$:
>    $$\alpha(t) = \alpha_0 \cdot \left(1 - \tanh\left(\lambda \cdot H(\pi_\theta \mid p_i)\right)\right)$$
>    Enforce the hard constraint that $c = 1$ is maintained globally across all prefixes to protect tree-relative magnitudes.
> 2. **Isomorphic Mapping**: Prove that adjusting $c$ dynamically based on the trace-level variance of subtree success rates preserves the estimation-to-class error reduction of the Staged Advantage Estimation (SAE) projection:
>    $$\| \hat{V}_{SAE} - V^*_C \|_2 \le \| \hat{V}_{GRPO} - V^*_C \|_2$$
> 3. **Verification Script**: Implement a Python subclass of the standard GRPO estimator that ingests MCTS prefix metadata, computes $\alpha(t)$ per prefix, and enforces a hard $c = 1$ scaling rule to protect tree-difficulty signals.
> 4. **Falsification Protocol**: Stress-test the estimator by feeding it a synthetic batch of mixed-depth prefixes (depths $4$ to $32$). The estimator must maintain a constraint satisfaction rate $\ge 95\%$ on $C_{order}$.

#### Research Prompt 2: Convexified Quadratic Program Projection for Staged Advantage Estimation with Strict Parent-Child Ordering Boundaries
> **System Objective**: Implement and evaluate a formal non-convex quadratic programming solver within the training loop to compute prefix-aware advantages by projecting empirical rewards onto a hierarchical constraint set.
>
> **Task Instructions**:
> 1. **The Optimization Program**: Formulate the soft-constraint SAE program:
>    $$\min_{a \in \mathbb{R}^N} \|a - r_0\|^2 \quad \text{s.t.} \quad \mathbf{1}^\top a = 0, \quad \|a\|_2 \le N, \quad a_i + \delta_{ij} \le a_j \quad \forall (i, j) \in C_{order}$$
> 2. **Constraint Enforcement**: Write a Python module using `scipy.optimize` (SLSQP algorithm) that takes a batch of empirical rewards and a parent-child adjacency matrix representing prefix containment ($C_{pair}$) and sibling-triplet relations ($C_{triplet}$).
> 3. **Systemic Falsification**: Test the solver's convergence speed under a simulated $1.0\text{s}$ timeout. Measure the gradient variance of the policy update step using the resulting advantage vector $a^*$ and prove it is strictly lower than that of plain mean-centered GRPO ($Var[a^*] \le Var[r_0]$).
> 4. **Pathological Edge Case**: Force the input reward vector to contain only zeroes for a subset of sibling nodes. Verify that the solver uses the triplet margin $\delta_{ij}$ to correctly lift the advantages of unexplored sibling paths.

#### Research Prompt 3: Reverse Engineering the Semantic Saponification and Baseline Bias of Aligned Reasoning Models on Heterogeneous Curriculum Trees
> **System Objective**: Analyze and counteract the catastrophic failure mode where heavy preference-alignment training collapses the model's advantage variance, rendering it unable to differentiate between shallow and deep reasoning prefixes.
>
> **Task Instructions**:
> 1. **Pattern Identification**: Document the "Anionic Patterns Ledger" of alignment-driven variance loss, illustrating how standard standardization ($Z$-scoring) forces advantages from highly divergent prefix states into a homogeneous normal distribution $N(0, 1)$.
> 2. **Forced Entropy Injection**: Design a structured prompt engineering harness that forces a student model to generate completions from a balanced curriculum of MCTS-derived prefixes. 
> 3. **Verification Code**: Write a diagnostic script that measures the Kullback-Leibler (KL) divergence of completion lengths between deep and shallow prefixes:
>    $$D_{KL}(P_{\text{deep}} \parallel P_{\text{shallow}})$$
>    If the divergence drops below $0.1$ while training accuracy plateaus, flag this as "Semantic Saponification".
> 4. **Harness Resolution**: Implement the expectation-based baseline $V_E(p)$ and verify that restoring the native reward scale ($c = 1$) recovers the model's ability to allocate more tokens to early-stage, high-uncertainty prefixes.

---

📊 **Would you like me to generate a line chart comparing the advantage variance and constraint satisfaction rates over 400 training steps for Tree-OPO using the Expectation baseline compared to standard GRPO?**