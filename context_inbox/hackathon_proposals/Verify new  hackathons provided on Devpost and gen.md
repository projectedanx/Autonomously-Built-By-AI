<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Verify new  hackathons provided on Devpost and generate a high value problem to solve and Ideas to solve the chosen problem to solve

Here’s a structured hackathon-ready concept based on a **currently active Devpost challenge** and a clearly scoped, high‑value problem.

## Verified new Devpost hackathons

Devpost’s “new and upcoming” listings and individual challenge pages show several active public hackathons in early 2026, including:[^1_1][^1_2]

- **Authorized to Act: Auth0 for AI Agents** – build any agentic AI app, as long as it uses **Auth0 for AI Agents Token Vault** as the identity and authorization layer; deadline **April 6, 2026** (late night PDT).[^1_3][^1_4][^1_5][^1_6][^1_7]
- **ZerveHack** – build data products (analyses, APIs, or apps) on the **Zerve AI‑native data science platform**, using real datasets and ideally deploying your work; deadline **April 29, 2026**.[^1_8][^1_9][^1_10][^1_11][^1_12][^1_13][^1_14]
- **Agents Assemble – The Healthcare AI Endgame** – build interoperable healthcare agents or MCP tools integrated into the **Prompt Opinion multi‑agent platform**, using synthetic/de‑identified data; deadline **May 11, 2026**.[^1_15][^1_16][^1_17][^1_18][^1_19][^1_20]

These events are promoted directly by Devpost and partner channels, and all three have submission windows that are open right now, confirming them as current opportunities rather than past hackathons.[^1_6][^1_19][^1_13]

For your purposes, **Authorized to Act: Auth0 for AI Agents** is particularly well‑suited: it is broad in theme but very specific in platform requirement (Auth0 for AI Agents’ **Token Vault**), and its judging criteria focus on **Security Model**, **User Control**, and **Insight Value**.[^1_4][^1_3]

***

## Chosen hackathon and high‑value problem

### Chosen hackathon

- **Hackathon:** Authorized to Act: Auth0 for AI Agents[^1_5][^1_3][^1_4]
- **Platform:** Auth0 for AI Agents, with mandatory use of **Token Vault** (handles OAuth flows, token storage, consent delegation, and step‑up auth for agents).[^1_21][^1_3][^1_4]
- **Judging focus:**
    - Security Model (scoped access, protected credentials, high‑stakes actions guarded).[^1_3]
    - User Control (clear consent, understandable permissions, revocation).[^1_3]
    - Insight Value (patterns and lessons about agent authorization).[^1_4][^1_3]


### High‑value problem (who, what, why)

**Problem statement (one sentence):**
How can **on‑call SRE and DevOps teams at SaaS companies** safely delegate routine production operations to AI agents **without ever handing over raw credentials**, while preserving human control over high‑risk actions?

- **Community served:** On‑call SREs, DevOps, and platform engineers at mid‑size/enterprise SaaS companies who maintain production systems and repeatedly execute runbooks (restart services, roll back deployments, scale infrastructure, clear queues, etc.).[^1_22][^1_8][^1_21]
- **Why it matters:** These teams are exactly the kind of power users who benefit most from agentic automation, but are also the ones who **cannot** risk leaking long‑lived cloud credentials or giving unconstrained powers to an LLM agent. Auth0 for AI Agents’ Token Vault is designed to solve this by acting as a secure, auditable delegation layer where agents get scoped, time‑bound access instead of static keys.[^1_23][^1_21][^1_22][^1_4][^1_3]

Below are **two concrete, demonstrable ideas** that attack this same problem from different angles, both optimized for this hackathon’s criteria and constraints.

***

## Idea 1 – “Runbook Guardian” (secure agent for on‑call runbooks)

### One‑sentence pitch

An AI **Runbook Guardian** that reads your existing incident runbooks and safely executes low‑risk production actions via Auth0’s Token Vault, while routing high‑risk operations through explicit, step‑up approvals.

### Target prize category / judging focus and why

- **Target:** Score maximally on **Security Model** and **User Control** in the Authorized to Act judging rubric.[^1_3]
- **Why:** The core concept is to show that powerful runbook automation can be done **without static secrets**, with visibly scoped permissions and clear user approvals for sensitive actions, exactly matching the hackathon’s definition of a strong security model and user control.[^1_21][^1_4][^1_3]


### The “demo moment”

