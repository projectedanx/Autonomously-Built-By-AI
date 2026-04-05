# Devpost 2026 Hackathons and an Auth0 Agentic AI Challenge Idea

## Overview

This report verifies current public hackathons on Devpost in early 2026 and selects one active event as the anchor for a high‑value problem definition and concrete project ideas. The chosen event is **Authorized to Act: Auth0 for AI Agents**, which focuses on secure, permissioned AI agents using Auth0’s Token Vault, making it well‑suited for impactful, security‑centric projects.[^1][^2][^3][^4][^5]

## Newly Active Devpost Hackathons (Early 2026)

Several high‑profile, currently active hackathons are visible on Devpost’s "new and upcoming" listings and related challenge pages.[^2][^1]

| Hackathon | Theme / Platform Focus | Deadline (2026) | Notes |
| --- | --- | --- | --- |
| Authorized to Act: Auth0 for AI Agents | Build agentic AI apps using Auth0 for AI Agents Token Vault | April 6 (late night PDT) | Wide‑open topic; single hard requirement is using Token Vault for secure, delegated access to APIs/services.[^3][^4][^5][^6][^7] |
| ZerveHack | AI‑native data science on the Zerve platform, shipping analyses, APIs, or apps | April 29 | Requires using Zerve to analyze real datasets and ideally deploy as an app or API.[^8][^9][^10][^11][^12][^13][^14] |
| Agents Assemble – The Healthcare AI Endgame | Interoperable healthcare agents using MCP, A2A, FHIR on Prompt Opinion | May 11 | Requires healthcare AI tools or agents integrated into Prompt Opinion, with synthetic or de‑identified data only.[^15][^16][^17][^18][^19][^20] |

These hackathons are promoted by Devpost itself (including social posts) and have active submission periods that extend beyond the current date, confirming they are current opportunities rather than past events.[^6][^19][^13]

## Why Focus on the Auth0 “Authorized to Act” Hackathon

The **Authorized to Act: Auth0 for AI Agents** hackathon invites builders to create any kind of agentic AI application, provided it uses **Auth0 for AI Agents Token Vault** as the identity and authorization layer. Token Vault handles OAuth flows, token management, and consent delegation so that agents can authenticate and call APIs or services "like a user" while staying within clear permission boundaries.[^3][^4][^5][^21]

Judging emphasizes three core dimensions: a strong **security model** (scoped access, protected credentials, high‑stakes actions guarded with step‑up authentication), robust **user control** (understandable permissions, clear consent, revocation), and **insight value** (surfacing patterns or lessons about how agent authorization should evolve). This makes it an ideal setting for a high‑value problem around real‑world, safely empowered AI agents.[^4][^3]

## High‑Value Problem to Solve

### Problem Statement

**"How can on‑call SRE and DevOps teams at SaaS companies safely delegate routine production operations to AI agents without ever handing over raw credentials, while preserving human control over high‑risk actions?"**

On‑call SREs and DevOps engineers often perform repetitive, cognitively simple but operationally risky tasks such as restarting services, scaling infrastructure, clearing queues, or rolling back a bad deployment. These actions typically require powerful API keys or cloud credentials; handing those directly to AI agents creates significant security and compliance risks, yet manually mediating every action undermines the productivity benefits of agents.[^8][^21][^22][^23]

The target community is therefore:

- **Community:** On‑call SREs and platform teams at mid‑size and enterprise SaaS companies who maintain production systems.

Auth0 for AI Agents’ Token Vault is uniquely aligned with this problem because it can store, scope, and rotate tokens, execute OAuth flows on behalf of users, and enforce step‑up or asynchronous consent for higher‑risk actions. This allows agents to act with "borrowed" and tightly scoped authority instead of static secrets.[^21][^3][^4]

## Idea 1 – "Runbook Guardian" (Secure Agent for On‑Call Runbooks)

### One‑Sentence Pitch

An AI "Runbook Guardian" that reads your existing incident runbooks and safely executes low‑risk production actions via Token Vault, while routing high‑risk operations through explicit, step‑up approvals.

### Target Prize Dimension and Why

- **Primary judging focus:** Security Model and User Control, two of the explicit judging criteria for the Authorized to Act hackathon.[^3]
- The project is intentionally designed to demonstrate tight permission boundaries, granular scopes, and clear consent UX for production automation, which maps directly onto these criteria.[^4][^3]

### Core Demo Moment

In the demo, a live on‑call dashboard shows an incident: high error rates on a service.

