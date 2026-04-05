<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Verify new  hackathons provided on Devpost and generate a high value problem to solve and Ideas to solve the chosen problem to solve

Here are verified current Devpost hackathons and a focused, high‑value problem plus concrete ideas you can build around it.

## 1. Verified new Devpost hackathons

From Devpost and aggregator listings, these are active, online AI-focused hackathons right now:

- **Authorized to Act: Auth0 for AI Agents** – Build agentic AI apps using Auth0 for AI Agents Token Vault as the identity/authorization layer; deadline early April 2026.[^1][^2][^3][^4]
- **Agents Assemble – The Healthcare AI Endgame** – Build interoperable healthcare agents on the Prompt Opinion platform using MCP or A2A standards; runs March–May 2026.[^5][^6][^7][^8][^9]
- **The 2030 AI Challenge** – Design an interactive AI application that tackles one or more UN Sustainable Development Goals (SDGs); requires a working app, 2‑minute video, and technical report; backed by Featherless.ai inference sponsorship.[^10][^11][^12][^3]

All three are listed as open “joinable” hackathons on Devpost or partner sites, with clear timelines, online participation, and AI-heavy themes, so they are valid current targets for a new project.[^2][^7][^3][^4][^1][^10][^5]

For your goals (independent research + high social value), **The 2030 AI Challenge** is the most flexible and impact‑oriented, so the rest of this answer centers on that.[^3][^10]

***

## 2. Chosen high‑value problem space

**Problem:**
Helping frontline community workers target and track *climate‑related health risks* (heatwaves, air pollution, floods, vector‑borne disease) in low‑resource neighborhoods.

Why this is high‑value and hackathon‑friendly:

- Climate change is amplifying extreme heat, poor air quality, and flooding, which in turn drive spikes in hospitalizations, especially in dense, low‑income areas.[^13][^14]
- The data needed to anticipate these spikes (weather, heat index, air quality, basic local health indicators) exists but is typically fragmented and hard to interpret at the street or household level for non‑technical workers.[^15][^14]
- Community health workers and local NGOs are already doing door‑to‑door outreach, but largely without tools that prioritize who to see *today* and what simple interventions to push (hydration checks, cooling centers, asthma adherence, mosquito control).[^14][^13][^15]

This maps cleanly onto UN SDGs **3 (Good Health and Well‑Being)**, **11 (Sustainable Cities and Communities)**, and **13 (Climate Action)**, which The 2030 AI Challenge explicitly encourages. It also naturally calls for AI: you need models to fuse heterogeneous signals into risk scores, summarize them for humans, and generate localized recommendations.[^16][^14][^10]

***

## 3. Solution direction: “Climate Health Field Copilot”

You can frame the overall solution direction as:

> An interactive AI “field copilot” for community health workers that combines simple local inputs with climate and pollution data to produce prioritized risk alerts and plain‑language action plans for specific blocks or households.

Core pillars to design around:

- **Local context intake** – Location, community profile tags (e.g., high proportion of elderly, informal housing), and a small set of synthetic patient/household attributes.
- **Environmental feeds** – Live or forecast heat index, AQI, and severe weather alerts via public APIs for the selected area.[^14]
- **AI risk assessment** – Lightweight model or heuristic + LLM that turns the above into short‑term risk ratings (e.g., low/medium/high heat stress risk) with explanations in natural language.[^16][^14]
- **Actionable outputs** – Checklists and outreach scripts tuned to the worker’s role and the community (e.g., “visit these 10 households first; call these 5; send flyers to this block”).

This fits The 2030 AI Challenge’s requirement for an *interactive* AI application tied to an SDG, with a clear story about why it matters by 2030, and is scoped small enough to demo well in a 2‑minute video.[^10]

Below are three distinct, hackathon‑sized ideas inside this problem space.

***

## 4. Idea 1 – Neighborhood Heat‑Risk Triage Dashboard

### One‑sentence pitch

An AI‑powered dashboard that helps community health workers triage which streets or households to visit during a heatwave by dynamically scoring and explaining heat‑related health risk.

### Target prize category and why

- SDG **3 (Good Health and Well‑Being)** and **11 (Sustainable Cities and Communities)** under The 2030 AI Challenge, focusing on urban climate‑health resilience.[^10]
- Strong story: “This tool helps prevent heat‑related illness and deaths in vulnerable urban communities by telling workers exactly where to go first.”


