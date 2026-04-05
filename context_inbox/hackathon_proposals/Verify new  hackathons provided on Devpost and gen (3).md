<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Verify new  hackathons provided on Devpost and generate a high value problem to solve and Ideas to solve the chosen problem to solve

Here are some of the newest Devpost hackathons right now and, based on them, a concrete high‑value problem plus three hackathon‑ready ideas you could build.

## New hackathons on Devpost (March–May 2026)

- **Authorized to Act: Auth0 for AI Agents** – Online hackathon where every project must use the **Auth0 for AI Agents Token Vault** so agents can authenticate and act on users’ behalf with proper OAuth flows, token management, consent delegation, and optional step‑up authentication; prize pool around 10,000 USD and submissions are open through early April 2026.[^1][^2][^3]
- **GitLab AI Hackathon: You Orchestrate. AI Accelerates.** – Global online hackathon to build AI agents and flows on the **GitLab Duo Agent Platform** that remove friction from the software development lifecycle, with a prize pool around 65,000 USD and a submission deadline of March 25, 2026.[^4][^5][^6]
- **Agents Assemble – The Healthcare AI Endgame** – Online challenge to build healthcare agents or MCP servers integrated into the **Prompt Opinion** multi‑agent platform, with strict requirements for synthetic/de‑identified data, FHIR‑aligned workflows, and a deadline of May 11, 2026.[^7][^8][^9][^10]

These are all currently listed among Devpost’s featured or upcoming online hackathons, with the Auth0 and GitLab challenges highlighted on Devpost’s “new \& upcoming hackathons” listings.[^11][^12][^1][^4]

## Chosen focus and high‑value problem

Let’s focus on **Authorized to Act: Auth0 for AI Agents**, because it tackles one of the most pressing issues in the emerging “AI agents” ecosystem: **how to let agents act with real credentials safely, transparently, and under user control.**[^13][^14][^1]

**High‑value problem statement (for this hackathon):**
> How can non‑expert users safely delegate real‑world actions (across tools like GitHub, Slack, email, and project management) to AI agents, with **least‑privilege access, explicit consent, and auditable guardrails**, using Auth0’s Token Vault instead of hard‑coded API keys?

This maps tightly to the hackathon’s requirement to build with **Auth0 for AI Agents’ Token Vault**, which is explicitly designed to handle OAuth flows, token storage, consent delegation, and even async and step‑up authentication for high‑risk actions—freeing builders to focus on UX and policy instead of low‑level auth plumbing.[^1][^13]

Below are three ideas that all solve that same problem for different communities. Each is scoped to be buildable by a small team in a few hackathon days.

***

## Idea 1 – “Agent Control Center for Open‑Source Maintainers”

**One‑sentence pitch**
A web dashboard that lets open‑source maintainers safely delegate triage and repo housekeeping (labeling, closing, cherry‑picking, backporting) to an AI agent, with Auth0‑powered approvals for anything risky.

**Target prize category and why**

- Target: **Main Auth0 prize / best use of Token Vault + strongest “Security Model” and “User Control”** judging criteria.[^1]
- Why: Maintainers are a clear community, and the core of the app is fine‑grained, visible permissioning for repo actions (exactly what the hackathon emphasizes as a security and consent challenge).[^13][^1]

**The “demo moment”**
You show an issue in a GitHub repo; the agent proposes: “Close as duplicate and comment with link,” categorized as a medium‑risk action. The maintainer hits “Approve,” sees an Auth0 step‑up screen for their GitHub scope, and then watches the agent perform the action live on GitHub—complete with an activity log that shows exactly which scoped token was used and why.[^13][^1]

**Platform features used and how each is visible**

