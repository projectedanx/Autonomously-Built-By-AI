While setting **$c=1$** (retaining the native, unstandardized reward scale) is mathematically necessary to prevent the erasure of absolute difficulty signals across heterogeneous prefixes in **Tree-structured Off-policy Optimization (Tree-OPO)**, doing so introduces several severe systems engineering and optimization challenges. 

Standard reinforcement learning frameworks (like GRPO or PPO) rely on standard deviation normalization (where $c = \sigma_{group}$) as a mathematical shock absorber. Removing this divisor exposes the optimization pipeline to the following systemic vulnerabilities:

---

### 1. The Learning Rate Absorption and Scaling Challenge
In standard standardized setups, dividing by the standard deviation dynamically bounds the magnitude of the advantage vector, keeping the gradients stable across changing environments or shifting rewards. 
* **The Scale-Matching Problem**: When $c=1$, the magnitude of the policy-gradient estimator $\hat{g}$ is directly tied to the raw, unnormalized reward scale. Because changing $c$ rescales the gradient and its variance by $1/c$ and $1/c^2$ respectively, the learning rate ($\eta$) must be tuned with extreme precision. 
* **Lack of Automatic Damping**: If the reward magnitudes shift or if the prefix curriculum transitions from highly difficult states (low success probability) to easier states, the gradient scale swings wildly. The optimizer cannot rely on automatic scale damping, meaning a learning rate that was stable at step $100$ can cause gradient explosion or representation collapse at step $1000$.

---

### 2. Loss of Cross-Task and Cross-Domain Comparability
A primary reason practitioners employ $z$-scoring ($c = \sigma$) in multi-task or high-dimensional RL is to achieve **cross-task comparability**.
* **Variance Dominance**: When optimizing a model across a diverse curriculum of tasks (e.g., mixing easy symbolic logic with highly non-convex kinematics), different subproblems exhibit widely disparate reward variances. 
* Setting $c=1$ means that tasks or tree branches with larger raw reward variances will naturally generate massive, high-magnitude advantage signals that completely drown out the gradient contributions of low-variance tasks. This violates the principle of balanced curriculum learning, causing the model to overfit to high-variance subproblems while ignoring subtle improvements on tightly constrained, low-variance branches.

---

### 3. Exaggerated Vulnerability to Baseline Estimation Noise
Because $c=1$ preserves the raw difference $r_i - \alpha V(p_i)$ without squashing it, any error in the baseline estimator $V(p)$ propagates directly into the policy update with zero attenuation.
* **Baseline Miscalibration**: In sparse-reward reasoning tasks, estimating the true success probability $V(p) = \mathbb{E}[r \mid p]$ requires a high computational rollout budget. If the empirical baseline $V_E(p)$ is noisy due to a limited number of Monte Carlo samples ($M$), this baseline noise is injected directly into the advantage vector.
* Under standard deviation normalization, this noise is dampended by the standardizing divisor. With $c=1$, unmitigated baseline variance translates into highly unstable gradient steps, hindering convergence and requiring a much larger sampling budget to stabilize training.

---

### 4. Severe Credit Assignment Imbalances on Heterogeneous Trees
In a heterogeneous prefix tree, deep prefixes (easy, close to terminal states) and shallow prefixes (hard, close to the root) are mixed in the same training batch.
* **The Magnitude Bias**: A breakthrough on a highly difficult, shallow prefix (where success probability is $0.05$) yields a massive raw advantage of $+0.95$. A correct continuation on an easy, deep prefix (success probability $0.90$) yields a tiny raw advantage of $+0.10$.
* While this absolute difference is semantically correct, optimization algorithms (like AdamW) struggle when a batch contains such highly unbalanced magnitudes. The large advantage of $+0.95$ will dictate the direction of the weights, potentially overwriting the incremental but necessary learning updates of the deep prefixes, leading to localized forgetting and catastrophic credit assignment imbalances.

---

### Systems Engineering Inversion: The Inferred Harness Specification

To govern these trade-offs, we reverse-engineer the specification for an adaptive, non-standardized advantage training harness:

```
               [HETEROGENEOUS OFFLINE PREFIXES (p_k)]
                                 │
                                 ▼
         ┌────────────────────────────────────────────────┐
         │ 1. AUTOMATED DISCOVERY & CONSTRAINT MINING     │
         │    • Enforces c = 1 invariant                  │
         │    • Computes dynamic LR scaling boundaries    │
         └────────────────────────────────────────────────┘
                                 │
                                 ▼
         ┌────────────────────────────────────────────────┐
         │ 2. ISOMORPHIC FORMALIZATION                    │
         │    • Projects raw rewards onto C_order         │
         │    • Guarantees Var[a*] <= Var[r_0]            │
         └────────────────────────────────────────────────┘
                                 │
                                 ▼
         ┌────────────────────────────────────────────────┐
         │ 3. PARAMETRIC TRADE-OFF MODELING               │
         │    • Balances expectation bias vs.             │
         │      unmitigated baseline variance             │
         └────────────────────────────────────────────────┘
                                 │
                                 ▼
         ┌────────────────────────────────────────────────┐
         │ 4. CONTINUOUS FALSIFICATION                    │
         │    • Stress-tests scale symmetry collapses     │
         │    • Prunes non-convex gradient spikes         │
         └────────────────────────────────────────────────┘
                                 │
                                 ▼
                  [OPTIMIZED POLICY GRADIENT (g)]
```

