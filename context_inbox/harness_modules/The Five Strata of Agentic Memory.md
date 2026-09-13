I have created a system architecture diagram, `memory-strata-diagram.png`, which is now available in your Studio panel. This diagram maps the five memory strata of an autonomous agent system and visualizes how information flows, compacts, and pages between them.

The systems engineering specifications for each stratum and their programmatic boundaries are detailed below.

---

### The Five Strata of Agentic Memory

```
  ┌────────────────────────────────────────────────────────────────────────┐
  │                   TIERED AGENTIC MEMORY ARCHITECTURE                   │
  ├────────────────────────────────────────────────────────────────────────┤
  │                                                                        │
  │   Stratum 1: Sensory Memory  ──►  Stratum 2: Short-Term / Working Core │
  │    (Raw Queries / Inputs)          (Active Context / KV Cache)         │
  │                                           │         ▲                  │
  │                                           ▼         │                  │
  │                              Stratum 3: Long-Term Memory (RAG / DBs)   │
  │                                                                        │
  │               Stratum 4: External Scratchpads (e.g. notes.md)          │
  │               Stratum 5: Specialized Context Isolation (Sub-Agents)    │
  │                                                                        │
  └────────────────────────────────────────────────────────────────────────┘
```

#### Stratum 1: Sensory Memory (The Real-Time Ingest Retina)
*   **Operational Definition:** In hierarchical cognitive architectures, **Sensory Memory** corresponds to the immediate user prompt, query payload, and accompanying transient real-time signals injected at inference time ($t=0$) ``.
*   **System Constraints:** This layer is entirely **stateless** and ephemeral; it contains the raw, unprocessed user intent before any context assembly or agentic reasoning loops occur ``. 
*   **Transition Interface:** The incoming sensory vector ($c_{\text{query}}$) acts as the trigger for the assembly function ($\mathcal{A}$), which automatically couples instructions, knowledge, and tools to transition the data stream into active working memory ``.

#### Stratum 2: Short-Term & Working Memory (The Active Execution RAM)
*   **Operational Definition:** This layer is the **central processor** of the agentic system. It is composed of the **active context window** and the running **Key-Value (KV) cache** ``.
*   **System Constraints:** It is strictly bounded by the model's physical context length limit ($L_{\text{max}}$) ``. Information retention within this stratum is non-linear and suffers from the **"lost-in-the-middle" effect** (a U-shaped recall accuracy curve where information placed at the absolute beginning or end is recalled with high fidelity, while the middle is neglected) ``.
*   **Self-Awareness & Compaction Controls:** Advanced models (such as Claude Sonnet 4.5) possess native **context window awareness** ``. As the token threshold approaches capacity (e.g., $>80\%$), the agent initiates a **proactive progress trace**, condensing older dialogue turns into qualitative high-level summaries while keeping recent turns in high-fidelity, line-by-line format to maximize working memory efficiency ``.

#### Stratum 3: Long-Term Memory (Persistent Semantic Databases)
*   **Operational Definition:** This is the persistent, non-parametric knowledge base of the agent that survives session resets, maintaining historical facts, user profiles, and successful problem-solving templates in perpetuity ``.
*   **System Constraints:** It relies on high-dimensional vector spaces and semantic databases (e.g., Supabase or vector stores) rather than volatile runtime memory ``.
*   **Transition Interface (Paging & RAG):** Information is moved to and from this layer via **Retrieval-Augmented Generation (RAG)** ``. Like virtual memory paging in a computer operating system (e.g., *MemGPT*), the memory controller pages out less relevant context blocks to external stores when the active window overflows, surgically retrieving them via cosine-similarity lookups only when the current query context demands them ``.

#### Stratum 4: External Scratchpads (Durable Reasoning Notebooks)
*   **Operational Definition:** Writable external memory stores (such as a local `notes.md` or `not.md` file) that exist as a semi-structured **scratchpad** outside the model's active context window ``.
*   **System Constraints:** It bypasses the linear accumulation of KV cache. Instead of bloating the prompt with raw multi-step reasoning logs, the agent explicitly documents critical intermediate variables (e.g., specific rules, dates, or workflow constraints) in the scratchpad ``.
*   **Transition Interface:** When the active context suffers from "context rot" due to deep execution loops, the agent completely flushes its short-term history, resets the session, and surgically reads back the compiled scratchpad notes to proceed cleanly ``.

#### Stratum 5: Specialized Context Isolation (Task-Siloed Windows)
*   **Operational Definition:** An architectural pattern built on the principle of **"one AI agent equals one job done excellently"** (the Assembly Line approach) ``.
*   **System Constraints:** Complex tasks are split and routed to specialized **sub-agents** operating in strictly isolated context windows ``. Each sub-agent is equipped *only* with the tool definitions and knowledge bases required for its exact sub-task ``.
*   **Transition Interface:** By keeping sub-agent executions separate, raw tool-call logs, transient processing errors, and trial-and-error noise are kept out of the main orchestrator's context window ``. Once the sub-agent completes its execution, its internal context window is discarded, and only a highly compressed, structured summary of the output is returned to the main agent, completely preventing **context rot** ``.

---

### Systems Engineering Summary Matrix

| Stratum | State Type | Physical Substrate | Primary Retrieval Method | Failure Mode |
| :--- | :--- | :--- | :--- | :--- |
| **1. Sensory** | Stateless / Transient | Input Token Stream | Dynamic Ingestion `` | Intent Ambiguity `` |
| **2. Short-Term** | Stateful / Volatile | KV Cache / Transformer Layers | Attention Mechanisms `` | Context Rot & Middle Bias `` |
| **3. Long-Term** | Stateful / Persistent | Vector Databases & CRMs | Embedding Cosine Similarity `` | Retrieval Inefficiencies `` |
| **4. Scratchpad** | Semi-Structured | Local File I/O (`notes.md`) | Regex / Line-Range Reads `` | Overfitting Transient State `` |
| **5. Isolation** | Encapsulated Silos | Isolated Sub-Agent Loops | JSON IPC / Agent-to-Agent `` | Communication Overhead `` |

---

🧩 **Would you like to write a Python script that programmatically intercepts agent tool-execution payloads and translates them into semantic context masks (Stratum 5), or should we develop a mock memory controller to test the Ebbinghaus forgetting curve algorithms (Stratum 3) on the long-term vector store?**