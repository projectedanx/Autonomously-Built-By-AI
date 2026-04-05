# New Devpost Hackathons and a High-Impact AI Agent Safety Problem with Buildable Project Ideas

## Overview

Devpost currently lists several new and upcoming hackathons in early 2026, including events focused on AI agents, software development automation, environmental sustainability, and inclusive technology. These hackathons provide strong contexts for projects that address an emerging, high-value problem: making autonomous AI agents safe, controllable, and auditable when they act on behalf of real users.[^1][^2][^3][^4]

This report first verifies a set of notable new Devpost hackathons and their themes, then defines a concrete, high-impact problem around AI agent safety and authorization, and finally proposes three buildable project concepts that could be demonstrated within a typical hackathon timeframe.

## New and Upcoming Devpost Hackathons

### Representative hackathons

Several notable hackathons active or recently launched on Devpost as of March 2026 include:

- **GitLab AI Hackathon: You Orchestrate. AI Accelerates.** This online hackathon asks participants to build AI agents on the GitLab Duo Agent Platform that remove friction from the software development lifecycle (SDLC), such as automating security fixes, streamlining code reviews, and generating compliance reports, with explicit emphasis on multi-agent flows and action-taking agents rather than simple chatbots. The event offers up to 65,000 USD in prizes, including dedicated bonuses for using Google Cloud, Anthropic models through GitLab, and for "Green Agents" that consider sustainability.[^5][^4]

- **Authorized to Act: Auth0 for AI Agents.** This featured online hackathon centers on building agentic AI applications using Auth0 for AI Agents, specifically the Token Vault, which handles OAuth flows, token management, and consent delegation so agents can authenticate and authorize against external APIs the way humans do. The only hard requirement is that submissions must integrate Token Vault, and judging criteria explicitly reward strong security models, user control over permissions, and insight into how agent authorization should evolve.[^6][^7]

- **Hack for Humanity | 2026.** Santa Clara University’s 13th Annual Social Good Hackathon, Hack for Humanity 2026, runs as a one-month event focused on "developing software for the environment" and environmental issues more broadly.[^8][^9][^10] The hackathon combines in-person and online participation, offering roughly 13,000 USD in prizes and emphasizing humanitarian impact, responsible AI, and sustainability.[^9][^10]

- #75HER Challenge Hackathon 2026. This hackathon is part of CreateHER Fest’s 75-day build journey leading up to an International Women’s Day demo day and focuses on creating technology with and for women and marginalized communities, across AI/ML, AR/VR/XR, and blockchain tracks. It emphasizes problem-framed, evidence-backed, responsible solutions, with demo day presentations in three tracks and track-specific awards for best use of AI/ML (with Goose), AR/VR/XR, and blockchain.[^11]

