# Devpost AI Agent Hackathons 2026: High-Value Problem Selection and Buildable Project Ideas

## Overview

This report identifies current AI-focused Devpost hackathons, verifies their status, and then selects a high‑value problem to solve with concrete, buildable project concepts suitable for a small team within a typical online hackathon timeframe. The focus is on ideas that can be demonstrated in a short video, clearly showcase the required platform features, and deliver tangible value for a specific community.[^1][^2]

## New AI Agent Hackathons on Devpost (March 2026)

### Authorized to Act: Auth0 for AI Agents

- **Host / Platform:** Devpost challenge sponsored by Okta/Auth0, focused on Auth0 for AI Agents and its Token Vault feature.[^3][^4]
- **Theme:** Build an "agentic" AI application that uses Auth0 for AI Agents Token Vault so agents can authenticate, authorize, and interact with APIs and services like humans do.[^5][^3]
- **Key requirement:** All winning submissions must use the Token Vault feature of Auth0 for AI Agents for secure tool calling and OAuth-based delegation.[^6][^3]
- **Status & deadline:** Featured online hackathon with a deadline around April 6–7, 2026 (Devpost internal submission page lists "Deadline: Apr 6, 2026 @ 11:45pm PDT", while marketing posts refer to "Apr 7, 2026").[^4][^7][^8]
- **Prizes:** Approximately 10,000 USD in shared cash prizes.[^8][^4]
- **Judging emphasis:** Security model, user control and consent, robustness of authorization boundaries, and the insight value of how agent authorization should evolve.[^3]

This hackathon is well-suited for projects that make AI agents visibly safer and more controllable when they operate against real-world APIs (cloud tools, developer platforms, SaaS applications) on behalf of human users.

### Agents Assemble – The Healthcare AI Endgame

- **Host / Platform:** Devpost challenge built around the Prompt Opinion multi‑agent platform, which supports Model Context Protocol (MCP) servers and Agent‑to‑Agent (A2A) standards for interoperable agents.[^9][^10]
- **Theme:** Build interoperable healthcare AI agents or tools at the intersection of MCP, A2A, and FHIR so that agents can collaborate and integrate safely into healthcare workflows.[^11][^9]
- **Technical paths:** Participants must either build a specialized MCP server (“Superpower”) or a full agent that uses A2A and conversational interoperability on the Prompt Opinion platform.[^10][^9]
- **Status & deadline:** Featured online hackathon with a submission period from March 4, 2026 to May 11, 2026; the Devpost rules and project gallery pages confirm a deadline of May 11, 2026 around 8–11 pm, depending on time zone labeling.[^12][^13][^14][^9][^10]
- **Prizes:** Prize pool around 25,000 USD for winning teams, as advertised in participant and social posts.[^15][^11]
- **Judging criteria:** "AI Factor" (does it leverage generative AI beyond traditional software), "Potential Impact" (improved outcomes, reduced cost or time), and "Feasibility" (privacy, safety, regulatory realism, and working integration on the Prompt Opinion platform).[^9][^10]

This hackathon is optimized for healthcare‑focused builders who can scope a realistic workflow, respect privacy constraints (synthetic or de‑identified data only), and demonstrate interoperable agents or tools in Prompt Opinion’s marketplace and runtime.[^10]

## Chosen Hackathon and High‑Value Problem

### Why focus on Agents Assemble (Healthcare)

Healthcare is a domain where small workflow improvements can have outsized impact on clinician burnout, patient safety, and system cost. The Agents Assemble challenge explicitly asks participants to build agents or tools that could realistically exist in a modern healthcare system while respecting privacy and open standards, making it an ideal context for a problem‑first, high‑value build.[^9][^10]

Compared with a general agent security challenge, the healthcare endgame brief comes with a sharper definition of the target environment (FHIR‑based systems, multi‑agent coordination, Prompt Opinion marketplace), which helps constrain the problem and ensures that a demo can be both realistic and evaluable within the judging rubric.[^10][^9]

