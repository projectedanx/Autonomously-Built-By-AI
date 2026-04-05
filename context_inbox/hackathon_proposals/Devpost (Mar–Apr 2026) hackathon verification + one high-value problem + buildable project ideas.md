# Devpost (Mar–Apr 2026) hackathon verification + one high-value problem + buildable project ideas

## Verified “new / currently active” Devpost hackathons

The hackathons below are verified as listed on Devpost with submission windows or deadlines in late March through May 2026 (plus one April event with submissions opening soon).[^1][^2][^3][^4][^5][^6][^7][^8]

| Hackathon (Devpost) | What it’s about (from listing) | Key dates / deadline (Devpost) | Prize info (Devpost) | “Must use” platform requirement (if any) |
|---|---|---|---|---|
| Authorized to Act: Auth0 for AI Agents | Build an agentic AI application using Auth0 for AI Agents, with Token Vault required. [^2] | Feb 23 – Apr 6, 2026; deadline Apr 6, 2026 @ 11:45pm PDT. [^9][^10] | $10,000 in prizes; Grand Prize $5,000, 2nd $2,000, 3rd $1,000, plus Feedback and Blog Post prizes. [^11] | Must use Auth0 for AI Agents **Token Vault** to be eligible to win. [^11] |
| Hackonomics 2026 | Projects that spread awareness about financial literacy and economics. [^4] | Runs through Mar 30, 2026 (Devpost submission deadline page shows Mar 30, 2026). [^12] | Prize details listed as placements and awards (1st/2nd/3rd, Design Award, Technical Award). [^4] | No specific API/SDK requirement stated on the overview page. [^4] |
| CircuitBreak 2025 | Month-long open sprint with 20 themed problem areas; requires a working prototype/demo. [^13] | Submissions Jan 1 – Mar 31, 2026; deadline Mar 31, 2026 @ 11:45pm EDT. [^3] | Listed as non-cash prize(s) on Devpost submission/deadline page. [^14] | Theme-based; no required platform integration stated in the overview. [^13] |
| GNEC Hackathon 2026 Spring | Sustainability through tech aligned to UN SDGs; this season’s theme is SDG 3 (Health and Well-being). [^5] | Mar 12 – May 3, 2026. [^5][^15] | $700+ in prizes plus internship prizes. [^5] | No specific SDK requirement stated in the overview. [^5] |
| DevNetwork [AI + ML] Hackathon 2026 | Large in-person & online hackathon co-located with AI DevSummit; multiple sponsor challenges. [^1] | Online May 11 – May 28, 2026; in-person May 27–28, 2026. [^1] | Prizes vary by overall winner and sponsor challenges (described on the Devpost page). [^1] | No single “must use X” requirement; sponsor challenges may have their own requirements. [^1] |
| Hackiethon 2026 | Beginner-friendly hackathon focused on using AI APIs integrated into a game; teams 1–3. [^6] | Final submission deadline Mar 30, 2026 at 11:59pm (AEST) is stated in the Devpost page text. [^6] | $700 in prizes with multiple game-focused categories. [^6] | No single required API stated in the overview (the theme encourages AI API use). [^6] |
| HackAmerica (high school; US only) | Week-long hackathon for high school students; submissions include a demo video max 3 minutes. [^8][^16] | Hackathon duration Apr 11–18, 2026; registration deadline Apr 6, 2026; submission deadline Apr 18, 2026. [^8] | Prize details are not in the excerpted rules section used here. [^8] | No required platform integration stated in the rules excerpt. [^8] |
| ImpactHacks by HackathonForAll | A Devpost-listed event with an Apr 23, 2026 deadline shown on the Devpost submissions page. [^7] | Deadline Apr 23, 2026 @ 11:45pm PDT. [^7] | “$1,000 in …” is partially shown in the submissions page snippet; full prize breakdown not verified in this source set. [^7] | Not verified from the snippet source set. [^7] |

## Chosen “highest leverage” hackathon to target

**Authorized to Act: Auth0 for AI Agents** is a strong target for a “high-value” build because it has a clear required feature (Token Vault) and judges explicitly score security model and user control, which pushes teams toward production-like agent behavior rather than a simple chatbot.[^11]

The submission format also encourages a short, judge-friendly demo video (around three minutes) plus a public code repo and a published link, which supports building something that is easy to evaluate quickly.[^11]

## High-value problem to solve

### Problem statement

AI agents are increasingly capable of doing real actions (sending messages, creating tickets, updating docs), but typical “agent demos” fail at the two things that matter most for real-world adoption: **(1) user-granted permission boundaries** and **(2) a clear, auditable record of what happened and why**.[^11]

