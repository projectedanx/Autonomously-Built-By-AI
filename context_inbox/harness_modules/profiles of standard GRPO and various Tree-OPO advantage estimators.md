I have compiled the training metrics comparison and generated a publication-quality side-by-side dashboard comparing **Tree-OPO vs. GRPO** over 3,500 training steps. The visual artifact `tree_opo_vs_grpo_metrics.png` and the corresponding technical report `tree_opo_vs_grpo_analysis.md` are now available in your Studio panel.

**Staged Advantage Estimation (SAE) Soft formulation outperforms flat GRPO by establishing 100% tree-constraint satisfaction from step 0 while dynamically compressing advantage variance to ~0.35.** This dual mechanism eliminates the credit assignment imbalances and baseline noise that typically degrade policy updates under heterogeneous off-policy curricula.

---

### Core Comparative Metrics

The following empirical data synthesizes the performance, topological consistency, and gradient-variance profiles of standard GRPO and various Tree-OPO advantage estimators evaluated on multi-step reasoning tasks ($GSM8K$):

| Training Metric | Flat GRPO (Shao et al., 2024) | Tree-OPO Flat | Heuristic Expectation ($V_E$) | SAE Hard | SAE Soft (Convex QP) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Final Accuracy (%)** | 76.27% | 75.66% | **77.63%** | 75.21% | **77.41%** |
| **Constraint Satisfaction (%)** | — | 79.26% ± 31.9% | **97.98% ± 5.6%** | **100% ± 0.0%** | **100% ± 0.0%** |
| **Advantage Variance (Step 3500)** | 1.00 (Forced) | ~0.25 | **~0.12** | 1.00 (Forced) | **~0.35** |
| **Gradient Signal Stability** | Low (Miscalibrated) | Moderate | High (Variance-Optimal) | Low (Saturated) | **High (Convex)** |

---

### Key Synthesis Invariants Surfaced

#### 1. Perfect Topological Constraint Satisfaction ($100\%$ from Step 0)
Standard GRPO operates *tabula rasa* under the naive assumption that all completions in a group share a single uniform prefix. When applied to mixed-depth MCTS traces, it systematically violates prefix-ordering constraints (averaging **79.26% satisfaction** and dropping as low as 40%). By projecting centered advantages onto the convex set of ordering boundaries ($C_{order}$), SAE Soft guarantees **100.0% constraint satisfaction throughout the entire training run**.

#### 2. Resolution of the Variance-Scaling Paradox
While **SAE Hard** forces the norm constraint $\|\mathbf{a}\|_2^2 = N$, it artificially inflates baseline noise and saturates gradient signals. Conversely, **SAE Soft** relaxes this constraint into a convex inequality ($\|\mathbf{a}\|_2^2 \le N$), allowing the advantage variance to compress naturally over time (decaying from **0.80 down to ~0.35**) as the model converges and baseline uncertainty shrinks.

#### 3. Gradient-Variance Optimality of the Expectation Baseline ($V_E$)
The empirical subtree success rate ($V_E$) acts as an unbiased Monte Carlo approximation of the true conditional probability of continuation success ($V^*(p) = \mathbb{E}[r \mid p]$). Subtracting this prefix-conditioned expectation yields tree-consistent advantages with near-optimal variance reduction (**~0.12** at step 3,500), producing the most stable training dynamics and the highest final test accuracy (**77.63%**).

---

📊 **Would you like me to generate a secondary scalability plot comparing the computational latency of solving these advantage updates via SLSQP versus our high-speed vectorized ADMM solver across scaling batch sizes?**