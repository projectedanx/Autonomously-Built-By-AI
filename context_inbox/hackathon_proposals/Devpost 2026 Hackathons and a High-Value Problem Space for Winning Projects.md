# Devpost 2026 Hackathons and a High-Value Problem Space for Winning Projects

## Overview

This report identifies current and upcoming hackathons on Devpost in 2026, extracts common thematic directions, and then proposes a single high‑value problem area to target across multiple events: trustworthy autonomous AI agents in regulated and high‑risk domains. It then develops three concrete, hackathon‑ready project concepts aligned with this problem space and with the judging criteria commonly used in these events.[^1][^2][^3]

## New and Upcoming Devpost Hackathons in 2026

Devpost maintains a central "New & upcoming hackathons" directory that currently features events such as **"Authorized to Act: Auth0 for AI Agents"**, **"ZerveHack"**, and **"Agents Assemble - The Healthcare AI Endgame"** as online hackathons running through March and April 2026. These listings confirm that AI agents, security, and applied healthcare AI are among the most visible themes on the platform this season.[^2][^3][^1]

Beyond the featured list, several 2026 hackathons highlight AI, social impact, and student‑friendly innovation:

- **DeveloperWeek 2026 Hackathon** (online and in‑person) brings 800+ participants to work on challenge‑driven projects, including sponsor tracks around open‑source dev tools, AI workloads on cloud infrastructure, and AI‑generated internal tools.[^4]
- **Frostbyte Hackathon 2026** is framed as a global AI and tech competition, with tracks specifically for software engineering, AI/ML, and data analytics, encouraging "real‑world challenges" and impact‑oriented solutions.[^5]
- **MEGA Hackathon 2026** focuses on the UN Sustainable Development Goals 11 (Sustainable Cities and Communities) and 16 (Peace, Justice, and Strong Institutions), explicitly inviting STEM‑driven solutions to global development problems.[^6]
- **HackHive 2026** and **Hack the Coast 2026** offer general‑purpose hackathon formats with judging criteria emphasizing creativity, technical difficulty, functionality, and impact, again rewarding projects that solve “real problems or provide value.”[^7][^8]

Several explicitly social‑impact and climate‑oriented hackathons also align with AI‑for‑good themes:

- **Hack for Humanity 2026** is a month‑long event focused on environmental issues, rewarding projects that tackle real‑world environmental challenges.[^9]
- **The Climate Change‑Makers Challenge: 2026** is a 48‑hour youth hackathon concentrating on inter‑connected challenges in fighting climate change, culminating in a four‑minute video submission and live finals.[^10]
- Earlier AI‑for‑good events like **AI for Change Hackathon** and **SolutionHacks** target AI solutions for climate sustainability, ocean conservation, and social equality, as well as "projects that solve real‑world problems using AI."[^11][^12]

These events collectively show strong demand for AI‑centric, socially impactful projects, with recurring emphasis on practical prototypes, clear demos, and visible user‑facing value.

## Common Judging Patterns

Reviewing multiple Devpost hackathon pages reveals recurring judging criteria:[^13][^14][^4][^7]

- **Creativity/Innovation** – originality and novelty of the idea.
- **Technical Difficulty** – complexity and sophistication of the implementation.
- **Functionality/Execution** – whether the demo works and delivers on its stated goal.
- **Impact/Relevance/Practicality** – how well the project addresses a real problem and the potential for real‑world use.
- **Design/User Experience** – clarity, usability, and polish of the interface and workflow.
- **Presentation** – clear articulation of problem, solution, and impact in a short video.

Civic and social‑impact hackathons further emphasize **feasibility** and the potential to make a significant difference in specific civic or social issues. Design‑oriented events like Figma’s **FigBuild 2026** highlight a focused build weekend plus a well‑defined judging period, again centering on clear visual presentation and interaction design.[^14][^15]

These patterns imply that winning projects should:

- Demonstrate visible user workflows, not just backend APIs.
- Show a before/after transformation on a real user problem.
- Keep scope tight enough to fully demo in 3–5 minutes while hinting at extensibility.

## High‑Value Problem Space: Trustworthy Autonomous AI Agents in Sensitive Domains

### Why this problem is timely