### Selected high‑value problem

> **Problem:** Fragmented care for chronic‑condition patients leads to unsafe medication changes and delayed follow‑up because no single actor has a live, interoperable view of the patient’s multi‑system journey.

In practice, chronic patients (for example, with heart failure, diabetes, or chronic kidney disease) see multiple clinicians, use different hospital systems, and often receive medications from several pharmacies. Each system may expose data via FHIR APIs, but frontline clinicians rarely have time to reconcile conflicting medication lists, recent discharges, and lab trends during a 15‑minute visit.[^9][^10]

The high‑value opportunity for this hackathon is to use interoperable AI agents to:

- Continuously watch for risky fragmentation in synthetic multi‑system FHIR data (e.g., possible drug–drug interactions or missed follow‑up after discharge).
- Surface a "single story" of the patient’s recent journey in a way that is explainable and auditable.
- Do this **within Prompt Opinion**, using MCP and A2A, so that other agents can plug into or extend this capability.[^10][^9]

The target community is **care teams managing complex chronic‑condition patients inside hospital systems or large clinics**, rather than "everyone" or purely consumer use cases.

## Idea 1: CareWeaver – Multi‑System Care Timeline Agent

### One‑sentence pitch

An interoperable AI agent that assembles a unified, explainable care timeline from fragmented FHIR records across multiple systems, highlighting medication and follow‑up risks for chronic‑condition patients inside the Prompt Opinion platform.

### Target prize category and why

- **Target:** Main Agents Assemble awards as a "Full Agent" built via Path B (A2A‑enabled agent on Prompt Opinion).[^9][^10]
- **Why:** The judging rubric emphasizes generative AI solving a problem traditional rule‑based software cannot, clear impact on healthcare workflows, and feasible integration into real systems; a timeline‑weaving agent aligns closely with these criteria.[^10][^9]

### The demo moment

In the demo, a judge opens the Prompt Opinion interface and invokes CareWeaver for a synthetic test patient who has visits and medications scattered across three simulated FHIR sources (primary care, cardiology clinic, and recent hospital discharge).[^9][^10]

Within seconds, the agent:

- Renders a chronological timeline with labeled events (admission, discharge, prescriptions, lab results) and clearly tags which source system each event came from.
- Highlights a red banner: "Potentially unsafe combination: newly prescribed beta‑blocker plus existing calcium channel blocker – cardiology follow‑up overdue by 10 days (synthetic data)."
- Shows a one‑click, natural‑language explanation: "Here’s how these entries from System A, B, and C were reconciled into this conclusion" so the judge can see the generative reasoning step beyond a static rules engine.

This creates a memorable, human‑understandable moment that demonstrates both interoperability (multi‑system FHIR) and the "AI Factor" (narrative synthesis and risk explanation) without touching real PHI.[^10][^9]

### Platform features used and how they are visible

- **Prompt Opinion A2A Agent Runtime (Path B – Build an Agent):** The core CareWeaver entity is configured as a Prompt Opinion agent that can be discovered and invoked from the platform’s UI; the demo visibly selects it from the marketplace and triggers it on a synthetic patient scenario.[^9][^10]
- **Prompt Opinion Marketplace Integration:** The project is published so that judges can see it discoverable and invokable in the marketplace, satisfying Stage One technical qualification requirements.[^10]
- **MCP‑Backed Tools for FHIR Access:** Behind the scenes, CareWeaver uses one or more MCP servers that expose synthetic FHIR endpoints (e.g., separate "Hospital FHIR", "Clinic FHIR", "Pharmacy FHIR" tools), and the demo visibly shows the agent calling these tools and attributing events to specific systems.[^9][^10]
- **Synthetic‑Only Data Mode:** The demo explicitly toggles a "synthetic data" badge and explains that all patient identifiers are fictitious, aligning with the rules that strictly prohibit real PHI; calling this out in the UI shows respect for data‑integrity constraints.[^10]