- **Auth0 for AI Agents Token Vault** – All GitHub/Slack/Jira tokens are fetched from Token Vault; the UI explicitly shows that “Agent is using a delegated GitHub token with `repo:issues` scope,” never exposing secrets to the frontend or LLM.[^1]
- **Auth0 consent \& scopes UI** – When the maintainer first connects GitHub/Slack, they see and choose scopes on an Auth0 consent screen; your app then displays those scopes in a human‑readable permissions panel (“Agent can: label issues, comment; cannot: push to main”).[^13][^1]
- **Step‑up authentication for high‑risk actions** – Anything like deleting a branch or posting to a public Slack channel triggers a step‑up Auth0 flow; the demo clearly pauses until the maintainer confirms in a second factor (e.g., WebAuthn or OTP).[^14][^1]

**What makes this not a wrapper**
The core value is a **policy and consent layer for AI repo automation**, powered by Token Vault and explicit risk tiers (low/medium/high) rather than a generic “GitHub bot” UI; without Auth0’s delegated tokens and step‑up flow, you’d be stuck hard‑coding API keys or building your own brittle permission system.[^1][^13]

**Honest build estimate (person‑days)**

- 6–8 person‑days for an MVP:
    - 1–2 for Auth0 + Token Vault setup and GitHub app integration
    - 2–3 for dashboard UI and risk‑tier policies
    - 2–3 for simple LLM‑backed issue/PR triage logic and activity log

**Primary risk**
Getting the full GitHub + Auth0 + Token Vault flow working end‑to‑end (especially correct scopes and step‑up triggers) may take longer than expected; if integration snags happen late, it could reduce how much agent functionality you can actually demo.[^13][^1]

***

## Idea 2 – “Community Ops Agent for University Hackathon Clubs”

**One‑sentence pitch**
An AI “club ops” assistant that can schedule events, send announcements, and sync tasks across Slack, Google Calendar, and Notion for a university hackathon club—always under explicit, revocable permissions managed by Auth0 Token Vault.

**Target prize category and why**

- Target: **Auth0 main prize + User Control / Insight Value criteria**.[^1]
- Why: This targets a specific community (university hackathon organizers) and showcases how Token Vault can keep a multi‑tool agent from going rogue, surfacing real usability and governance insights about AI in student communities.[^15][^1]

**The “demo moment”**
A club lead types: “Plan a GitLab AI Hackathon watch party next Friday at 6 pm, announce it in \#events, and create prep tasks for officers,” and the agent:

1) Proposes the exact Calendar event, Slack message, and Notion task list.
2) Shows which tokens and scopes it will use (e.g., Slack `chat:write`, Calendar `events.insert`).
3) After the lead confirms, executes everything live—then logs all actions in a simple “Agent journal.”[^4][^1]

**Platform features used and how each is visible**

- **Auth0 for AI Agents Token Vault** – All connections (Slack workspace, Google Calendar, Notion) are managed through Token Vault, and the UI shows which account is active for each integration and which scopes are in play.[^1]
- **Async and delegated auth flows** – If someone else in the club wants to let the agent schedule events on *their* calendar, they receive an Auth0‑mediated delegation link and consent screen; you can demo how the agent can work across different humans’ accounts without sharing passwords.[^13][^1]
- **Revocation and permission editing** – A visible “Kill switch” lets the officer revoke the Slack token or narrow its scopes, and the next agent run fails gracefully and explains that its permission was revoked—demonstrating real‑time enforcement.[^14][^1]

**What makes this not a wrapper**
The distinctive value is **multi‑user, multi‑tool delegation governance for a small community**, not just a “Slack bot that also touches Google Calendar”—you are demonstrating concrete patterns for how student organizations can safely adopt agentic automation by leaning on Auth0’s identity and delegation model.[^13][^1]

**Honest build estimate (person‑days)**

- 7–9 person‑days for a polished MVP:
    - 2–3 for Auth0 + Token Vault setup with at least Slack + Google Calendar
    - 3–4 for event‑planning flows, preview/approve UX, and action log
    - 2 for a simple Notion (or other PM tool) integration and “agent journal” UI

**Primary risk**
OAuth and calendar APIs can be finicky, and coordinating three integrations might stretch a short hackathon; you may need to prioritize two integrations for a rock‑solid demo rather than three mediocre ones.