In the video, a simple on‑call dashboard shows an active incident:

1. The on‑call SRE types:
“Guardian, restart the payments‑service in staging and, if health checks pass for 10 minutes, roll traffic back from the canary.”
2. The agent responds with a **plan** plus a panel showing which **scopes** it will request from Token Vault (e.g., `restart_service:staging`, `deploy:canary`).[^1_4][^1_3]
3. It automatically uses existing scopes to **inspect metrics and logs**, then when it needs a higher‑risk `rollback:production` scope, the browser pops an **Auth0 step‑up prompt**: the user re‑authenticates and grants just that permission.[^1_21][^1_4][^1_3]
4. After approval, the agent executes the rollback and the UI shows an **audit log**: who approved what, when, and which actual API calls were made.

That visible “I never gave the agent a key, but it still safely did the rollback with my explicitly granted scope” is the main wow moment.

### Platform features used (and how each is visible in the demo)

- **Auth0 for AI Agents – Token Vault**
    - All infra tokens (Kubernetes, CI/CD, monitoring APIs) live in Token Vault; the agent requests short‑lived tokens for specific scopes instead of storing secrets.[^1_4][^1_21][^1_3]
    - The UI has a **“Current delegation”** sidebar listing active tokens/scopes the agent holds, pulled in real time from Token Vault, so judges **see** the delegation model.
- **Consent delegation \& OAuth flows**
    - When the agent needs a new capability, it triggers an Auth0 OAuth consent screen that clearly describes the new permission (“Allow Runbook Guardian to roll back production traffic for service X”).[^1_21][^1_3][^1_4]
    - The demo explicitly walks through this flow and then shows that revoking consent in the Auth0 user dashboard immediately prevents further use of that scope.
- **Step‑up authentication**
    - Low‑risk queries (metrics/health checks) proceed silently, but high‑stakes actions (production rollback, cluster scale‑up) trigger **step‑up auth**—for example WebAuthn or OTP—before the new scope is granted.[^1_3][^1_4]
    - The difference between “no friction” and “step‑up required” is clearly visible in the video, reinforcing the security model.


### What makes this not a wrapper

- The **entire architecture** is built around Auth0 for AI Agents: the agent never sees raw cloud credentials, only scoped, time‑bound tokens from Token Vault.[^1_4][^1_21][^1_3]
- The main product value is **precisely** the secure delegation and auditability that Token Vault enables; this isn’t “a random bot with Auth0 login bolted on,” it’s a showcase of authenticated, controlled delegation to agents, which is what the hackathon is about.[^1_3][^1_4]

Without Auth0 for AI Agents, you’d either give the agent static keys (unacceptable) or need to build your own token vault and consent UX—far beyond hackathon scope.

### Honest build estimate (person‑days)

Assuming a small team of **2–3 people** over about **5 calendar days** (roughly the remaining window before the deadline):[^1_5][^1_4]

- **1.5–2 person‑days** – Auth0 for AI Agents integration: configuring an application, wiring Token Vault calls, implementing scoped tokens and revocation.
- **1.5–2 person‑days** – Building a simple web UI: incident panel, chat interface, sidebars showing current scopes and an audit log; plus a backend service simulating infra APIs.
- **1–2 person‑days** – Agent logic and prompts, runbook ingestion (even if just YAML/Markdown), and demo scripting/polish.

Realistic total: **4–6 person‑days** of focused work, which can be covered by 2–3 people working ~4 hours/day across 5 days.

### Primary risk

- **Risk:** Trying to integrate with real AWS/GCP/Kubernetes in production instead of mocking core operations could burn most of the time and introduce brittle failure points during the demo.[^1_23][^1_22]
- **Mitigation:** Use **mocked but realistic** infra endpoints (e.g., a local service that logs “scaled cluster from N→M”); highlight clearly in the demo that the same pattern could be wired to real systems post‑hackathon.

***

## Idea 2 – “Access Ledger” (user‑facing consent and activity portal for agents)

### One‑sentence pitch

An **Access Ledger** web portal where users can see, approve, and revoke what their AI agents are authorized to do across services, powered entirely by Auth0 for AI Agents’ Token Vault.

### Target prize category / judging focus and why

- **Target:** Excel on **User Control** and **Insight Value** in the Authorized to Act judging criteria.[^1_3]
- **Why:** This idea makes agent permissions and activity explainable to non‑experts, and generates analytics about how humans actually grant and revoke permissions—directly answering the hackathon’s call for insight into agent authorization patterns.[^1_4][^1_3]