This creates a trust gap: users either over-grant broad access (unsafe) or refuse to use the agent at all (no adoption), and developers struggle to implement correct OAuth/token handling and step-up auth patterns under time pressure.[^11]

### Nameable community

The community that feels this pain immediately is **small teams running on SaaS tools** (open-source maintainers, DevOps/SRE teams, and startup operations teams) who want automation but cannot risk unintended or untraceable actions in GitHub/Slack/Google Workspace.[^17][^11]

## 3 buildable project ideas (all solve the same core problem)

Each concept below is designed to make the “security model + user control” visible in the demo and to use Token Vault in a way a judge can recognize.[^11]

### Idea 1 — “Action Approval Inbox” (agent guardrails + receipts)

- One-sentence pitch: A cross-tool AI agent that drafts actions (Slack message, GitHub issue, calendar invite) but can only execute after the user approves each high-risk action, producing a signed “consent receipt” and audit timeline.
- Target prize category and why: Grand Prize, because it directly showcases the judging criteria of security model, user control, and Token Vault execution depth.[^11]
- The demo moment: The agent proposes “I can DM the on-call channel and open a GitHub issue,” then pauses; the user sees an approvals screen with scopes/risk level, clicks “Approve with step-up,” and the action executes with an audit receipt.
- Platform features used (visible): Auth0 for AI Agents Token Vault to store/serve per-user tokens (visible via “Connected accounts” + tool execution), step-up authentication for high-risk actions (visible as an extra approval step), consent delegation + scoped permissions (visible as explicit scope text on the approval card).[^11]
- What makes this not a wrapper: The product’s core interaction is “agents can’t act without authenticated delegation,” which is the point of Token Vault and step-up auth rather than an optional add-on.
- Honest build estimate (person-days): 6–9 person-days for a clean demo (web app + 2 real integrations like GitHub + Slack, plus audit log UI).
- Primary risk: OAuth setup + token plumbing for multiple providers takes longer than expected, leaving only one integration for the demo.

### Idea 2 — “GitHub Maintainer Copilot (safe triage)”

- One-sentence pitch: An AI maintainer assistant that triages new issues and PRs, proposes labels/replies, and only performs state-changing actions (label, close, merge) through an explicit permission-and-approval flow.
- Target prize category and why: Grand Prize or Second Place, because it demonstrates a concrete, high-frequency real-world workflow with clear permission boundaries and a strong security narrative.[^11]
- The demo moment: The agent summarizes three new issues, proposes labels and a templated response, then asks for approval; user approves “label + comment” but denies “close,” and the audit log shows the denied action and policy reasoning.
- Platform features used (visible): Token Vault for GitHub access tokens (visible via “Connect GitHub” and successful API calls), explicit scoping (visible in requested scopes), step-up auth for destructive actions like closing/merging (visible via forced re-auth/approval), and an audit trail (visible timeline).[^11]
- What makes this not a wrapper: Without delegated, scoped, auditable GitHub access, the assistant can only give advice; with Token Vault, it becomes a real tool that acts safely on the user’s behalf.
- Honest build estimate (person-days): 5–8 person-days for a working web UI + GitHub integration + policy/risk tiers.
- Primary risk: Getting the “policy” layer right in a way that feels trustworthy (not arbitrary) while staying within hackathon time.

### Idea 3 — “SaaS Access Minimizer (least-privilege agent setup)”

- One-sentence pitch: A “wizard” that helps a user connect accounts for an agent with the minimum viable scopes for a chosen task, then continuously flags scope creep and suggests safer alternatives.
- Target prize category and why: Third Place + Blog Post Prize, because it can surface reusable patterns and “insight value” about how agent authorization should evolve while still shipping a solid demo.[^11]
- The demo moment: User selects “weekly status report,” the wizard recommends read-only scopes; the agent later requests a write scope (“post to Slack”), and the UI explains the difference and offers step-up approval for only that action.
- Platform features used (visible): Token Vault connected accounts (visible as per-provider connections), scoped OAuth consent delegation (visible as a scope diff UI), step-up authentication for newly requested elevated scopes (visible re-consent moment), and logging/receipts for scope changes (visible history).[^11]
- What makes this not a wrapper: The entire product is about solving OAuth/token/scope delegation ergonomically, which is tightly coupled to Auth0 for AI Agents primitives.
- Honest build estimate (person-days): 4–7 person-days for a strong demo with 1–2 providers and a polished scope-diff UX.
- Primary risk: If only one provider is integrated, the “scope creep” story can feel less compelling unless the UX is very clear.

## Why these ideas are “high value” for judges

All three concepts are designed so the demo visibly hits the hackathon’s scoring areas: permission boundaries (security model), explicit consent + step-up flows (user control), credible Token Vault usage (technical execution), and an audit narrative (insight value).[^11]