### The “demo moment”

In the video:

1. You paste or upload a tiny CSV of anonymized household rows (age bands, chronic conditions flag, housing type) for a test neighborhood.
2. You click **“Assess Heatwave Risk”**.
3. The dashboard instantly shows:
    - A list or simple map where rows/blocks turn red/yellow/green.
    - For one red entry, an AI‑generated explanation:
“High risk due to multiple residents over 70, top‑floor metal‑roof housing, and forecasted heat index of 42°C between 14:00–17:00.”

That one click → clear visualization + explanation is what will stick in a judge’s mind.

### Platform / AI features that are visibly used

Even without a specified sponsor platform, you can make the “AI-ness” and integrations obvious:

- **Featherless or similar inference API**: call it from the backend when the user clicks “Assess Heatwave Risk”, and show a spinner + then the generated natural‑language explanations beside each row.[^3][^10]
- **Weather/heat API integration**: expose a date/time slider or “Change day” selector, refetch environmental data, and re‑compute risk live on screen to show that environmental context actually matters.[^14]
- Optional: **User accounts / project selection** to hint at multi‑neighborhood use; this can be simple but makes it feel like a product rather than a toy.


### Why this is not “just a wrapper”

- You are not merely visualizing a weather feed; you are fusing *community attributes* (age, housing, comorbidities) with climate data and surfacing a prioritized worklist and explanatory rationale.[^13][^14]
- The AI layer carries real logic: “given these inputs, what is the likely short‑term heat risk and why, in words a community worker will understand?” That interpretive step is what makes it “agentic” and SDG‑aligned rather than just a chart.


### Honest build estimate (person‑days)

For a small, reasonably experienced team:

- Backend (weather API integration, basic risk rules, API for frontend): **2–3 person‑days**.
- Frontend (table/list view, basic filters, simple map or neighborhood cards): **3–4 person‑days**.
- AI integration (prompt design for explanations + outreach suggestions, testing a few scenarios): **2–3 person‑days**.

Total: roughly **7–10 person‑days** to get to a polished demo.

### Primary risk

The main risk is over‑engineering the risk model (too many variables, pseudo‑clinical scoring) and getting bogged down. To de‑risk:

- Start with **one city** and **one type of event** (e.g., extreme heat only).
- Use very simple, explainable rules plus LLM text, and frame it clearly as *decision support* on synthetic data, not a medical tool.

***

## 5. Idea 2 – Climate‑Aware Visit Planner for Community Nurses

### One‑sentence pitch

A mobile‑friendly planner that helps community nurses reorder and adapt their daily home‑visit schedule based on patient vulnerability and forecasted heat and air‑quality conditions.

### Target prize category and why

- SDG **3 (Good Health and Well‑Being)** + **13 (Climate Action)**, again under The 2030 AI Challenge’s SDG requirement.[^10]
- The story is tight: “This saves time and reduces avoidable emergency visits by proactively reshuffling visits on high‑risk days.”


### The “demo moment”

In the video:

1. Load a synthetic schedule: six home visits with basic tags (Elderly COPD, Dialysis patient, Low‑risk follow‑up, etc.).
2. Show a panel with “Today’s Forecast: High heat alert, AQI 160 from 2–5pm.”
3. Tap **“Optimize Day”**:
    - The order of visits visibly changes.
    - High‑risk patients bubble to the top with short AI explanations, e.g.,
“Move Mr. J. to a morning slot due to predicted AQI spike at 3pm and history of severe asthma.”
    - Low‑risk follow‑ups get suggested as remote calls with generated SMS templates.

That before/after schedule flip is a powerful visual.

### Platform / AI features that are visibly used

- **AI ranking + explanation**: compute a simple risk score and then use an LLM to turn it into natural‑language reasons for reordering (clearly labeled as “AI suggestion”).[^16][^14]
- **Environmental feed**: small banner showing live or mocked forecast that, when changed, causes a re‑optimization.
- Optional: **“What‑if” controls** (e.g., toggle car availability or time window) to rerun AI suggestions and show responsiveness.


### Why this is not “just a wrapper”

- Route optimizers exist, but here the differentiator is the explicit **climate‑aware clinical reasoning**: it’s not minimizing distance, it is re‑ranking based on risk and generating communication content tailored to risk level.[^13][^14]
- The AI’s contribution is front‑stage (ranking + explanations + SMS scripts), not hidden in the backend.