Each of these features is visible to the judge during the run: marketplace discovery, agent invocation, step‑wise tool calls, and labeled synthetic data sources.

### What makes this not a wrapper

CareWeaver is not just a wrapper over a random LLM or dashboard; it depends on Prompt Opinion’s native support for:

- **A2A conversational interoperability**, so other agents (e.g., a scheduling agent or education agent) can later consume CareWeaver’s synthesized timeline as a first‑class input.[^9]
- **MCP‑based tools** representing different FHIR systems, which lets the agent dynamically query multiple backends and reason about inconsistencies rather than relying on a pre‑merged data lake.[^10][^9]
- **Marketplace verification and direct invocation** within Prompt Opinion, which is a core requirement of the hackathon and cannot be replicated by a standalone web app without the platform.[^10]

The value proposition – cross‑system timeline weaving and agent‑to‑agent collaboration – is tightly coupled to this open, standards‑based agent infrastructure, not just generic AI text generation.[^9][^10]

### Honest build estimate (person‑days)

Assuming a small team already comfortable with basic FHIR structures and LLM tooling, an honest build breakdown could be:

- 2–3 person‑days: Set up Prompt Opinion workspace, understand A2A and MCP examples, and scaffold the agent plus one example MCP server.
- 2–3 person‑days: Implement synthetic FHIR sources (e.g., static JSON or light mock servers) and create a few realistic patient journeys.
- 2–3 person‑days: Implement the CareWeaver agent logic (tool selection, timeline generation, risk rule scaffolding, and explanation prompts) and integrate with the synthetic FHIR tools.
- 1–2 person‑days: Build a minimal but clear UI flow inside Prompt Opinion, polish the prompt templates, edge‑case handling, and prepare the live demo flow plus script.

This yields roughly **7–11 person‑days** of focused work, which is realistic for 2–3 people working part‑time across several weeks before the May deadline.

### Primary risk

The main risk is **over‑scoping the clinical logic**, attempting to cover too many conditions or complex medication interactions and getting stuck tuning prompts and rules instead of shipping a narrow, convincing demo.[^9][^10]

There is also a moderate integration risk if the team underestimates the time needed to learn Prompt Opinion’s marketplace publishing and A2A configuration semantics, potentially leading to a working prototype that fails the Stage One technical qualification checks.[^10]

## Idea 2: DischargeRelay – Post‑Discharge Follow‑Up Orchestration Agent

### One‑sentence pitch

An orchestration agent on Prompt Opinion that coordinates post‑discharge follow‑up tasks across multiple synthetic systems (primary care, cardiology, scheduling, and patient messaging), ensuring no chronic‑condition patient "falls through the cracks" after leaving the hospital.

### Target prize category and why

- **Target:** Agents Assemble main awards, framed as a hybrid approach: a Prompt Opinion agent that consumes one or more MCP "Superpowers" focused on scheduling and patient messaging.[^9]
- **Why:** The challenge explicitly welcomes both Superpowers (MCP servers) and full agents; this idea demonstrates both by combining a follow‑up orchestration agent with supporting tools, which directly addresses the "Potential Impact" and "Feasibility" judging criteria.[^10][^9]

### The demo moment

In the demo, the judge selects a synthetic patient recently discharged with heart failure from a hospital FHIR source inside Prompt Opinion. DischargeRelay immediately:[^9]

- Reads the discharge summary via an MCP FHIR tool, detects that cardiology and primary‑care follow‑ups are recommended within 7 and 14 days respectively.
- Checks a synthetic scheduling MCP server to see available cardiology and primary‑care slots.
- Proposes a concrete follow‑up plan visible on screen: "Schedule cardiology on Day 5 at 10:00, primary care on Day 12 at 15:00, send patient education messages on Days 2, 4, and 10," with a human‑readable rationale note.
- With a single confirmation click from the judge (acting as clinician), it orchestrates calls to the scheduling MCP tool and a messaging MCP tool and shows a log of the tasks it executed.

