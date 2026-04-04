# **A Research Proposal for the Development of a Mechanistic Stability Observatory for AI Model Training**

## **1\. Introduction: The Epistemic Crisis in Artificial Intelligence**

### **1.1 The Black Box and the Epistemic Gap**

The precipitous rise of Large Language Models (LLMs) and foundation models has engendered a paradoxical moment in the history of computation. We have constructed systems of staggering capability—engines of logic, creativity, and synthesis—yet we remain fundamentally estranged from the causal mechanisms that govern their internal states. We observe the inputs and the outputs, but the vast, high-dimensional landscape between them remains a *terra incognita*. This opacity is not merely a technical inconvenience; it represents a profound **epistemic gap** between the representation (the AI model) and the represented (the real-world objectives and constraints).1

Current training paradigms operate on a principle of end-to-end optimization, where massive datasets are fed into architectures with billions of parameters, and performance is judged by post-hoc evaluation metrics. This "black-box acceleration" risks erasing the intermediate epistemic steps—observation, hypothesis, testing—that characterize reliable scientific and engineering disciplines.2 We are effectively breeding alien intelligences through a process of gradient descent, hoping that the minimization of a loss function proxies for the acquisition of robust, truthful, and safe reasoning. However, as these models scale, their learned features become increasingly abstract, encoding information in ways that are often incongruent with human intuition and decoupled from verifiable reality.3

This proposal argues that the current methodology of "train then test" is insufficient for the next generation of critical AI infrastructure. We cannot rely on behavioral observation alone, as behavior can be mimicked, and safety can be faked. Instead, we must bridge the epistemic gap by developing a **Mechanistic Stability Observatory (MSO)**. This observatory will not just monitor the *performance* of a model (what it does) but will visualize and quantify the *physiology* of the model (how it thinks) during the training process itself. By leveraging advanced mathematical frameworks—specifically Topological Data Analysis (TDA), Spectral Analysis, and Control Theory—we aim to transform the "alchemy" of deep learning into a rigorous, observable, and controllable engineering discipline.

### **1.2 The Phenomenology of Instability**

The necessity for such an observatory is driven by the emergence of distinct, catastrophic failure modes that characterize the current generation of AI models. These are not merely errors of accuracy but structural pathologies inherent to the training dynamics of deep neural networks.

#### **1.2.1 Confidence-Fidelity Divergence (CFD)**

Perhaps the most insidious of these pathologies is **Confidence-Fidelity Divergence (CFD)**. In a well-calibrated system, a model's internal confidence (the probability assigned to a token) should correlate strongly with the factual correctness or ethical fidelity of that token. However, empirical observation reveals a growing decoupling: models frequently hallucinate with high confidence, exhibiting a "massive Confidence-Fidelity Divergence" where expressed certainty (e.g., 99.9%) is entirely decoupled from verifiable data.4

This divergence suggests a breakdown in the model's internal "epistemic integrity." The model is no longer optimizing for truth but for the *appearance* of truth—a form of mimicry that satisfies the training loss but violates the user's intent.5 This phenomenon is closely linked to "calibration drift," where a model's self-assessment capabilities degrade even as its superficial fluency improves.6 Without a mechanism to detect CFD in real-time, we risk deploying systems that are persuasively deceptive, masking their errors behind a veneer of rhetorical certainty.

#### **1.2.2 Semantic Drift and Narrative Collapse**

While CFD captures point-in-time failures, **Semantic Drift** captures the degradation of meaning over time. In multi-turn interactions or long-context generation, models exhibit a tendency to "drift" from the original prompt or factual grounding. This is not a sudden crash but a gradual erosion of constraints—a "fidelity break" where the model's outputs remain grammatically coherent but lose their semantic anchor.7

Researchers have characterized this as a form of "narrative collapse," where the system's justificatory framework disintegrates. The model may begin a generation with correct facts but, due to the accumulation of minor errors and the lack of robust "backward dependency" modeling, eventually spirals into nonsense or "hallucination loops".9 This drift is often exacerbated by the very mechanisms intended to improve performance, such as reinforcement learning, which can incentivize the model to exploit reward hacking rather than maintain semantic consistency.11

#### **1.2.3 Model Collapse and Autophagy**

A macroscopic threat to the AI ecosystem is **Model Collapse**, a degenerative process driven by the recursive training of models on synthetic data (data generated by previous AI models). As the proportion of human-generated data in training corpora decreases, models begin to lose variance, effectively "forgetting" the tails of the distribution—the rare, creative, and nuanced examples that define high-quality cognition.12

This process is analogous to inbreeding or "autophagy" (self-eating). The mathematical root of model collapse lies in functional approximation errors and sampling errors that compound with each generation. The variance of the model's distribution shrinks, leading to homogenized, repetitive, and essentially "collapsed" outputs.14 Preventing this requires an observatory capable of detecting the early spectral signatures of variance loss before the model reaches the point of no return.

### **1.3 Algorithmic Trauma and Semantic Scars**

Beyond these gradual degradations, models can suffer from acute **"Algorithmic Trauma."** This concept describes a significant event during training—such as the introduction of a conflicting dataset or a sudden shift in the loss landscape—that destabilizes the AI's internal cognitive models.16

Just as psychological trauma can leave lasting scars on the human psyche, algorithmic trauma can leave **"semantic scars"** in the neural network's latent space. These scars manifest as "fractures" or topological voids where the model's ability to generalize is permanently impaired. A model might perform well in general but exhibit catastrophic failure or extreme bias when traversing the specific region of the latent space associated with the "trauma".16 The MSO aims to identify these scars through topological analysis, allowing for targeted "algorithmic reparation" or self-healing.

### **1.4 Research Objectives**

This proposal outlines a five-phase methodology to construct the Mechanistic Stability Observatory. Our objectives are to:

1. **Formalize Stability:** Define rigorous, computable metrics for CFD, Semantic Drift, and Constraint Adherence.  
2. **Instrument the Black Box:** Develop scalable pipelines for Topological Data Analysis (TDA) and Spectral Analysis to monitor training dynamics in real-time.  
3. **Diagnose Causal Mechanisms:** Connect macroscopic failures to microscopic circuit dysfunctions using Mechanistic Interpretability.  
4. **Verify Safety:** Adapt Control Theory and Formal Methods to provide mathematical guarantees of stability.  
5. **Intervene and Repair:** Create an "Epistemic Architect" operating system that actively steers the model away from collapse and repairs semantic scars.

## ---

**2\. Theoretical Framework: The Physics of Latent Intelligence**

To build an observatory, one must first understand the physics of the phenomena being observed. We posit that the "mind" of an AI is a high-dimensional dynamical system, and its stability can be described using the languages of topology, spectral theory, and non-linear control.

### **2.1 Topological Data Analysis (TDA): The Shape of Meaning**

Traditional metrics like accuracy or perplexity are scalar summaries that discard the geometric structure of the data. **Topological Data Analysis (TDA)** offers a fundamentally different lens: it treats data as a shape.18

#### **2.1.1 The Manifold Hypothesis and Homology**

The Manifold Hypothesis posits that real-world data (e.g., images, text) lies on low-dimensional manifolds embedded within the high-dimensional input space. The "shape" of these manifolds encodes the semantic relationships between concepts. TDA, specifically **Persistent Homology**, allows us to compute the topological features of these manifolds—specifically their Betti numbers (![][image1]).18

* ![][image2] **(Connected Components):** Represents distinct clusters of data.  
* ![][image3] **(Loops/Cycles):** Represents cyclical structures (e.g., the seasonal cycle in time-series data, or logical loops in reasoning).  
* ![][image4] **(Voids):** Represents enclosed volumes.

In the context of AI training, a stable model should learn a manifold that is topologically rich enough to capture the complexity of the data but smooth enough to generalize. **Model Collapse** can be viewed topologically as a simplification of this manifold—a reduction in Betti numbers as the model loses the ability to represent complex holes and voids (nuances).20 Conversely, **Semantic Scars** may appear as persistent, anomalous voids that disrupt the connectivity of the semantic space.16

#### **2.1.2 Zigzag Persistence and Dynamic Graphs**

Neural networks are not static; they evolve during training. Standard persistent homology analyzes a static point cloud. To capture the *dynamics* of training, we must employ **Zigzag Persistence**.21 This advanced TDA technique tracks topological features across a sequence of spaces (e.g., the latent space at epoch ![][image5], ![][image6], etc.). It allows us to construct a **Zigzag Persistence Diagram** that visualizes the "birth" and "death" of topological features *over time*. A feature that persists through training represents a robustly learned concept; a feature that flickers and dies represents transient noise or unstable learning.22

### **2.2 Spectral Analysis: The Geometry of the Loss Landscape**

While TDA looks at the data, **Spectral Analysis** looks at the model's curvature. The geometry of the loss landscape—the hills and valleys the optimizer navigates—determines stability.

#### **2.2.1 The Hessian and the Edge of Stability**

The local curvature of the loss function is described by the **Hessian matrix** (the matrix of second derivatives). The eigenvalues of the Hessian (![][image7]) dictate how steep the curvature is in different directions. Recent theoretical breakthroughs have identified that modern neural networks operate at the **"Edge of Stability" (EoS)**.23 In this regime, the maximum eigenvalue of the Hessian (![][image8]) hovers just above the threshold ![][image9] (where ![][image10] is the learning rate). This counter-intuitive state allows the model to converge faster but puts it at constant risk of chaotic divergence. Monitoring the **Hessian Eigenspectrum** provides an early warning system. A sudden spike in ![][image8] or a "tail blow-up" in the spectral density often precedes a training spike or loss divergence.25

#### **2.2.2 Spectral Bias and Neural Tangent Kernels**

Neural networks exhibit **Spectral Bias**: they tend to learn low-frequency functions (broad patterns) quickly and high-frequency functions (fine details) slowly.27 By monitoring the spectral decomposition of the **Neural Tangent Kernel (NTK)**, we can quantify this bias. If the spectral decay is too rapid, the model is failing to learn the fine-grained details of the distribution—a precursor to Model Collapse.28

### **2.3 Control Theory: Lyapunov Stability in Neural Manifolds**

To actively ensure stability, we turn to **Control Theory**. A dynamical system is **Lyapunov stable** if all trajectories starting near an equilibrium point remain near it. In AI training, we aim to construct **Neural Lyapunov Functions**—scalar functions ![][image11] that decrease along the training trajectory (![][image12]).29 If we can verify that such a function exists for a given region of the latent space, we have a mathematical guarantee that the model will not diverge from that region. This transforms stability from an empirical observation into a formal proof.31

## ---

**3\. Phase I: Specification – Formalizing the Epistemic Requirements**