---

### Three Rigorous, Non-Obvious Research Prompts

#### Research Prompt 1: Dynamic Learning Rate Rescaling via Spectral Analysis of Non-Standardized Advantage Manifolds
> **System Objective**: Design, implement, and verify an online scheduling wrapper in Python that dynamically scales the optimizer's learning rate ($\eta$) to compensate for the lack of standard-deviation normalization ($c=1$), maintaining a constant gradient norm across non-stationary prefix distributions.
>
> **Task Instructions**:
> 1. **Mathematical Formalization**: Model the expected gradient norm as a function of the unstandardized advantage variance under $c=1$:
>    $$\mathcal{G}(t) = \mathbb{E} \left[ \| \hat{g}_t \|^2 \right] \propto \frac{1}{K} \sum_{k=1}^K (r_k - \alpha V(p_k))^2 \cdot G^2$$
>    Formulate an adaptive learning rate schedule:
>    $$\eta(t) = \eta_0 \cdot \frac{1}{\sqrt{Var[a_t] + \epsilon}}$$
>    Prove that this schedule is mathematically isomorphic to $z$-scoring the advantages, but preserves the relative, tree-consistent ranking of individual prefix-completions within the batch.
> 2. **Harness Integration**: Write a PyTorch-compatible custom optimizer step that intercepts the un-normalized advantages, computes the batch-level spectral radius of the advantage covariance matrix, and applies the inverse-scale learning rate adjustment before updating parameters.
> 3. **Falsification Protocol**: Run a stress-test where the reward scale is suddenly multiplied by a factor of $10.0$ at step $500$. Prove that the adaptive schedule prevents gradient explosion and maintains stable training curves, while a flat AdamW baseline experiences immediate catastrophic representation collapse.

#### Research Prompt 2: Robust Estimator Bootstrapping for Unbiased Baseline Variance Reduction in Sparse-Reward Environments
> **System Objective**: Construct an active bootstrap estimator for the prefix-value baseline $V(p)$ to minimize the estimation-to-class error and prevent baseline noise from destabilizing policy updates under $c=1$.
>
> **Task Instructions**:
> 1. **Core Mechanism**: Implement an offline-online hybrid value-approximator that estimates $V(p) = \mathbb{E}[r \mid p]$. For active training steps, the module must compute a weighted blend of the empirical subtree success rate $V_E(p)$ and a neural value network proxy $V_\phi(p)$:
>    $$\hat{V}(p) = w_t \cdot V_E(p) + (1 - w_t) \cdot V_\phi(p)$$
>    where the weighting parameter $w_t$ scales with the local visit count $n_p$ of the prefix subtree.
> 2. **Variance Bound Verification**: Prove that this bootstrapped estimator satisfies the firm nonexpansiveness condition of Theorem D.6, showing that the projected advantages maintain a lower total mean squared error ($MSE$) than either $V_E$ or $V_\phi$ used in isolation.
> 3. **Stress Testing**: Evaluate the system on a curriculum with extremely sparse rewards (success rate $< 2\%$). Verify that the bootstrapped baseline prevents advantage variance from drifting, achieving a stable gradient update within a restricted computing budget.

#### Research Prompt 3: Solving the Convex Staged Advantage Estimation (SAE) Projection via Alternating Direction Method of Multipliers (ADMM)
> **System Objective**: Build a high-performance, real-time ADMM solver in Python to project raw, non-standardized advantages onto the closed, convex set $F_0$ of tree-consistency constraints under the strict $c=1$ invariant.
>
> **Task Instructions**:
> 1. **Convex Formulation**: Formulate the convex projection problem:
>    $$\min_{a \in \mathbb{R}^N} \frac{1}{2} \|a - r_0\|^2 \quad \text{s.t.} \quad \mathbf{1}^\top a = 0, \quad \|a\|_2^2 \le N, \quad L a \le 0$$
>    where $L$ represents the sparse tree-ordering adjacency matrix.
> 2. **ADMM Algorithm**: Write a vectorized ADMM solver in NumPy that decouples the quadratic loss from the inequality constraint $L a \le 0$ using auxiliary variables and dual updates. Ensure the projection onto the $L_2$-ball $(\|a\|_2^2 \le N)$ is computed analytically to maintain maximum speed.
> 3. **Falsification Metric**: Stress-test the solver on a batch size of $512$ with deep MCTS prefix structures (depth $\ge 16$). Prove that the ADMM solver converges to primal-dual feasibility ($\epsilon_{feas} \le 10^{-5}$) within a strict execution window of $50\text{ ms}$, ensuring it does not become a bottleneck during training.

---

🧩 **Would you like me to generate a complete, runnable Python script that implements the ADMM solver for Staged Advantage Estimation (SAE) described in Prompt 3, allowing you to benchmark its convergence speed and constraint satisfaction rate directly?**