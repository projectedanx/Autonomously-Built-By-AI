# **DRP‑ANALOGY‑MINING‑FRAMEWORKS‑2026: Discovery of Historical Frameworks & Prompt Pattern Archetypes**

## **1\. Executive Summary: The Archaeology of Machine Cognition**

The transition of Large Language Models (LLMs) from stochastic text generators to reasoning engines has not been a linear evolution of model architecture alone; it has been equally defined by the discovery and refinement of symbolic cognitive scaffolds. This research report, designated DRP‑ANALOGY‑MINING‑FRAMEWORKS‑2026, presents a comprehensive excavation of the named frameworks and prompt pattern archetypes that govern modern agentic AI. By analyzing historical corpora, technical papers, and codebases, we identify a phylogenetic tree of cognitive architectures that transform raw next-token prediction into structured, goal-directed behavior.

Our analysis posits that "Prompt Engineering" is a misnomer for what is effectively **Cognitive Architecture Design**. The field has moved beyond simple instruction tuning to the implementation of robust control loops that mimic human metacognition. We observe a convergence between classical decision-making models from operations research—such as the OODA Loop and CRISP-DM—and contemporary agentic patterns like ReAct (Reasoning \+ Acting) and PEER (Plan, Execute, Express, Review). These frameworks act as externalized prefrontal cortices, imposing necessary constraints on the generative capabilities of LLMs to ensure reliability, auditability, and safety.

This report distinguishes between transient "patterns" (e.g., Few-Shot prompting) and enduring "frameworks" (e.g., Reflexion, Voyager). A framework is characterized here as a named, multi-turn control structure with defined roles, stepwise logic, and symbolic delimiters that manage the state of interaction. We meticulously catalog these structures, dissecting their components—from the "Thought-Action-Observation" loops of ReAct to the "Skill Libraries" of Voyager—to provide a definitive registry for agent architects. Furthermore, we analyze the "failure modes" of these systems, identifying anti-patterns like hallucination propagation and infinite looping that arise when cognitive scaffolds fracture under entropy.

The findings suggest that the future of AI interaction lies not in unconstrained conversation, but in the rigorous application of these structural archetypes. As models scale, the value of these frameworks shifts from inducing reasoning (which models increasingly possess natively) to orchestrating autonomy, managing long-term memory, and enabling multi-agent consensus.

## ---

**2\. Foundations of Framework Archaeology**

To rigorously map the landscape of machine reasoning, one must first establish a taxonomy that differentiates between mere heuristics and true cognitive frameworks. The "archaeological" approach adopted here treats prompt structures as artifacts of functional intent—evidence of how engineers have attempted to bridge the gap between human intent and machine execution.

### **2.1 Defining the Unit of Analysis: Frameworks vs. Patterns**

In the chaotic lexicon of AI development, terms are often used interchangeably. For the purpose of this registry, we establish strict definitions based on structural complexity and control flow features identified in the corpus.1

A **Prompt Pattern** is defined as a discrete, repeatable input-output configuration. It is often linear and transactional. For example, "Zero-Shot" or "Few-Shot" prompting are patterns; they dictate how information is presented but do not necessarily impose a control loop or a state machine upon the interaction.4 Patterns are the bricks of prompt engineering.

A **Cognitive Framework**, by contrast, is a composed architecture that orchestrates multiple patterns to achieve a higher-order goal. It acts as a symbolic control structure. Our analysis identifies three invariant requirements for a system to be classified as a framework:

1. **Role Definition**: The model adopts a specific functional stance (e.g., "You are a Controller," "You are a Critic").5  
2. **Stepwise Logic**: The interaction follows a defined sequence of operations (e.g., Plan $\\rightarrow$ Execute $\\rightarrow$ Evaluate) rather than a single generation pass.6  
3. **Symbolic Control Structure**: The use of specific tokens or delimiters (e.g., Thought:, Action:, Observation:) to manage the state of the interaction and separate internal reasoning from external output.7

This distinction is crucial. While a "chain of thought" is a technique, **ReAct** is a framework because it enforces a loop of environmental interaction governed by strict syntactic rules.

### **2.2 The Taxonomy of Cognitive Architectures**

The evolution of these frameworks follows a clear trajectory, which we categorize into three distinct epochs based on the level of autonomy and complexity involved.3

#### **2.2.1 The Pre-Agentic Epoch (Pre-2022)**

This era was characterized by linear, single-turn interactions. The dominant paradigms were **In-Context Learning (ICL)** and **Prefix-Tuning**. The cognitive load was entirely on the user to structure the prompt to elicit the correct response. Frameworks from this period are largely static templates or "Prompt Libraries" rather than dynamic control flows. The focus was on "prompt design" rather than "agent design".3

#### **2.2.2 The Reasoning Emergence (2022–2023)**

The discovery that LLMs could generate intermediate reasoning steps marked a paradigm shift. This epoch saw the rise of **Chain-of-Thought (CoT)** and its immediate derivatives like **Self-Consistency** and **Least-to-Most Prompting**. These frameworks focus on *thought generation*—forcing the model to verbalize its rationale to reduce error rates in probabilistic reasoning. The structure is primarily linear or tree-based (branching thoughts), moving from input to output via explicit logical bridges.4

#### **2.2.3 The Agentic Loop Epoch (2023–Present)**

The current epoch is defined by **Cyclic Systems** that incorporate environmental feedback, persistent memory, and tool use. Frameworks like **ReAct**, **Reflexion**, and **Voyager** act as state machines. They do not just generate thoughts; they execute actions, observe results, and self-correct. This introduces the concept of "Agency"—the ability to pursue a goal over multiple turns without continuous human intervention. The complexity has shifted from the prompt itself to the *orchestration* of the prompt within a software runtime (e.g., LangChain, AutoGen).5

### **2.3 Methodology of Discovery**

Our mining methodology involved scanning historical corpora, arXiv preprints, and GitHub repositories for acronyms and capitalized conceptual structures.15 We utilized a heuristic filter: a framework is only included in this registry if it has at least two independent citations or a documented implementation in a major library. This filters out the "hallucinated naming" phenomenon where papers propose catchy acronyms that never generalize beyond the initial publication. We specifically looked for structural schemas—evidence of "Step 1, Step 2" logic or specific string templates used to drive model behavior.18

## ---

**3\. Historical Archaeology: The Rediscovery of Classical Decision Models**

A striking finding of this research is the degree to which modern AI agent frameworks are reinventions or direct adaptations of pre-computational decision-making models. Frameworks developed for military strategy, industrial data mining, and behavioral psychology have been "digitized" into prompt templates, serving as the foundational logic for autonomous agents.

### **3.1 CRISP-DM: The Ancestor of the Data Agent**