1. The user types or speaks: "Guardian, restart the payments‑service in staging and, if health checks pass for 10 minutes, roll traffic back from the canary."  
2. The agent responds with a clear plan and shows which actions it intends to take and which tokens/scopes it will request from Token Vault.  
3. For low‑risk actions (e.g., querying metrics), it proceeds automatically; for a higher‑risk action (e.g., production rollback), it triggers a **step‑up Auth0 login prompt** where the SRE must re‑authenticate and approve the specific scope.[^21][^3][^4]
4. After approval, the agent executes, and the UI shows an auditable log: which user granted which scopes, what the agent did, and when.

The "wow" factor is that the agent appears to be operating with full production powers, yet every sensitive action is demonstrably constrained and auditable without exposing long‑lived secrets.

### Platform Features Used and How They Are Visible

- **Auth0 for AI Agents – Token Vault:**  
  - All cloud and CI/CD tokens are stored and retrieved through Token Vault, never hard‑coded into the agent.[^3][^4]
  - The UI includes a "Token Vault Access" panel showing which short‑lived access tokens are currently checked out and for which scopes (e.g., `restart_service:staging`, `deploy:canary`).

- **Consent delegation and OAuth flows:**  
  - When the agent needs a new scope (for example, `rollback:production`), it triggers a visible OAuth flow in the browser using Auth0, where the SRE sees a human‑readable description of what the agent is asking permission to do.[^4][^21][^3]
  - The demo explicitly shows the consent screen and how revoking consent in the Auth0 user dashboard immediately cuts off the agent’s ability to act.

- **Step‑up authentication:**  
  - High‑stakes actions (e.g., "scale production cluster", "rotate database master") force a re‑authentication with a stronger factor (e.g., WebAuthn or OTP), making Auth0’s step‑up behavior very visible in the flow.[^3][^4]
  - The demo highlights this by first showing a low‑risk query that proceeds silently and then a high‑risk action that explicitly requires step‑up.

### What Makes This Not Just a Wrapper

This project relies on Auth0 for AI Agents for the core security and delegation model rather than treating it as a generic OAuth provider.

- The agent never holds raw cloud credentials; it only receives short‑lived, scoped tokens from Token Vault, which is exactly the new capability being showcased.[^21][^4][^3]
- The UX is designed around consent boundaries, revocation, and auditability, directly reflecting the hackathon’s focus on understanding how agent authorization should evolve, rather than simply bolting login onto an existing app.[^4][^3]

Without Auth0 for AI Agents, replicating this delegated, auditable permission model for agents would require significant custom security infrastructure that is out of scope for a typical small team.

### Honest Build Estimate (Person‑Days)

Assuming a small team of **2–3 people** working part‑time over approximately **5 days** (around the remaining time window before the April 6 deadline):[^5][^4]

- 1.5–2 person‑days: Integrating Auth0 for AI Agents Token Vault, wiring OAuth flows, and modeling scopes/permissions.  
- 1.5–2 person‑days: Building a simple web UI (incident panel, chat interface, audit log view) plus backend API to talk to the agent and a mocked infrastructure layer (e.g., fake Kubernetes or CI/CD endpoints).  
- 1–2 person‑days: Prompt/agent design, guardrail logic, demo scripting, and polish.

Total: roughly **4–6 person‑days** of focused effort, which fits within a typical small hackathon team’s capacity.

### Primary Risk

The main risk is under‑scoping the infrastructure simulation: trying to wire real cloud environments (AWS, GCP) instead of mocking core operations could consume the entire schedule and introduce breakage during the live demo. Keeping the "systems" mocked but realistic is critical to land the concept within hackathon time.[^22][^23]

## Idea 2 – "Access Ledger" (User‑Facing Consent and Activity Portal for Agents)

### One‑Sentence Pitch

A unified "Access Ledger" portal where end users can see, approve, and revoke what their AI agents are authorized to do across services, powered entirely by Auth0 for AI Agents Token Vault.

### Target Prize Dimension and Why

- **Primary judging focus:** User Control and Insight Value, two of the highlighted judging criteria.[^3]
- The idea centers on making delegated permissions and agent actions interpretable to non‑expert users, and surfacing insights about how agent authorization UX should evolve.[^4][^3]

### Core Demo Moment

In the demo, the user logs into the Access Ledger and sees a timeline of actions performed by one or more AI agents (for example, "Calendar Agent" or "Travel Planner Agent") along with the scopes those agents currently hold.

1. The user clicks an agent and views a card that says, in plain language, "This agent can: read your calendar events, send emails on your behalf to contacts marked as ‘Approved’, and access your task list."  
2. The user flips a toggle to revoke "send emails"; in the background, the app uses Auth0 APIs to update scopes in Token Vault.  
3. The demo then shows the agent trying to send an email, failing gracefully, and presenting a message like "Your human has revoked this permission"—demonstrating that revocation is immediate and enforced.