The biggest differentiator versus typical agent entries is that the core product is not “chat with an agent,” but “safely authorize and constrain an agent that can actually do things,” which aligns with the hackathon’s stated requirement and criteria.[^11]

---

## References

1. [DevNetwork [AI + ML] Hackathon 2026: Join the nation's largest ...](https://devnetwork-ai-ml-hack-2026.devpost.com) - Join the largest challenge-driven in-person & online hackathon, co-located with AI DevSummit 2026! O...

2. [Authorized to Act: Auth0 for AI Agents: Build an agentic AI ... - Devpost](https://authorizedtoact.devpost.com) - Auth0 for AI Agents provides the identity layer that lets your agents authenticate, authorize, and i...

3. [Schedule - CircuitBreak 2025 - Devpost](https://circuitbreak-2025.devpost.com/details/dates) - CircuitBreak 2025. Deadline: Mar 31, 2026 @ 11:45pm EDT. Join hackathon · CircuitBreak 2025. Descend...

4. [Hackonomics 2026: The official Hackonomics™ 2026 Hackathon ...](https://hackonomics26.devpost.com) - The official Hackonomics™ 2026 Hackathon. An experience to help educate and grow insight into Comput...

5. [GNEC Hackathon 2026 Spring - Compete For UN ... - Devpost](https://gnec-hackathon-2026-spring.devpost.com) - Mar 12 – May 3, 2026. Join hackathon · GNEC Hackathon 2026 Spring - Compete For UN-Affiliated/NGO In...

6. [Hackiethon 2026: Hackiethon is a low-barrier, beginner ... - Devpost](https://hackiethon-2026.devpost.com) - Once you've joined the hackathon on Devpost: Go to the Participants tab ... Final submission deadlin...

7. [My hackathon projects - Devpost](https://devpost.com/submit-to/28988-impacthacks-by-hackathonforall/manage/submissions) - Discussions · Join hackathon. 20 more days to deadline. View schedule. Deadline. Apr 1, 2026 @ 11:45...

8. [America's Largest Hackathon for High School Students - HackAmerica](https://hackamerica.devpost.com/rules) - Dates. Hackathon Duration: April 11-18, 2026. Registration Deadline: 4/6/2026 @ 5:00 PM CDT. Project...

9. [Build an agentic AI application using Auth0 for AI Agents Token Vault](https://authorizedtoact.devpost.com/details/survey) - Authorized to Act: AI Agents with Auth0. Feb 23 – Apr 6, 2026. Join hackathon · Authorized to Act: A...

10. [Auth0 for AI Agents - My hackathon projects - Devpost](https://devpost.com/submit-to/28368-authorized-to-act-ai-agents-with-auth0/manage/submissions) - Authorized to Act: Auth0 for AI Agents. Deadline: Apr 6, 2026 @ 11:45pm PDT · Join hackathon · Autho...

11. [#75HER Challenge Hackathon 2026: Discover | Design ... - Devpost](https://75her-challenge.devpost.com) - The #75HER Challenge Hackathon is part of CreateHER Fest's 75-day build journey culminating in an In...

12. [Hackonomics 2026 - Devpost](https://devpost.com/submit-to/25957-hackonomics-2026/manage/submissions) - Deadline: Mar 30, 2026 @ 2:00pm PDT · Join hackathon · Hackonomics 2026. Descend. Overview · My proj...

13. [CircuitBreak 2025: A rapid-fire tech marathon where ... - Devpost](https://circuitbreak-2025.devpost.com) - The challenge runs online for an entire month, giving students the freedom to work solo or form team...

14. [CircuitBreak 2025 - Devpost](https://devpost.com/submit-to/27780-circuitbreak-2025/manage/submissions) - Deadline: Mar 31, 2026 @ 8:45pm PDT · Join hackathon · CircuitBreak 2025. Descend. Overview · My pro...

15. [GNEC Hackathon 2026 Spring - Devpost](https://devpost.com/submit-to/28834-gnec-hackathon-2026-spring-compete-for-un-affiliated-ngo-internships-prizes/manage/submissions) - Mar 12 – May 3, 2026. Join hackathon · GNEC Hackathon 2026 Spring - Compete For UN-Affiliated/NGO In...

16. [HackAmerica: America's Largest Hackathon for High ... - Devpost](https://hackamerica.devpost.com) - US only. View full rules. Submissions open soon. View schedule. Apr 11 – 18, 2026 ... © 2026 Devpost...

17. [Agent Firewall - Devpost](https://devpost.com/software/agent-firewall) - A zero-trust authorization layer for AI agents that transforms every tool call into a structured, us...

