# Systems Specification: Durable Agentic Memory & Surgical Markdown Scratchpads

In production-grade multi-agent systems, managing the **80% dynamic context window** is critical to preventing **context rot and cognitive decay** [20, 198, 305]. When conversations grow lengthy, continuously feeding the entire execution history to a model becomes prohibitively expensive, introduces high latency, and degrades reasoning quality [201, 321].

This document formalizes the **Durable Agentic Memory Specification**, establishing a standardized, machine-readable `memory.md` (or `notes.md`) file schema [7, 240]. It details the programmatic protocols for **Surgical Querying** and **Edit Compaction**, enabling agents to treat local markdown files as external virtual memory to bypass physical context limits [7, 203, 321].

---

## 1. System Architecture: The Memory-Paging Loop

To maintain continuity across independent development sessions without overloading the transformer's Key-Value (KV) Cache, the agent's memory is divided into three functional tiers [203]:

1. **Sensory Memory:** Ephemeral real-time user inputs [109, 203].
2. **Short-Term Memory:** Active conversational context and session-specific states [109, 203].
3. **Durable Scratchpad (Durable Memory):** A local, persistent Markdown file (`memory.md`) acting as externalized working RAM [7, 203].

### The Paging Mechanism
Instead of retaining verbose reasoning steps and tool execution histories in the active context, the agent offloads structured data to the local file system [7, 240]. When the active context window approaches its utilization threshold (e.g., $>80\%$), the agent initiates a compaction cycle:
* It compiles current facts, state values, and preferences into the Markdown file [7, 240].
* It flushes volatile session history [201].
* It reads back only the summarized and structured Markdown blocks at the start of the next execution turn, preserving critical directives while freeing up to **50% of the active context window** [2, 3].

---

## 2. Standardized Markdown Memory Schema (`memory.md`)

Below is the non-negotiable structural blueprint for the agent's persistent memory file. This schema uses strict Markdown headings, YAML front-matter, and JSON code blocks to support both human readability and deterministic programmatic parsing [19, 320, 1038]:

```markdown
---
session_id: "sess-99482-A"
last_updated: "2026-07-26T19:04:05-07:00"
agent_version: "roo-compiler-v5.3"
---

# 1. CORE MISSION & ATTRIBUTES
> **Purpose:** Establishes the agent's operational mandate, strategic goals, and high-level behavioral constraints [207, 224].

- **Agent Persona:** Precise Software Engineer and Architectural Guardian [224, 991].
- **Core Directives:** Maintain momentum toward the solution, leverage parallel execution, and enforce strict type safety [135, 225, 1039].
- **Design System:** Enforce utility-first styling using Tailwind CSS and semantic tokens; absolutely ban ad-hoc CSS [26, 367, 444].

# 2. LONG-TERM USER & PROJECT POLICIES
> **Purpose:** Preserves persistent preferences, technology choices, and stylistic rules across multiple independent sessions to ensure consistency [15, 203, 654].

- **prefer-async-await:** Mandate the use of asynchronous Swift and TypeScript routines; strictly prohibit legacy promise chains or Combine pipelines [15, 240, 655].
- **modularity-first:** Functionality must be split into concise components restricted to under 300–400 lines [1243]. Monolithic files are forbidden [27, 444].
- **secure-by-default:** Row Level Security (RLS) must be enabled on all database schemas [28, 444]. Hardcoding secrets is strictly prohibited [28, 444].

# 3. ACTIVE TASK BOARD
> **Purpose:** A dynamic, step-by-step checklist to deconstruct complexity, prevent scope drift, and provide an auditable trace of task execution [24, 919, 1037].

- [x] **TASK-01:** Analyze codebase structure and file dependencies [232].
- [/] **TASK-02:** Surgically refactor authentication controller `auth_controller.swift` [237].
- [ ] **TASK-03:** Execute SwiftLint validation suite and correct anomalies [234, 1039].

# 4. SCAR TISSUE ARCHIVE (STA)
> **Purpose:** Logs historical failure states, logical contradictions, and edge cases to enable Failure-Informed Prompt Inversion and prevent recurring errors [690, 1094].

```json
{
  "scars": [
    {
      "id": "SCAR-001",
      "timestamp": "2026-07-26T18:02:11Z",
      "type": "Linter Loop Exhaustion",
      "context": "Attempting to compile async block within synchronous Combine pipeline in Swift",
      "failure_mode": "Compiler error: 'async' call in a function that does not support concurrency",
      "remediation_inversion": "Invert the caller function signature to 'async throws' and check signature typing before writing modifications"
    }
  ]
}
```
```