The presence of **"Authorized to Act: Auth0 for AI Agents"** as a featured online hackathon shows that sponsors see secure, authorized AI agents as a first‑class problem area worthy of its own competition. The featured **"Agents Assemble - The Healthcare AI Endgame"** indicates parallel interest in applying AI agents specifically to healthcare workflows, where safety, consent, and regulation are paramount.[^3][^1][^2]

At the same time, large AI‑for‑good and national AI hackathons (such as WitchHunt 2026, referenced in AI‑for‑Good and TrackShift updates) explicitly call for scalable AI solutions across education, climate action, health and wellbeing, and smart cities, underscoring that autonomous or semi‑autonomous systems are expected to interact with sensitive data and high‑impact decisions.[^16][^17]

### The core problem statement

Across enterprises, NGOs, and public institutions, decision‑makers increasingly want AI agents that can take actions (sending emails, modifying records, triaging support requests, coordinating volunteers, or drafting policy memos) rather than merely generating static text. However, three barriers repeatedly appear:

1. **Non‑technical stakeholders lack intuitive ways to define what an agent is and is not allowed to do** (e.g., which data sources it may access, which tools it may invoke, and which entities it may contact).
2. **Organizations have little real‑time visibility into what agents are actually doing across tools and accounts**, beyond raw logs that are unreadable to most non‑engineers.
3. **Regulated domains (healthcare, public services, justice, finance) require demonstrable consent, auditability, and justifications for actions**—requirements that current agent prototypes often treat as afterthoughts.

Framed concisely:

> Non‑technical organizations cannot safely deploy AI agents in regulated or high‑risk workflows because they lack simple, visual ways to constrain, monitor, and justify agent actions.

This problem is directly aligned with themes in current Devpost events (AI agents, healthcare AI, AI for social impact) and gives clear room for visible, interactive demos that judges can immediately understand.[^1][^9][^10][^2][^11]

## Design Principles for Ideas in this Space

Given common Devpost constraints (small teams, weekend‑scale builds, 3–5 minute demos), project ideas in this space should:

- **Target a specific vertical** (e.g., healthcare case management, student support operations, civic engagement) to keep scope narrow and demos concrete.[^6][^9]
- **Expose a clear user‑facing console or workflow**, not just an API, so judges can see policies, approvals, and incident handling in action.[^4][^7]
- **Integrate at least one sponsor or platform‑specific feature visibly** (such as an auth provider, data platform, or design environment) for stronger alignment with specific Devpost challenges.[^4][^1]
- **Include an obvious “failure mode” scenario** (e.g., an over‑reaching agent) where the tool visibly catches, explains, and corrects the behavior during the demo.

The following three ideas are crafted to satisfy these constraints and to be realistically buildable by a small team in a few days, assuming prior familiarity with web development and AI tooling.

## Idea 1: Guardrail Studio for AI Agents

### One‑sentence pitch

A no‑code "guardrail studio" that lets non‑technical admins visually define, test, and monitor what AI agents are allowed to do across data sources and tools.

### Target prize category and why

- **Best Use of Auth0 / Secure AI Agents** – directly aligned with "Authorized to Act: Auth0 for AI Agents," focusing on safe authorization and action boundaries for agents.[^2][^1]
- **Best Dev Tool / Infrastructure Hack** – fits DeveloperWeek‑style tracks that reward open‑source tools and cloud‑native AI/ML workloads.[^5][^4]

### The demo moment

In the demo, an "HR assistant" agent attempts to export a full employee dataset that violates policy; the Guardrail Studio UI shows a live event feed where the action is blocked, highlights the specific policy rule that fired, and offers a one‑click human approval or modification flow. The presenter edits a visual policy node (for example, changing "export" from "blocked" to "requires approval for anonymized fields"), re‑runs the scenario, and the agent is now allowed to export only non‑sensitive columns while the UI displays a natural‑language explanation of why the action is now permitted.

### Platform features used and visibly surfaced

Because specific sponsor stacks vary by hackathon, the core idea is to make at least three platform‑level features visible in the UI:

- **Authentication & Authorization provider (e.g., Auth0 in "Authorized to Act")** – use hosted login and roles/permissions to log admins and agents into the studio, showing role‑based views in the demo (admin vs. observer), and visibly tagging agent actions with the issuing identity.[^1]
- **Cloud or agent platform logs** – stream agent tool‑use events into a dashboard timeline, with filters for user, agent, tool, and outcome; judges see real‑time updates whenever the agent invokes a tool, hits a policy, or is blocked.[^4]
- **Rules/Actions or webhook extensions** – demonstrate that changing a visual rule in the Guardrail Studio immediately affects downstream behavior, by re‑running the same agent prompt and showing a different outcome without code changes.

All three are visible to a judge watching the UI: they see login flows, the real‑time event timeline, and policy edits propagating in seconds.

### What makes this more than a wrapper

The core value is a constraint DSL (domain‑specific language) and visualization that sits between LLM‑based agents and real‑world tools, turning raw logs and opaque prompts into human‑legible policies and event streams. Rather than simply hosting an agent, the project focuses on:

- Translating natural‑language guardrails ("This HR agent should never access salary data for executives") into structured constraints.
- Representing those constraints as composable visual blocks that can be tested and simulated.
- Injecting these constraints at runtime into the agent’s tool‑invocation layer.

This combination—visual DSL, simulation mode, and live enforcement—would not exist without an agent‑capable platform that exposes fine‑grained logs and extensibility; it is not just a UI shell over an API.[^1][^4]

### Honest build estimate

- **Person‑days**: roughly 12–16 person‑days.
- Breakdown: 3–4 days for a basic web dashboard and timeline, 3–4 days for a simple policy engine integrated with one agent/tool stack, and 2–4 days for demo scripting, polish, and integration with the hackathon’s auth or logging provider.

### Primary risk

The main risk is over‑scoping the policy engine and agent simulation: trying to support too many tools or complex policies could make it hard to reach a stable, demo‑ready prototype within a few days. Keeping scope to one or two concrete workflows (e.g., HR exports and support‑ticket triage) mitigates this.

## Idea 2: Consent Lens for Healthcare AI Agents

### One‑sentence pitch

A "consent lens" web console that sits in front of healthcare AI agents, enforcing patient and compliance consents on every agent action and providing an auditable timeline of who approved what.

### Target prize category and why

- **Healthcare AI / Agents in Medicine** – tailored for events like "Agents Assemble - The Healthcare AI Endgame," where agent workflows intersect with protected health information and clinical processes.[^3][^2]
- **AI for Social Good / Health & Wellbeing** – aligns with AI‑for‑good hackathons seeking scalable solutions in health and wellbeing.[^17][^16]

### The demo moment

In the demo, a "care‑coordination agent" attempts to view full medical histories for a patient whose consent allows only visit summaries to be shared with third‑party providers. The Consent Lens UI pops up a real‑time approval card for a compliance officer, clearly showing:

- What the agent is trying to access.
- Which consent rule is being triggered.
- A justification string the agent provides (e.g., "needed for medication reconciliation").

The officer rejects the request, and the agent’s chat view updates to show a natural‑language explanation of the denial. The presenter then updates the patient’s consent profile in the UI (granting limited additional access) and re‑runs the scenario, showing a successful, but scoped, data retrieval and a complete audit trail entry.

### Platform features used and visibly surfaced

For healthcare‑focused hackathons, the project can visually demonstrate at least three platform‑level or sponsor‑provided capabilities:

- **FHIR or healthcare data sandbox (if provided)** – use a standard patient record format to show which resources the agent is allowed to read, with a visible resource tree in the UI.
- **Audit log or observability stack** – every agent request and decision is logged to a timeline, with filters by patient, agent, and outcome.
- **Role‑based access controls** – separate views for patients, clinicians, and compliance officers, with different consent‑editing and approval permissions.

In the absence of a real EHR, mock FHIR resources or a simplified patient‑record schema can still be used to demonstrate the pattern in a way judges understand.

### What makes this more than a wrapper

Rather than just adding another chat UI to a healthcare model, Consent Lens formalizes and visualizes consent as a first‑class object in the agent loop. It:

- Encodes granular consent rules at the level of resource types and fields, not just "on/off" toggles for data sources.
- Forces every sensitive agent operation through a consent check that can trigger human‑in‑the‑loop approvals.
- Produces an auditable narrative timeline that regulators and institutional review boards could inspect.