***

## Idea 3 – “Safe Delegation Studio for Customer Success Teams”

**One‑sentence pitch**
A web app where SaaS customer‑success managers can design and test “playbooks” that AI agents run on CRMs and helpdesks—like drafting outreach, updating tickets, and tagging risk accounts—while Token Vault enforces strict scopes and step‑up approvals for anything that touches customers.

**Target prize category and why**

- Target: **Auth0 main prize + strongest Security Model / Insight Value submission**.[^1]
- Why: This focuses on a clear professional community (customer success teams at B2B SaaS companies) and explores how to encode real‑world risk policies into agent permissions, directly reflecting the hackathon’s emphasis on permission boundaries and insight into agent authorization models.[^16][^13][^1]

**The “demo moment”**
On a “Playbook Designer” screen, you pick a playbook like “Renewal Risk Follow‑up,” connect a sandbox CRM account through Auth0, and watch as the agent:

1) Shows a dry‑run list of proposed actions (e.g., “Draft email to 5 at‑risk accounts; tag them as ‘Risk: Usage Drop’”).
2) Marks some actions as “high risk – requires approval” and pops a step‑up Auth0 flow just before sending emails.
3) After approval, executes the actions and shows before/after snapshots of records.

**Platform features used and how each is visible**

- **Auth0 Token Vault for CRM/helpdesk access** – CRM tokens (e.g., for HubSpot or a generic REST CRM) are stored and accessed via Token Vault, and each playbook clearly shows “This playbook can: read account metrics; write to `risk_tag` field; draft but not send emails.”[^13][^1]
- **Explicit risk‑tier mapping to Auth0 policies** – Your UI lets admins classify API calls into low/medium/high risk tiers, and you map those tiers to scopes and step‑up rules enforced by Auth0 (visible in a configuration panel and during demo).[^14][^1]
- **Auditability and insight** – Every agent run writes a human‑readable log (who delegated what, when, using which scopes), which you can export; this directly addresses the “Insight Value” criterion about surfacing pain points and patterns in agent authorization.[^1][^13]

**What makes this not a wrapper**
Instead of a generic “AI for CRM,” you are building a **design surface for safe delegation**, where the core IP is how you translate non‑technical risk language (“never email customers without human approval”) into concrete scopes and Token Vault‑mediated flows; without Auth0’s agent identity layer, this kind of playbook‑driven, multi‑tenant risk control would be much harder.[^16][^13][^1]

**Honest build estimate (person‑days)**

- 8–10 person‑days for a focused MVP:
    - 3–4 for Auth0 + Token Vault + one CRM integration (even mocked endpoints)
    - 3–4 for playbook designer UI, risk tiers, and preview/approve flow
    - 2 for logs, basic analytics, and a strong demo script

**Primary risk**
Crafting a UX that’s understandable to non‑technical CSMs while also accurately reflecting scopes and risk tiers is non‑trivial; you might spend more time on interaction design and copywriting than expected, which could limit technical depth if not scoped carefully.

***

If you tell me which hackathon and community you’re personally leaning toward (e.g., GitLab + open‑source maintainers versus Auth0 + student clubs), I can refine one of these into a concrete feature list, data model, and demo script tailored to that specific challenge page.
<span style="display:none">[^17][^18][^19][^20][^21][^22][^23][^24][^25][^26][^27][^28][^29][^30][^31][^32][^33][^34][^35][^36][^37][^38][^39][^40][^41][^42][^43][^44][^45][^46][^47][^48][^49][^50][^51][^52][^53][^54][^55][^56][^57][^58][^59][^60][^61][^62]</span>

<div align="center">⁂</div>

[^1]: https://authorizedtoact.devpost.com

[^2]: https://x.com/devpost/status/2031038886928101778

[^3]: https://devpost.com/fred-patton/challenges

[^4]: https://gitlab.devpost.com

[^5]: https://gitlab.devpost.com/resources