### Honest build estimate (person‑days)

- Schedule UI (list of visits, drag‑and‑drop or simple re‑list, basic edit form): **2–3 person‑days**.
- Simple routing / ordering logic (even without full GIS): **1–2 person‑days**.
- AI integration for risk‑aware ranking and text generation: **3–4 person‑days**.

Total: about **6–9 person‑days** to reach a clean, demo‑ready version.

### Primary risk

Most likely failure mode: trying to be clinically authoritative. Keep it clearly scoped as *non‑clinical decision support with synthetic data*, and emphasize that nurses retain judgment; that’s enough for hackathon judging.

***

## 6. Idea 3 – Community Climate Health Storyboard

### One‑sentence pitch

An interactive storytelling tool that turns short incident reports from community workers into SDG‑linked insights and narratives for local advocacy on climate‑related health issues.

### Target prize category and why

- Hits SDG **3 (Health)**, **11 (Cities)**, and **10 (Reduced Inequalities)** by highlighting disproportionate climate impacts on marginalized communities.[^15][^13][^10]
- Extremely strong for The 2030 AI Challenge’s *presentation* and *creativity* criteria, since the final artifact is an explorable narrative dashboard instead of a pure utilitarian tool.[^10]


### The “demo moment”

In the video:

1. Enter 3–5 short, structured incident reports (e.g., “Three elders fainted at community center during heatwave,” “Two children had asthma attacks on high‑AQI day near highway”).
2. Click **“Generate Community Storyboard”**.
3. Show:
    - A small summary panel with counts and simple charts (incidents over time, by location/type).
    - Next to it, an AI‑generated narrative like:
“Over the last month, heatwaves and poor air quality have caused at least 7 reported health incidents concentrated near the central market and riverside settlement, directly touching SDG 3.3, 11.5, and 13.1.”
    - Optional: an AI‑generated “talking points” section for a community meeting.

This makes the tool’s purpose immediately obvious to judges.

### Platform / AI features that are visibly used

- **Summarization and SDG mapping**: the LLM clusters incidents into themes and maps them to a *small* set of SDG targets, which you display explicitly in a “Related SDGs” panel.[^15][^13][^10]
- **Dual view toggle**: “Data View” (counts, charts) vs. “Story View” (generated narrative); flipping between them demonstrates the AI translation from raw to human‑readable insight.
- Optional: AI‑generated follow‑up questions (“Ask the worker: Were cooling centers open that day?”) to guide better future data collection.


### Why this is not “just a wrapper”

- You are encoding a simple ontology that maps local qualitative reports to specific SDG goals/targets, which is a non‑trivial layer of reasoning beyond generic summarization.[^13][^15]
- The advocacy angle (turning micro‑incidents into a community narrative) is tightly coupled to the SDG framing of The 2030 AI Challenge, and would be hard to replicate with a generic chatbot UI alone.[^10]


### Honest build estimate (person‑days)

- Incident capture UI (form, tags, validation) and basic aggregation logic: **2–3 person‑days**.
- Simple charts/tables in the frontend: **2–3 person‑days**.
- AI pipeline for clustering, SDG mapping, and narrative generation: **3–4 person‑days**.

Total: about **7–10 person‑days** for a solid proof‑of‑concept.

### Primary risk

The main risk is that SDG mapping feels arbitrary or opaque; mitigate by:

- Restricting to a **small subset of SDG targets** relevant to your prototype community.
- Showing a short “Why this SDG?” explanation under each mapping, generated by the AI.

***

## How to pick among these

- **You care most about operations and triage** → start with **Idea 1 (Heat‑Risk Triage Dashboard)**.
- **You want a strong narrative about supporting nurses and healthcare systems** → **Idea 2 (Visit Planner)**.
- **You want maximum storytelling value and presentation points** → **Idea 3 (Storyboard)**.

All three are:

- Directly aligned with The 2030 AI Challenge rules (interactive app, clear AI component, explicit SDG mapping, demo‑able in ~2 minutes).[^10]
- Realistically buildable by a small team in well under two focused weeks, assuming ~4 productive hours per person per day.