### The “demo moment”

In the video, a user logs into the Access Ledger and sees **cards for each agent** (“Calendar Agent”, “Travel Booker”, “Inbox Triage Agent”) plus a timeline of recent actions.

1. Opening the **Calendar Agent** card shows: “This agent can read your calendar events and create new events, but cannot delete or invite new attendees.” Scopes and human‑readable descriptions sit side‑by‑side.
2. The user flips a toggle to revoke “create new events.” Behind the scenes, the app calls Auth0 to update scopes in Token Vault.[^1_4][^1_3]
3. The demo then shows the agent trying to schedule a meeting and failing gracefully with: “Your permission to create events has been revoked.”
4. Finally, an analytics view shows simple insights like: “Most frequently revoked scopes this week” and “Common first‑time grants,” based entirely on synthetic event data.

The judge sees **real‑time, visible control** over an agent’s capabilities plus insight into how people interact with those permissions.

### Platform features used (and how each is visible in the demo)

- **Token Vault as source of truth**
    - The portal queries Token Vault for each agent to show current tokens and scopes; a “Show technical scopes” button displays raw OAuth scopes, while the main UI shows friendly descriptions.[^1_21][^1_3][^1_4]
    - When a permission is revoked, the portal immediately updates the list from Token Vault so the change is visibly confirmed.
- **Consent delegation flows**
    - Clicking “Grant a new capability” for an agent launches an Auth0 consent flow where the user sees a clear list like “Allow Travel Agent to read your itinerary; allow it to modify your calendar.”[^1_21][^1_3][^1_4]
    - The video explicitly walks through this re‑consent and then shows how the agent can immediately use the new capabilities.
- **Revocation plus step‑up authentication**
    - Revoking a high‑impact permission—say “authorize payments” for a future commerce agent—forces a **step‑up auth** prompt so judges see that sensitive changes go through stronger verification.[^1_3][^1_4]
    - The difference between revoking low‑ and high‑impact scopes is a key part of the demo narrative.


### What makes this not a wrapper

- The product **is** an opinionated UX directly on top of Auth0 for AI Agents: all state about what agents can do comes from Token Vault and Auth0’s consent records, not a separate home‑grown ACL system.[^1_21][^1_4][^1_3]
- Its main value is turning Auth0’s delegation primitives into a **human‑understandable control plane** and analytics surface, which is exactly the kind of “insight value” the hackathon wants people to explore.[^1_4][^1_3]

You could not convincingly fake this with a generic OAuth provider in a weekend; it relies on Auth0’s agent‑oriented token and consent model.

### Honest build estimate (person‑days)

With **2–3 people** over **~5 days**:

- **1.5–2 person‑days** – Integrate Auth0 for AI Agents: list per‑agent scopes, wire grant/revoke calls, and ensure the app uses Token Vault as the auth source.[^1_3][^1_4]
- **1.5–2 person‑days** – Build the Ledger UI (agent list, detail cards, activity timeline) and a simple mock agent that checks scopes before acting.
- **1–1.5 person‑days** – Implement a small analytics layer on a synthetic event stream plus demo polish and UX copy tuning.

Realistic total: **4–5.5 person‑days** of focused effort, again within reach for a small team.

### Primary risk

- **Risk:** Over‑scoping the analytics and data side—trying to feed in real logs from multiple external services instead of synthetic events—could eat up critical time and introduce complexity unrelated to the core Auth0 story.[^1_8][^1_23]
- **Mitigation:** Keep a small, in‑memory event store that simulates “agent X called API Y with scope Z,” and generate a couple of pre‑baked insight widgets from that.

***

If you’d like, the next step can be to pick **one** of these ideas and break it down into an implementation checklist (tech stack, endpoints, data models, and a detailed 3–5 minute demo script) tailored to your preferred stack.
<span style="display:none">[^1_24][^1_25][^1_26][^1_27][^1_28][^1_29][^1_30][^1_31][^1_32][^1_33][^1_34][^1_35][^1_36][^1_37][^1_38][^1_39][^1_40][^1_41][^1_42][^1_43][^1_44][^1_45][^1_46][^1_47][^1_48][^1_49][^1_50][^1_51][^1_52][^1_53][^1_54][^1_55][^1_56][^1_57][^1_58][^1_59][^1_60][^1_61][^1_62]</span>