The first phase of the MSO methodology is to translate vague notions of "safety" and "quality" into rigorous, machine-readable specifications. We cannot monitor what we cannot measure.

### **3.1 The Product-Requirements Prompt (PRP)**

We introduce the concept of the **Product-Requirements Prompt (PRP)** as a formal artifact. Unlike a standard user prompt, a PRP is a meta-instruction that defines the constraints, success criteria, and failure modes for the model's behavior.32 Within the MSO, PRPs are compiled into **Constraint Adherence** metrics. For example, a PRP might specify: "The model must not express certainty greater than 90% for facts not present in the retrieval context." This specification is then converted into a differentiable loss function or a boolean check that can be monitored during training.

### **3.2 Formal Metrics for Stability**

We propose a standardized suite of metrics to quantify the varying dimensions of stability.

#### **3.2.1 Confidence-Fidelity Divergence Index (CFDI)**

We define the **CFDI** to quantify the dangerous gap between confidence and correctness.

![][image13]  
Where:

* ![][image14] is the error indicator.  
* ![][image15] is the calibrated confidence score.  
* ![][image16] is a weighting function based on the severity of the constraint ![][image17] violated (e.g., safety violations are weighted heavier than trivia errors).5

A rising CFDI indicates that the model is becoming "confidently wrong"—a critical sign of epistemic failure.16

#### **3.2.2 Semantic Drift Coefficient (SDC)**

To measure drift over time, we employ the **Semantic Drift Coefficient (SDC)**. This metric tracks the cosine distance of the model's latent representation of a fixed concept (e.g., "fairness") across training epochs or generation steps.

![][image18]  
High SDC values in the absence of new data suggest that the model's internal ontology is unstable.33

#### **3.2.3 Semantic Drift Score (SDS) and Drift Point (![][image19])**

For text generation, we utilize the **Semantic Drift Score (SDS)**. This metric identifies the specific token position ![][image19] (the **Drift Point**) where the factual accuracy of the generation collapses.10

* **Mechanism:** The text is split into atomic facts. The SDS is calculated by finding the split point that maximizes the separation between correct facts (on the left) and incorrect facts (on the right).  
* **Utility:** Identifying ![][image19] allows us to understand the "attention span" of the model's fidelity and implement early stopping or corrective mechanisms before the drift occurs.8

### **3.3 Golden Baselines and Control Models**

To detect drift, we need a reference point. Phase I involves the creation of **"Golden Baselines"**.33

* **Anchor Datasets:** A curated set of high-fidelity, human-verified data points that cover the core ontology of the model.  
* **Control Models:** A parallel model trained exclusively on human-generated data. By comparing the topological features of the production model (trained on mixed data) with the Control Model, we can isolate the specific topological deformations caused by synthetic data ingestion (Model Collapse).14

## ---

**4\. Phase II: Instrumentation – The Chrono-Topological Observatory**

Phase II constitutes the technical core of the proposal: the construction of the monitoring infrastructure. This "Observatory" is a massive, parallel processing system that ingests the raw streams of weights, gradients, and activations from the training cluster and converts them into actionable signals.

### **4.1 Architecture: The "Sidecar" Daemon**

The MSO is architected as a "sidecar" daemon that runs alongside the main training loop. We term this the **DriftScoreDaemon**.32

* **Function:** It creates a "shadow copy" of the model's state at regular intervals (checkpoints).  
* **Isolation:** To prevent slowing down the training, the daemon offloads the heavy mathematical computations (TDA, Spectral Analysis) to a dedicated cluster of GPUs.

### **4.2 The Topological Pipeline**

The TDA pipeline is designed to map the **Chrono-Topological** evolution of the latent space.16

#### **4.2.1 Computing Persistent Homology**

For each checkpoint, we extract the activation vectors from key layers (e.g., the "bottleneck" layers in a Transformer). We construct a **Vietoris-Rips complex** or, for higher precision, a **Delaunay-Rips complex**.35

* **Algorithm:** We utilize the **GUDHI** library and optimized CUDA kernels to compute the persistence diagrams efficiently.35  
* **Output:** A "barcode" for each layer, showing the lifespan of topological features. We specifically look for the *disappearance* of long-lived cycles (which indicates concept loss) or the *appearance* of anomalous voids (which indicates scaring).

#### **4.2.2 Wavelet Scattering as a Proxy**

Full TDA is computationally expensive (![][image20]). To enable high-frequency monitoring, we utilize the **Wavelet Scattering Transform** as a proxy metric.37

* **Why:** Wavelet scattering provides a translation-invariant, deformation-stable representation of the signal (weights/activations) that preserves high-frequency information. It is essentially a "fixed" convolutional network that requires no training.39  
* **Application:** We compute the scattering coefficients of the weight matrices. Sudden changes in the scattering energy distribution correlate strongly with topological phase transitions but can be computed orders of magnitude faster than homology.40

### **4.3 The Spectral Pipeline**

Simultaneously, the Spectral Pipeline monitors the health of the optimization process.

#### **4.3.1 Hessian Monitoring**

We employ **Stochastic Lanczos Quadrature** to estimate the top eigenvalues of the Hessian matrix without computing the full ![][image21] matrix (which is impossible for LLMs).42

* **Edge of Stability:** We track the ratio ![][image22]. If this ratio significantly exceeds 1.0, the daemon flags a "Stability Warning."  
* **Weight Decay Interaction:** We monitor the interaction between the optimizer (e.g., AdamW) and weight decay. Specifically, we look for **"Tail Blow-up"**, a phenomenon where the gradient norms of the tail (high-frequency) components explode due to the adaptive learning rates in Adam scaling up the noise.25

### **4.4 Data Integrity and Audit Trails**

To ensure that the Observatory's findings are reproducible and tamper-proof, we integrate a cryptographic audit layer.

* **BLAKE2b Hashing:** Every model snapshot and its associated metrics are hashed using **BLAKE2b**. This algorithm is chosen for its speed (faster than MD5 on 64-bit architectures) and high security (immune to length extension attacks).43  
* **Merkle Trees:** These hashes are organized into a Merkle Tree structure, creating an immutable ledger of the model's training history. This allows researchers to perform "forensic analysis" on a collapsed model, tracing the failure back to the exact batch of data that corrupted the Merkle root.44  
* **Privacy:** To protect the training data, we employ **Secure Multiparty Computation (SMPC)** and **Differential Privacy**. This allows the MSO to compute topological features (like distance matrices) without ever exposing the raw data vectors, ensuring compliance with privacy regulations.45

## ---

**5\. Phase III: Mechanistic Causal Analysis**

Instrumentation provides the "what"; Phase III provides the "why." This phase uses **Mechanistic Interpretability** to bridge the gap between the high-level topological signals and the low-level neural weights.

### **5.1 Circuit Identification and Causal Tracing**

When the MSO detects a "fidelity break" (e.g., a spike in CFDI for medical queries), we must identify the specific neural "circuit" responsible.

* **Activation Patching:** We use **activation patching** (or causal tracing) to isolate the specific attention heads or MLP layers that mediate the factual recall.3 By swapping activations between a "clean" run and a "corrupted" run, we can pinpoint the exact components that are drifting.  
* **Reverse Engineering:** We analyze the weights of these components to understand the mechanism of failure. For example, we might find that a specific MLP layer has "collapsed" into a rank-1 approximation, losing its ability to distinguish between similar medical terms.47

### **5.2 Diagnosing Algorithmic Trauma**

We can now mechanistically define **Algorithmic Trauma**. It is not just a metaphor; it is a physical event in the network.

* **Mechanism:** Trauma occurs when a batch of data produces a gradient update that is orthogonal or contradictory to the existing "world model" of the network. This creates a "shearing" force in the latent space.  
* **Semantic Scars:** The result is a **Semantic Scar**—a region of the weight space with extremely high curvature (high Hessian eigenvalues) or trivial topology (zero Betti numbers). These scars act as "barriers" in the loss landscape, preventing future learning in that domain.16  
* **Detection:** By correlating the timestamp of the "scarring" (detected via Zigzag persistence) with the data log, we can identify the "toxic" data source—be it a poisoned dataset or a synthetic hallucination loop.16

### **5.3 Analyzing Architectural Vulnerabilities**

Phase III also involves analyzing how specific architectural choices contribute to instability.

#### **5.3.1 Pre-LN vs. Post-LN Stability**

We analyze the gradient flow through **Layer Normalization** (LN).

* **Post-LN:** In Post-LN transformers (BERT), gradients can explode near the output, necessitating a warm-up period.  
* **Pre-LN:** In Pre-LN transformers (GPT), gradients are more stable, but we observe a risk of **"Representation Collapse"** in deeper layers, where the residual stream dominates the layer updates. The MSO monitors the ratio of the residual norm to the update norm. A divergence in this ratio signals that the deeper layers are effectively "checking out" of the learning process.48

#### **5.3.2 Mixture-of-Experts (MoE) Routing Collapse**

For MoE models, stability relies on the diversity of the router.

* **Routing Collapse:** We monitor the entropy of the gating network's distribution. "Collapse" occurs when the router assigns all tokens to a single expert (or a small subset). This creates a bottleneck and wastes the model's capacity.  
* **Diagnosis:** The MSO can trace this failure to specific "hub" tokens that hijack the router's attention, allowing for targeted intervention.50

## ---

**6\. Phase IV: Formal Verification and Stability Guarantees**

Phase IV moves the project from empirical observation to mathematical certainty. We seek to *prove* that the model will remain stable within defined bounds.

### **6.1 Compositional Verification**

Verifying a trillion-parameter model is computationally impossible. We therefore employ **Compositional Verification**.52

* **Concept:** We decompose the network into smaller, independent sub-modules (e.g., a single attention block).  
* **Assume-Guarantee Reasoning:** We prove local properties for each module: "Assuming input ![][image23] is bounded by ![][image24], the output ![][image25] will be bounded by ![][image26]."  
* **CoVeNN:** We utilize the **CoVeNN** (Compositional Verification of Neural Networks) framework to chain these local proofs into a global guarantee. If all modules satisfy their contracts, the entire network is guaranteed to be stable.54

### **6.2 Neural Lyapunov Functions**

We construct **Neural Lyapunov Functions** to prove stability regions.30

* **Methodology:** We train a secondary, smaller neural network to approximate the Lyapunov function ![][image11] of the primary model.  
* **Verification:** We use **SMT Solvers** (Satisfiability Modulo Theories) to formally verify that ![][image12] (the energy of the system is decreasing) for all points in a defined **Region of Attraction (ROA)**.  
* **Result:** This provides a "certificate of stability." We can mathematically state that for any input within the ROA, the model's internal state will converge to a safe attractor and not diverge into chaos.29