If you tell me your team size, tech stack, and how many days you realistically have, I can help you choose one of these and break it into a concrete build plan (MVP feature list + demo script).
<span style="display:none">[^17][^18][^19][^20][^21][^22][^23][^24][^25][^26][^27][^28][^29][^30][^31][^32][^33][^34][^35][^36][^37][^38][^39][^40][^41][^42][^43][^44][^45][^46][^47][^48][^49][^50][^51][^52][^53][^54][^55][^56][^57][^58][^59][^60]</span>

<div align="center">⁂</div>

[^1]: https://authorizedtoact.devpost.com

[^2]: https://the-2030-ai-challenge.devpost.com

[^3]: https://agents-assemble.devpost.com

[^4]: https://devpost.com/submit-to/28368-authorized-to-act-ai-agents-with-auth0/manage/submissions

[^5]: https://arxiv.org/pdf/2501.09674.pdf

[^6]: https://devpost.com/fred-patton/challenges

[^7]: https://agents-assemble.devpost.com/rules

[^8]: https://digitomize.com/hackathons/27874

[^9]: https://devpost.com/submit-to/28656-the-2030-ai-challenge/manage/submissions

[^10]: https://skillsetcourse.com/practice/devpost-the-2030-ai-challenge

[^11]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4511834/

[^12]: https://www.tandfonline.com/doi/full/10.1080/15710882.2024.2378933

[^13]: https://arxiv.org/html/2503.23492v1

[^14]: https://arxiv.org/pdf/2403.17918.pdf

[^15]: https://305hackmar2026.devpost.com

[^16]: https://devpost.com/c/artificial-intelligence

[^17]: https://developerweek-2026-hackathon.devpost.com

[^18]: https://hackthecoast.devpost.com

[^19]: https://devpost.com/hackathons

[^20]: https://developerweek-2025-hackathon.devpost.com

[^21]: https://hackuncp-2026.devpost.com

[^22]: https://hackforhope.devpost.com

[^23]: https://75her-challenge.devpost.com

[^24]: https://devpost.com/c/blockchain

[^25]: https://hack4good-2026.devpost.com

[^26]: https://shellhacks2025.devpost.com

[^27]: https://sasehacks.devpost.com

[^28]: https://devpost.com

[^29]: https://devpost.com/hackathons?themes[]=Beginner+Friendly

[^30]: http://arxiv.org/pdf/2410.03286.pdf

[^31]: https://arxiv.org/pdf/2103.10167.pdf

[^32]: https://arxiv.org/pdf/2103.01145.pdf

[^33]: https://arxiv.org/abs/2207.01015

[^34]: https://arxiv.org/pdf/2106.00309.pdf

[^35]: https://developerweek-2026-hackathon.devpost.com/details/dates

[^36]: https://developnext.devpost.com

[^37]: https://treehacks-2026.devpost.com

[^38]: https://hackdevpost.devpost.com

[^39]: https://octopushack.devpost.com

[^40]: https://developerweek-2022-hackathon.devpost.com

[^41]: https://hackhive-2026.devpost.com

[^42]: https://devpost.com/rayen-gragba/challenges

[^43]: https://devpost.com/software/ai-devops-agent-with-secure-auth0-access

[^44]: https://devpost.com/software/authaiagent

[^45]: https://devpost.com/software/ai-assistant-for-everyday-questions

[^46]: https://devpost.com/submit-to/27874-agents-assemble-the-healthcare-ai-endgame/manage/submissions

[^47]: https://devpost.com/software/green-guide-uo7dn5

[^48]: https://devpost.com/software/shieldclaw-ehigc2

[^49]: https://agents-assemble.devpost.com/project-gallery

[^50]: https://arxiv.org/pdf/2501.10114.pdf

[^51]: https://arxiv.org/pdf/2406.08689.pdf

[^52]: https://arxiv.org/pdf/2412.01769.pdf

[^53]: https://arxiv.org/pdf/2411.05285.pdf

[^54]: https://arxiv.org/html/2412.08445

[^55]: https://aclanthology.org/2023.emnlp-demo.51.pdf

[^56]: https://x.com/devpost/status/2031038886928101778

[^57]: https://digitomize.com/hackathons/28656

[^58]: https://www.linkedin.com/posts/devpost_authorized-to-act-auth0-for-ai-agents-activity-7429990057421352960-dxNF

[^59]: https://x.com/devpost/status/2029986452604412300

[^60]: https://devpost.com/users/register?flow[data][challenge_id%5D=28656\&flow%5Bname%5D=register_for_challenge