This approach requires explicit modeling of consent semantics and real‑time mediation between agents and data sources, going beyond simple wrappers around a healthcare API.[^9][^6]

### Honest build estimate

- **Person‑days**: roughly 14–18 person‑days.
- Breakdown: 4–5 days to build the multi‑role UI and consent editor, 4–5 days to integrate with an agent stack and a simple healthcare schema or sandbox, and 4–8 days to harden the approval workflow and script a compelling demo scenario.

### Primary risk

The biggest risk is attempting deep integration with real EHR systems or overly complex FHIR subsets within hackathon time. Constraining scope to a narrow, well‑defined subset of healthcare data (e.g., medications and allergies) and one or two agent tasks is crucial.

## Idea 3: Impact Sandbox for Civic AI Agents

### One‑sentence pitch

An "impact sandbox" that lets NGOs and civic groups safely prototype AI agents for outreach and advocacy by simulating, constraining, and visualizing their actions before they touch real people.

### Target prize category and why

- **Civic Innovation / Hacktivism / Peace & Justice** – well‑aligned with hackathons like Hacktivism II and MEGA Hackathon 2026, which target civic issues and SDG 16 (Peace, Justice, and Strong Institutions).[^14][^6]
- **Climate or Environmental Action** – can be framed for Hack for Humanity and Climate Change‑Makers as a way to prototype agents for climate campaigns and community mobilization without causing real‑world spam or misinformation.[^10][^9]

### The demo moment

In the demo, the team configures an "urban‑heat resilience campaign" targeting residents in specific neighborhoods. A naive outreach agent proposes sending thousands of identical messages and scraping personal data from public directories. The Impact Sandbox simulates this plan and renders a dashboard showing:

- A high "risk score" for spam complaints and privacy violations.
- A map of simulated outreach showing oversaturation in certain demographics.

The presenter then tightens constraints in the UI (limiting daily contact volume, enabling opt‑out, restricting data sources, and requiring human approval for sensitive content), re‑runs the simulation, and shows improved risk metrics and a more balanced outreach pattern. A subset of simulated messages is auto‑generated and displayed so judges can see content quality and tone.

### Platform features used and visibly surfaced

Depending on the hackathon platform and sponsors, at least three visible capabilities can be showcased:

- **Messaging or notification APIs** – even if calls are stubbed in sandbox mode, the UI shows which channels (email, SMS, social DMs) the agent would use and at what volume.
- **Mapping or data‑visualization components** – a map or chart visualizes where and how many contacts are simulated, tying directly to SDG 11 goals about sustainable cities and communities.[^6]
- **Policy and risk‑scoring engine** – configurable policy sliders or toggles in the UI adjust a computed "impact vs. risk" score that updates in real time as constraints change.

These features make the platform integration visible rather than staying as a pure backend optimization.

### What makes this more than a wrapper

Impact Sandbox elevates "what if" exploration for AI‑driven civic campaigns into a tangible, visual workflow:

- It models populations, channels, and constraints as entities the agent must respect.
- It surfaces risks (spam, privacy, reputational damage) quantitatively and visually before any real messages are sent.
- It gives non‑technical campaigners a safe playground to dial up or down autonomy and reach, making responsible deployment an inherent part of the design rather than a bolt‑on.

This combination of simulation, risk modeling, and constraint editing—tied directly to agent plans—goes beyond simply using AI to draft outreach text.[^14]

### Honest build estimate

- **Person‑days**: roughly 12–16 person‑days.
- Breakdown: 3–4 days for a basic front‑end with scenario configuration and results visualization, 3–4 days for a simple population and messaging simulator, and 4–8 days for integrating an LLM/agent stack and crafting compelling civic scenarios.

### Primary risk

The biggest risk is attempting overly realistic population modeling or external data integration (e.g., real voter rolls or social graphs) that is both time‑consuming and potentially sensitive. Using synthetic but structurally realistic populations and focusing on relative risk/impact metrics keeps the build feasible and ethically safer within hackathon constraints.

## Conclusion

Devpost’s 2026 hackathon landscape is heavily skewed toward AI agents, secure and authorized autonomy, and AI‑for‑good applications in healthcare, climate, and civic life. The high‑value problem of "trustworthy autonomous AI agents in sensitive domains" directly intersects with flagship events like "Authorized to Act" and healthcare‑focused agent challenges while remaining applicable to broader social‑impact hackathons.[^11][^9][^10][^2][^6][^14][^1]