[^6]: https://devpost.com/submit-to/28106-gitlab-ai-hackathon/manage/submissions

[^7]: https://agents-assemble.devpost.com

[^8]: https://agents-assemble.devpost.com/rules

[^9]: https://devpost.com/submit-to/27874-agents-assemble-the-healthcare-ai-endgame/manage/submissions

[^10]: https://x.com/devpost/status/2029986452604412300

[^11]: https://devpost.com

[^12]: https://devpost.com/hackathons

[^13]: https://arxiv.org/pdf/2501.09674.pdf

[^14]: https://arxiv.org/pdf/2406.08689.pdf

[^15]: http://arxiv.org/pdf/1901.02710.pdf

[^16]: https://arxiv.org/pdf/2501.10114.pdf

[^17]: https://75her-challenge.devpost.com

[^18]: https://devnetwork-ai-ml-hack-2026.devpost.com

[^19]: https://devpost.com/c/artificial-intelligence

[^20]: https://hackthecoast.devpost.com

[^21]: https://machacks.devpost.com

[^22]: https://developerweek-2026-hackathon.devpost.com

[^23]: https://devpost.com/submit-to/28998-weber-state-ai-hackathon-2026/manage/submissions

[^24]: https://hackru-fall-2025.devpost.com

[^25]: https://mega-hackathon-2026-students.devpost.com

[^26]: https://devpost.com/submit-to/28437-hack-ai-2026/manage/submissions

[^27]: https://shellhacks2025.devpost.com

[^28]: https://sasehacks.devpost.com

[^29]: https://hack-for-humanity-26.devpost.com

[^30]: https://devpost.com/submit-to/29242-devnetwork-api-cloud-ai-hackathon-2026/manage/submissions

[^31]: https://www.tandfonline.com/doi/full/10.1080/15710882.2024.2378933

[^32]: https://arxiv.org/html/2503.23492v1

[^33]: http://arxiv.org/pdf/2410.03286.pdf

[^34]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4511834/

[^35]: https://arxiv.org/pdf/2103.10167.pdf

[^36]: https://arxiv.org/pdf/2103.01145.pdf

[^37]: https://arxiv.org/abs/2207.01015

[^38]: https://hackdevpost.devpost.com

[^39]: https://th26.devpost.com

[^40]: https://hackai-2026.devpost.com

[^41]: https://hacktivism2.devpost.com

[^42]: https://developerweek-2026-hackathon.devpost.com/register?flow[data][challenge_id%5D=27050\&flow%5Bname%5D=register_for_challenge

[^43]: https://hackgenration.devpost.com

[^44]: https://reality-hack-2026.devpost.com

[^45]: https://devpost.com/hackathons?themes[]=Beginner+Friendly

[^46]: https://gitlab.devpost.com/rules

[^47]: https://devpost.com/software/ai-devops-agent-with-secure-auth0-access

[^48]: https://devpost.com/software/gitlab-ai-hackathon-planner-your-ai-powered-co-pilot

[^49]: https://devpost.com/software/agent-firewall

[^50]: https://devpost.com/software/agentbridge

[^51]: https://agents-assemble.devpost.com/project-gallery

[^52]: https://devpost.com/software/authaiagent

[^53]: https://agents-assemble.devpost.com/resources

[^54]: https://arxiv.org/pdf/2403.17918.pdf

[^55]: https://arxiv.org/pdf/2412.01769.pdf

[^56]: https://arxiv.org/pdf/2411.05285.pdf

[^57]: https://arxiv.org/html/2412.08445

[^58]: https://aclanthology.org/2023.emnlp-demo.51.pdf

[^59]: https://www.competehub.dev/en/competitions/devpost27874

[^60]: https://www.linkedin.com/posts/devpost_authorized-to-act-auth0-for-ai-agents-activity-7429990057421352960-dxNF

[^61]: https://gitlab.devpost.com/forum_topics

[^62]: https://digitomize.com/hackathons/27874