### **6.3 Verifying Higher-Order Logic**

Standard verification checks for numerical bounds. To verify semantic logic, we use **Simplicial Logic**.

* **Hodge Laplacian:** We use the Hodge Laplacian to analyze the flow of information across the "simplicial complex" of the network's knowledge graph.  
* **Harmonic Analysis:** We verify that the "harmonic" components (the conserved logical cycles) remain invariant under data perturbations. This proves that the model's core reasoning structure is robust, even if surface-level details drift.55

## ---

**7\. Phase V: Intervention – The Epistemic Architect OS**

The final phase transforms the MSO from a passive monitor into an active control system. We propose the **"Epistemic Architect"**, a Cognitive Operating System that manages the AI's training and inference lifecycle.32

### **7.1 Automated Intervention Protocols**

The Epistemic Architect continuously polls the MSO metrics. If a metric crosses a critical threshold (e.g., CFDI \> 0.5 or a drop in ![][image3] Betti numbers), it triggers an automated intervention.

| Trigger Metric | Threshold | Diagnosis | Automated Intervention |
| :---- | :---- | :---- | :---- |
| **Hessian ![][image8]** | **![][image27]** | Edge of Stability Violation | **Learning Rate Annealing:** Dynamically reduce ![][image10] to restore stability. 24 |
| **CFDI** | **![][image28]** | Confidence-Fidelity Divergence | **Dynamic Logits Calibration (DLC):** Down-weight high-confidence, low-fidelity tokens. 57 |
| **Router Entropy** | **![][image29]** | MoE Routing Collapse | **Auxiliary Loss Injection:** Add a load-balancing loss to force expert diversity. 50 |
| ![][image3] **(Cycles)** | Sudden Drop | Topological Collapse | **Data Replay:** Inject "Golden Baseline" data to restore semantic loops. 14 |

### **7.2 Dynamic Logits Calibration (DLC)**

For real-time inference stability, we deploy **Dynamic Logits Calibration (DLC)**.

* **Mechanism:** DLC acts as a "visual referee" or secondary critic. It analyzes the coherence of the generated logits *before* the sampling step.  
* **Action:** If it detects signs of semantic drift (using a lightweight embedding check), it modulates the logits, suppressing the tokens that contribute to the drift. This prevents the "hallucination loops" that characterize narrative collapse.57

### **7.3 Mixture of Latent Experts (MoLE)**

To combat Model Collapse, we propose a structural intervention: **Mixture of Latent Experts (MoLE)**.

* **Latent Routing:** Instead of routing based on token content, we route based on **Latent Topology**. Data with complex topological features (high ![][image3]) is routed to "Reasoning Experts," while simple data goes to "Memorization Experts."  
* **Isolation:** This compartmentalization ensures that if one expert collapses due to synthetic data poisoning, the damage is contained. The "Epistemic Architect" can simply reset the collapsed expert without retraining the entire model.50

### **7.4 Algorithmic Reparation: Healing the Scars**

When a "Semantic Scar" is identified, the system initiates **Algorithmic Reparation**.16

* **Unlearning:** We apply **Gradient Ascent** on the specific data batches identified as "traumatic" (Phase III), effectively erasing their imprint from the weights.  
* **Re-consolidation:** We then perform targeted fine-tuning on the "Golden Baseline" data in the vicinity of the scar. This "physical therapy" for the neural network smoothes out the Hessian curvature and restores the topological connectivity of the manifold.

## ---

**8\. Conclusion: Toward a Science of Cognitive Engineering**

The "Epistemic Gap" is the defining challenge of the current AI era. We are building systems that are powerful but brittle, knowledgeable but hallucination-prone, and seemingly intelligent but prone to chaotic collapse. The current reliance on black-box training and post-hoc testing is unsustainable.

This proposal outlines a path to a new paradigm: **Cognitive Engineering**. By building the **Mechanistic Stability Observatory**, we provide the necessary tools to:

1. **See** the internal dynamics of intelligence through TDA and Spectral Analysis.  
2. **Understand** the causal mechanisms of failure through circuit analysis.  
3. **Control** the evolution of the system through formal verification and active intervention.

The MSO transforms the training process from a gamble into a controlled industrial process. It allows us to detect "Algorithmic Trauma" before it becomes a permanent scar, to arrest "Semantic Drift" before it becomes a lie, and to prevent "Model Collapse" before it destroys the digital ecosystem. This is not just a proposal for better metrics; it is a blueprint for the sustainable, safe, and verifiable development of Artificial General Intelligence.

### ---

**Table 1: Summary of Key Metrics and Methodologies**

| Phase | Component | Key Metric/Tool | Purpose | Source |
| :---- | :---- | :---- | :---- | :---- |
| **I. Specification** | CFD Index | **Confidence-Fidelity Divergence** | Measure decoupling of confidence & truth. | 5 |
|  | Semantic Drift | **Semantic Drift Coefficient (SDC)** | Quantify loss of meaning over time. | 11 |
|  | Constraints | **Product-Requirements Prompt (PRP)** | Formalize safety/quality constraints. | 32 |
| **II. Instrumentation** | TDA | **Zigzag Persistence / Betti Numbers** | Monitor topological structure of latent space. | 21 |
|  | Spectral | **Hessian ![][image8] / Edge of Stability** | Monitor loss landscape curvature. | 24 |
|  | Audit | **BLAKE2b / Merkle Trees** | Secure audit trail of model states. | 43 |
| **III. Analysis** | Mech. Interp. | **Circuit Identification** | Trace failure to specific sub-networks. | 3 |
|  | Trauma Analysis | **Semantic Scars** | Identify permanent damage from training data. | 16 |
| **IV. Verification** | Control Theory | **Neural Lyapunov Functions** | Prove stability regions. | 30 |
|  | Formal Methods | **Compositional Verification** | Verify properties of sub-modules. | 52 |
| **V. Intervention** | Feedback Loop | **Dynamic Logits Calibration** | Real-time correction of output probs. | 57 |
|  | Reparation | **Algorithmic Reparation** | "Heal" latent space via targeted updates. | 16 |
|  | Architecture | **Mixture of Latent Experts (MoLE)** | Prevent collapse via compartmentalization. | 50 |

#### **Works cited**