The three proposed concepts—Guardrail Studio, Consent Lens, and Impact Sandbox—are designed to:

- Be demonstrable in a short video with a clear, visual "wow" moment.
- Align closely with common judging criteria around innovation, impact, and execution.
- Be realistically buildable by a small team in a weekend or short sprint.

This makes them strong candidates for a focused, high‑leverage hackathon strategy across multiple Devpost events in 2026.

---

## References

1. [Devpost - The home for hackathons](https://devpost.com) - Featured online hackathons ; Authorized to Act: Auth0 for AI Agents. 14 days left. Mar 02 - Apr 07, ...

2. [New & upcoming hackathons - Devpost](https://devpost.com/hackathons?themes%5B%5D=Beginner+Friendly) - All hackathons ; Authorized to Act: Auth0 for AI Agents. 14 days left. Mar 02 - Apr 07, 2026 ; Agent...

3. [New & upcoming hackathons - Devpost](https://devpost.com/hackathons) - All hackathons ; Authorized to Act: Auth0 for AI Agents. 13 days left. Mar 02 - Apr 07, 2026 ; Agent...

4. [DeveloperWeek 2026 Hackathon: Join the nation's ... - Devpost](https://developerweek-2026-hackathon.devpost.com) - Our hackathons regularly attract over 800+ participants -- and we are inviting the international dev...

5. [Frostbyte Hackathon - Devpost](https://frostbyte.devpost.com) - Mar 14, 2026 @ 2:00pm PDT · Apple · Google · Outlook. Online. Public. $5,200 in cash, 1001 participa...

6. [MEGA Hackathon 2026: A collaborative hackathon ... - Devpost](https://mega-hackathon-2026-students.devpost.com) - MEGA Hackathon 2026. A collaborative hackathon integrating computer science, STEM, economics, and in...

7. [Hack the Coast 2026: Ride the wave of innovation ... - Devpost](https://hackthecoast.devpost.com) - Participants are encouraged to build a functioning prototype or demo that fits within one of our hac...

8. [HackHive 2026: Where Innovation Swarms. - Devpost](https://hackhive-2026.devpost.com) - With 250 hackers from across North America coming together under one roof, you'll be surrounded by p...

9. [Hack for Humanity | 2026: Developing software for the ... - Devpost](https://hack-for-humanity-26.devpost.com) - Hack for Humanity is a hackathon that brings technologists together in a 1-month event to come up wi...

10. [The Climate Change-Makers Challenge: 2026: Join youth ... - Devpost](https://climatechangemakers2026.devpost.com) - The Climate Change-Makers Challenge: 2026. Join youth from across the world in this three-day challe...

11. [AI for Change Hackathon: Design innovative solutions to ... - Devpost](https://ai-for-change.devpost.com) - Design innovative solutions to pressing social and environmental challenges using Artificial Intelli...

12. [SolutionHacks: Create projects that solve real-world problems ...](https://solutionhacks.devpost.com) - Create projects that solve real-world problems using AI! · Requirements · Hackathon Sponsors · Prize...

13. [HackRU Fall 2025: Rutgers University's 24-hour ... - Devpost](https://hackru-fall-2025.devpost.com) - Rutgers University's 24-hour, student-ran hackathon! Join us in building amazing software and hardwa...

14. [Hacktivism II: Driving innovation, creating solutions ... - Devpost](https://hacktivism2.devpost.com) - In this hackathon, we're calling on you to tackle pressing civic challenges using the power of techn...

15. [FigBuild 2026: Figma's second annual design-a-thon for ... - Devpost](https://figbuild2026.devpost.com) - FigBuild 2026. Figma's second annual design-a-thon for students! This hackathon has ended. Find more...

16. [Harnessing the power of AI for Positive Social Impact - Devpost](https://ai-for-good.devpost.com/updates) - Registration Open: The WitchHunt 2026 National AI Hackathon ... We have identified 4 critical areas ...

17. [Updates - TrackShift Innovation Challenge - Devpost](https://trackshift.devpost.com/updates) - Registration Open: The WitchHunt 2026 National AI Hackathon ... We have identified 4 critical areas ...