The impressive moment is seeing one confirmation trigger multi‑system, agent‑mediated actions, all derived from synthetic but realistic discharge data, while respecting explicit human control and auditability.

### Platform features used and how they are visible

- **Prompt Opinion Agent Orchestration:** DischargeRelay runs as an agent that the judge picks from the Prompt Opinion interface, then it orchestrates tool calls rather than acting as a standalone web service.[^9]
- **Multiple MCP "Superpower" Servers:** At least two MCP servers are visible in the configuration and logs: a synthetic "Scheduling MCP" that exposes appointment slots and booking operations, and a "Patient Messaging MCP" that simulates sending SMS/app notifications with education content.[^10][^9]
- **Marketplace Discovery and Invocation:** The project is configured and published so that it passes marketplace validation; the demo explicitly shows the "discoverable and invokable" requirements being met in the Prompt Opinion UI.[^10]
- **Safety and Data Integrity Controls:** A visible banner and configuration panel explicitly state that only synthetic or de‑identified discharge data is used, aligning with hackathon rules and showing the feasibility of extending to real PHI under compliance review.[^10]

All platform features are surfaced in the demo: marketplace listing, agent invocation, MCP tools list, and visible logs of cross‑tool orchestration.

### What makes this not a wrapper

The orchestration logic depends on Prompt Opinion’s ability to:

- **Connect multiple MCP servers** via a single agent configuration so that discharge summaries, scheduling systems, and messaging channels are all first‑class tools rather than hard‑coded API calls in a monolithic app.[^9]
- **Run under A2A and conversational interoperability**, allowing future agents (for example, a medication reconciliation agent) to plug into the same workflow without rewiring everything.[^9]
- **Enforce platform‑level technical checks** (marketplace verification, protocol adherence, synthetic‑data use) that are required for this hackathon but would be external boilerplate in a generic SaaS product.[^10]

Without Prompt Opinion’s agent runtime, marketplace, and standards support, DischargeRelay would devolve into just another scheduling microservice glued to an LLM; the platform makes the orchestration auditable, composable, and reusable by other agents.

### Honest build estimate (person‑days)

A realistic build breakdown for a small team could be:

- 2–3 person‑days: Learn Prompt Opinion’s configuration and set up a baseline agent and example MCP server following the starter templates.
- 2–3 person‑days: Implement synthetic FHIR discharge data and basic parsing logic to extract recommended follow‑ups and constraints.
- 2–3 person‑days: Build the Scheduling MCP and Messaging MCP servers (can be simple Node or Python services) with a small but realistic API surface and mock storage.
- 2–3 person‑days: Implement orchestration prompts and logic in DischargeRelay, wire tool calls together, add confirmation flows and visible task logs, and prepare a smooth demo path.

This totals around **8–12 person‑days**, again feasible for a 2–3 person team across a few weeks, leaving some buffer for integration debugging.

### Primary risk

The core risk is **integration complexity across three different synthetic systems** (FHIR, scheduling, messaging) and the Prompt Opinion platform; underestimating this could lead to brittle demos that fail intermittently when judges run them.[^9][^10]

There is also a product‑risk dimension: unless the team keeps the scope tight (for example, focusing on a single condition such as heart failure), the agent may become a generic reminder bot that does not clearly demonstrate superior value over existing discharge checklists and templated messaging.

## How to choose between the two ideas

- **CareWeaver** is better if the team has stronger data‑modeling and explainability instincts and wants to showcase generative narrative synthesis and risk detection across fragmented records.
- **DischargeRelay** is better if the team prefers workflow automation and orchestration and wants a powerful "one click, many systems" demo moment grounded in hospital operations.

Both ideas are scoped to:

- Use Prompt Opinion and the hackathon’s open standards visibly in the demo.[^10][^9]
- Serve a clearly defined community: hospital and clinic care teams managing chronic‑condition patients.
- Be buildable in under two calendar weeks of focused part‑time work by a small team, with clear primary risks that can be managed by keeping scope tight.

---

## References