A follow‑up moment could show analytics such as "Top agent permissions granted this week" or "Scopes most commonly revoked after first use," feeding insights back into how to design better defaults.

### Platform Features Used and How They Are Visible

- **Token Vault as the source of truth for agent permissions:**  
  - The Access Ledger displays current scopes and tokens per agent directly from Token Vault, not from a separate custom store, making Auth0’s role visible.[^3][^4]
  - A "View raw scopes" button shows the underlying OAuth scopes, while the main UI renders human‑friendly explanations.

- **Consent delegation flows:**  
  - When the user clicks "Grant new permission" for an agent (e.g., allowing access to a new API), the portal redirects them through an Auth0‑powered OAuth and consent flow that lists the new capabilities being granted.[^21][^4][^3]
  - The demo highlights how granting consent from this central hub immediately propagates to the agent in downstream systems.

- **Revocation and step‑up authentication:**  
  - Revoking high‑impact permissions (e.g., "authorize payments" or "delete files") triggers a step‑up Auth0 authentication prompt before the change is applied, making stronger auth visibly tied to more sensitive scope changes.[^4][^3]
  - The demo walks through this experience so judges clearly see how Auth0 is used beyond a simple sign‑in screen.

### What Makes This Not Just a Wrapper

Most current agent demos treat identity and permissions as hidden plumbing; this idea makes Auth0 for AI Agents the **primary surface** the end user interacts with.

- The Ledger positions Token Vault as the canonical record of agent capabilities, with Auth0‑managed scopes driving the UX and analytics.[^21][^3][^4]
- The "insight value" comes from analyzing how users actually grant, trim, and revoke agent scopes over time, offering product feedback on safe default permissions and better consent copy; this directly aligns with the hackathon’s goal of surfacing patterns and pain points in agent authorization.[^3][^4]

This is difficult to replicate generically because it depends on having a stable, centralized permission and token store linked to user identities and consent history—exactly what Auth0 for AI Agents provides.

### Honest Build Estimate (Person‑Days)

Again assuming a **2–3 person** team working part‑time over **5 days**:

- 1.5–2 person‑days: Implement core Auth0 for AI Agents integration, including listing scopes per agent from Token Vault and driving consent/revocation flows.  
- 1.5–2 person‑days: Build the Access Ledger UI (agent list, timeline, detail views, analytics widgets) plus a simple mock agent that actually uses these permissions.  
- 1–1.5 person‑days: Analytics and insight layer (basic aggregations over mock events), demo scripting, and polishing UX copy for clarity.

Total: around **4–5.5 person‑days**, again realistic for a small hackathon team.

### Primary Risk

The main risk is over‑engineering the analytics layer or trying to ingest real log data from multiple services; this can be replaced with a controlled, simulated event stream representing actions agents might take. That keeps the scope manageable while still demonstrating how the Ledger would behave in production.[^8][^22]

## Final Notes

Both ideas are designed so that the most impressive parts of the demo are **directly tied** to Auth0 for AI Agents’ strengths: secure token handling, scoped delegation, consent UX, and step‑up authentication. They serve clearly defined communities (on‑call SRE teams and power users managing multiple agents) and stay within realistic build effort for the remaining hackathon timeline, while aligning tightly with the event’s judging criteria.[^21][^4][^3]

---

## References

