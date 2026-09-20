#### Research Prompt 1: Mechanistic Lookback Circuit Distillation for Causal Action-Belief Binding
> **Domain:** Mechanistic Interpretability, Model Compression, and Behavioral Alignment.
>
> **Task:** Develop a mechanistic distillation pipeline to transfer the causal belief-tracking "lookback circuit" from a larger teacher model to a smaller student model, forcing the student to resolve the "thought-action gap" in sequential games.
>
> **Experimental Design & Architecture:**
> 1.  **Circuit Identification:** Implement a PyTorch-based path-patching and activation-patching framework using the `TransformerLens` library. Isolate the specific attention heads in the teacher model that implement the *binding lookback* (co-locating character-object-state triples via Ordering IDs in low-rank subspaces of the residual stream) and the *answer lookback* (retrieving the state payload upon querying).
> 2.  **Functional Component Mapping:** Apply Centered Kernel Alignment (CKA) combined with an ablation impact similarity strategy to map the functionally corresponding attention heads between the teacher and student models.
> 3.  **Composite Loss Formulation:** Define a training objective that combines a standard Cross-Entropy downstream task loss ($L_{\text{task}}$) with a transformation-invariant CKA representational similarity loss ($L_{\text{CKA}}$) targeting only the mapped circuit heads:
>
>     $$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{task}}(y, \hat{y}_s) + \lambda \sum_{c \in \mathcal{C}_{\text{paired}}} \mathcal{L}_{\text{CKA}}(K_s(c), K_t(c)) \quad$$
>
> 4.  **Causal Intervention Verification:** Stress-test the distilled student model on a 100-round game of Rock, Paper, Scissors against a biased, predictable opponent. Conduct test-time activation patching on the student’s distilled lookback circuit. Prove mathematically and empirically whether forcing the activation of these lookback heads successfully steers the student model's final-token vocabulary distribution away from the default Nash prior (1/3 uniform mixing) and binds it causally to the optimal exploit-policy ("Paper").