<div align="center">⁂</div>

[^1_1]: https://devpost.com/hackathons

[^1_2]: https://devpost.com

[^1_3]: https://authorizedtoact.devpost.com

[^1_4]: https://authorizedtoact.devpost.com/updates

[^1_5]: https://devpost.com/submit-to/28368-authorized-to-act-ai-agents-with-auth0/manage/submissions

[^1_6]: https://x.com/devpost/status/2031038886928101778

[^1_7]: https://www.linkedin.com/posts/devpost_authorized-to-act-auth0-for-ai-agents-activity-7429990057421352960-dxNF

[^1_8]: https://zervehack.devpost.com

[^1_9]: https://zervehack.devpost.com/rules

[^1_10]: https://devpost.com/submit-to/28498-zervehack/manage/submissions

[^1_11]: https://zervehack.devpost.com/resources

[^1_12]: https://zervehack.devpost.com/project-gallery

[^1_13]: https://www.linkedin.com/posts/devpost_zervehack-activity-7434265058060328960-_x1K

[^1_14]: https://zervehack.devpost.com/details/dates

[^1_15]: https://agents-assemble.devpost.com

[^1_16]: https://agents-assemble.devpost.com/rules

[^1_17]: https://devpost.com/submit-to/27874-agents-assemble-the-healthcare-ai-endgame/manage/submissions

[^1_18]: https://agents-assemble.devpost.com/project-gallery

[^1_19]: https://x.com/devpost/status/2029986452604412300

[^1_20]: https://digitomize.com/hackathons/27874

[^1_21]: https://arxiv.org/pdf/2501.09674.pdf

[^1_22]: https://arxiv.org/pdf/2501.10114.pdf

[^1_23]: https://arxiv.org/pdf/2406.08689.pdf

[^1_24]: https://dwny-2026-hackathon.devpost.com

[^1_25]: https://305hackmar2026.devpost.com

[^1_26]: https://developerweek-2026-hackathon.devpost.com

[^1_27]: https://liveai-ivyplus-2026.devpost.com

[^1_28]: https://75her-challenge.devpost.com

[^1_29]: https://devhouse.devpost.com

[^1_30]: https://tecstorm26.devpost.com

[^1_31]: https://devstudiologitech2026.devpost.com

[^1_32]: https://techthrive-march-26.devpost.com

[^1_33]: https://hackviolet-2026.devpost.com

[^1_34]: https://devpost.com/c/artificial-intelligence

[^1_35]: https://hack-for-humanity-26.devpost.com/rules

[^1_36]: https://rosehack.devpost.com

[^1_37]: https://arxiv.org/html/2503.23492v1

[^1_38]: https://www.tandfonline.com/doi/full/10.1080/15710882.2024.2378933

[^1_39]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4511834/

[^1_40]: http://arxiv.org/pdf/2410.03286.pdf

[^1_41]: https://arxiv.org/pdf/2103.10167.pdf

[^1_42]: https://arxiv.org/pdf/2103.01145.pdf

[^1_43]: http://arxiv.org/pdf/1901.02710.pdf

[^1_44]: https://arxiv.org/abs/2207.01015

[^1_45]: https://hack-for-humanity-26.devpost.com

[^1_46]: https://octopushack.devpost.com

[^1_47]: https://mega-hackathon-2026-students.devpost.com

[^1_48]: https://devpost.com/submit-to/26781-mega-hackathon-2026/manage/submissions

[^1_49]: https://hackonomics26.devpost.com

[^1_50]: https://figbuild2026.devpost.com

[^1_51]: https://cruzhacks--2026.devpost.com

[^1_52]: https://devpost.com/submit-to/28251-figbuild-2026/manage/submissions

[^1_53]: https://hackillinois-2026.devpost.com

[^1_54]: https://devpost.com/247r1a66p0/challenges

[^1_55]: https://devpost.com/software/ai-devops-agent-with-secure-auth0-access

[^1_56]: https://devpost.com/software/current-ai-87kjts

[^1_57]: https://arxiv.org/pdf/2403.17918.pdf

[^1_58]: https://arxiv.org/pdf/2412.01769.pdf

[^1_59]: https://arxiv.org/pdf/2411.05285.pdf

[^1_60]: https://arxiv.org/html/2412.08445

[^1_61]: https://aclanthology.org/2023.emnlp-demo.51.pdf

[^1_62]: https://devpost.com/software/shieldclaw-ehigc2