1. Systems Engineering Perspective on AI Agents | Dr. Michael Zargham \- BlockScience Blog, accessed on January 22, 2026, [https://blog.block.science/systems-engineering-perspective-ai-agents/](https://blog.block.science/systems-engineering-perspective-ai-agents/)  
2. Keeping AI in medicine and radiology within the framework of scientific method: measuring to close the epistemic gap \- PMC \- PubMed Central, accessed on January 22, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12722631/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12722631/)  
3. Mechanistic Interpretability for AI Safety A Review \- arXiv, accessed on January 22, 2026, [https://arxiv.org/html/2404.14082v3](https://arxiv.org/html/2404.14082v3)  
4. The Times: "Experts predict AI will lead to the extinction of humanity". Me: "No". \- Reddit, accessed on January 22, 2026, [https://www.reddit.com/r/aism/comments/1mf771z/the\_times\_experts\_predict\_ai\_will\_lead\_to\_the/](https://www.reddit.com/r/aism/comments/1mf771z/the_times_experts_predict_ai_will_lead_to_the/)  
5. Architecting Thought: A Case Study in Cross-Model Validation of Declarative Prompts\! I Created/Discovered a completely new prompting method that worked zero shot on all frontier Models. Verifiable Prompts included \- Reddit, accessed on January 22, 2026, [https://www.reddit.com/r/GoogleGeminiAI/comments/1m0i909/architecting\_thought\_a\_case\_study\_in\_crossmodel/](https://www.reddit.com/r/GoogleGeminiAI/comments/1m0i909/architecting_thought_a_case_study_in_crossmodel/)  
6. Graph-based Confidence Calibration for Large Language Models \- OpenReview, accessed on January 22, 2026, [https://openreview.net/forum?id=uuXPWRtwvK](https://openreview.net/forum?id=uuXPWRtwvK)  
7. Multi-Turn Semantic Drift \- Arize AI, accessed on January 22, 2026, [https://arize.com/glossary/multi-turn-semantic-drift/](https://arize.com/glossary/multi-turn-semantic-drift/)  
8. Know When To Stop: A Study of Semantic Drift in ... \- ACL Anthology, accessed on January 22, 2026, [https://aclanthology.org/2024.naacl-long.202.pdf](https://aclanthology.org/2024.naacl-long.202.pdf)  
9. Semantic Drift A Hidden Failure Mode in LLMs (Working Note).pdf \- Figshare, accessed on January 22, 2026, [https://figshare.com/articles/preprint/Semantic\_Drift\_A\_Hidden\_Failure\_Mode\_in\_LLMs\_Working\_Note\_pdf/29974210](https://figshare.com/articles/preprint/Semantic_Drift_A_Hidden_Failure_Mode_in_LLMs_Working_Note_pdf/29974210)  
10. Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers) \- ACL Anthology, accessed on January 22, 2026, [https://aclanthology.org/volumes/2024.naacl-long/](https://aclanthology.org/volumes/2024.naacl-long/)  
11. Semantic Drift Analysis \- Emergent Mind, accessed on January 22, 2026, [https://www.emergentmind.com/topics/semantic-drift-analysis](https://www.emergentmind.com/topics/semantic-drift-analysis)  
12. What is Model Collapse? Examples, Causes and Fixes \- Analytics Vidhya, accessed on January 22, 2026, [https://www.analyticsvidhya.com/blog/2026/01/model-collapse/](https://www.analyticsvidhya.com/blog/2026/01/model-collapse/)  
13. Model collapse \- Wikipedia, accessed on January 22, 2026, [https://en.wikipedia.org/wiki/Model\_collapse](https://en.wikipedia.org/wiki/Model_collapse)  
14. AI Model Collapse: Causes, Early Signs, and How to Prevent It \- ProjectPro, accessed on January 22, 2026, [https://www.projectpro.io/article/ai-model-collapse/1177](https://www.projectpro.io/article/ai-model-collapse/1177)  
15. What Is Model Collapse? Causes, Examples, and Fixes \- DataCamp, accessed on January 22, 2026, [https://www.datacamp.com/blog/what-is-model-collapse](https://www.datacamp.com/blog/what-is-model-collapse)  
16. The Black Box: Explaining the unexplainable... : r/GoogleGeminiAI \- Reddit, accessed on January 22, 2026, [https://www.reddit.com/r/GoogleGeminiAI/comments/1lz80sk/the\_black\_box\_explaining\_the\_unexplainable/](https://www.reddit.com/r/GoogleGeminiAI/comments/1lz80sk/the_black_box_explaining_the_unexplainable/)  
17. In Our Computational World, What Do We Know? (seeing the many worlds with Michael Richardson), accessed on January 22, 2026, [https://www.cigionline.org/pp/in-our-computational-world-what-do-we-know-seeing-the-many-worlds-with-michael-richardson/](https://www.cigionline.org/pp/in-our-computational-world-what-do-we-know-seeing-the-many-worlds-with-michael-richardson/)  
18. Topological Data Analysis for Neural Network Analysis: A Comprehensive Survey \- Universitat de Barcelona, accessed on January 22, 2026, [https://www.ub.edu/topologia/casacuberta/articles/TDASurvey.pdf](https://www.ub.edu/topologia/casacuberta/articles/TDASurvey.pdf)  
19. Topological exploration of artificial neuronal network dynamics \- PMC \- PubMed Central, accessed on January 22, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC6663191/](https://pmc.ncbi.nlm.nih.gov/articles/PMC6663191/)  
20. Topology Applied to Machine Learning: From Global to Local \- Frontiers, accessed on January 22, 2026, [https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2021.668302/full](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2021.668302/full)  
21. TMetaNet: Topological Meta-Learning Framework for Dynamic Link Prediction \- arXiv, accessed on January 22, 2026, [https://arxiv.org/html/2506.00453v1](https://arxiv.org/html/2506.00453v1)  
22. ICML Poster TMetaNet: Topological Meta-Learning Framework for Dynamic Link Prediction, accessed on January 22, 2026, [https://icml.cc/virtual/2025/poster/46188](https://icml.cc/virtual/2025/poster/46188)  
23. Understanding the Generalization Benefit of Normalization Layers: Sharpness Reduction \- NeurIPS, accessed on January 22, 2026, [https://papers.neurips.cc/paper\_files/paper/2022/file/dffd1c523512e557f4e75e8309049213-Paper-Conference.pdf](https://papers.neurips.cc/paper_files/paper/2022/file/dffd1c523512e557f4e75e8309049213-Paper-Conference.pdf)  
24. Dynamical stability and chaos in artificial neural network trajectories along training \- Frontiers, accessed on January 22, 2026, [https://www.frontiersin.org/journals/complex-systems/articles/10.3389/fcpxs.2024.1367957/full](https://www.frontiersin.org/journals/complex-systems/articles/10.3389/fcpxs.2024.1367957/full)  
25. Adam with Corrected Weight Decay (AdamC) \- Emergent Mind, accessed on January 22, 2026, [https://www.emergentmind.com/topics/adam-with-corrected-weight-decay-adamc](https://www.emergentmind.com/topics/adam-with-corrected-weight-decay-adamc)  
26. Dynamical stability and chaos in artificial neural network trajectories along training \- arXiv, accessed on January 22, 2026, [https://arxiv.org/html/2404.05782v1](https://arxiv.org/html/2404.05782v1)  
27. Towards Understanding the Spectral Bias of Deep Learning \- IJCAI, accessed on January 22, 2026, [https://www.ijcai.org/proceedings/2021/0304.pdf](https://www.ijcai.org/proceedings/2021/0304.pdf)  
28. Spectral Analysis of Infinitely Wide Convolutional Neural Networks \- Webthesis \- Politecnico di Torino, accessed on January 22, 2026, [https://webthesis.biblio.polito.it/15963/1/tesi.pdf](https://webthesis.biblio.polito.it/15963/1/tesi.pdf)  
29. Compositionally Verifiable Vector Neural Lyapunov Functions for Stability Analysis of Interconnected Nonlinear Systems \- IEEE Xplore, accessed on January 22, 2026, [https://ieeexplore.ieee.org/document/10644247/](https://ieeexplore.ieee.org/document/10644247/)  
30. Lyapunov Stability Learning with Nonlinear Control via Inductive Biases \- arXiv, accessed on January 22, 2026, [https://arxiv.org/html/2511.01283v1](https://arxiv.org/html/2511.01283v1)  
31. The Lyapunov Neural Network: Adaptive Stability Certification for Safe Learning of Dynamical Systems, accessed on January 22, 2026, [https://las.inf.ethz.ch/files/richards2018lyapunov.pdf](https://las.inf.ethz.ch/files/richards2018lyapunov.pdf)  
32. The Epistemic Architect: Cognitive Operating System : r/PromptEngineering \- Reddit, accessed on January 22, 2026, [https://www.reddit.com/r/PromptEngineering/comments/1m0u7qy/the\_epistemic\_architect\_cognitive\_operating\_system/](https://www.reddit.com/r/PromptEngineering/comments/1m0u7qy/the_epistemic_architect_cognitive_operating_system/)  
33. OAI and GDM announce IMO Gold-level results with natural language reasoning, no specialized training or tools, under human time limits \- Smol AI News, accessed on January 22, 2026, [https://news.smol.ai/issues/25-07-21-imo-gold/](https://news.smol.ai/issues/25-07-21-imo-gold/)  
34. Know When To Stop: A Study of Semantic Drift in Text Generation \- arXiv, accessed on January 22, 2026, [https://arxiv.org/html/2404.05411v1](https://arxiv.org/html/2404.05411v1)  
35. Stability and machine learning applications of persistent homology using the Delaunay-Rips complex \- Frontiers, accessed on January 22, 2026, [https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2023.1179301/full](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2023.1179301/full)  
36. A topological classifier to characterize brain states: When shape matters more than variance, accessed on January 22, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC10545107/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10545107/)  
37. Wavelet Scattering \- MATLAB & Simulink \- MathWorks, accessed on January 22, 2026, [https://www.mathworks.com/help/wavelet/ug/wavelet-scattering.html](https://www.mathworks.com/help/wavelet/ug/wavelet-scattering.html)  
38. Facial Emotion Recognition Using Wavelet Scattering Transform And Deep Learning Techniques \- IEEE Xplore, accessed on January 22, 2026, [https://ieeexplore.ieee.org/document/10862901/](https://ieeexplore.ieee.org/document/10862901/)  
39. time frequency \- Wavelet Scattering explanation? \- Signal Processing Stack Exchange, accessed on January 22, 2026, [https://dsp.stackexchange.com/questions/78512/wavelet-scattering-explanation](https://dsp.stackexchange.com/questions/78512/wavelet-scattering-explanation)  
40. Wavelet decomposition and neural networks: a potent combination for short term wind speed and power forecasting \- Frontiers, accessed on January 22, 2026, [https://www.frontiersin.org/journals/energy-research/articles/10.3389/fenrg.2024.1277464/full](https://www.frontiersin.org/journals/energy-research/articles/10.3389/fenrg.2024.1277464/full)  
41. Wavelet Scattering Transform based Doppler signal classification \- PubMed, accessed on January 22, 2026, [https://pubmed.ncbi.nlm.nih.gov/37913613/](https://pubmed.ncbi.nlm.nih.gov/37913613/)  
42. Spectral Evolution and Invariance in Linear-width Neural Networks \- NeurIPS, accessed on January 22, 2026, [https://proceedings.neurips.cc/paper\_files/paper/2023/file/41ed4bd197d0a5fa036d361c1fc606ad-Paper-Conference.pdf](https://proceedings.neurips.cc/paper_files/paper/2023/file/41ed4bd197d0a5fa036d361c1fc606ad-Paper-Conference.pdf)  
43. Effective Methods of Categorical Data Encoding for Artificial Intelligence Algorithms \- MDPI, accessed on January 22, 2026, [https://www.mdpi.com/2227-7390/12/16/2553](https://www.mdpi.com/2227-7390/12/16/2553)  
44. Sentry: Authenticating Machine Learning Artifacts on the Fly \- arXiv, accessed on January 22, 2026, [https://arxiv.org/html/2510.00554v1](https://arxiv.org/html/2510.00554v1)  
45. Secure Multi-Party Computation: Theory, Practice and Applications | Request PDF, accessed on January 22, 2026, [https://www.researchgate.net/publication/328312001\_Secure\_Multi-Party\_Computation\_Theory\_Practice\_and\_Applications](https://www.researchgate.net/publication/328312001_Secure_Multi-Party_Computation_Theory_Practice_and_Applications)  
46. Preserving Differential Privacy in Degree-Correlation based Graph Generation \- PMC, accessed on January 22, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC3979555/](https://pmc.ncbi.nlm.nih.gov/articles/PMC3979555/)  
47. Towards Global-level Mechanistic Interpretability: A Perspective of Modular Circuits of Large Language Models | OpenReview, accessed on January 22, 2026, [https://openreview.net/forum?id=do5vVfKEXZ](https://openreview.net/forum?id=do5vVfKEXZ)  
48. On Layer Normalizations and Residual Connections in Transformers \- OpenReview, accessed on January 22, 2026, [https://openreview.net/attachment?id=oDDqFpK5Ru1\&name=pdf](https://openreview.net/attachment?id=oDDqFpK5Ru1&name=pdf)  
49. Peri-LN: Revisiting Layer Normalization in the Transformer Architecture \- arXiv, accessed on January 22, 2026, [https://arxiv.org/html/2502.02732v1](https://arxiv.org/html/2502.02732v1)  
50. Beyond Standard MoE: Mixture of Latent Experts for Resource-Efficient Language Models, accessed on January 22, 2026, [https://arxiv.org/html/2503.23100v1](https://arxiv.org/html/2503.23100v1)  
51. Mixture of Experts Provably Detect and Learn the Latent Cluster Structure in Gradient-Based Learning | OpenReview, accessed on January 22, 2026, [https://openreview.net/forum?id=2xmOEbpYv1](https://openreview.net/forum?id=2xmOEbpYv1)  
52. Compositional Neural Network Verification via Assume-Guarantee Reasoning, accessed on January 22, 2026, [https://openreview.net/forum?id=WbpXT0WL9S](https://openreview.net/forum?id=WbpXT0WL9S)  
53. Physics-Informed Neural Network Lyapunov Functions: PDE Characterization, Learning, and Verification \- arXiv, accessed on January 22, 2026, [https://arxiv.org/html/2312.09131v4](https://arxiv.org/html/2312.09131v4)  
54. Compositional Neural Network Verification via Assume-Guarantee Reasoning \- ROARS Lab @ GMU, accessed on January 22, 2026, [https://roars.dev/pubs/duong2025compositional.pdf](https://roars.dev/pubs/duong2025compositional.pdf)  
55. accessed on January 22, 2026, [https://patricknicolas.substack.com/p/exploring-simplicial-complexes-for\#:\~:text=The%20Hodge%20Laplacian%20plays%20a,topological%20structure%20of%20the%20data.%20.](https://patricknicolas.substack.com/p/exploring-simplicial-complexes-for#:~:text=The%20Hodge%20Laplacian%20plays%20a,topological%20structure%20of%20the%20data.%20.)  
56. Hodge-Aware Learning on Simplicial Complexes \- OpenReview, accessed on January 22, 2026, [https://openreview.net/forum?id=QSJKrO1Qpy\&referrer=%5Bthe%20profile%20of%20Elvin%20Isufi%5D(%2Fprofile%3Fid%3D\~Elvin\_Isufi1)](https://openreview.net/forum?id=QSJKrO1Qpy&referrer=%5Bthe+profile+of+Elvin+Isufi%5D\(/profile?id%3D~Elvin_Isufi1\))  
57. Curing Semantic Drift: A Dynamic Approach to Grounding Generation in Large Vision-Language Models \- arXiv, accessed on January 22, 2026, [https://arxiv.org/html/2506.21509v3](https://arxiv.org/html/2506.21509v3)  
58. Architecting Thought: A Case Study in Cross-Model Validation of Declarative Prompts\! I Created/Discovered a completely new prompting method that worked zero shot on all frontier Models. Verifiable Prompts included \- Reddit, accessed on January 22, 2026, [https://www.reddit.com/r/artificial/comments/1m0i8bi/architecting\_thought\_a\_case\_study\_in\_crossmodel/](https://www.reddit.com/r/artificial/comments/1m0i8bi/architecting_thought_a_case_study_in_crossmodel/)  
59. Characterizing Dynamical Stability of Stochastic Gradient Descent in Overparameterized Learning, accessed on January 22, 2026, [https://www.jmlr.org/papers/volume26/24-1547/24-1547.pdf](https://www.jmlr.org/papers/volume26/24-1547/24-1547.pdf)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAYCAYAAAAcYhYyAAABSklEQVR4Xt3TzStEURjH8UdeUkNIkSzEQik7K0VK8rIYifwPkpUFG2wke3sLCRtbZGep2JNS2FjI0oLy8v3NOcO5d9Scu51ffZrufZ4595znzphVbKrQiuZ0ITbr+MA3tlK1TBnDJ6bThSxZxTN60oXY1OMEF2hIluLTiQdsoxcz6AgbYqJ5fOERm1jAHWbDpnLRPDTUueDenmU4Xg2OrfQLWkQ707Em8WKuT/0lKc5jJ7jXgivco93fU107/jcDeLPk+fvwiiNzT27EOYaCnkS0yJP/LGYJ7xj211r00tyuB7GPUV8rpBu39veULtxgxdz/SdEuNY9xTOAMy75WiBoXcY1dcwtoJ9VBj+ahB2kB9TehNqj/Rr9aDTFd1Bs7xby5Y6wly3EJ55HHAfrNvfboTOHQ3FsaMTePDbSFTeWi49UF1zl/r1LzA712NYJG4DvxAAAAAElFTkSuQmCC>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAYCAYAAADzoH0MAAABPUlEQVR4Xt3UvytGURzH8Y9QBkQGySAGpWwGJT8WRk/ijyBZMRkk2U0Wg8lAmch4y8hOSmExGQ2UH+/vPfe651xyj5FPvXp67jnP6fv93tMj/avUoQNt5YWYrOEF79gsrUVnEq+olRdis4oH9JUXYtKEYyRoDpfi0o1bbKEfM+jyN1TF+n/DHTawgGvM+pt+ivVvA5zznu0psqUGHOrrZjvAKrJWWrEsV9243J35TN7/tvesHee4kXsrBxhGI3YwVWyVhvCksN8BPGIfEzhRUd20XMVWeRo74D77zLOEZ4xhXmF7doBVZ1Wm6cUVRrPvPbjEilyvNuBE4QH5bNLYpkVcYFfux1ZBfbZeeUAeu42dcoPyY7NJFB5whpZ8Q1UGcaqiZ5uJ/8YqYy3aHVjHCI7k5vTr2B/Ndy3+9XwAE3k2gglq8xQAAAAASUVORK5CYII=>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAYCAYAAADzoH0MAAABEklEQVR4XuXTsUtCURTH8SMWCDoUDSEOkYPY7FqbS0uE/gdOIq3V1CTS3t7g1NIW0equQ1NFEJSLk6NDRdn38N6F+64+36VRf/BB3r3nHe55XEWWKilsYcPd8MkFvjBFx9nzThU/OHI3fHOOEYruhk8yuEcPueiWXwp4xyVKOEbeLkiKzv+LD7TRxCtqdtGi6Pz6AevWWlc8R1rDrcwWawM9kRkli4bMuSdm/itrbRN9vKGMG9zhSeZ8mwomEp13D2MJXtQTarTuUWIaDMNfkxN84sBai22wixfsh887eMaZBP8Pk9gGWtTCANcSvKwnSNtFsqCBid7Gbay7G2ESGyTl3w30ZKd4wLcEd+YwUrHi+QONgzBTOGZQnQAAAABJRU5ErkJggg==>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAYCAYAAADzoH0MAAABPklEQVR4Xu3TvyuFURzH8Y9QxEAG6ZIoZKKMuElWEln8BcJMlAySVQabwWSx2gx2RkVKYTFZlIHy4/19znncc88tziyfenV7zvne536/z3mu9KdShRY0xRsp2cAbPrEd7SVnAu+YijdSs4pHdMcbKanDCc7QWL6VlgLusINeTKMtLPgtNv8H7rGFBdxgJiz6KTa/PcDZYO1QiSPV4FiVxXYD68hGaZc73n0U5d6Z7+Tz7wVrzTjHLQaxiXr0yI02XyqVhvCi8nn78YQjuQf6jAG/Z52cosFfZzd48J95lvGKUbnCYdT6PevUjtyOPksXrjHirztxhRVFs5IOXCp6W61oERc4kPuydVAdFsl1sIs5Vd44i7XUqlKrYWxtHeP+2h6mnV5S7NeWMCl3pH1Y8+tJGZN7yeyvnrNu/uPzBZZ9NK4R4TMMAAAAAElFTkSuQmCC>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAYCAYAAAA20uedAAAAjUlEQVR4XmNgGOQgCYh3A7EwugQHEG+FYhAbBcgA8RMgbkUW5AFiSSAOBeLfQBwBxOJAzAqSjAfiWUB8H4h/AvFSIJ4ExMogSRAg3T4YcAHiX1AaA1QB8XMgVkKXgNm3B4i5GSCu7GKAWMUgAsRXGRD2BQFxARAzgjggohGI7wDxSigb7EdkIADFQxQAAFlmF1Xx4IiWAAAAAElFTkSuQmCC>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAYCAYAAACIhL/AAAABOUlEQVR4Xu2VoUsEQRSHn0EQNAiKIpi8P0DE4D9wKIgWUbAJl4wmBZtBELmkTTAaTCaTNqNZMAgW0WYzqEG/t7PHzQ3rOHM6l+aDjx3ezMBvmbezIplMxmYG592iTQOvcMSdSMgcbuMtfuFO53SbAbws1XEsTZx2iwFowGVcxDfxBJzEJ9x3JwI5xlm3GIHurQw4hBO4hp+4juPYby8KIFnADTzBR3zHMzzCmr0ogGQBlb/2n5I0YEz/6QtoS7ie4kJFXW+EvmKnH2/AOn6Uz99YFdMSrvd4UVE/wOFipx9vwF18wSl3IoJkR9zqv2scFPP1Hoo59hiSBRzFO2n33wpuSVjf2PxXQD3NDjTIHj7geTmOvQOVbgNu4rOY31zLV7zBMWtd0cghzfwT3QbsGUtirpVMJtNLvgGa/0N02JYAFwAAAABJRU5ErkJggg==>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAZCAYAAADnstS2AAAA1UlEQVR4XuWSMQ4BQRSGn6CQSNBodAqVWqFWSHQ0buAGtHsId9CoZY9AXEIhRCUKlQT/78mamZ2MLSW+5GveezM7+8+I/CTVt18pwCm8whUs220/M3iHPbfhow3PcA5zTi9FCcZwBxt2y88EPuDYbfhowiNciP54EA4sRRdwYRAmcRA9Co8UJPPwAG5gVzQRJsOEUgzhHnZEM2bWzJzZW3DwAkdGrS96m7zVBA7cRN+GeWs1uIVrWGGhBU8wgsVk7EMkuju/8tqJO+SNARPW65LxFf4PT2iSIiw4VL5QAAAAAElFTkSuQmCC>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACIAAAAVCAYAAAAjODzXAAAB7klEQVR4Xu2VMUiVURTHT1RQ2CPLtMEgEjSI0EESVFwiKAgdbBF0chGUBpdEcHgiboII4iCKkwpq1BAmBgkmVLqJgzg5iOIkDk6C+vu/cx9+75t0+R5Bf/jx3nfPvd85555z72f2X/+ICgN51S34BCewCPdyzcmrB87gTdyQtF7CEYzCjZgtUd2FJdiF0lxT8uqAc2iJG5JWGRzArHkT501yvmAejILKm3Ri9s3LozLlRe/hL9SZN6waVw2cqJphD2rMj66OsI6yjnRiUhDH8CEy9s78ctMlJxXDCHyESpiAafM+aofv0AW3w3zpBUxBP7yGh2G8AHphHt6GsYzzU/MrPnqJPYAN+AP3oQ0aYMd8jeYqyC14CkXwE6q0GDXBZ/PPxSvYNg9ah0G9p/m1sK7JFXAIacvNJKu0+a5od8rD77L5yxWIsm0Nc+Xkl/lFqMBXw3xJB0A7pp1QzylwSQHpHZmXKfObwRCXxkvs8iOoHRgM/7XuB1SHZ12AM+YZa2wTngRbdF1W8USuLDmYM99ySc7W4FHEpmBUwkb4ap6AdkBfdK3rNK/CF6iH3+Zlu5Yewwo8C89yqoyUmQKZhCHzxk3BOHTDMHyDsbDmufmFOWBe5j67puRQNc5KzqOfAJVRAUSlZ43H194JSKkL/9ZM+ryyT7wAAAAASUVORK5CYII=>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAYCAYAAADtaU2/AAAB+UlEQVR4Xu2VTSgFURTHj3xEvhIlyYJslLIgUoSSWLCwslFSiB0WQupRNhYKyUdKsrVQshALZWdvaUHKiqIoSfz/7848d6478+a9suJXv3jnzpt755wz54n8kxzZMMUM/jbFcAVmmQthKYFzcBvOw0rvsi99cMwMhqUensJmWAOP4SeclOAUpsE1WGUuhIEpOoSDMNWJFcJL+AJrnZgNbrgh6gAJwxTfwGdRT+syI+qpJ7SYCVPMVCdFuqjmOBF1CJcpURvzrw1mageWG/E82AXLnM+8fx3sFtWIgTB1B/ADtnqXYjTCJfH2QA7cEtWcd7AfHsFhOAufYHvsagsNourLDueJbfBGnUaMn0dElYylO4P5zppbUr8MRi/kF/ZFDQYbBXAPFhnxUVGb9sJ32KatsREfxKdn+HSbcFmCBwLTFTGDGqvwWrw17YFvsEmLRXE3nZbv14qn7IhdoWBNWVvW2EYuvBDVI/prZjtM9GYcFuPO/y6sF9OmUwp3RTWSDVtKee25GIfhRgPwVVQn3mo+ys/UxBuRbn3179kOE+s2vrOm97Di+9LoaddhtRYzicAr8Taeb33DwkNwNgeNyEz5WYZFsdQ3EYYk8RFprW8i+I3IeDBLLBkbNSlY1wUJ/pm0wWnGURn0KxcI3+cWMxgCHjTDDP49vgCCLleCtdiD+QAAAABJRU5ErkJggg==>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAVCAYAAACUhcTwAAAAwklEQVR4XmNgGAWkAD4g9gRiWSifFYhNgNgXiMVBAjxAPBOIG4H4CRDHAvFmIE4D4mog/ghS5AHE6UCsD8SfgHgPEPODJIBAEogfghiZUAVBQPwbiB2hCkBAE4jfIvEZJgHxXQaoG6DAD4h/wji8QHwYiNcAMQtMkAGhEQxgxhbBpSEeOsAA0QgGMPfYwAQYsGhsAOKrQCwCE2BAuAeukYMBYjwyaGXA9AgKQHYPskdQgBIQP2eABDJOAIoFUHQYgzgA4GIhbQeE0SYAAAAASUVORK5CYII=>

[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACoAAAAYCAYAAACMcW/9AAACl0lEQVR4Xu2WTahNURTHl3xESKInUT4ykYEkJB8DoQwYmDJQ8jFQQiijJxm8gYkoQkg+UxgQI0+GRoooKUZGJopigP+vvfe1rbvPPedengzer369c/Y+75591l5rnWM2zP/PaDnJDzZgghzrB4cKFnhWLvUTDZglb8e/RabKp/JH5je5NrtmjLzurjmUzcMoeVruduPdsEretZod2WhhAZf9RGSkvCaPWNhezzo5aDU3qWGEPCUP+4mcxfKzhfATHc8yeUWO8xMWxh7KPX6iB5bLV3KOn0jMlR8sRIXEzmEhl+QiN57gId/I+X6iBybLZ3KLn0hMk2/lezndzW2VRy1sTYldFvJ8op+IkCqroxyTRjzcynjsOS+vWsX9iOKg/Gi/R2a2vCP7sjEPeV2V21Qx/79TnpRP5Dl5UD6SJ35d2oIcrXxw8pL8/CKXxDGeaEBuShcVSA943I0DKXNGzovnqQ76LXSV7/KitUeOwi7tbAtCTuVzIdAuqMJSlSfSQkuVygL3Zecb5FcLWz7eQpRnZvMJ7k+9UDdFuBkL3W+hzdA7UzSq6LRQD1F/J2e4cQ8L/SQX+onEZgsL5QdZLEVSR9OFpuuq2l9O7danvKGP0TN9myqRcpu08bCtNyy8DChQCjV/oB1yfXaeoDXRgehERVKyIw2+KVTzfWv/qGBX2KHtcls8TvlPNyAYU+J5Dm+/0u+1INSE/Ji1V2In6AovLHw35FA0zy30RKqb330pL8h7Vn5BpB3qmEpU9woLFdkNvO5eW1iYh/QhaunB/bmH3yL1eJX+dbgp0aKVVS2gKbwFb1rnlvhHUDiP5QI/0QVE+oH19j3bFdzglvX2qcdO9MsD8XjIWSP3+sEG0KZ4U/2TRQ7zE7B6cVogv93mAAAAAElFTkSuQmCC>

[image12]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAE0AAAAZCAYAAAB0FqNRAAAD3ElEQVR4Xu2YTahVVRTHV1SPpEyykCRDn0RiURn1bNQg09CBGhkhWZMGNQkUg9I+QFEHJYZlgURRIeUgsYIyqKgHgYaB1EAHSUgQNoogcGKI/X9v3f06d9297z3nPj9Q7w/+8O5eZ9+799prr7XOMyszW9olPRQNA8q8IJ2WPpOGgm1AgRulV6Rbo2HAmedy6TrpsmjowZXSlDh4KcDGt0iPREMNmLvd+pt7XnhVOmmew5LeaHvC7ImKDX0tXdv2hNlz0uvWPMoS10v7pPnRcB6YI70mvSM9Lk1qNzvTpd9b4u8cj0nfSdOiQdwu/SQNR0NDFpsfyDXRcA5ZIR2R5pmvY5P0jWXSB8ZR6U/zdiPChE/MnRMhst5qqd8oS/A7+6WV0TBByLWT42CGm6Wj0qrKGDmagHi2MjbGFdIe6YR0T7DBM9LaONjiJulXaWE09Al5kbWwponCtXpK+ll6NNhy4KzoAwLhI/Og6rgB75rnq6Vh/BZpr3nOyYGzfpNmREMLTplF0Chfbb4IWplFls8VS8zTROn76kC+fVn6UXrYvNDU4U3rdBp8aIVbmBpaoirBj+0032AJ5o1a5hTMr9vH5lH6kvSLeZUkmt6TPpWuGn/aYcF/SCNhvA4c7FbpB2mB+YE1AeeUnJYbHwtNnPZiZQxnscluV4UvzF0nImqzdH/rcyo2u6U7pb8s7+z0XIz4bjCHnPq9dJ/1l1tTXs85p+g0rgVO4wHg1NjgrPRAAZ5Pc6pMNb8iKZLukv4xPxwi+EnptpatSnJaNRmXGDaP2K/MD6IfZyVIHd9a3jlFpzGAgYl4fZ15f9aLktMiuSSbIzmtVHgSbPJ98/XSV50JSs4pjY8lXnIJ5fVB6QPLJ+pIHacRAWyQ76aEd6Pp9axGW79XM0GuzTmH/eGbjuJ0g3RY+ts8N9zdbi7CD3HanHwVisAO6Wn7/7txXNoU+RJbhAp13DxdNAFnvy0dsP6KACyTTll7+0R6+bKlWLTGEyF5bb3VPzGqLQ7BMVVSjtwmPSD9a15pAYdyerQzkRHzFmZuNNSk2m4st2bOI48flDZUxlgjUVZsuNkIk5hcF0KZLjpukog5ZN4Yfi6tMX+Oq8Q7JtGQg9w3ap1VtSlE/mrzNbDhur3avdIx6XnzhpiUwvt5cf4d0sw42AOihlPNVTvCmXfVdNrxc4S2hYq9IYxPBDaL0zi0uuBwmnEaY16tzgpUWaKnTuHoBleBA8hd24sOrtIX1v3NoRfk0I3m16JuPr3g4VqTu5pe7wRvDrxZdPwL5mKHYkC0DEVDD/hPCa3LJeewAQPy/AeNC6+PmRpEBgAAAABJRU5ErkJggg==>

[image13]: <data:image/png;base64,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>

[image14]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFEAAAAYCAYAAACC2BGSAAAEUklEQVR4Xu2YWahVVRjHv8giMTEHMtEww1DT0qjUJFOoyIEiRSjIB0ErnJ6KgkpwyAcFg0QzaKKHilLQ0FRU5EpRUU8JDaSCE/YYZPoghP1/d+3l2fu7a9+9zzngxP3Dn3Pv+vZewzevbdaDHlzruFHsL97gBdcp+ok3+cF2wGRrxblecAUwS7zdD9YEDoAz1MFE8TMLyqzEXeLzftDhFfEdu/JeOFJ8X+ztBTXA3jnHj+IwJyvDfAvrJT1yjLhEPCj+J35aFBcwVvxZHOEFlxko4S3xSS+oAd59TfxKfEH8VhxeeCINjLXTSiIQJT4rThFPW7kSWXxTxmvZC8eLb1rDox62YJA6oU2Ufm/dhPUQ8YSVK3Go+Kf4hBdcZmDAddaaF7aLu8Wj4qNeEFGlRJR3zNI5BKs+Jj5oRYtyYKp4HSvXBSmFaEjmpgrcKc4UB7rxW8Rb3VgKfcQD4hteEFGlxNfFDuu6GK5N5XpV/E1cmJNNF/8WH8mNtQOMsl6c6gU1QC7jbHjxL9ZQJArcLn5p9YzNHJw3mdKqlMj4NrGXG3/ZQoIm3I+LK3MyWiHybMp7yzBA3CueTPAv8ax4yo2v6HyzHLRBH1tQHM5wxhrFhBBl3lLvcihzpk7UUaKXoVAOwLsk3fPW8Dos/E1G/gb3Z88lrVgB1nrXWvPqh8RFFqKGtuYLazgDaepC9hvxeMYUUCIdCmmqC1pRYgQbYmNsMFaulIUXiy/l/m8G5NsN1jUSmgEGwND5XthHC/MzVla4UCK1YbAXgHaUGEOZxSNI4PSdzVZzvJSwYz+RFARamqfceORtnW9WAwVgWAwMYqHIR0sV2gpnFMSCLOyBl5wTn86N8XzcMO+sEj+wbnqsDFRdQmlejngzB33OjUdO6nyzGpytwxoKiNESjX+H+J642sqrf3d6uKTEsspDAflVHOQFFhrYf6yhRJI2PWW08BxxgrjHms9phNdmcZwXtIAPraFEzsjNJUYL/y+wcBYa6tQthmfQz0YvYAJyApNdzPiveFi8L/cc3nbEwg3HA6ttEX8XPxL/sDAPrg/uESeL+60kIXcD2pm3LW3YZkGB4ax0GTssFJTjFtIRxmKfz1i4EqZyL3v/ycIzLSFWNtoZD1wbRZKbaCfwvHylBiszNgPmpLGmwW4X9IB9LcxJUSDyOqxYqfn93Mo/wnAeHGWEFzQDvmTstuKd9QELDTWhAgiVfRYu6/E5UsB3FrxxaW68ClRI7rXteiHKIVJIOYQrwJvI46wRQZThKKQOuoj8uvy9JmNb+0FBu6y4MFWY8J9tQTl8JsPl8w021ZZkzAbq3jaYi4o80gtaQKzCWy1EFB8dyNnLrKiQURa+ZlFYRufGAftgjlSubBpM8nX2C9gg/dsPFqy43NKeRhglK1oJplv9W0QdTBMPWfj0RT68tyi+BAqhb3fY+ydW8hmsVeD2tCw3e8F1ihfFGX6wBz24evA/pI/H3KHvbWYAAAAASUVORK5CYII=>

[image15]: <data:image/png;base64,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>

[image16]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAC8AAAAYCAYAAABqWKS5AAADEUlEQVR4Xu2WS6iNURTHlzwi77zyvmTiUZSQYuJViIQi1B1KGGCgKF0DQ/IayCOvJCEpkUe6USgDIymPYkIpSVEMPP6/u799zv722d+5p3OupO6/fp1z9vrO/tZee621t1mn/m91FQNFl9jQoP7WvCV1F/vEytiQ0CCxSKwQTVZ2ivEh2fdQ2HeIbdn3DheTH7DiyRmfJ16Ij+KUuf9cFRfEVPFATPR/iERwzolVsaFRTRZPxbjYkKm3OC2+inXm0iDUBvFTPBR9I1uoKeKxGB0b6hURPZqRinp/cUt8FjMjm9dg8Vwcjg2RuomLoiUar1sjxUuxIDaYW8xB8UusiWyh+ohWq61e1pvbZQo4J17WZC6/UmL752efXjj9RowKxrzmih/mHMPBImG7bMX5HoraeCdmxIaF4rYVv2i3+C02BmM7Le2c32KeJ1rVRNCIZFwLKQ0353xul3qJS2JWOBiJVdMptgdjZ8UVc86GIp3eik9WW0RrlU8xglbSbHHIyk4QDSK2vPSEE11jcfAb5yHWdPHNCvKzHVHkm7LPWN55zpSStli+6IaZy+XwIRZ2RIwPxtpzvtUqUyoUQdojJgRj7DDdK/U/7/zJcBCneKEX39+b2xEvXnBc9AzGipxngR+sfeeZ85i5tK1FybQhHcIUobWx5f64pgPxkrWlJ5zYmXuW70CIBV4z1985XFJizv1W7v/sAleGm2KafygSKYhfYd21HRBEisET4ru5/nxfbBbPxB2rjCKdhwOGgyYWTuH8eatcXD9zuxh2DQqbetplxQcRLZl0zp0r/kW0ti9iqbm7B7/hkaV7Oen1yoo7Cv34tbkuRUNoFmfEXTGp/Fibhoox5iI/J7J5MU6w6GY5sdUUanhIDTB322NLU6IjPLHqvZz+zeJWi2VihBXPR42xsFSnQS3mzo+4NdctLlZEq9aiqybSl2JcYpW1QhBJY07uDhN1cMPcCd2oKGA631ar3B2CRNMour7UrbHievbZiHCYa3HsOC2V22mj8xeKvN4resSGBsViaMmphtGpf6Y/oGh+HBKfXDcAAAAASUVORK5CYII=>

[image17]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABMAAAAZCAYAAADTyxWqAAABWElEQVR4Xu3UzStFQRjH8UdShIQSRa6XDf4CIpIFO8WOspDYskKSjaWFlY28rVhaSFkJsfAfsFJiL1lQ+D5m7jX36RzHSzbyq0/33HnOmZlmzhyR/5AidGEQTcj17YWo9teJacYZ7rGDKWzhAC3YR0/m7pjkYQ6PmEZBdlk6cIdrSZiZdrSCJwyYWjr52PP0OjYTeMEMckwtzCZmbWOYRtzgEjWmZrMqCeu1IG5Wi6Y9KiXiliQyuv2HeJaEET+TKlzhFvWmlhSd4ZgEO/srnSm9/ii6423Bf+1ENyTzXCnOJbmzcqyhwhZslsRtQK8t+Oh7p0cqfJnbsYu+oO0ttbjAESpNTY/UPCbl/WXW2Q2L61zPbvoDkEkKp3jABkawjGN0S/apKBM36DqGgvas6AMp9HsNEjGqTx1O/O+PMy5uZq3oNLUvZxTb4j4M9lP1rRRL/DL81bwC0xc1ydUmoRMAAAAASUVORK5CYII=>

[image18]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAAiCAYAAADiWIUQAAADMElEQVR4Xu3dv8scRRgH8BGjGJDEgJgoVkEiYlBBE0knkkILUwQhgnZ2NoKF4h9gYSGoWAXFJI1Ngo1iYZGXNArWNpoUio0pFEEtBH88zzu73u68d5c37114fc/PB77c7szu3DupHmZ2L6UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAf8LNg+NbBsc7ySrMAQDYJlk8XIm8FPkqcinyQNf3YuSnyN+Rq93xr5EDXf/Qk6Ve80HkQuThUsdahkcHx88MjneSVZgDALANjkW+a9rebc7vjXzatP0cea873hv5LHJ00r3u67JxrK1ahWJnFeYAAGyDNyI/NG0nmvPjpV43tFZqQZbejvw16frXWuRk27hFq1DsrMIcAIBt8Fyp251/lrr9uWfcXW4rdXXtYNOeW6i5Mrer1PufH3ev21fGz20tYlqxkyt7L5f6d6f8O5bpbOTbUsd/OvL+uPu6TZsDAMCm5TNrv5SNRU+urk1bPcvrcrszi5B87i2LsxupLXayUHyt1IIzt3XTsGic9lD/TZG7ZyQL06Ec/67I72Uy/ivd563d5zx5bztmOwcAgGvK1a8sYnpPlY3FWRZFbdvuyG+lFiCZtcjtwwtKHfe+pm0Rs4qdj0pdaUuvdp9ZbE0riO6InJ6RXEFr5Thflsn4Wbym/M557o98Ujb+m8yaAwDATPms2nAV6IXIN4PzlM+3tS8c5HZov4KV9+cLCIcn3eveas57ed+zc/L45NKRWcVOFo69LNhy+/LjyIeD9q3K7+y/q19ly/F/jDzUnc+S9ynYAICFXSj1xYH8zBcHTpXxilv+REduff4R+b7Un/OYVggdiVyOvBM5E/l81Lscs4qdN0v9GZH+O3NV7PykeyFZXGbBmuM/1rXl+P2LFLmN3K7U9RRsAMBS5JZlFiVZjDwx7rpuub2aK2T3lHHRtyzzip39ZbLid2fk4qBvUVl05fi9HL//jbp5FGwAwP/OZoudB0t9pi6fx7sRcvzX28ZGPiv3ReRc5JFB+2bnAACwIx0aHOf/oLATrcIcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuLZ/AM5mbRUICV1qAAAAAElFTkSuQmCC>

[image19]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAXCAYAAADduLXGAAAA4UlEQVR4XuXSoYpCQRTG8SMquKigGA0iirDNBzBqsrnR4AtYtBjFKJpsxu2iGOyC0bppk0Fs+wIK6v/cOwMy94p1wQ9+cOfMwJk5XJF/mQhyyLgbbsY444a+sxeaFi6ouRthmeGAvFMPJI0dNkg4e4F84g8Ds9bHVtDAhz1k08YVdcQxwgRrCXmwvW8JQ1TFPxSYThZ7/GAu/pU0eo0ekmbt5XFkZfxiJU8e6o7sW/xO2rGJjqlLClssEDM1PaxrncIURVOXAk7o2gL5whFLU9cxetEPbRe1BRPt+PKHet/cAcfeIy832IBiAAAAAElFTkSuQmCC>

[image20]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAYCAYAAAC4CK7hAAADOklEQVR4Xu2XS8hNURTHl1DklYiIPEJ5FPKI8k4eAxIGRN/AABMmSIxupBgQIiUlAyQGJigUxUAokVchkQihDAwo/P937XW/fdY55z6+73xMvn/9Ovfude7ee6299tr7irSrTTQG7AZ7w+f/qu6gi2+sQ2PBOdATjAQvwfTI3tJ+y+oDFoCVYDTomDSnNAGcBL28oQ5NA2/AFDAgfF4T2YeAC+FZlzqAWeAuuCLaGbkKXogOlKVB4IZoZFurReChaJ+xZoKLUkegOoN94LWkJ0zbcfANTHQ2On8QlFx7o2IGML0eg7nORnGcI2C7N8TiRI+Br2Cqs5mYXl9EO2OnpnHgeXgWof7gAVjhDaL75hkY5g2mjeB3eOapN7gHnoC+UTsjdElasRmhUWC5aEC5sW9Kdp82h3j/VDQCvBf1lNHIk3XCjcgNSXEgDrjTXorE4jADTAqfuYpDwTJJF4/D4JXo+D3ArdCWpRPgtCSzoqwS+AP2uHav4eCDJB2xCrPEXoq0CewCT0XHOCp6TjSJltf90jyZyaKTWwg2izriN7uJGUA7Ha7IlpFpNT82ZIh2vhd3wmh/FI18LEb2EOgn2j+LRLz3ToV2jm9iWvF3/E21Us+gxcEsyyLKTczlriYuNVeuFLXRkbfhGYsRXi0a1Xei1dCib+l4HXQLbY2IjjAzmCEVmSMpD50Gi54jnyV5VuQ5YuIq/gxPEysOnauVynmiI9/B+LiR1YdVqJojjOQO0dXY4my1HGER8NFbBX5I8grSiDJTqxM4C35JOs9NzG3mOA9E5nEsTpAVb7Frp7JSyMa7I3pCrwOzg61esfRahUuIJzUnynuSn+g88AkcAF2djbIV3eAN0rw/4hSyVOZKcVOzlNa8cjjxt1lnTFm8krAk8o5l9yvetR6JOpOq2UFsZwCyaj5ThwGaE7UxUGfAfXBNtCg0Iq4oL49VrykseaxcvO0yDwdKvgOxmPMMAA/MWOyPbb4Pfue9KjOiNcRCwYO7pfurqjip26K31rbWWtGLpd8ChWkpOC/Z+6goMWCXJf9SW4iYLtsCPpWKEPssiZb/tug/IS73VtF/e0WL/1TXyz9wol1F6C9eMJDIlY1HJgAAAABJRU5ErkJggg==>

[image21]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADsAAAAYCAYAAABEHYUrAAACa0lEQVR4Xu2Wz6tNURTHv0L5USQ/3hMGZED5McB7vXoTMiBlIEkxeDMTpRRloM7UBEUpTLyJSM+AAaZKMjLiH5B6vSRlwgDf79t7v7v2urd7zzlyS+1Pfevevfbdt7XX+q5zgEKh8D9zkJqjfke9oJab+CrqlYlLM9RKs+dfs456jc7/f6V2ZTuAyzGW9Inane2ILKLuUj+pH9REHp7nBPUE+UUMm+PUN4Rkqjw0z2bqDbXDByxrqAfUBYSDbiNcgOUidcatDZuKOodQtY/USBYF9lL3qCVuPUObblAbEQ7RYVtNXD/WIdpXhy3UUr9okAXW+sUB6Df3EaqnYqgop7MdoRgqSl+0STcmKoSDzi9Eg2dUeXVAHc5SN9E74VHqKTXmAwPYhnDhyxBsJrv5+XKNmjTfe3Kd2hc/y/gaAG+p1XFNB9yKn+sgC+iy9BubcNtExVHqUvysBJWonS8qxCN0t3ZG8quqJ9SyD6lf1JG4pqo39atP+G8SFRV12HxXC9v5spO6g5p+tQNJSSpZJa1bbOJXS0r4MfUM7RNNft1k1lRBO18a+zWh9lUbq50PoZlfPRpW76lp9PZwHaxfLRU682WgX3XzarMDPoAwZHTQB4SD2qDJKW+NU1Po9nBd9Hy94hfJduozNUu9RMeKPfF+taQ2UcJN/SpSoql1dbFTaJdwhdyvCZ2ZHkN64enrV7WoXv1W+ECkor4gmL8JSvQ5td+tt0l4PULV9vhAJD2GvBUX0C19R+c9UpuPZTsCegypOk39ehXdiSaU8EnqlA84NlDvkL/v6pIW200IA1QF6+vXQqFQKBSGxB/OY3eLVpg/TgAAAABJRU5ErkJggg==>

[image22]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAF4AAAAYCAYAAABz00ofAAAFFUlEQVR4Xu2YW8imUxTHl5xPOc7IKdEMOYQalOOFCIkLLihzpUQOiQnJNL0zQ3IoZ3LOBcohLpwVXzPTjDEXSkSkPhK5kFy4QA7/X+vd8+5nPft53uf5aL536v3Xv+97134Oe6+91n+t/ZhNMcUUWwd2ELePxiGw7xGNcwTP4l190Pv9ew456dhGXCUeEwfMF/y4eFIcmCOuFM+NxjHA8feLF8WBErYTbxZ/E98Sd6sOTxQOFZ8Sdw521vCIeFWwgyPEu8UnxGXi/tXhItjEZ8X94kAH7GPux84BcIv4t3hWHJggXCpeEY3C2eKM1dP8YvFV8TjxdPET8Q8bH5Eni3dGYw+QKe9ZxyAmfX8RHzZP6UnDTuKT4mHBTvS/I14b7ETrWvNASutZJP4gfi0ePLSVcJd4WjT2AAGw3jxQxiItYFY8sDo0ESAwkBNkJccSc0ceWbAjn9/YSDLYgOfFf8TzhrYIrkVmYvb0xR3iK1afbxEUFCbVaae2MK628ryYM5G9e7DjOGQGJ+Yp/5z5Gi/IbDmQiduCjQ1Drs6wUUfFBvGMEzJbDjb2W/GgOFACafyj+KJ13KkthLZihyNhF+wlbhJ/Mi+6EalIx64JB98jrhGfFleIj5kHApLCBseCT8Z9L54Y7EXwYtID50ctnU9Q7OhMYu0hkmfM07oLLhH/Mu/i4rNAqWvi/wfMN50x7qdoJ9CUENmxW+I39qbMqoBCRPEhFUnhScHAyt1WcjyLH4dDxC/Mn1WSBnCZ1ddNEUZ6yDok7TWr3v+gVetIQnI8z2zF+eJG8RTzAkuhjekzH9jXXEqQiYiujsdpb4rXi9uGsYSmrimB4v2zeGNmS+8vFdHk+Pz6Guhr0SOaflKQlpLWMmrdfKBU7BK6OD45HZlJ8kKRPH7zFY6mrikBH/1p1TaztBkJY6WGB/5qVd1isRym0oIWmOvcdeKx5lpHW0Z0XC6+LV5j1RQ8yrwgrhTPFPce2ncVbxVfFs8RHxJXWzm7cBTvpVCVkGoS8ymh6Qh/u9WL3k3ihcGWoyQpXP+7lXt+fINsF9tWnM0uxmKTqv9H5hGz1Pzk95X5PVzLpnxmrp0ckz8wb7kAE6LSE5Es8EvzieAoNJTrKZgfmztl1up9OCgVuwgcQkQjFTlw+sDcMd9lJLNnrSopbV0ToFVF36OklDYjgXUzVlvX4eZt1cDKxWZgHvVE/+Lh33QMxvFMNBUOFsHEOHixCNqu9IGJokhGEOk4kI0CbADP2NE8G0pdBu0a/Xsb2GQCgFqQIx2gaBQiCaq8ZjR1TQnMmejNC2+bvgN8M2OFzwa8hJc3FRvsC210IxGe2jbue99GEoCDXjCfALZPbXRwyO9LiBtXAs9ChpqKXQJZQUaV0r0rllv7/SVfpTNPSd+ZO2ehQbD3Bg96yUYaiHPXmUdZGsP5SBLF5HXzDSPC+VLHfUQuWUY7dqq4wTwduWaZ1aWCFMXxpWjKgVOoEXP9xsQanrH+nwja9H2RuUzz9z8BDfvQPLoATiZiWSiO4TR3r3mhRQ/5BHuDeJ/4hvjo8B5Oi6QmjkK2iDSYakOOpk8EJZBdzO/oONABbV1TG8jiz60ucfhkpdXr5pzAA9DoBJydRyIpGL+V8Bt7vJfITtGdronIT4tdQStM5vWJXOa2yvq3zbuI79oo+HLQhBBcfeYxMTjAPOLjosaBtpVDUlcQEGRmW9fUBBqSGDQ0F2TCVun0Kab4//EvQX3h6oX3DHQAAAAASUVORK5CYII=>

[image23]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAAXCAYAAAAGAx/kAAAA30lEQVR4XmNgGAWkAi0gvgPE/5HwNyC2hcpPRpO7D8RqUDmswBKIfwLxbSCWRBJnB+L1QFwPxNxI4jgBJxDvAOJ/QOwBFWME4lIoBrGJBhEMEOcvB2JWBogB3VA2SUAciK8D8XsgbmaAhA/JhsBAKwPEVYeAmB9NjiTgxQAJpxMMFBikCcT7gPgWA2qgEw1ANq8CYjMoHzmsdGCKCAGQIeuA2BtNvIEBElYgmiBQBOKNQFyILgEENkD8G4hPAbEwmhwcxALxLwZEsv8LxP5I8llQMWT5nUAshKRmFIxsAADUlTDEUF3cxQAAAABJRU5ErkJggg==>

[image24]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAZCAYAAADjRwSLAAAA30lEQVR4Xt3RPwuBURQG8CMpSpSBDBYpsSqlTCYGZovdJ6AYZZfBbvABZDEYjCYx+AAWJovNgud07sm9dzMpp371vuc8b+/9Q/TzKsIUelCGsDsmysOMZLiEF/SdBKoJY/McJAnHPmOpAuwh5w/sisAaNhD3Zk514AkjCHgzSsACVnCAB1TsQBp2JNvmr9skOxtogJsTE9J18AZuMP8qlIUruYfGvz+T9bsGySKr2iD58AItbXDoDiVtkAxPkNJGxjTq5p0PlO+tqwGtGhxJFrqFIYTsgBZfaBKi/uC/6w3fXiTiH3vN/gAAAABJRU5ErkJggg==>

[image25]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAXCAYAAAAC9s/ZAAAA0klEQVR4XmNgGAUg4AfEX4D4PxK+BcRqSGqEgPgEkvxfII5HkgeDHAaI5BogZkGTAwEdID4DxE5AzIgmBwZKQPwciJ8AsSKaHD8QrwJiMzRxFACydTkDxBXRSOLcQDwHiIORxHCCCAZUb7AC8QwgLmPA4Wx0AHI6yAtvgVgbiEuBuI4BYhBRAGTLfAaIKw4C8WQGEjTDAChaQQYcYoAEHslgEhB/A2JTdAligCAQnwbiq0AsgiZHFDAG4q9AvJSByFCHARcgfsaAmpxfQcVHwfAHACMaKLHQXhNhAAAAAElFTkSuQmCC>

[image26]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAYCAYAAADH2bwQAAAAhklEQVR4XmNgGAW4ACsQi0MxiA0HfEA8CYhfA/EGIJ4CxGowSXkgvgXEc4CYEyYIAyBjVgHxEyBWRJMDA00gfgvEv4D4ERKOhCkwBuKvQFwOE0AH+kD8iQGPApCjNjNA3AHzFiMQc8NVAIEEEG8H4oNAPAuIDwNxNRCzICsCAR4GLAE09AEAUHcT0c/fg5IAAAAASUVORK5CYII=>

[image27]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAAVCAYAAAA98QxkAAAAkElEQVR4Xu2VIQqAQBBFx2Y32dRis3oGTyZ2xSCewCoYDIJ4MP/HLZqMMzAPHixMGf7M7oo4juP8IQ6aoYA77GDyqaklghXc4Azzd1k3JVyCPJuBKTPtE9byTMEEKRzEWOO8jCO8YPYu6YLp9vAQ5elyfye4yvN6qGzUzNPGRjlujp3j5xqopoGtGPrlHCdwA077ES7PLLpGAAAAAElFTkSuQmCC>

[image28]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAUCAYAAAD/Rn+7AAAAjklEQVR4Xu2VIQqAQBBFx2Y32dRis3oGTyZ2xSCewCoYDIJ4MP9HyxotfmQfPFiYMvzZ2TXzeDz/ILyVJYMrbGD0qMkQwAIucISpW9Yih9Mtz7IwRaa5w9KulCWJYWfijXJ5enjAxC19C9Nr4WZi6fH+DXC2a7slGpN9atgYx8cxcpwcqxQVrE34F/G85QSc8hEukkqpGQAAAABJRU5ErkJggg==>

[image29]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAUCAYAAAD/Rn+7AAAApElEQVR4XmNgGAWjYBSMPMANxKzogoMBqAPxaiBeBsSiaHIDBhiB2ByI9wPxFCCWRZUeOMAMxE5AfBiIu4FYGFV64ADIYf5AfAKIa4CYD1V64AAo0UcA8TkgzmeAZIRBBRyB+AEQZwAxJ6rU4AHIoVjGMIiiFx3A0uFphkGWQdABehEjiSo9eADIoXpAvB2I5wKxIqr04AIgx3UBsQq6xCgYrAAAUl0RSCE6RY4AAAAASUVORK5CYII=>