1. [New & upcoming hackathons - Devpost](https://devpost.com/hackathons) - All hackathons ; Authorized to Act: Auth0 for AI Agents. 7 days left. Mar 02 - Apr 07, 2026 ; Agents...

2. [Devpost - The home for hackathons](https://devpost.com) - Featured online hackathons ; Authorized to Act: Auth0 for AI Agents. 7 days left. Mar 02 - Apr 07, 2...

3. [Authorized to Act: Auth0 for AI Agents: Build an agentic AI ... - Devpost](https://authorizedtoact.devpost.com) - Authorized to Act: Auth0 for AI Agents. Build an agentic AI application using Auth0 for AI Agents To...

4. [Build an agentic AI application using Auth0 for AI Agents Token Vault](https://authorizedtoact.devpost.com/updates) - Authorized to Act: Auth0 for AI Agents. Deadline: Apr 6, 2026 @ 11 ... © 2026 Devpost, Inc. All righ...

5. [Auth0 for AI Agents - My hackathon projects - Devpost](https://devpost.com/submit-to/28368-authorized-to-act-ai-agents-with-auth0/manage/submissions) - Authorized to Act: Auth0 for AI Agents. Deadline: Apr 6, 2026 @ 11:45pm PDT · Join hackathon · Autho...

6. [Build the identity layer for AI](https://x.com/devpost/status/2031038886928101778) - Authorized to Act: Auth0 for AI Agents. Build an agentic AI application using Auth0 for AI Agents To...

7. [Authorized to Act: Auth0 for AI Agents | Devpost - LinkedIn](https://www.linkedin.com/posts/devpost_authorized-to-act-auth0-for-ai-agents-activity-7429990057421352960-dxNF) - What happens when your AI agent actually has the "keys" to the door? Use Auth0's new Token Vault to ...

8. [ZerveHack: Stop thinking about it. Build it. Zerve AI ... - Devpost](https://zervehack.devpost.com) - ZerveHack · Stop thinking about it. Build it. Zerve AI Hackathon, $10,000 in prizes. · Requirements ...

9. [ZerveHack (the “Hackathon”) Official Rules - Devpost](https://zervehack.devpost.com/rules) - Entrants may enter by visiting zervehack.devpost.com (“Hackathon Website”) and following the below s...

10. [ZerveHack - Devpost](https://devpost.com/submit-to/28498-zervehack/manage/submissions) - ZerveHack. Deadline: Apr 29, 2026 @ 11:00am PDT · Join hackathon · ZerveHack. Descend. Overview · My...

11. [Resources - ZerveHack - Devpost](https://zervehack.devpost.com/resources) - ZerveHack. Deadline: Apr 29, 2026 @ 11:00am PDT · Join hackathon · ZerveHack. Descend. Overview · My...

12. [Project gallery - ZerveHack - Devpost](https://zervehack.devpost.com/project-gallery) - ZerveHack. Deadline: Apr 29, 2026 @ 11:00am PDT · Join hackathon · ZerveHack. Descend. Overview · My...

13. [ZerveHack | Devpost - LinkedIn](https://www.linkedin.com/posts/devpost_zervehack-activity-7434265058060328960-_x1K) - ... 🗓️ Deadline: April 29, 2026 Learn more: https://zurl.co/FVJiC · ZerveHack zervehack.devpost.com....

14. [Schedule - ZerveHack - Devpost](https://zervehack.devpost.com/details/dates) - ZerveHack. April 29 at 11:00AM PDT. Join hackathon · ZerveHack. Descend. Overview · My projects · Pa...

15. [Agents Assemble - The Healthcare AI Endgame: Build ... - Devpost](https://agents-assemble.devpost.com) - Agents Assemble: The Healthcare AI Endgame Challenge. Build Interoperable Healthcare Agents at the I...

16. [The Healthcare AI Endgame (the “Hackathon”) Official Rules](https://agents-assemble.devpost.com/rules) - Agents Assemble - The Healthcare AI Endgame. Deadline: May 11, 2026 @ 8:00pm PDT · Join hackathon · ...

17. [The Healthcare AI Endgame - My hackathon projects - Devpost](https://devpost.com/submit-to/27874-agents-assemble-the-healthcare-ai-endgame/manage/submissions) - Agents Assemble - The Healthcare AI Endgame. Deadline: May 11, 2026 @ 8:00pm PDT · Join hackathon · ...

18. [Project gallery - Agents Assemble - The Healthcare AI Endgame](https://agents-assemble.devpost.com/project-gallery) - Agents Assemble - The Healthcare AI Endgame · Overview · My projects · Participants (152) · Resource...

19. [Agents Assemble - The Healthcare AI Endgame](https://x.com/devpost/status/2029986452604412300) - Join the Agents Assemble - The Healthcare AI Endgame hackathon! Build tools that give healthcare AI ...

20. [Agents Assemble - The Healthcare AI Endgame - Digitomize](https://digitomize.com/hackathons/27874) - devpost. Agents Assemble - The Healthcare AI Endgame. 4:00 AM. 68 d 15 h. 8:00 PM. the hackathon has...

21. [Authenticated Delegation and Authorized AI Agents](https://arxiv.org/pdf/2501.09674.pdf) - The rapid deployment of autonomous AI agents creates urgent challenges around
authorization, account...

22. [Infrastructure for AI Agents](https://arxiv.org/pdf/2501.10114.pdf) - Increasingly many AI systems can plan and execute interactions in open-ended
environments, such as m...

23. [Security of AI Agents](https://arxiv.org/pdf/2406.08689.pdf) - AI agents have been boosted by large language models. AI agents can function
as intelligent assistan...