Origin: Data Mining (1996)  
Expansion: CRoss-Industry Standard Process for Data Mining.  
Originally designed to structure human data science teams, CRISP-DM has been resurrected as a cognitive blueprint for Autonomous Data Agents (e.g., the "Data Analyst" persona in OpenAI's GPTs). The framework's six phases map almost perfectly to the state transitions of a code-interpreting agent.20

* **Business Understanding**: The agent parses the user's natural language query to define the analytical goal (e.g., "Analyze the sales trend").  
* **Data Understanding**: The agent executes initial code (e.g., df.head(), df.info()) to "observe" the schema and quality of the uploaded file.  
* **Data Preparation**: The agent autonomously writes code to handle missing values, normalize columns, or merge datasets based on the previous observation.  
* **Modeling**: The agent selects an algorithm (regression, clustering) and writes the execution code.  
* **Evaluation**: The agent interprets the output metrics (R-squared, accuracy) and validates them against the initial query.  
* **Deployment**: The agent generates a final chart or textual report.

**Structural Analysis**: In the context of LLMs, CRISP-DM serves as a "meta-prompt" that enforces a sequential constraint. Without this structure, LLMs tend to jump straight to modeling code without first verifying data quality, leading to execution errors. By enforcing the "Data Understanding" phase as a prerequisite step in the prompt chain, architects reduce the hallucination rate of code generation agents.24 The framework converts a chaotic open-ended request into a linear workflow of dependencies.

### **3.2 The OODA Loop: Military Strategy as Agent Control**

Origin: Military Strategy (John Boyd, USAF)  
Expansion: Observe, Orient, Decide, Act.  
The OODA Loop is arguably the most influential historical framework in the domain of agentic AI, providing the direct conceptual lineage for the **ReAct** pattern. Originally describing the cycle of air combat maneuvering, it models how an entity processes chaotic environmental information to take effective action.26

* **Observe**: The acquisition of raw data. In AI agents, this corresponds to the input from tools, APIs, or the user prompt (e.g., Observation: The search API returned 404).  
* **Orient**: The analysis of this data in the context of memory, culture, and genetic heritage. For LLMs, this is the "Context Processing" phase where the model attends to the observation history and aligns it with its pre-trained knowledge base and system instructions.29  
* **Decide**: The formulation of a hypothesis or plan. This maps to the Thought: step in ReAct, where the model verbalizes its next move ("I need to try a different search term").  
* **Act**: The physical execution. This maps to the Action: step where the model emits a tool call or final response.30

**Agentic Adaptation**: Framework archaeologists note that libraries like LangChain essentially operationalized the OODA loop into a software design pattern. The "Agent Executor" is an OODA loop that runs until a termination condition is met.31 However, modern implementations often simplify Boyd's complex "Orientation" phase—which involves dismantling and creating mental models—into a simple context update. This simplification is a source of failure, as agents often struggle to "re-orient" when observations contradict their initial assumptions, leading to the "looping" failure mode discussed later.34

### **3.3 Behavioral Frameworks: Fogg and Hook**

Origin: Behavioral Psychology / UX Design  
Domains: User Engagement, Agent Personalization.  
While CRISP and OODA govern task execution, frameworks from behavioral psychology are increasingly used to structure the *interaction* layer of agents, particularly in tutoring, coaching, or "companion" agents.35

**The Fogg Behavior Model (B=MAP)**:

* **Expansion**: **B**ehavior \= **M**otivation $\\times$ **A**bility $\\times$ **P**rompt.  
* **Agentic Application**: This framework is used to design "Proactive Agents." The agent evaluates the user's state. If the user has high motivation but low ability, the agent acts as a **Facilitator** (simplifying the task). If the user has high ability but low motivation, the agent acts as a **Spark** (incentivizing).  
* **Structural Schematic**: System prompts for these agents often include a classification step: Classify User State: \[Low Ability/High Motivation\] \-\> Strategy: Simplify. This dynamic persona adaptation prevents the agent from overwhelming a novice user or boring an expert.37

**The Hook Model**:

* **Expansion**: **T**rigger $\\rightarrow$ **A**ction $\\rightarrow$ **V**ariable Reward $\\rightarrow$ **I**nvestment.  
* **Agentic Application**: Used in "Habit-Forming" agents (e.g., Duolingo's AI, fitness coaches). The "Variable Reward" is crucial; ensuring the agent's responses are not deterministic but offer variety (creativity, humor, insight) keeps the user engaged in the feedback loop. The "Investment" phase corresponds to the user providing more data (context), which makes the agent smarter and the switching cost higher.39

### **3.4 Educational Scaffolding: Bloom's Taxonomy**

Origin: Educational Psychology (1956)  
Domain: Instructional Design / Prompt Scaffolding.  
Bloom's Taxonomy has been adapted into a prompt engineering framework to ensure complex concepts are taught or analyzed systematically. It categorizes cognitive tasks into a hierarchy: Remember $\\rightarrow$ Understand $\\rightarrow$ Apply $\\rightarrow$ Analyze $\\rightarrow$ Evaluate $\\rightarrow$ Create.41

* **Prompt Structure**: Instead of asking an LLM to "Write an essay on X" (Create), a Bloom-based framework forces the model to traverse the hierarchy: "First, list the key facts about X (Remember). Then, explain the underlying mechanism (Understand). Finally, synthesize these into an essay (Create)."  
* **Impact**: This scaffolding dramatically improves the coherence of long-form generation by ensuring the model has "loaded" the necessary context into its active memory before attempting the highest-order task. It is the pedagogical ancestor of **Least-to-Most Prompting**.43

## ---

**4\. The Reasoning Revolution (2022–2023)**

The period between 2022 and 2023 marked the "Cambrian Explosion" of prompt engineering techniques. As models scaled, researchers discovered that explicit verbal reasoning—forcing the model to "talk to itself"—unlocked capabilities that were latent in the weights. This epoch shifted the focus from input optimization to thought generation.

### **4.1 Chain-of-Thought (CoT) & Its Lineage**

Status: Foundational / Ubiquitous  
Source: Wei et al. (2022) 3  
**Chain-of-Thought (CoT)** is the progenitor of modern cognitive architectures. It posits that LLMs are not just pattern matchers but can simulate reasoning chains if prompted to do so.

* **Mechanism**: By appending "Let's think step by step" (Zero-Shot CoT) or providing exemplars of reasoning (Few-Shot CoT), the model distributes the computational load of a complex problem across multiple tokens. Each generated token serves as a new context for the subsequent token, effectively expanding the model's "working memory".45  
* **Structural Evolution**:  
  * *Standard CoT*: Q \-\> Reasoning \-\> A  
  * *Zero-Shot CoT*: Q \-\> "Let's think step by step" \-\> Reasoning \-\> A  
* **Critique & Limitations**: While revolutionary, CoT suffers from **Hallucination Propagation** (or the "Domino Effect"). Since the chain is linear, a single logical error in Step 1 propagates to Step 5, leading to a confident but incorrect answer. There is no mechanism for the model to look back and correct a previous step once it has been generated.46 This limitation drove the development of non-linear frameworks like Tree of Thoughts.

### **4.2 ReAct: The Framework that defined Agency**

Name: ReAct  
Expansion: Reasoning \+ Acting  
Source: Yao et al. (2022) 7  
If CoT gave LLMs an inner voice, **ReAct** gave them hands. It is the single most critical framework in the history of agentic AI, defining the standard control loop used by virtually all agent runtimes (LangChain, AutoGen, CrewAI). It synergizes the internal reasoning of CoT with external tool usage.

* **The Structural Schematic (The Loop)**:  
  1. **Thought**: The agent reasons about the current state ("I need to find the current stock price of Apple").  
  2. **Action**: The agent selects a specific tool and formats the input (SearchTool\["AAPL price"\]).  
  3. **Observation**: The environment (runtime) executes the tool and returns the raw output ("$150.00") into the context window.  
  4. **Integration**: The model attends to the observation.  
  5. **Thought**: The agent synthesizes the new information ("The price is $150. I need to compare this to yesterday's close...").  
  6. **Loop**: The process repeats until a "Final Answer" is generated.

**Cognitive Architecture**: ReAct creates a feedback loop that grounds the model's reasoning in external reality. The Observation step acts as a "reality check," correcting hallucinations before they propagate. However, ReAct is computationally expensive and prone to "context overflow" as the history of thoughts and observations grows.49 It also introduces specific failure modes like the "Infinite Loop," where an agent continually repeats an action if the observation is not informative enough to trigger a state change.50

### **4.3 Decomposition Frameworks: Breaking Complexity**

To address the limitations of context windows and the fragility of long reasoning chains, decomposition frameworks emerged to break complex problems into manageable sub-atomic units.

#### **4.3.1 Least-to-Most Prompting (LtM)**

Source: Zhou et al. (2022) 51  
Structure:

1. **Decomposition**: The model is prompted to list the sub-problems required to solve the main query.  
2. **Sequential Solving**: The model solves the first sub-problem.  
3. Context Expansion: The answer to Sub-problem 1 is appended to the prompt for Sub-problem 2\.  
   Use Case: Highly effective for symbolic manipulation and compositional generalization (e.g., "concatenation of the second letter of the word 'apple' and the third letter of 'banana'").54

#### **4.3.2 Plan-and-Solve (PS)**

Source: Wang et al. (2023) 11  
Structure: Explicitly decouples the Planning Phase from the Execution Phase.

1. **Plan**: "Devise a plan to solve the problem."  
2. Solve: "Carry out the plan."  
   Advantage: This framework addresses "missing step errors" common in Zero-Shot CoT. By forcing the model to articulate the entire roadmap before performing any calculation, it reduces the likelihood of getting lost in the details during execution.58

#### **4.3.3 Skeleton-of-Thought (SoT)**

Source: Ning et al. (2023) 59  
Goal: Latency Optimization.  
Structure:

1. **Skeleton**: The model generates a concise outline of the answer (the "skeleton").  
2. Expansion: The system makes parallel API calls to expand each point of the skeleton simultaneously.  
   Implication: This is a framework designed for speed and efficiency. It moves away from the sequential, autoregressive nature of standard generation by treating the answer as a set of independent chunks that can be processed in parallel. It works well for informational queries but poorly for logical dependencies where Point B depends on Point A.62

### **4.4 Topological Reasoning: From Chains to Graphs**

As tasks grew in complexity, linear chains proved insufficient. "Topological" frameworks were introduced to allow for non-linear exploration of the solution space.

#### **4.4.1 Tree of Thoughts (ToT)**

Source: Yao et al. (2023) 12  
Structure: ToT treats reasoning as a search problem over a tree structure.

* **Node**: A coherent unit of text (a "thought").  
* **Branching**: The model generates multiple possible next steps.  
* **Evaluation**: The model (or a separate critic) scores each branch as "Sure," "Maybe," or "Impossible."  
* Search Algorithm: The system uses Breadth-First Search (BFS) or Depth-First Search (DFS) to navigate the tree, backtracking when a branch is evaluated as a dead end.  
  Use Case: Essential for tasks requiring strategic lookahead, such as creative writing, crossword puzzles, or the "Game of 24," where a greedy linear approach (CoT) often fails.65

#### **4.4.2 Graph of Thoughts (GoT)**

Source: Besta et al. (2023) 66  
Structure: Generalizes ToT into a Directed Acyclic Graph (DAG).

* **Operations**: GoT introduces graph operations like **Aggregation** (combining multiple thoughts into one), **Refinement** (looping back to improve a thought), and **Distillation**.  
* **Advantage**: It allows for synergy between disparate reasoning paths. Information from one branch can be merged with another, mimicking the complex, associative nature of human brainstorming. GoT represents the most complex topological structure currently available for prompt engineering.69

## ---

**5\. Agentic Design Patterns & Meta-Frameworks (2024–2026)**

The current epoch is defined by "Meta-Frameworks"—systems that orchestrate multiple agents or enforce rigorous quality control loops. These frameworks move beyond individual reasoning to managing state, memory, and collaboration.

### **5.1 Reflexion: The Rise of Episodic Memory and Self-Correction**

Name: Reflexion  
Domain: Reinforcement Learning / Self-Correction  
Source: Shinn et al. (2023) 70  
Reflexion addresses the inability of standard agents to learn from their mistakes without model fine-tuning. It introduces a "verbal reinforcement learning" loop that updates the agent's *memory* rather than its weights.

* **Architecture**:  
  1. **Actor**: The agent attempts to solve the task, generating a trajectory.  
  2. **Evaluator**: A critic scores the output (Binary Success/Fail or Scalar Reward).  
  3. **Self-Reflector**: If the task failed, this module analyzes the trajectory to determine *why* it failed. It generates a verbal "Reflection" (e.g., "I failed because I searched for the wrong term. Next time I should check the spelling").  
  4. **Episodic Memory**: The reflection is stored in a long-term memory buffer.  
  5. **Repeat**: The Actor retries the task, but the prompt is now conditioned on the retrieved reflection.

**Insight**: Reflexion transforms "failure" from a terminal state into a learning signal. It creates agents that get "smarter" the longer they operate, purely through prompt context management.73 This is critical for preventing the "Infinite Loop" failure mode found in basic ReAct agents.

### **5.2 PEER: The Repetitive Refinement Loop**

Name: PEER  
Expansion: Plan, Execute, Express, Review  
Source: AgentUniverse (2024) 17  
PEER formalizes the collaborative workflow often seen in human teams into a single or multi-agent structure. It is particularly effective for content generation and complex analysis where a single draft is rarely sufficient.

* **Structure**:  
  * **Plan**: The agent decomposes the user query into sub-steps and information requirements.  
  * **Execute**: The agent gathers necessary data via RAG or Web Search.  
  * **Express**: The agent synthesizes the gathered information into a coherent draft or solution.  
  * **Review**: A critic agent (or the same model in a different role) evaluates the draft against specific criteria (e.g., accuracy, tone, completeness). If the review fails, the system loops back to the **Plan** or **Express** phase with specific feedback.

**Application**: PEER is widely adopted in enterprise "Content Generation" agents where accuracy and tone are critical. The explicit "Review" step acts as a quality gate, preventing the agent from outputting hallucinated or low-quality content.77

### **5.3 RAISE: The Memory-Augmented Agent**

Name: RAISE  
Expansion: Reasoning, Acting, Iterating, Self-Correction, Evaluation (Note: Expansion varies, primarily associated with ReAct \+ Memory).  
Source: Omidi Shayegan et al. (2024) 78  
RAISE addresses the "short attention span" of standard ReAct agents. Standard agents lose context as the conversation window fills up. RAISE incorporates a dual-component memory system to mimic human cognition.

* **Mechanism**:  
  * **Scratchpad (Short-Term Memory)**: Maintains the state of the current thought process, similar to RAM. It holds immediate observations and current plans.  
  * **Retrieval Database (Long-Term Memory)**: A vector database that stores relevant examples, past successful strategies, or domain knowledge. The agent retrieves from this database to inform its reasoning.  
* **Significance**: This allows the agent to "remember" previous failures or successful strategies across different sessions, effectively enabling "experience" to persist beyond the immediate context window.81

### **5.4 Voyager: The Curriculum Learning Agent**

Name: Voyager  
Domain: Embodied Agents / Gaming (Minecraft)  
Source: Wang et al. (2023) 14  
Voyager represents the apex of "self-improving" agents. Operating in the open-ended world of Minecraft, it demonstrates how agents can expand their own capabilities without human code updates.

* **Core Innovation: The Skill Library**: When Voyager successfully solves a novel task (e.g., "Mine a Diamond"), it doesn't just move on. It takes the successful code/plan and saves it as a "Skill" in a vector database. For future tasks (e.g., "Make a Diamond Pickaxe"), it retrieves this "Mine Diamond" skill and executes it as a primitive function.  
* **Automatic Curriculum**: The agent does not wait for user commands. It proposes its own tasks based on its current inventory and skill level (e.g., "I have wood, I should make a pickaxe"). This mimics intrinsic motivation.

**Implication**: Voyager demonstrates that agents can exhibit "lifelong learning" by accumulating a library of executable tools (code) rather than just text memories. It bridges the gap between neural reasoning (LLM) and symbolic execution (Code).82

### **5.5 Generative Agents: The Simulacra Architecture**

Name: Generative Agents  
Source: Park et al. (2023) 85  
Famous for the "Smallville" simulation, this architecture is designed for believable social behavior rather than task optimization. It models the complexity of human memory and social interaction.

* **Architecture**:  
  1. **Memory Stream**: A comprehensive, time-stamped log of *all* observations (visual, linguistic) the agent experiences.  
  2. **Retrieval**: To act, the agent fetches relevant memories based on three scores: **Recency** (how long ago), **Importance** (significance of the event), and **Relevance** (semantic similarity to current situation).  
  3. **Reflection**: Periodically, the agent pauses to synthesize low-level memories into high-level insights (e.g., "Klaus acts nervous around Maria"). These reflections are added back to the memory stream.  
  4. **Planning**: The agent generates daily schedules based on its reflections and goals.

**Insight**: The "Reflection" module is the key innovation. Without it, the memory stream becomes a noisy swamp of details. Reflection compresses experience into personality, allowing the agent to maintain consistent behavior over long periods.88

## ---

**6\. Domain-Specific & Specialized Frameworks**

Certain domains require specialized architectures that enforce specific constraints, such as causality, legality, or mathematical rigour. These frameworks demonstrate how generic agent patterns are adapted for high-stakes environments.

### **6.1 CREPE: Causal Reasoning Framework**

Name: CREPE  
Expansion: Causal Reasoning of Entities and Planning Events (Inferred from context).  
Source: Zhang et al. (2023) 90  
CREPE is both a benchmark and a framework designed to evaluate and enhance an agent's understanding of the *physical* and *causal* implications of its actions. Unlike standard text generation, causal reasoning requires tracking the state of entities (e.g., "Is the pan hot?") and predicting the likelihood of events.

* **Structural Components**:  
  * **Entity State Tracking**: The framework explicitly monitors variables (e.g., Temperature, Location, status).  
  * **Event Plausibility**: It predicts the likelihood change ($\\delta$) for hypothetical events based on the agent's actions (e.g., "If I turn on the stove, the likelihood of 'water boiling' increases").  
* **Prompt Strategy**: CREPE utilizes a decomposition strategy where prompts are structured as logical assertions about object states. It forces the model to verify preconditions before predicting outcomes, reducing "causal hallucinations" where agents predict physically impossible results. It often uses a "Code-like" representation for events to leverage the logical strictness of code-trained models.94

### **6.2 AgentsBench: The Judicial Framework**

Name: AgentsBench  
Domain: Legal / Judgment / Decision Making  
Source: Jiang & Yang (2025) 95  
AgentsBench is a multi-agent framework designed to simulate the collaborative deliberation of a judicial collegial bench. It addresses the bias and variance inherent in single-agent decision-making by orchestrating a "society of agents."

* **Architecture**:  
  1. **Bench Selection**: The system forms a panel comprising diverse roles: a **Professional Judge** (Presiding) and randomly selected **Lay Jurors** with different backgrounds.  
  2. **Independent Sentencing**: Each agent analyzes the case facts and laws independently to form an initial opinion.  
  3. **Deliberation Loop**: The agents engage in iterative rounds of debate. In each round, an agent updates its view based on the arguments of others ($s^{(t+1)}\_i \= U(s^{(t)}\_i, D^{(t)})$).  
  4. **Consensus Evaluation**: The Presiding Judge agent evaluates whether a consensus has been reached. If not, the deliberation continues or a final ruling is made by the judge.

**Insight**: This framework empirically demonstrates that "Ensembling" agents with distinct personas and a structured debate protocol yields more robust, fair, and legally accurate decisions than a single "unbiased" agent. It operationalizes the concept of "institutional wisdom".96

### **6.3 Program-Aided Reasoning (PoT / PAL)**

Name: PoT (Program of Thoughts) / PAL (Program-Aided Language models)  
Source: Chen et al. (2022); Gao et al. (2023) 97  
Recognizing that LLMs are excellent semantic reasoners but poor arithmetic calculators, this framework enforces a strict separation of concerns.

* **Structure**:  
  1. **Thought**: The model reasons about the problem in natural language ("I need to calculate the compound interest...").  
  2. **Code**: Instead of hallucinating the number, the model generates executable Python code (interest \= principal \* (1 \+ rate)\*\*time).  
  3. **Execution**: The system runs the code in a deterministic Python interpreter.  
  4. **Response**: The execution result is fed back into the context for the final answer.

**Archetype**: This is the "Code Interpreter" pattern. It is the gold standard for math, finance, and logic puzzles, effectively solving the "calculation error" failure mode of standard CoT.100

## ---

**7\. Optimization & Meta-Learning Frameworks**

A emerging category of frameworks treats the *prompt itself* as an object to be optimized by the agent. These are "Meta-Frameworks" that generate or refine the instructions for other agents.

### **7.1 APE: Automatic Prompt Engineer**

Name: APE  
Source: Zhou et al. (2022) 101  
APE treats prompt engineering as a "program synthesis" problem. It automates the search for the optimal instruction to guide a model.

* **Workflow**:  
  1. **Proposal**: An LLM generates a set of candidate prompts based on a few input-output examples.  
  2. **Scoring**: The system tests these prompts against a validation set to score their performance.  
  3. **Selection**: The best-performing prompt is selected for the production task.

**Significance**: APE demonstrated that LLMs are often better at writing prompts for themselves than humans are. They can find counter-intuitive triggers or phrasings that maximize activation patterns in the latent space, which a human engineer might never guess.103

### **7.2 Meta-Prompting**

Name: Meta-Prompting  
Source: Zhang et al. (2024) 104  
Meta-Prompting abstracts the problem-solving process. Instead of prompting for the *answer*, it prompts the model to generate the *process* (the meta-prompt) to find the answer.

* **Structure**:  
  1. **Type Abstraction**: The model identifies the *class* of the problem (e.g., "This is a geometry problem").  
  2. **Template Generation**: The model generates a structural template relevant to that class (e.g., "Step 1: List axioms. Step 2: Define variables...").  
  3. **Instantiation**: The model fills the template with the specific details of the current problem to generate the solution.

**Insight**: This acts as a "higher-order" cognitive function. It allows the model to switch strategies dynamically based on the problem type, essentially selecting its own cognitive framework on the fly.107

### **7.3 System 2 Attention (S2A)**

Name: S2A  
Source: Weston & Sukhbaatar (2023) 108  
S2A addresses the issues of "sycophancy" (agreeing with user bias) and distraction in long contexts. It forces the model to consciously decide what parts of the context are relevant *before* generating an answer.

* **Structure**:  
  1. **Regenerate Context**: The model is prompted to "Rewrite the context to remove irrelevant information and bias, keeping only what is necessary to answer the query."  
  2. **Answer**: The model answers the query using this new, cleaned context.

**Mechanism**: This separates the "attentional filter" (System 2\) from the "generative response" (System 1). By physically removing distractor tokens from the context window, S2A improves factuality and reduces the likelihood of the model attending to irrelevant correlations.111

## ---

**8\. The Framework Registry**

The following table serves as a consolidated, structured index of the identified frameworks. It categorizes them by their primary cognitive function and provides the structural pattern that defines them.

| Acronym | Expansion | Domain | Structural Pattern | Key Source |
| :---- | :---- | :---- | :---- | :---- |
| **ReAct** | Reasoning \+ Acting | Agent Autonomy | Thought $\\rightarrow$ Action $\\rightarrow$ Obs $\\rightarrow$ Thought | 7 |
| **CRISP-DM** | Cross-Industry Standard Process for Data Mining | Data Science | BizUnd $\\rightarrow$ DataUnd $\\rightarrow$ Prep $\\rightarrow$ Model $\\rightarrow$ Eval | 20 |
| **OODA** | Observe, Orient, Decide, Act | Strategic Control | Observe $\\rightarrow$ Orient $\\rightarrow$ Decide $\\rightarrow$ Act | 26 |
| **CoT** | Chain of Thought | Reasoning | Input $\\rightarrow$ Let's think step by step $\\rightarrow$ Output | 4 |
| **ToT** | Tree of Thoughts | Search/Planning | Generate $\\rightarrow$ Evaluate $\\rightarrow$ Search (BFS/DFS) | 12 |
| **GoT** | Graph of Thoughts | Complex Reasoning | Aggregation $\\rightarrow$ Refinement $\\rightarrow$ Distillation | 66 |
| **Reflexion** | (Concept: Self-Reflection) | Reinforcement Learning | Act $\\rightarrow$ Eval $\\rightarrow$ Self-Reflect $\\rightarrow$ Memory $\\rightarrow$ Act | 70 |
| **PEER** | Plan, Execute, Express, Review | Collaborative Writing | Plan $\\rightarrow$ Exec $\\rightarrow$ Express $\\rightarrow$ Review | 17 |
| **DEPS** | Describe, Explain, Plan, Select | Embodied Agents | Describe $\\rightarrow$ Explain $\\rightarrow$ Plan $\\rightarrow$ Select | 112 |
| **RAISE** | ReAct \+ Iteration \+ Self-Eval | Agent Memory | ReAct Loop \+ Scratchpad \+ LongTerm Mem | 78 |
| **APE** | Automatic Prompt Engineer | Meta-Optimization | Gen Prompts $\\rightarrow$ Eval $\\rightarrow$ Select | 102 |
| **S2A** | System 2 Attention | Attention Control | Rewrite Context $\\rightarrow$ Generate Answer | 108 |
| **PoT** | Program of Thoughts | Math/Logic | Thought $\\rightarrow$ Code $\\rightarrow$ Exec $\\rightarrow$ Answer | 97 |
| **AoT** | Algorithm of Thoughts | Search Strategy | Define $\\rightarrow$ Hypothesize $\\rightarrow$ Test $\\rightarrow$ Conclude | 113 |
| **RaR** | Rephrase and Respond | Comprehension | Rephrase Q $\\rightarrow$ Expand $\\rightarrow$ Respond | 114 |
| **SoT** | Skeleton of Thought | Latency Opt. | Skeleton $\\rightarrow$ Parallel Expansion | 59 |
| **CREPE** | Causal Reasoning... | Causal Logic | Entity State $\\rightarrow$ Event Plausibility Check | 90 |
| **ART** | Auto Reasoning & Tool-use | Tool Integration | Select Task $\\rightarrow$ Generate Program $\\rightarrow$ Exec | 115 |

*Table 1: The Consolidated Registry of Cognitive Frameworks.*

## ---

**9\. Failure Archetypes & Anti-Patterns**

The excavation of these frameworks reveals not just success stories but consistent "failure archetypes"—structural flaws that lead to agent collapse. Understanding these is as critical as understanding the frameworks themselves.

### **9.1 The "Infinite Loop" Trap**

Pattern: An agent in a ReAct loop keeps performing the same action (e.g., Search\["weather"\]) repeatedly. The observation returns the same data, but the agent's "Thought" step fails to recognize that the information sufficiency threshold has been met.  
Root Cause: Lack of "state change" validation in the prompt. The agent doesn't realize it has already acquired the information, or the observation text is too noisy for the model to parse the answer.  
Mitigation: Frameworks like Reflexion specifically address this by adding a "Self-Reflector" component that detects repetition. The reflector injects a memory: "I have already searched for X and it failed. I should try strategy Y." This forces a divergence in the trajectory.34

### **9.2 Hallucination Propagation (The Domino Effect)**

Pattern: In Chain-of-Thought, a minor error in Step 1 (e.g., "The capital of Australia is Sydney") is accepted as truth in Step 2, leading to a perfectly logical but factually incorrect conclusion.  
Root Cause: Linear dependency without verification. The model treats its own generated tokens as ground truth.  
Mitigation: Tree of Thoughts (ToT) and PEER mitigate this by introducing evaluation steps ("Check") before moving to the next node. PoT mitigates this by offloading the calculation to a deterministic engine (Python), ensuring that the "facts" (calculation results) are correct.45

### **9.3 The "Dead Framework" Cemetery**

Some frameworks appear in the literature but fail to gain traction, becoming "Dead Acronyms."

* **Active-Prompt**: While theoretically sound (using uncertainty metrics to select questions for human annotation), the engineering overhead of "human-in-the-loop" makes it less attractive than fully automated methods like APE or OPRO. It failed to generalize because it disrupted the automation pipeline.116  
* **Directional Stimulus Prompting**: This technique involved training a small policy model to generate "hints" for the larger model. It has been effectively superseded by general "System Prompting" and advancements in model alignment (RLHF), which allow users to provide hints directly without a separate policy model.117

These "dead" frameworks often fail because they require too much external orchestration relative to the performance gain, or they are subsumed by improvements in the base models (e.g., GPT-4's native reasoning abilities made some complex decomposition scaffolds less necessary).

## ---

**10\. Conclusion: The Future of Symbolic Scaffolding**

The archaeology of prompt frameworks reveals a clear and undeniable trend: the field is moving from **instruction** (telling the model what to do) to **architecture** (designing the environment in which the model thinks).

The earliest frameworks, like CoT, were simple linear scaffolds—training wheels for reasoning. The second generation, led by ReAct, introduced loops and environmental grounding, effectively creating the first "operating systems" for LLMs. The current generation—Reflexion, Voyager, AgentsBench—introduces **state, memory, and society**. These frameworks acknowledge that a single inference pass is insufficient for complex tasks; intelligence emerges from the *interaction* of multiple inference passes, mediated by structured feedback loops.

The "winning" frameworks share common traits:

1. **Modularity**: They separate reasoning (LLM) from execution (Tools) and memory (Vector DB).  
2. **Recursion**: They allow the model to critique its own outputs (Reflexion, PEER).  
3. **Constraints**: They use strict formats (JSON, Code, defined Steps) to bind the stochastic model to deterministic workflows.

As LLMs continue to scale, simple prompt engineering will likely obsolesce. It will be replaced by **Cognitive Architecture Engineering**—the design of these complex, named frameworks that govern the lifecycle of synthetic thought. The frameworks documented here—CRISP, ReAct, OODA, and their progeny—are not just historical artifacts; they are the blueprints for the autonomous systems of the next decade.

---

Report ID: DRP-2026-FRAMEWORKS  
Date: January 16, 2026  
Analyst: Framework Archaeologist Agent

#### **Works cited**

1. Effective context engineering for AI agents \- Anthropic, accessed on January 16, 2026, [https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)  
2. The Evolution of Prompt Engineering: The Brain of Agentic AI Systems \- Inclusion Cloud, accessed on January 16, 2026, [https://inclusioncloud.com/insights/blog/the-evolution-of-prompt-engineering/](https://inclusioncloud.com/insights/blog/the-evolution-of-prompt-engineering/)  
3. Prompt engineering \- Wikipedia, accessed on January 16, 2026, [https://en.wikipedia.org/wiki/Prompt\_engineering](https://en.wikipedia.org/wiki/Prompt_engineering)  
4. A brief history of Prompt Engineering | by YZhou \- Medium, accessed on January 16, 2026, [https://medium.com/@yzhou1988/a-brief-history-of-prompt-engineering-cb7c7d7cd422](https://medium.com/@yzhou1988/a-brief-history-of-prompt-engineering-cb7c7d7cd422)  
5. The 2026 Guide to AI Agent Workflows \- Vellum AI, accessed on January 16, 2026, [https://www.vellum.ai/blog/agentic-workflows-emerging-architectures-and-design-patterns](https://www.vellum.ai/blog/agentic-workflows-emerging-architectures-and-design-patterns)  
6. Towards Unified Mathematical Reasoning inLarge Language Models via a Multi-Paradigm Perspective \- arXiv, accessed on January 16, 2026, [https://arxiv.org/html/2501.11110v4](https://arxiv.org/html/2501.11110v4)  
7. What is a ReAct Agent? | IBM, accessed on January 16, 2026, [https://www.ibm.com/think/topics/react-agent](https://www.ibm.com/think/topics/react-agent)  
8. ReAct: Synergizing Reasoning and Acting in Language Models \- Google Research, accessed on January 16, 2026, [https://research.google/blog/react-synergizing-reasoning-and-acting-in-language-models/](https://research.google/blog/react-synergizing-reasoning-and-acting-in-language-models/)  
9. The Evolving Art and Science of Prompt Engineering: A Chronological Journey \- Medium, accessed on January 16, 2026, [https://medium.com/@yujiisobe/the-evolving-art-and-science-of-prompt-engineering-a-chronological-journey-948c0a5a96f9](https://medium.com/@yujiisobe/the-evolving-art-and-science-of-prompt-engineering-a-chronological-journey-948c0a5a96f9)  
10. From Prompt Chains to Cognitive Systems: A Timeline of Agent Reasoning \- Medium, accessed on January 16, 2026, [https://medium.com/@yhocotw31016/from-prompt-chains-to-cognitive-systems-a-timeline-of-agent-reasoning-8bfb7d679687](https://medium.com/@yhocotw31016/from-prompt-chains-to-cognitive-systems-a-timeline-of-agent-reasoning-8bfb7d679687)  
11. What Is Plan-and-Solve Prompting? | by Deepak kumar sahoo | The Synaptic Stack, accessed on January 16, 2026, [https://medium.com/the-synaptic-stack/what-is-plan-and-solve-prompting-59293b8b41b1](https://medium.com/the-synaptic-stack/what-is-plan-and-solve-prompting-59293b8b41b1)  
12. What is Tree Of Thoughts Prompting? \- IBM, accessed on January 16, 2026, [https://www.ibm.com/think/topics/tree-of-thoughts](https://www.ibm.com/think/topics/tree-of-thoughts)  
13. AI Agent Frameworks: Choosing the Right Foundation for Your Business | IBM, accessed on January 16, 2026, [https://www.ibm.com/think/insights/top-ai-agent-frameworks](https://www.ibm.com/think/insights/top-ai-agent-frameworks)  
14. From Minecraft to AI: Learnings from Voyager for industry solutions \- Outshift | Cisco, accessed on January 16, 2026, [https://outshift.cisco.com/blog/from-minecraft-to-ai-learnings-from-voyager-for-industry-solutions](https://outshift.cisco.com/blog/from-minecraft-to-ai-learnings-from-voyager-for-industry-solutions)  
15. \[2502.19135\] A Temporal Planning Framework for Multi-Agent Systems via LLM-Aided Knowledge Base Management \- arXiv, accessed on January 16, 2026, [https://arxiv.org/abs/2502.19135](https://arxiv.org/abs/2502.19135)  
16. \[2410.12720\] HEnRY: A Multi-Agent System Framework for Multi-Domain Contexts \- arXiv, accessed on January 16, 2026, [https://arxiv.org/abs/2410.12720](https://arxiv.org/abs/2410.12720)  
17. \[2407.06985\] PEER: Expertizing Domain-Specific Tasks with a Multi-Agent Framework and Tuning Methods \- arXiv, accessed on January 16, 2026, [https://arxiv.org/abs/2407.06985](https://arxiv.org/abs/2407.06985)  
18. NLP Extraction : Techniques, Applications, and Best Tools for AI \- Kairntech, accessed on January 16, 2026, [https://kairntech.com/blog/articles/nlp-extraction/](https://kairntech.com/blog/articles/nlp-extraction/)  
19. Analyzing Natural Language Processing Techniques to Extract Meaningful Information on Skills Acquisition From Textual Content, accessed on January 16, 2026, [https://ieeexplore.ieee.org/iel8/6287639/10380310/10684699.pdf](https://ieeexplore.ieee.org/iel8/6287639/10380310/10684699.pdf)  
20. CRISP-DM for Data Science Teams: 5 Actions to Consider, accessed on January 16, 2026, [https://www.datascience-pm.com/crisp-dm-for-data-science-teams-5-actions-to-consider/](https://www.datascience-pm.com/crisp-dm-for-data-science-teams-5-actions-to-consider/)  
21. What is CRISP DM? \- Data Science PM, accessed on January 16, 2026, [https://www.datascience-pm.com/crisp-dm-2/](https://www.datascience-pm.com/crisp-dm-2/)  
22. Crisp DM methodology \- Smart Vision Europe, accessed on January 16, 2026, [https://www.sv-europe.com/crisp-dm-methodology/](https://www.sv-europe.com/crisp-dm-methodology/)  
23. CRISP-DM framework: A foundational data mining process model | by Avikumar Talaviya, accessed on January 16, 2026, [https://medium.com/@avikumart\_/crisp-dm-framework-a-foundational-data-mining-process-model-86fe642da18c](https://medium.com/@avikumart_/crisp-dm-framework-a-foundational-data-mining-process-model-86fe642da18c)  
24. The CRISP-DM Process: A Comprehensive Guide | by Shawn Chumbar | Medium, accessed on January 16, 2026, [https://medium.com/@shawn.chumbar/the-crisp-dm-process-a-comprehensive-guide-4d893aecb151](https://medium.com/@shawn.chumbar/the-crisp-dm-process-a-comprehensive-guide-4d893aecb151)  
25. Data Science Methodologies and Frameworks Guide, accessed on January 16, 2026, [https://www.datascience-pm.com/data-science-methodologies/](https://www.datascience-pm.com/data-science-methodologies/)  
26. The OODA Loop: How Fighter Pilots Make Fast and Accurate Decisions \- Farnam Street, accessed on January 16, 2026, [https://fs.blog/ooda-loop/](https://fs.blog/ooda-loop/)  
27. The OODA Loop \- The Decision Lab, accessed on January 16, 2026, [https://thedecisionlab.com/reference-guide/computer-science/the-ooda-loop](https://thedecisionlab.com/reference-guide/computer-science/the-ooda-loop)  
28. OODA loop \- Wikipedia, accessed on January 16, 2026, [https://en.wikipedia.org/wiki/OODA\_loop](https://en.wikipedia.org/wiki/OODA_loop)  
29. OODA Loop: A Blueprint for the Evolution of Military Decisions \- RTI, accessed on January 16, 2026, [https://www.rti.com/blog/ooda-loop-a-blueprint-for-the-evolution-of-military-decisions](https://www.rti.com/blog/ooda-loop-a-blueprint-for-the-evolution-of-military-decisions)  
30. Evolving the OODA Loop for Strategy \- Marine Corps Association, accessed on January 16, 2026, [https://www.mca-marines.org/gazette/ooda-loop-for-strategy/](https://www.mca-marines.org/gazette/ooda-loop-for-strategy/)  
31. I think I just solved a true autonomy. Meet OODA Agents. \- Risolto, accessed on January 16, 2026, [https://risolto.co.uk/blog/i-think-i-just-solved-a-true-autonomy-meet-ooda-agents/](https://risolto.co.uk/blog/i-think-i-just-solved-a-true-autonomy-meet-ooda-agents/)  
32. Optimizing Data Center Performance with AI Agents and the OODA Loop Strategy, accessed on January 16, 2026, [https://developer.nvidia.com/blog/optimizing-data-center-performance-with-ai-agents-and-the-ooda-loop-strategy/](https://developer.nvidia.com/blog/optimizing-data-center-performance-with-ai-agents-and-the-ooda-loop-strategy/)  
33. Autonomous Agents and Agent Simulations | Hacker News, accessed on January 16, 2026, [https://news.ycombinator.com/item?id=35635225](https://news.ycombinator.com/item?id=35635225)  
34. The Dark Psychology of Multi-Agent AI: 30 Failure Modes That Can Break Your Entire System | by Rakesh Sheshadri \- Medium, accessed on January 16, 2026, [https://medium.com/@rakesh.sheshadri44/the-dark-psychology-of-multi-agent-ai-30-failure-modes-that-can-break-your-entire-system-023bcdfffe46](https://medium.com/@rakesh.sheshadri44/the-dark-psychology-of-multi-agent-ai-30-failure-modes-that-can-break-your-entire-system-023bcdfffe46)  
35. Fogg Behavior Model: Motivation, Ability, and Prompts \- Northbeam, accessed on January 16, 2026, [https://www.northbeam.io/blog/fogg-behavior-model-motivation-ability-and-prompts](https://www.northbeam.io/blog/fogg-behavior-model-motivation-ability-and-prompts)  
36. The Hook Model: Retain Users by Creating Habit-Forming Products \- Amplitude, accessed on January 16, 2026, [https://amplitude.com/blog/the-hook-model](https://amplitude.com/blog/the-hook-model)  
37. Fogg Behavior Model & 2025 Tech Applications \- DEV Community, accessed on January 16, 2026, [https://dev.to/joaosc17/fogg-behavior-model-2025-tech-applications-10g3](https://dev.to/joaosc17/fogg-behavior-model-2025-tech-applications-10g3)  
38. AI Agent Behavioral Science \- arXiv, accessed on January 16, 2026, [https://arxiv.org/html/2506.06366v3](https://arxiv.org/html/2506.06366v3)  
39. Understanding the Hook Model: How to Create Habit-Forming Products \- Dovetail, accessed on January 16, 2026, [https://dovetail.com/product-development/what-is-the-hook-model/](https://dovetail.com/product-development/what-is-the-hook-model/)  
40. What is the hook model? How to build habit-forming products \- LogRocket Blog, accessed on January 16, 2026, [https://blog.logrocket.com/product-management/what-is-the-hook-model-how-to-build-habit-forming-products/](https://blog.logrocket.com/product-management/what-is-the-hook-model-how-to-build-habit-forming-products/)  
41. Blooms Taxonomy Prompt \- Elevating cognitive skills in AI engineering \- Juuzt AI, accessed on January 16, 2026, [https://juuzt.ai/knowledge-base/prompt-frameworks/blooms-taxonomy-prompts/](https://juuzt.ai/knowledge-base/prompt-frameworks/blooms-taxonomy-prompts/)  
42. Using Bloom's Taxonomy as a Framework for Student-led Discussions \- Bellarmine University, accessed on January 16, 2026, [https://www.bellarmine.edu/docs/default-source/faculty-development-docs/16-using-bloom.pdf?sfvrsn=0](https://www.bellarmine.edu/docs/default-source/faculty-development-docs/16-using-bloom.pdf?sfvrsn=0)  
43. Bloom's Taxonomy — AI for Education, accessed on January 16, 2026, [https://www.aiforeducation.io/prompts/blooms-taxonomy](https://www.aiforeducation.io/prompts/blooms-taxonomy)  
44. Using Bloom's Taxonomy to Refine Learning Goals with AI Prompting : r/elearning \- Reddit, accessed on January 16, 2026, [https://www.reddit.com/r/elearning/comments/1ji0m9y/using\_blooms\_taxonomy\_to\_refine\_learning\_goals/](https://www.reddit.com/r/elearning/comments/1ji0m9y/using_blooms_taxonomy_to_refine_learning_goals/)  
45. Chain of Thoughtlessness? An Analysis of CoT in Planning \- OpenReview, accessed on January 16, 2026, [https://openreview.net/forum?id=kPBEAZU5Nm\&referrer=%5Bthe%20profile%20of%20Subbarao%20Kambhampati%5D(%2Fprofile%3Fid%3D\~Subbarao\_Kambhampati1)](https://openreview.net/forum?id=kPBEAZU5Nm&referrer=%5Bthe+profile+of+Subbarao+Kambhampati%5D\(/profile?id%3D~Subbarao_Kambhampati1\))  
46. A Critique of Pure LLM Reason \- Cybernetic Forests, accessed on January 16, 2026, [https://mail.cyberneticforests.com/a-critique-of-pure-llm-reason/](https://mail.cyberneticforests.com/a-critique-of-pure-llm-reason/)  
47. ReAct \- Prompt Engineering Guide, accessed on January 16, 2026, [https://www.promptingguide.ai/techniques/react](https://www.promptingguide.ai/techniques/react)  
48. ReAct: Synergizing Reasoning and Acting in Language Models \- arXiv, accessed on January 16, 2026, [https://arxiv.org/pdf/2210.03629](https://arxiv.org/pdf/2210.03629)  
49. Keys To Understanding ReAct: Synergizing Reasoning and Acting in Language Models, accessed on January 16, 2026, [https://arize.com/blog/keys-to-understanding-react/](https://arize.com/blog/keys-to-understanding-react/)  
50. Exploring Autonomous Agents: A Closer Look at Why They Fail When Completing Tasks, accessed on January 16, 2026, [https://arxiv.org/html/2508.13143v1](https://arxiv.org/html/2508.13143v1)  
51. Least-to-most prompting templates \+ how to implement : r/PromptEngineering \- Reddit, accessed on January 16, 2026, [https://www.reddit.com/r/PromptEngineering/comments/1ewukfi/leasttomost\_prompting\_templates\_how\_to\_implement/](https://www.reddit.com/r/PromptEngineering/comments/1ewukfi/leasttomost_prompting_templates_how_to_implement/)  
52. LEAST-TO-MOST PROMPTING ENABLES COMPLEX REASONING IN LARGE LANGUAGE MODELS \- Department of Computing Science, accessed on January 16, 2026, [https://webdocs.cs.ualberta.ca/\~dale/papers/iclr23a.pdf](https://webdocs.cs.ualberta.ca/~dale/papers/iclr23a.pdf)  
53. \[2205.10625\] Least-to-Most Prompting Enables Complex Reasoning in Large Language Models \- arXiv, accessed on January 16, 2026, [https://arxiv.org/abs/2205.10625](https://arxiv.org/abs/2205.10625)  
54. Least-to-Most Prompting (LtM) \- Emergent Mind, accessed on January 16, 2026, [https://www.emergentmind.com/topics/least-to-most-prompting-ltm](https://www.emergentmind.com/topics/least-to-most-prompting-ltm)  
55. Least-to-Most Prompting Enables Complex Reasoning in Large Language Models | Request PDF \- ResearchGate, accessed on January 16, 2026, [https://www.researchgate.net/publication/360804483\_Least-to-Most\_Prompting\_Enables\_Complex\_Reasoning\_in\_Large\_Language\_Models](https://www.researchgate.net/publication/360804483_Least-to-Most_Prompting_Enables_Complex_Reasoning_in_Large_Language_Models)  
56. Plan-and-Solve Prompting: Improving Reasoning and Reducing Errors, accessed on January 16, 2026, [https://learnprompting.org/docs/advanced/decomposition/plan\_and\_solve](https://learnprompting.org/docs/advanced/decomposition/plan_and_solve)  
57. Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models \- ACL Anthology, accessed on January 16, 2026, [https://aclanthology.org/2023.acl-long.147/](https://aclanthology.org/2023.acl-long.147/)  
58. Master Plan and Solve Prompting Techniques for Better Problem Solving \- Relevance AI, accessed on January 16, 2026, [https://relevanceai.com/prompt-engineering/master-plan-and-solve-prompting-techniques-for-better-problem-solving](https://relevanceai.com/prompt-engineering/master-plan-and-solve-prompting-techniques-for-better-problem-solving)  
59. Reducing Latency with Skeleton of Thought Prompting \- PromptHub, accessed on January 16, 2026, [https://www.prompthub.us/blog/reducing-latency-with-skeleton-of-thought-prompting](https://www.prompthub.us/blog/reducing-latency-with-skeleton-of-thought-prompting)  
60. Skeleton-of-Thought Prompting: Faster and Efficient Response Generation, accessed on January 16, 2026, [https://learnprompting.org/docs/advanced/decomposition/skeleton\_of\_thoughts](https://learnprompting.org/docs/advanced/decomposition/skeleton_of_thoughts)  
61. \[2307.15337\] Skeleton-of-Thought: Prompting LLMs for Efficient Parallel Generation \- arXiv, accessed on January 16, 2026, [https://arxiv.org/abs/2307.15337](https://arxiv.org/abs/2307.15337)  
62. Skeleton-of-Thought: Prompting LLMs for Efficient Parallel Generation | OpenReview, accessed on January 16, 2026, [https://openreview.net/forum?id=mqVgBbNCm9](https://openreview.net/forum?id=mqVgBbNCm9)  
63. Tree of Thoughts: Deliberate Problem Solving with Large Language Models \- NeurIPS, accessed on January 16, 2026, [https://proceedings.neurips.cc/paper\_files/paper/2023/file/271db9922b8d1f4dd7aaef84ed5ac703-Paper-Conference.pdf](https://proceedings.neurips.cc/paper_files/paper/2023/file/271db9922b8d1f4dd7aaef84ed5ac703-Paper-Conference.pdf)  
64. Tree of Thoughts: Deliberate Problem Solving with Large Language Models \- arXiv, accessed on January 16, 2026, [https://arxiv.org/pdf/2305.10601](https://arxiv.org/pdf/2305.10601)  
65. How Tree of Thoughts Prompting Works \- PromptHub, accessed on January 16, 2026, [https://www.prompthub.us/blog/how-tree-of-thoughts-prompting-works](https://www.prompthub.us/blog/how-tree-of-thoughts-prompting-works)  
66. accessed on January 16, 2026, [https://medium.com/@JacekWo/llms-graph-of-thoughts-framework-c5607a46aa9a\#:\~:text=The%20Graph%20of%20Thoughts%20(GoT,LLMs%20to%20process%20these%20operations.](https://medium.com/@JacekWo/llms-graph-of-thoughts-framework-c5607a46aa9a#:~:text=The%20Graph%20of%20Thoughts%20\(GoT,LLMs%20to%20process%20these%20operations.)  
67. Graph of Thoughts (GoT) Framework \- Emergent Mind, accessed on January 16, 2026, [https://www.emergentmind.com/topics/graph-of-thoughts-got](https://www.emergentmind.com/topics/graph-of-thoughts-got)  
68. Graph of Thoughts: Solving Elaborate Problems with Large Language Models, accessed on January 16, 2026, [https://ojs.aaai.org/index.php/AAAI/article/view/29720/31236](https://ojs.aaai.org/index.php/AAAI/article/view/29720/31236)  
69. Official Implementation of "Graph of Thoughts: Solving Elaborate Problems with Large Language Models" \- GitHub, accessed on January 16, 2026, [https://github.com/spcl/graph-of-thoughts](https://github.com/spcl/graph-of-thoughts)  
70. Reflexion | Prompt Engineering Guide, accessed on January 16, 2026, [https://www.promptingguide.ai/techniques/reflexion](https://www.promptingguide.ai/techniques/reflexion)  
71. \[2303.11366\] Reflexion: Language Agents with Verbal Reinforcement Learning \- arXiv, accessed on January 16, 2026, [https://arxiv.org/abs/2303.11366](https://arxiv.org/abs/2303.11366)  
72. Reflexion: Language Agents with Verbal Reinforcement Learning \- OpenReview, accessed on January 16, 2026, [https://openreview.net/pdf?id=vAElhFcKW6](https://openreview.net/pdf?id=vAElhFcKW6)  
73. How AI Teaches Itself: A Beginner's Guide to the Reflexion Framework \- Medium, accessed on January 16, 2026, [https://medium.com/@faulknerproject/how-ai-teaches-itself-a-beginners-guide-to-the-reflexion-framework-98935c9f6259](https://medium.com/@faulknerproject/how-ai-teaches-itself-a-beginners-guide-to-the-reflexion-framework-98935c9f6259)  
74. MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs \- arXiv, accessed on January 16, 2026, [https://arxiv.org/html/2512.20845](https://arxiv.org/html/2512.20845)  
75. Revolutionize Your AI Projects: Harness the Power of the PEER Pattern for Multi-Agent Systems \- DEV Community, accessed on January 16, 2026, [https://dev.to/jay\_all\_day/revolutionize-your-ai-projects-harness-the-power-of-the-peer-pattern-for-multi-agent-systems-kc3](https://dev.to/jay_all_day/revolutionize-your-ai-projects-harness-the-power-of-the-peer-pattern-for-multi-agent-systems-kc3)  
76. PEER: Expertizing Domain-Specific Tasks with a Multi-Agent Framework and Tuning Methods \- arXiv, accessed on January 16, 2026, [https://arxiv.org/html/2407.06985v1](https://arxiv.org/html/2407.06985v1)  
77. agentUniverse is a LLM multi-agent framework that allows developers to easily build multi-agent applications. \- GitHub, accessed on January 16, 2026, [https://github.com/agentuniverse-ai/agentUniverse](https://github.com/agentuniverse-ai/agentUniverse)  
78. \[2401.02777\] From LLM to Conversational Agent: A Memory Enhanced Architecture with Fine-Tuning of Large Language Models \- arXiv, accessed on January 16, 2026, [https://arxiv.org/abs/2401.02777](https://arxiv.org/abs/2401.02777)  
79. From LLM to Conversational Agent: A Memory Enhanced Architecture with Fine-Tuning of Large Language Models \- arXiv, accessed on January 16, 2026, [https://arxiv.org/html/2401.02777v1](https://arxiv.org/html/2401.02777v1)  
80. RAISE: Reliable Agent Improvement via Simulated Experience \- OpenReview, accessed on January 16, 2026, [https://openreview.net/forum?id=53oRwdZe6k](https://openreview.net/forum?id=53oRwdZe6k)  
81. Capgemini RAISE™ \- Reliable AI Solution Engineering, accessed on January 16, 2026, [https://www.capgemini.com/solutions/raise-reliable-ai-solution-engineering/](https://www.capgemini.com/solutions/raise-reliable-ai-solution-engineering/)  
82. MineDojo/Voyager: An Open-Ended Embodied Agent with Large Language Models \- GitHub, accessed on January 16, 2026, [https://github.com/MineDojo/Voyager](https://github.com/MineDojo/Voyager)  
83. Voyager: An Open-Ended Embodied Agent with Large Language Models \- arXiv, accessed on January 16, 2026, [https://arxiv.org/abs/2305.16291](https://arxiv.org/abs/2305.16291)  
84. Building Your First LLM Agent Application | NVIDIA Technical Blog, accessed on January 16, 2026, [https://developer.nvidia.com/blog/building-your-first-llm-agent-application/](https://developer.nvidia.com/blog/building-your-first-llm-agent-application/)  
85. What is Generative Agents | Iguazio, accessed on January 16, 2026, [https://www.iguazio.com/glossary/generative-agents/](https://www.iguazio.com/glossary/generative-agents/)  
86. \[2304.03442\] Generative Agents: Interactive Simulacra of Human Behavior \- arXiv, accessed on January 16, 2026, [https://arxiv.org/abs/2304.03442](https://arxiv.org/abs/2304.03442)  
87. Computational Agents Exhibit Believable Humanlike Behavior | Stanford HAI, accessed on January 16, 2026, [https://hai.stanford.edu/news/computational-agents-exhibit-believable-humanlike-behavior](https://hai.stanford.edu/news/computational-agents-exhibit-believable-humanlike-behavior)  
88. Generative Agents: Interactive Simulacra of Human Behavior \- arXiv, accessed on January 16, 2026, [https://arxiv.org/pdf/2304.03442](https://arxiv.org/pdf/2304.03442)  
89. An architectural framework for Generative Agents | by Daniele Nanni \- Medium, accessed on January 16, 2026, [https://medium.com/@daniele.nanni/from-npcs-to-generative-agents-part-2-d09d3af37738](https://medium.com/@daniele.nanni/from-npcs-to-generative-agents-part-2-d09d3af37738)  
90. Hierarchical Scheduling for Multi-Vector Image Retrieval \- arXiv, accessed on January 16, 2026, [https://arxiv.org/html/2510.08976v1](https://arxiv.org/html/2510.08976v1)  
91. A Limitation, future work, and societal impact B Implementation details, accessed on January 16, 2026, [https://proceedings.neurips.cc/paper\_files/paper/2023/file/63461de0b4cb760fc498e85b18a7fe81-Supplemental-Datasets\_and\_Benchmarks.pdf](https://proceedings.neurips.cc/paper_files/paper/2023/file/63461de0b4cb760fc498e85b18a7fe81-Supplemental-Datasets_and_Benchmarks.pdf)  
92. Causal Reasoning About Entities and Events in Procedural Texts \- Yue Yang, accessed on January 16, 2026, [https://yueyang1996.github.io/papers/crepe.pdf](https://yueyang1996.github.io/papers/crepe.pdf)  
93. arXiv:2301.10896v3 \[cs.CL\] 16 Feb 2023, accessed on January 16, 2026, [https://arxiv.org/pdf/2301.10896](https://arxiv.org/pdf/2301.10896)  
94. Causal Reasoning of Entities and Events in Procedural Texts, accessed on January 16, 2026, [https://arxiv.org/abs/2301.10896](https://arxiv.org/abs/2301.10896)  
95. AgentsBench: A Multi-Agent LLM Simulation Framework for Legal Judgment Prediction, accessed on January 16, 2026, [https://www.mdpi.com/2079-8954/13/8/641](https://www.mdpi.com/2079-8954/13/8/641)  
96. \[2412.18697\] Agents on the Bench: Large Language Model Based Multi Agent Framework for Trustworthy Digital Justice \- arXiv, accessed on January 16, 2026, [https://arxiv.org/abs/2412.18697](https://arxiv.org/abs/2412.18697)  
97. Implement Program of Thoughts (PoT) Prompting for Better Problem Solving \- Relevance AI, accessed on January 16, 2026, [https://relevanceai.com/prompt-engineering/implement-program-of-thoughts--pot--prompting-for-better-problem-solving](https://relevanceai.com/prompt-engineering/implement-program-of-thoughts--pot--prompting-for-better-problem-solving)  
98. Program-of-Thoughts Strategy \- Emergent Mind, accessed on January 16, 2026, [https://www.emergentmind.com/topics/program-of-thoughts-pot-strategy](https://www.emergentmind.com/topics/program-of-thoughts-pot-strategy)  
99. Towards Better Understanding of Program-of-Thought Reasoning in Cross-Lingual and Multilingual Environments \- arXiv, accessed on January 16, 2026, [https://arxiv.org/html/2502.17956v2](https://arxiv.org/html/2502.17956v2)  
100. Something-of-Thought in LLM Prompting: An Overview of Structured LLM Reasoning, accessed on January 16, 2026, [https://towardsdatascience.com/something-of-thought-in-llm-prompting-an-overview-of-structured-llm-reasoning-70302752b390/](https://towardsdatascience.com/something-of-thought-in-llm-prompting-an-overview-of-structured-llm-reasoning-70302752b390/)  
101. Automatic Prompt Engineer (APE) \- Emergent Mind, accessed on January 16, 2026, [https://www.emergentmind.com/topics/automatic-prompt-engineer-ape](https://www.emergentmind.com/topics/automatic-prompt-engineer-ape)  
102. Automatic Prompt Engineer (APE), accessed on January 16, 2026, [https://www.promptingguide.ai/techniques/ape](https://www.promptingguide.ai/techniques/ape)  
103. Large Language Models are Human-Level Prompt Engineers | OpenReview, accessed on January 16, 2026, [https://openreview.net/forum?id=92gvk82DE-](https://openreview.net/forum?id=92gvk82DE-)  
104. What is Meta Prompting? \- IBM, accessed on January 16, 2026, [https://www.ibm.com/think/topics/meta-prompting](https://www.ibm.com/think/topics/meta-prompting)  
105. Meta Prompting | Prompt Engineering Guide, accessed on January 16, 2026, [https://www.promptingguide.ai/techniques/meta-prompting](https://www.promptingguide.ai/techniques/meta-prompting)  
106. Meta Prompting for AI Systems \- arXiv, accessed on January 16, 2026, [https://arxiv.org/html/2311.11482v6](https://arxiv.org/html/2311.11482v6)  
107. Meta Prompts: The Invisible Framework Powering the New Age of AI | by Prabhu Srivastava, accessed on January 16, 2026, [https://medium.com/@prabhuss73/meta-prompts-the-invisible-framework-powering-the-new-age-of-ai-ef1118005c6b](https://medium.com/@prabhuss73/meta-prompts-the-invisible-framework-powering-the-new-age-of-ai-ef1118005c6b)  
108. \[R\] System 2 Attention (is something you might need too) : r/MachineLearning \- Reddit, accessed on January 16, 2026, [https://www.reddit.com/r/MachineLearning/comments/1854gp2/r\_system\_2\_attention\_is\_something\_you\_might\_need/](https://www.reddit.com/r/MachineLearning/comments/1854gp2/r_system_2_attention_is_something_you_might_need/)  
109. System 2 Attention (is something you might need too) \- Semantic Scholar, accessed on January 16, 2026, [https://www.semanticscholar.org/paper/System-2-Attention-%28is-something-you-might-need-Weston-Sukhbaatar/850538c1759c56a9f2dab8e84ec63801c41d6396](https://www.semanticscholar.org/paper/System-2-Attention-%28is-something-you-might-need-Weston-Sukhbaatar/850538c1759c56a9f2dab8e84ec63801c41d6396)  
110. \[2311.11829\] System 2 Attention (is something you might need too) \- arXiv, accessed on January 16, 2026, [https://arxiv.org/abs/2311.11829](https://arxiv.org/abs/2311.11829)  
111. The system-2 attention (S2A) prompt for long-context QA. The... \- ResearchGate, accessed on January 16, 2026, [https://www.researchgate.net/figure/The-system-2-attention-S2A-prompt-for-long-context-QA-The-CONTEXT-is-the-placeholder\_fig3\_384681142](https://www.researchgate.net/figure/The-system-2-attention-S2A-prompt-for-long-context-QA-The-CONTEXT-is-the-placeholder_fig3_384681142)  
112. Interactive Planning with Large Language Models Enables Open-World Multi-Task Agents \- NeurIPS, accessed on January 16, 2026, [https://proceedings.neurips.cc/paper\_files/paper/2023/file/6b8dfb8c0c12e6fafc6c256cb08a5ca7-Paper-Conference.pdf](https://proceedings.neurips.cc/paper_files/paper/2023/file/6b8dfb8c0c12e6fafc6c256cb08a5ca7-Paper-Conference.pdf)  
113. How Algorithm of Thoughts Prompting Works \- PromptHub, accessed on January 16, 2026, [https://www.prompthub.us/blog/how-algorithm-of-thoughts-prompting-works](https://www.prompthub.us/blog/how-algorithm-of-thoughts-prompting-works)  
114. \[2311.04205\] Rephrase and Respond: Let Large Language Models Ask Better Questions for Themselves \- arXiv, accessed on January 16, 2026, [https://arxiv.org/abs/2311.04205](https://arxiv.org/abs/2311.04205)  
115. Automatic Reasoning and Tool-use (ART) \- Prompt Engineering Guide, accessed on January 16, 2026, [https://www.promptingguide.ai/techniques/art](https://www.promptingguide.ai/techniques/art)  
116. Active Prompting with Chain-of-Thought for Large Language Models | by Cobus Greyling, accessed on January 16, 2026, [https://cobusgreyling.medium.com/active-prompting-with-chain-of-thought-for-large-language-models-b9708b2ddc22](https://cobusgreyling.medium.com/active-prompting-with-chain-of-thought-for-large-language-models-b9708b2ddc22)  
117. Guiding Large Language Models via Directional Stimulus Prompting \- Microsoft Research, accessed on January 16, 2026, [https://www.microsoft.com/en-us/research/publication/guiding-large-language-models-via-directional-stimulus-prompting/](https://www.microsoft.com/en-us/research/publication/guiding-large-language-models-via-directional-stimulus-prompting/)