---

## 3. Programmatic Query & Surgical Retrieval Protocols

To minimize token consumption, agents must never read the entire memory file unless a complete state synchronization is required [236]. Instead, they apply strict **Surgical Retrieval Protocols** [237, 646]:

### A. Regex-Driven Node Extraction (The "Scalpel" Pattern)
The agent utilizes specialized terminal tools or built-in script parsing to extract targeted sections [650]. For example, to read the **User & Project Policies** without ingesting the Task Board or the Scar Archive, the agent executes a regex-bound range query:

```bash
# Extract only the Long-Term Policies section using sed / awk boundary matching
sed -n '/^# 2. LONG-TERM/,/^# 3. ACTIVE/p' memory.md
```

### B. Python Parsing Engine for Semantic Extraction
The following Python script demonstrates how a meta-agent or context controller programmatically extracts and updates specific Markdown sections using abstract syntax trees or string patterns:

```python
import re
from pathlib import Path

class SurgicalMemoryEngine:
    def __init__(self, filepath: str):
        self.path = Path(filepath)
        self.content = self.path.read_text() if self.path.exists() else ""

    def extract_section(self, header_name: str) -> str:
        """Surgically extracts a section based on its markdown heading."""
        pattern = rf"^(#+ {re.escape(header_name)}.*?)(?=\n#+ |\Z)"
        match = re.search(pattern, self.content, re.MULTILINE | re.DOTALL)
        return match.group(1).strip() if match else ""

    def replace_section(self, header_name: str, new_content: str) -> None:
        """Surgically updates a specific section without touching unchanged blocks."""
        pattern = rf"^(#+ {re.escape(header_name)}.*?)(?=\n#+ |\Z)"
        replacement = f"## {header_name}\n{new_content}\n"
        
        if re.search(pattern, self.content, re.MULTILINE | re.DOTALL):
            self.content = re.sub(pattern, replacement, self.content, flags=re.MULTILINE | re.DOTALL)
        else:
            self.content += f"\n\n{replacement}"
            
        self.path.write_text(self.content.strip() + "\n")

# Example Usage:
# engine = SurgicalMemoryEngine("memory.md")
# policies = engine.extract_section("2. LONG-TERM USER & PROJECT POLICIES")
```

---

## 4. The Edit Compaction Protocol

When modifying memory files or codebase files, agents must follow the **Edit Compaction Protocol** to preserve context space and avoid redundant token-bloat [321, 646, 763]:

1. **Surgical Diffing:** The agent must only modify the specific lines containing the state changes or new rules [14, 237].
2. **Truncation Markers:** Unchanged sections of a file must be represented using language-appropriate truncation markers (e.g., `// ... existing code ...` or `<!-- ... existing nodes ... -->`) [14, 237, 394].
3. **Exact Matching:** Any find-and-replace block must match the existing indentation, whitespace, and special characters character-for-character to prevent parser failures [237, 802].
4. **Validation Verification:** Following any file modification, the agent must immediately execute linting or validation tools (the **"Fix Until Green" loop**) to guarantee syntactic and semantic integrity [320, 402].

---

## 5. Performance Trade-off Frontier

```
             High KV Cache Bloat ──────► Latency Spike & Context Rot [201, 321]
                      │
           [ Paged Markdown Scratchpad ]
                      │
                      ▼
         Low KV Cache Bloat ──────► 22% Reduction in Token Consumption [845]
```

* **KV Cache Optimization:** By shifting historical tool actions, detailed logs, and transient decisions out of the active context and into `memory.md`, runtime token consumption is reduced by **22% to 40%** in complex multi-step workflows [845, 846].
* **Latency Mitigation:** Moving from sequential, dialogue-heavy "conversational remembering" to parallelized local file access yields a **3x to 5x speedup** in initial task-phase ingestion [25, 322].
* **Epistemic Anchoring:** The inclusion of YAML front-matter and JSON-bound schemas enforces a structural "Cognitive Lock" [466]. The agent ceases to "guess" preferences and operates under deterministic programmatic rules, eliminating hallucination and preventing regression loops [319, 761].