These events collectively highlight two strong cross-cutting themes: deployment of AI agents in real workflows (GitLab and Auth0 hackathons) and responsible, human-centered technology for social and environmental good (Hack for Humanity and #75HER).[^8][^4][^11][^6]

## A High-Value Problem: Safe, Controllable AI Agents Acting on Behalf of Real Users

### Problem statement

As platforms such as GitLab Duo Agent Platform and Auth0 for AI Agents encourage developers to build agents that can perform real actions (e.g., modifying code, triggering deployments, sending messages, and interacting with external APIs), there is a growing need for robust authorization, control, and observability around these agents. Research has begun to formalize frameworks for authenticated, authorized, and auditable delegation from humans to AI agents, highlighting the need to tightly scope agent permissions and maintain clear chains of responsibility. Security-focused work on AI agents further documents vulnerabilities such as over-privileged access, prompt injection leading to unintended actions, and insufficient tooling for monitoring and constraining agent behavior.[^4][^12][^13][^6]

The high-value problem can be articulated as:

> **How can AI agents act autonomously across developer tools and online services while remaining strictly within human-granted, understandable, and revocable permission boundaries, with clear auditability and safety guarantees?**

This problem is important because both GitLab and Auth0 hackathons explicitly ask participants to build agents that do more than chat: GitLab requires agents that react to triggers and take actions in the SDLC using its Duo Agent Platform, while Auth0’s Token Vault exists precisely to let agents hold and use delegated access to third-party APIs securely. At the same time, social-good hackathons like Hack for Humanity and #75HER emphasize responsible AI, signaling that communities and organizers are concerned about the societal and ethical implications of such agents.[^9][^10][^11][^8][^6][^5][^4]

### Why this problem is well-suited to current Devpost hackathons

- **Platform fit.** The GitLab AI Hackathon already defines the project requirement as a working agent or flow built on GitLab Duo Agent Platform tools, triggers, and context, while Auth0’s hackathon mandates integration with Token Vault and focuses judging on security model and user control; both provide exactly the primitives needed to design fine-grained, observable authorization layers for AI agents.[^6][^5][^4]
- **Impact potential.** Work on AI agent infrastructure argues that as agents gain broader abilities to act, properly managing their interactions with existing institutions and digital services is critical to unlocking benefits without incurring unacceptable risks. Secure delegation and observability around agents can directly reduce the probability and impact of harmful or unauthorized actions, especially in development, operations, and communication tools.[^14]
- **Research connection.** Recent work on authenticated delegation and agent security identifies concrete design patterns—such as scoped tokens, step-up authentication for high-risk actions, and detailed, replayable audit logs—that can be implemented in hackathon-scale prototypes using platforms like Auth0 and GitLab.[^12][^13][^15]

## Project Idea 1: Agent Permissions Cockpit (Auth0 Token Vault)

### One-sentence pitch

A web dashboard that lets non-technical users see, simulate, and adjust exactly what their AI agents can do across GitHub, Slack, and other connected services, powered end-to-end by Auth0 for AI Agents Token Vault.

### Target prize category and why

- **Hackathon:** Authorized to Act: Auth0 for AI Agents.[^7][^6]
- **Fit:** The project is built around Token Vault, directly addresses the judging criteria on security model and user control, and surfaces "insight value" about how users understand and manage agent permissions.[^6]

### The "demo moment"

In the recorded demo, the presenter clicks a "Run as Agent" button for a high-risk action such as "Post deployment summary to #prod-alerts in Slack," and the UI shows a live, step-by-step flow: Token Vault fetching a scoped access token, the agent pausing on a step-up authentication screen on the user’s phone, and then the action executing with a real Slack message annotated with a permission label and audit link.

### Platform features used and how they are visible

- **Auth0 for AI Agents Token Vault.** All third-party API calls (GitHub, Slack, perhaps Google Drive) are made using tokens obtained via Token Vault; the UI explicitly shows which token and scopes are being used for each action (e.g., "GitHub: repo:read, issues:write"), demonstrating that the agent itself never stores refresh tokens.[^16][^6]
- **Step-up authentication and consent delegation.** For high-risk actions (e.g., posting to production Slack channels or pushing commits), the demo uses Auth0’s support for step-up authentication or CIBA-like flows so users must explicitly approve the action on a separate device before execution, which is clearly visible as an interrupting approval screen in the video.[^16][^6]
- **Auditability via connected accounts.** The Cockpit shows a chronological log of agent actions keyed to the user’s Auth0 identity and connected accounts, making visible which agent, acting under which delegated scopes, touched which resources.

### What makes this not a wrapper

The application does not merely call Auth0 for login; instead, it treats Token Vault as the core design primitive and builds a policy layer and user-facing mental model around it, including per-agent permission profiles, risk tiers for actions, and interactive simulations of what an agent would be allowed to do under current scopes. This kind of permission modeling and simulation would be extremely difficult to implement securely without a platform that already abstracts away OAuth flows and token exchange for multiple connected services.[^16][^6]

### Honest build estimate (person-days)

- Core UI, Auth0 integration, and basic policy engine: approximately 3–4 person-days.
- Adding support for two real third-party APIs (e.g., GitHub and Slack) with Token Vault, plus demo-quality flows and logging: an additional 3–4 person-days.
- Total: roughly 6–8 person-days for a two- or three-person team, achievable within a typical 1–2 week online hackathon window.

### Primary risk

The main risk is complexity in correctly configuring Token Vault for multiple third-party providers, including setting up the appropriate connections, purposes, and scopes for federated token exchange, as highlighted by existing developer experiences; getting this wrong could block the demo from fully executing end-to-end.[^16]

## Project Idea 2: Green Pipeline Orchestrator (GitLab Duo Agent Platform)

### One-sentence pitch

An AI agent on GitLab Duo Agent Platform that continuously analyzes your CI/CD pipelines, suggests greener and faster configurations, and automatically opens merge requests to implement the most impactful changes.

### Target prize category and why

- **Hackathon:** GitLab AI Hackathon.[^17][^4]
- **Category:** Main Grand Prize plus the **Green Agents** bonus and potentially Google Cloud or Anthropic integration bonuses if those platforms are used for inference and metrics.[^4]
- **Fit:** The agent removes friction from SDLC by automating performance and sustainability tuning of pipelines, aligning with the event’s core requirement to build agents that go beyond chat and perform triggered workflows.[^4]

### The "demo moment"

In the demo, a GitLab pipeline is intentionally configured with inefficient job ordering and redundant steps; the agent is triggered automatically after a merge to the default branch, inspects recent pipeline runs, and then opens a merge request that inlines job-level carbon and time savings annotations in the `.gitlab-ci.yml` diff. The presenter then accepts the merge request and re-runs the pipeline to show reduced duration and estimated emissions on a simple dashboard.

### Platform features used and how they are visible

- **GitLab Duo Agent Platform Tools and Triggers.** The agent is registered as an SDLC-focused agent that automatically runs whenever a pipeline finishes or when a developer comments with a trigger phrase on a merge request; the demo shows configuration of these triggers and the agent’s use of built-in tools to fetch pipeline histories and CI configuration.[^5][^4]
- **Context integration.** The platform’s context features are used to give the agent read-only access to pipeline logs, job runtimes, and repository metadata, which the agent summarizes into specific recommendations surfaced in comments and merge requests.[^4]
- **Green Agents bonus alignment.** The project uses simple, documented models or multipliers to convert job runtime and machine type into estimated energy usage or emissions, then surfaces a "Green Impact" badge directly in merge requests, clearly tying the agent’s work to the hackathon’s Green Agents bonus.[^4]

### What makes this not a wrapper

The orchestrator is not just an external script that calls GitLab’s API; it is implemented as a real Duo Agent that lives within GitLab’s ecosystem, uses official tools, triggers, and context streams, and is installed and configured through GitLab’s own agent management UI. The user-visible experience—automatic merge requests, inline annotations, and trigger-based interactions—relies on tight integration with GitLab’s agent platform, which a generic webhook-based system could not replicate as smoothly.[^5][^4]

### Honest build estimate (person-days)

- Setting up a GitLab project, agent registration, and a basic trigger that comments on merge requests: 2–3 person-days.
- Implementing more sophisticated analysis of pipeline logs, generating meaningful recommendations, and formatting merge requests with annotations and a small dashboard: 3–4 additional person-days.
- Total: approximately 5–7 person-days, feasible for a small team within the GitLab AI Hackathon’s submission window.

### Primary risk

The main risk is underestimating the effort required to learn and properly use the GitLab Duo Agent Platform’s tools, triggers, and context APIs in a short timeframe, which could lead to a project that only partially leverages the platform and thus scores lower on technological implementation and impact criteria.[^4]

## Project Idea 3: Community Agent Safety Console (Cross-cutting Auth0 + GitLab)

### One-sentence pitch

A unified "agent safety console" that lets community managers or small organizations define reusable policy templates (e.g., "junior developer agent," "release manager agent") and apply them across GitLab and other tools using Auth0 Token Vault-backed authorization.

### Target prize category and why

- **Hackathons:** Primarily Authorized to Act: Auth0 for AI Agents, with a secondary variant that could be submitted to GitLab AI Hackathon if the main agent runs on GitLab Duo Agent Platform.[^6][^4]
- **Fit:** The project addresses Auth0’s focus on secure, scoped agent authorization and user control, and can also meet GitLab’s requirement for agents that assist with SDLC tasks under well-defined permission boundaries.[^5][^6][^4]

### The "demo moment"

The demo shows a community manager choosing a pre-defined template like "Open-source maintainer agent" in the console, which automatically configures a policy that allows the agent to label issues, comment on merge requests, and open low-risk fix branches but not merge to protected branches. The presenter then switches to GitLab, triggers the agent on an issue, and demonstrates how the agent’s attempt to perform a disallowed action (e.g., merging to `main`) is blocked, with a clear, human-readable explanation surfaced in both the GitLab UI and the console.

### Platform features used and how they are visible

- **Auth0 Token Vault for cross-service delegation.** The console uses Token Vault to manage and store the delegated credentials for GitLab and any other integrated services, proving in the demo that agents operate via scoped tokens that are centrally revoked or rotated through Auth0 rather than embedded directly in configuration files.[^6][^16]
- **GitLab Duo Agent Platform for SDLC agents.** The SDLC-focused agent is implemented on GitLab’s platform, with the console pushing policy updates that translate into agent configuration or environment variables indicating allowed actions; the demo shows GitLab’s UI where the agent appears in issues or merge requests and behaves according to the template-selected permissions.[^5][^4]
- **Auditing and policy simulation.** A "simulate" mode in the console replays recent agent logs (either from GitLab or internal logs) and highlights which actions would be blocked or allowed under a given template, making policy effects visible without executing real changes.

### What makes this not a wrapper

Rather than simply providing a different front-end over existing authorization settings, this console creates a reusable abstraction layer over agent capabilities, expressed as high-level policy templates that map down to Auth0 scopes and GitLab-specific permissions. It leverages Auth0’s federated token exchange and GitLab’s agent context to enforce policies consistently across tools, a level of cross-platform coordination that would be difficult to achieve without these specific platforms.[^16][^6][^5][^4]

### Honest build estimate (person-days)

- Minimal vertical slice: basic console UI, one or two policy templates, Token Vault-backed connection to GitLab, and a GitLab agent that respects a single binary "can-merge" flag: 3–4 person-days.
- Enhanced demo with simulation mode and multiple templates (e.g., viewer, contributor, maintainer): additional 3–4 person-days.
- Total: approximately 6–8 person-days for a small team, assuming familiarity with at least one of the platforms.

### Primary risk

The primary risk is integration surface area: coordinating Auth0 configuration, GitLab agent configuration, and any additional tools within a short hackathon could lead to fragile demos if any one integration fails, and there is also a risk of overlapping with existing projects that already explore agent firewalls or secure DevOps agents, requiring clear differentiation in positioning.[^18][^16]

## Concluding Remarks

New Devpost hackathons in early 2026 create fertile ground for projects that address the emerging problem of safe, controllable, and auditable AI agents acting on behalf of users. By leveraging the specific capabilities of platforms like Auth0 for AI Agents and GitLab Duo Agent Platform, small teams can realistically deliver compelling, demonstrable prototypes—such as an Agent Permissions Cockpit, a Green Pipeline Orchestrator, or a Community Agent Safety Console—that both align with judging criteria and provide genuine value to developers and communities.[^2][^3][^1][^4]

---

## References

1. [New & upcoming hackathons - Devpost](https://devpost.com/hackathons) - Authorized to Act: Auth0 for AI Agents. 18 days left. Mar 02 - Apr 07, 2026 · 10,000 · 1462 ; Airia ...

2. [Devpost - The home for hackathons](https://devpost.com) - Featured online hackathons ; GitLab AI Hackathon. 3 days left. Feb 09 - Mar 25, 2026 ; Authorized to...

3. [New & upcoming hackathons - Devpost](https://devpost.com/hackathons?challenge_type%5B%5D=online) - All hackathons ; Authorized to Act: Auth0 for AI Agents. 16 days left. Mar 02 - Apr 07, 2026 ; Agent...

4. [GitLab AI Hackathon: You Orchestrate. AI Accelerates. - Devpost](https://gitlab.devpost.com) - $3,000 USD in prizes for Green Agents. Find details and resources here. Submission Requirements: The...

5. [Official Rules - GitLab AI Hackathon - Devpost](https://gitlab.devpost.com/rules) - Entrants must request access to the GitLab AI Hackathon group which is where all Projects must be pu...

6. [Authorized to Act: Auth0 for AI Agents: Build an agentic AI ... - Devpost](https://authorizedtoact.devpost.com) - Authorized to Act: Auth0 for AI Agents. Build an agentic AI application using Auth0 for AI Agents To...

7. [Fred Patton's (fred-patton) software portfolio - Devpost](https://devpost.com/fred-patton/challenges) - Authorized to Act: Auth0 for AI Agents · $10,000 in prizes · 26 days to submit · 751 participants .....

8. [Hack for Humanity | 2026: Developing software for the ... - Devpost](https://hack-for-humanity-26.devpost.com) - Hack for Humanity is a hackathon that brings technologists together in a 1-month event to come up wi...

9. [Dhruv Vootkuri's (dhruvvootkuri) software portfolio | Devpost](https://devpost.com/dhruvvootkuri/challenges) - Following · 0. Likes · Hack For Humanity 2026 ... Demonstrate your innovative problem solving skills...

10. [Tarang Goyal's (tgoyal582) software portfolio - Devpost](https://devpost.com/tgoyal582/challenges) - Hack For Humanity 2026. Santa Clara, CA, USA. Santa Clara University's 13th Annual Social Good Hacka...

11. [#75HER Challenge Hackathon 2026: Discover | Design ... - Devpost](https://75her-challenge.devpost.com) - The #75HER Challenge Hackathon is part of CreateHER Fest's 75-day build journey culminating in an In...

12. [Authenticated Delegation and Authorized AI Agents](https://arxiv.org/pdf/2501.09674.pdf) - The rapid deployment of autonomous AI agents creates urgent challenges around
authorization, account...

13. [Security of AI Agents](https://arxiv.org/pdf/2406.08689.pdf) - AI agents have been boosted by large language models. AI agents can function
as intelligent assistan...

14. [Infrastructure for AI Agents](https://arxiv.org/pdf/2501.10114.pdf) - Increasingly many AI systems can plan and execute interactions in open-ended
environments, such as m...

15. [AgentOps: Enabling Observability of LLM Agents](https://arxiv.org/pdf/2411.05285.pdf) - Large language model (LLM) agents have demonstrated remarkable capabilities
across various domains, ...

16. [Agent Firewall - Devpost](https://devpost.com/software/agent-firewall) - GitHub Repo. Submitted to. image. Authorized to Act: Auth0 for AI Agents. Created by. Prabhakaran Ja...

17. [Resources - GitLab AI Hackathon - Devpost](https://gitlab.devpost.com/resources) - GitLab AI Hackathon. Deadline: Mar 25, 2026 @ 11:00am PDT · Join hackathon · GitLab AI Hackathon. De...

18. [AI DevOps Agent with Secure Auth0 Access - Devpost](https://devpost.com/software/ai-devops-agent-with-secure-auth0-access) - GitHub Repo. Submitted to. image · Authorized to Act: Auth0 for AI Agents. Created by. Anusha Gayam ...