1. [Devpost - The home for hackathons](https://devpost.com) - Featured online hackathons ; Authorized to Act: Auth0 for AI Agents. 10 days left. Mar 02 - Apr 07, ...

2. [New & upcoming hackathons - Devpost](https://devpost.com/hackathons) - All hackathons ; Authorized to Act: Auth0 for AI Agents. 9 days left. Mar 02 - Apr 07, 2026 ; Agents...

3. [Authorized to Act: Auth0 for AI Agents: Build an agentic AI ... - Devpost](https://authorizedtoact.devpost.com) - Authorized to Act: Auth0 for AI Agents. Build an agentic AI application using Auth0 for AI Agents To...

4. [Dhinesh Kumar's (dinesh0666) software portfolio - Devpost](https://devpost.com/dinesh0666/challenges) - Authorized to Act: Auth0 for AI Agents. Featured. Online. Build an agentic AI application using Auth...

5. [Authorized to Act: Auth0 for AI Agents | Devpost - LinkedIn](https://www.linkedin.com/posts/devpost_authorized-to-act-auth0-for-ai-agents-activity-7429990057421352960-dxNF) - What happens when your AI agent actually has the "keys" to the door? Use Auth0's new Token Vault to ...

6. [Build an agentic AI application using Auth0 for AI Agents Token Vault](https://authorizedtoact.devpost.com/updates) - Authorized to Act: Auth0 for AI Agents. Deadline: Apr 6, 2026 @ 11 ... © 2026 Devpost, Inc. All righ...

7. [Auth0 for AI Agents - My hackathon projects - Devpost](https://devpost.com/submit-to/28368-authorized-to-act-ai-agents-with-auth0/manage/submissions) - Authorized to Act: Auth0 for AI Agents. Deadline: Apr 6, 2026 @ 11:45pm PDT · Join hackathon · Autho...

8. [AI Hackathons | Kirk Borne, Ph.D. - LinkedIn](https://www.linkedin.com/posts/kirkdborne_ai-hackathons-hosted-by-devpost-authorized-activity-7442611904491089920-8H56) - AI Hackathons - hosted by Devpost Authorized to Act: Auth0 for AI Agents by Okta PRIZES: $10000 in c...

9. [Agents Assemble - The Healthcare AI Endgame: Build ... - Devpost](https://agents-assemble.devpost.com) - Agents Assemble: The Healthcare AI Endgame Challenge. Build Interoperable Healthcare Agents at the I...

10. [The Healthcare AI Endgame (the “Hackathon”) Official Rules](https://agents-assemble.devpost.com/rules) - Agents Assemble - The Healthcare AI Endgame. Deadline: May 11, 2026 @ 8:00pm PDT · Join hackathon · ...

11. [Agents Assemble - The Healthcare AI Endgame](https://x.com/devpost/status/2029986452604412300) - Join the Agents Assemble - The Healthcare AI Endgame hackathon! Build tools that give healthcare AI ...

12. [The Healthcare AI Endgame - My hackathon projects - Devpost](https://devpost.com/submit-to/27874-agents-assemble-the-healthcare-ai-endgame/manage/submissions) - Agents Assemble - The Healthcare AI Endgame. Deadline: May 11, 2026 @ 8:00pm PDT · Join hackathon · ...

13. [Project gallery - Agents Assemble - The Healthcare AI Endgame](https://agents-assemble.devpost.com/project-gallery) - Agents Assemble - The Healthcare AI Endgame · Overview · My projects · Participants (152) · Resource...

14. [Agents Assemble - The Healthcare AI Endgame - Digitomize](https://digitomize.com/hackathons/27874) - devpost. Agents Assemble - The Healthcare AI Endgame. 4:00 AM. 68 d 15 h. 8:00 PM. the hackathon has...

15. [Rayen Gragba's (rayen-gragba) software portfolio | Devpost](https://devpost.com/rayen-gragba/challenges) - Agents Assemble - The Healthcare AI Endgame. Featured. Online. Build Interoperable Healthcare Agents...

