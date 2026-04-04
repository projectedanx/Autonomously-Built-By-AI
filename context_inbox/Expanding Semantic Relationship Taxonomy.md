# **The Architecture of Meaning: An Exhaustive Taxonomy of Semantic, Ontological, and Rhetorical Relationships**

## **1\. Introduction: The Cartography of the Invisible**

The endeavor to map the semantic relationships that bind concepts together is as old as philosophy itself, yet it remains one of the most dynamic frontiers in modern artificial intelligence and cognitive science. The organization of knowledge—whether in the biological neural networks of the human brain or the artificial architectures of large language models—relies fundamentally on the connections between concepts. To understand a concept is not merely to define it in isolation, but to locate it within a vast, multi-dimensional web of relationships. These relationships dictate how reasoning occurs, how unstated information is inferred, how narratives are constructed, and how the world is interpreted.

The taxonomy provided in the query—comprising terms such as *synonym, antonym, hypernym, hyponym, meronym, holonym, entails, presupposes,* and *agentive*—represents a sophisticated cross-section of lexical semantics, frame semantics, and cognitive linguistics. It covers the vertical hierarchy of types (taxonomy), the horizontal connections of association, and the functional links of agency and purpose. The user’s list includes advanced relations like *troponym* (manner of doing), *deontic* (obligation), and *constitutive* (parts/material), indicating a high level of granularity.

However, the landscape of semantic connectivity is far broader. When moving from simple word associations to complex knowledge representation, one encounters the "dark matter" of semantics—relationships that are essential for deep understanding but often absent from standard lists. These include the rigorous formalisms of **mereology** (the study of parts), the topological precision of **spatiotemporal** calculi, the macro-level structures of **discourse**, and the meta-level relationships of **semiotics** and **etymology**.

This report serves as an exhaustive guide to these missing links. It dissects the user's existing list to reveal deeper subtypes and introduces entirely new categories of relationships derived from computational linguistics, formal ontology, and cognitive science. The analysis identifies unsatisfied requirements in the original taxonomy, specifically in the domains of *ambiguity resolution*, *discourse coherence*, *temporal topology*, *thematic role assignment*, and *epistemic states*. By integrating these missing elements, we provide a blueprint for a truly comprehensive ontology capable of supporting advanced reasoning and world-modeling.

## ---

**2\. The Landscape of Ambiguity and Reference**

While the provided taxonomy includes "synonym" and "antonym," it largely overlooks the complex relationships of ambiguity and identity that arise when form and meaning diverge. These relationships are not merely linguistic curiosities; they are the primary obstacles in Word Sense Disambiguation (WSD) and Information Retrieval. To build a robust semantic system, one must model not just how meanings relate to meanings, but how *forms* relate to meanings.

### **2.1. Homonymy: The Illusion of Sameness**

In strict semantic taxonomies, **Homonymy** represents a relation of *accidental identity*. Unlike polysemy, where meanings are historically or conceptually bridged (a relationship effectively covered by the user's "derivational" or "related" tags), homonyms share a surface form but have no semantic connection. This distinction is vital for systems that must decide when to "split" a node in a knowledge graph rather than merge it.1

#### **2.1.1. Homophony and Acoustic Ambiguity**

**Homophony** connects terms that share a phonetic form but differ in orthography and meaning. This is a critical relationship for speech recognition systems, which must resolve semantic pointers based solely on acoustic identity.

* **Definition:** Relation ![][image1] where ![][image2] but ![][image3].  
* **Examples:** *Right* (direction/correct) vs. *Wright* (maker) vs. *Write* (inscribe).  
* **Implication:** For AI systems, homophony represents a high-entropy state where the acoustic signal does not constrain the semantic space sufficienty without collocational data. The user's list includes "sounds\_like," but "Homophone" is the strict formal relation required for disambiguation tables.

#### **2.1.2. Homography and Heteronymy**

**Homography** connects terms that share spelling but may differ in sound and meaning. Within this category lies the **Heteronym**, a specific subset of homographs that differ in pronunciation.

* **Relation:** *Heteronym\_of*  
* **Examples:** *Wind* (/wɪnd/, moving air) vs. *Wind* (/waɪnd/, to turn); *Lead* (/lɛd/, metal) vs. *Lead* (/liːd/, to guide).  
* **Insight:** These relations require Part-of-Speech (POS) tagging and syntactic analysis to disambiguate. A semantic network lacking this distinction cannot support text-to-speech synthesis, as the pronunciation depends on identifying the semantic node correctly.

#### **2.1.3. Capitonymy**

**Capitonymy** is a relation where meaning changes based on capitalization. This is frequently overlooked in standard taxonomies but is essential for Named Entity Recognition (NER).

* **Relation:** *Capitonym\_of*  
* **Examples:** *polish* (to shine) vs. *Polish* (relating to Poland); *march* (to walk) vs. *March* (the third month).  
* **Implication:** In sentiment analysis, failing to model capitonymy leads to catastrophic errors, such as interpreting a headline about a "March on Washington" as a "march" action rather than an event date or name. The semantic shift here is often from a common noun or verb to a proper noun, fundamentally altering the ontological category of the referent.

### **2.2. Metonymy: The Contiguity Principle**

The user lists "metaphorical," which is based on *similarity* or analogical mapping between domains. **Metonymy**, however, operates on a distinct cognitive mechanism: *contiguity* or association within a single conceptual frame. It allows one entity to stand for another with which it is closely associated.3 While "metaphor" maps structure from a Source Domain to a Target Domain (e.g., "Time is Money"), metonymy provides a referential shortcut within the same domain.

#### **2.2.1. Synecdoche (Part-for-Whole / Whole-for-Part)**

While "meronymy" describes the *ontological fact* that a finger is part of a hand, **Synecdoche** describes the *rhetorical usage* of the part to refer to the whole.

* **Part-for-Whole (Pars pro toto):** "All *hands* on deck" (referring to sailors).  
* **Whole-for-Part (Totum pro parte):** "The *police* are investigating" (referring to specific officers, not the abstract institution).  
* **Insight:** Knowledge graphs must distinguish between the ontological part-of relation and the linguistic synecdoche relation to avoid logical fallacies. If a system infers that "hands" are literally "deck-cleaning agents," it misses the human agent entirely.

#### **2.2.2. Functional Metonymy Types**

Beyond synecdoche, several specific metonymic relations are standard in linguistic processing but absent from the user's list:

* **Container-for-Contained:** "The *kettle* is boiling" (referring to the water).  
* **Author-for-Work:** "I am reading *Shakespeare*" (referring to his plays).  
* **Place-for-Institution:** " *Hollywood* is struggling" (referring to the film industry).  
* **Place-for-Event:** "Remember *Pearl Harbor*."

### **2.3. Autonymy: The Meta-Linguistic Loop**

**Autonymy** is the "mention-of" relation, where a word refers to itself as a lexical item rather than to its referent.5 This is also known as the **Use-Mention** distinction in analytic philosophy.

* **Relation:** *Autonym\_of*  
* **Example:** "*Cheese* has six letters."  
* **Significance:** This is distinct from "Cheese is a food." AI systems often fail on these sentences if they try to access the properties of the referent (edible, yellow) rather than the sign (six letters, begins with C). This relation is foundational for processing definitions, linguistic discussions, and distinguishing between the map and the territory. Without this relation, a system cannot represent the sentence " 'Red' is an adjective."

## ---

**3\. Refined Mereology: Deconstructing the Part-Whole Relationship**

The user's taxonomy includes "meronym" and "holonym." However, cognitive science and formal ontology—specifically the seminal work of Winston, Chaffin, and Herrmann (1987)—have demonstrated that "part-of" is not a unitary relation. It dissolves into a family of distinct sub-relations that behave differently regarding transitivity and logic.6 Treating them as identical leads to the **Transitivity Fallacy** (e.g., "A Simpson's finger is part of Simpson; Simpson is part of the Philosophy Department; therefore, Simpson's finger is part of the Philosophy Department"—a false conclusion).

To enable robust reasoning, an ontology must distinguish between types of parts. For instance, a handle is part of a cup in a way that is fundamentally different from how a tree is part of a forest.

### **3.1. The Six Types of Meronymy**

The following table articulates the six fundamental types of meronymy that are missing from the general "meronym" category in the user's list.

| Meronymy Type | Relational Logic | Example | Distinguishing Feature |
| :---- | :---- | :---- | :---- |
| **Component-Object** | Functional, Separable | *Engine \- Car* | The part has a distinct functional role within a structured whole. It is structurally connected. |
| **Member-Collection** | Non-functional, Homogeneous | *Tree \- Forest* | The part is a member of a group; implies spatial proximity but not necessarily structural connection. |
| **Portion-Mass** | Homeomeric | *Slice \- Bread* | The part shares the same substance nature as the whole (a slice of bread is still bread). |
| **Stuff-Object** | Constitutive | *Steel \- Bike* | The material composition relation. (Distinct from Constitutive in the user's list, which often refers to Qualia). |
| **Feature-Activity** | Phase-oriented | *Paying \- Shopping* | Temporal parts of a process or script. Essential for event segmentation. |
| **Place-Area** | Topological | *Oasis \- Desert* | Spatial inclusion where the part cannot be separated from the whole without destroying the region. |

### **3.2. Comeronymy: The Sibling Relation**

**Comeronymy** (or co-meronymy) defines the relationship between two parts of the same whole.7

* **Relation:** *Comeronym\_of*  
* **Example:** *Tire* and *Engine* are comeronyms of *Car*.  
* **Insight:** This relation is crucial for diagnostic reasoning. Comeronyms often share a fate (if the car is destroyed, both are destroyed) but may not interact directly. Defining this explicitly prevents the need to traverse up to the holonym and back down to find siblings in the graph.

## ---

**4\. The Architecture of Discourse and Rhetoric**

The user's list is heavily focused on *lexical* semantics (relations between words). However, meaning is constructed through the connection of propositions and text segments. **Rhetorical Structure Theory (RST)** and **Segmented Discourse Representation Theory (SDRT)** provide a rich taxonomy of relations that hold between events or arguments in a text. These are critical for answering "Why?" questions and for summarization.8

### **4.1. Nucleus-Satellite Relations (RST)**

RST posits that in most coherent text spans, one segment (the nucleus) is more central to the writer's purpose than the other (the satellite). The user's list contains "entails" and "causes," but lacks the structural relations that organize narrative.

* **Elaboration:** The satellite provides additional detail about the nucleus.  
  * *Example:* "I bought a car. *It is a red Ford.*"  
* **Background:** The satellite provides context necessary to understand the nucleus.  
  * *Example:* "*Having worked there for years*, John knew the code."  
* **Enablement:** The satellite increases the reader's ability to perform the action in the nucleus.  
  * *Example:* "To open the box, *pull the tab*."  
* **Evaluation:** The satellite assesses the nucleus.  
  * *Example:* "He tried to run. *It was a mistake.*"  
* **Justify:** The satellite provides grounds for the writer's *right* to state the nucleus.  
  * *Example:* "It's going to rain—*the barometer is falling*." (The barometer falling justifies the claim, but doesn't cause the rain).

### **4.2. Argumentative and Adversarial Nuances**

While the user lists "causes," discourse theories distinguish between *volitional* and *non-volitional* causality, and between cause and evidence.8

* **Volitional Cause:** A situation causes an agent to *choose* an action.  
  * *Example:* "Because I was hungry, I ate."  
* **Non-Volitional Cause:** Physical causality without agency.  
  * *Example:* "The rain caused the mud."  
* **Antithesis:** The writer favors one thesis and rejects another.  
  * *Example:* "I don't want a dog, I want a cat."  
* **Concession:** The writer acknowledges a point that potentially detracts from the main claim but affirms the claim anyway. This is a complex "adversative" relation missing from the simple "antonym" or "paradox" categories.  
  * *Example:* "Although it is expensive, I will buy it.".11

### **4.3. Veridicality in SDRT**

SDRT introduces the dimension of **Veridicality**: does the relation imply the truth of its arguments?

* **Veridical Relations:** (e.g., *Elaboration*, *Explanation*) imply that the events described actually happened.  
* **Non-Veridical Relations:** (e.g., *Alternation* "A or B", *Consequence* "If A then B") do not commit to the truth of the segments.10 This distinction is critical for fact-checking algorithms.

## ---

**5\. Spatiotemporal and Topological Relations**

The user's list includes "temporal," but this is a category, not a specific relation. In Artificial Intelligence, specifically in qualitative spatial reasoning (QSR) and temporal logic, we utilize precise calculi to define these relationships. "Contextual" or "related" is too vague for physical reasoning.

### **5.1. Allen’s Interval Algebra (Temporal)**

James Allen (1983) defined 13 mutually exclusive relations between time intervals, which are the industry standard for temporal reasoning.12 The user's "temporal" tag fails to capture the ordering constraints required for planning.

| Relation | Symbol | Inverse | Meaning |
| :---- | :---- | :---- | :---- |
| **Precedes** | p | Preceded-by | A occurs before B with a gap. |
| **Meets** | m | Met-by | A ends exactly when B begins (no gap). |
| **Overlaps** | o | Overlapped-by | A starts before B, and B starts before A ends. |
| **Starts** | s | Started-by | A and B share a start point, but A is shorter. |
| **During** | d | Contains | A is entirely inside B. |
| **Finishes** | f | Finished-by | A and B share an end point. |
| **Equals** | eq | Equals | A and B are identical intervals. |

### **5.2. Region Connection Calculus (RCC-8) (Spatial)**

For spatial semantics, the Region Connection Calculus (RCC-8) defines topological relations between regions.14 These are essential for robotic navigation and GIS systems.

* **DC (Disconnected):** No shared points.  
* **EC (Externally Connected):** Touch at boundaries only.  
* **PO (Partial Overlap):** Share some interior points.  
* **TPP (Tangential Proper Part):** Part of, touching the boundary.  
* **NTPP (Non-Tangential Proper Part):** Part of, strictly inside (no boundary contact).  
* **EQ (Equal):** Spatially identical.

These relations allow for transitive reasoning: "If A is NTPP of B, and B is DC from C, then A is DC from C." This logic is impossible with a generic "spatial" or "contextual" tag.

## ---

**6\. Thematic Roles and Event Structure (Deep Case)**

The user lists "agentive" and "instrumental," which are part of **Thematic Role Theory** (or Case Grammar). However, a complete taxonomy requires the full spectrum of semantic roles that define how entities participate in events.16 Without these, a system cannot distinguish between "John bought the car" and "The car was bought for John."

### **6.1. The Core Thematic Roles**

* **Patient / Theme:** The entity undergoing the action or being moved. (Distinct from *Agent*).  
  * *Example:* "Mary threw the *ball*."  
* **Experiencer:** The sentient entity that feels or perceives an event. This is distinct from Agent because it lacks volition in the act of perception.  
  * *Example:* " *Mary* saw the movie."  
* **Beneficiary / Benefactive:** The entity for whose benefit the action is performed.  
  * *Example:* "He baked a cake for *her*."  
* **Recipient:** The entity that receives something.  
  * *Example:* "Give *John* the book."  
* **Source:** The origin point of motion or transfer.  
  * *Example:* "He flew from *New York*."  
* **Goal:** The destination point of motion or transfer.  
  * *Example:* "He flew to *London*."  
* **Stimulus:** The entity that triggers a sensation in an Experiencer.  
  * *Example:* "The *noise* scared him."

### **6.2. Qualia Structure (Generative Lexicon)**

The user's list mentions "constitutive," "formal," "telic," and "agentive." These correspond perfectly to Pustejovsky’s **Qualia Structure**, a framework for describing the multifaceted meaning of nouns.18

* **Formal Role:** What is it? (Taxonomic type).  
* **Constitutive Role:** What is it made of? (Parts, materials).  
* **Telic Role:** What is its purpose? (Function).  
* **Agentive Role:** How did it come into being? (Origin).

**Missing Insight:** The interaction between these roles creates **coercion**. For example, "start a book" implies "start *reading* a book" (accessing the Telic role) or "start *writing* a book" (accessing the Agentive role). A static list of relations misses this dynamic process of *type coercion* where a noun functions as a verb argument based on its Qualia.

## ---

**7\. Epistemic, Intentional, and Affective Relations**

The user includes "emotional" and "teleological," but we can be more precise by incorporating the **Belief-Desire-Intention (BDI)** model and affective computing schemas.20 These relations model the "Theory of Mind" of agents.

### **7.1. The Mental State Layer**

* **Believes / Disbelieves:** An epistemic relation connecting an agent to a proposition.  
  * *Property:* Non-factive (The belief can be false).  
* **Knows:** A factive epistemic relation.  
  * *Property:* Factive (If X knows P, P must be true).  
* **Desires / Wants:** A motivational relation. ConceptNet defines **MotivatedByGoal** and **Desires** as distinct.  
  * *Distinction:* *Desires* links an agent to an object ("Person desires food"), while *MotivatedByGoal* links an action to a state ("Eat motivated by hunger").22  
* **Intends:** A commitment to a plan.  
* **ObstructedBy:** An adversarial relation where an entity or event prevents a goal.22

### **7.2. Affective and Sensory Specificity**

The user lists "sensory," but specific relations map to specific modalities, which is critical for grounding language in perception.23

* **Perceptual Relations:** *Visually-Similar-To*, *Auditorily-Similar-To*.  
* **Cross-Modal Correspondence (Synesthesia):** Relations that map features across senses (e.g., "High pitch" maps to "Bright color").  
* **Valence Relations:** *Positively-Associated*, *Negatively-Associated*.

## ---

**8\. Diachronic and Cross-Linguistic Relations**

The user's list is synchronic (current meaning). Diachronic (historical) and inter-lingual relations are essential for etymology, translation, and understanding semantic drift.25

### **8.1. Genealogical Relations**

* **Cognate:** Words in different languages descending from a common ancestor.  
  * *Example:* English *Mother* / German *Mutter*.  
* **Doublet:** Two words in the same language from the same root, usually entering at different times or through different routes.  
  * *Example:* *Frail* (via French) and *Fragile* (via Latin) are doublets.  
* **False Friend (False Cognate):** Words that look similar but have different meanings/origins.  
  * *Example:* English *Gift* (present) vs. German *Gift* (poison).

### **8.2. Borrowing Relations**

* **Loanword:** A word adopted directly with minimal phonetic adaptation.  
  * *Example:* *Sushi* (Japanese \-\> English).  
* **Calque:** A "loan translation" where the structure is translated element-by-element.  
  * *Example:* *Skyscraper* ![][image4] German *Wolkenkratzer* ("cloud-scraper").25

## ---

**9\. Logical and Formal Ontological Relations**

For knowledge graphs (like SUMO, BFO, or OWL ontologies), precise logical definitions are required beyond the user's "entails" and "presupposes".27 These relations define the mathematical properties of the graph itself.

### **9.1. Set-Theoretic Relations**

* **Disjointness:** Two classes cannot share any instances.  
  * *Example:* *Mammal* and *Bird* are disjoint.  
* **Equivalence:** Two classes share all instances.  
  * *Example:* *Morning Star* and *Evening Star* (referentially equivalent).  
* **Intersection:** The set of things belonging to both classes.  
* **Union:** The combined set of instances.

### **9.2. Property Characteristics (Meta-Relations)**

These are relations *about* relations.

* **Symmetry:** If A relates to B, B relates to A.  
  * *Example:* *Spouse\_of*.  
* **Transitivity:** If A ![][image4] B and B ![][image4] C, then A ![][image4] C.  
  * *Example:* *Ancestor\_of*.  
* **Reflexivity:** A relates to itself.  
  * *Example:* *Equals*.  
* **Inverse:** The reversal of a relation.  
  * *Example:* *Parent\_of* is the inverse of *Child\_of*.

## ---

**10\. Adversarial and Competitive Relations**

While "inhibitory" covers biological repression, general semantic modeling requires a broader set of **Adversarial Relations**.29 These are critical for game theory, military strategy modeling, and narrative conflict.

* **Antagonist:** The active opponent of an agent.  
* **Competitor:** An entity seeking the same goal (mutually exclusive success).  
* **Obstacle:** A passive barrier to a goal (conceptually distinct from an inhibitor, which may be an active agent).  
* **Counter-measure:** An action taken to negate an effect.

## ---

**11\. Measurement and Magnitude Relations**

For scientific text processing and data normalization, relations regarding quantity are vital.31 The user's "scalar" is a start, but insufficient for metrology.

* **Unit-of:** Links a measurement unit to the dimension it measures.  
  * *Example:* *Meter* is a unit of *Length*.  
* **Magnitude-of:** Links a value to a property.  
  * *Example:* *Brightness* is a magnitude of *Light*.  
* **Precision / Accuracy:** Relations describing the quality of a measurement (Trueness vs. Repeatability).

## ---

**12\. Semiotic and Meta-Semantic Relations (The "Anionic" Puzzle)**

The user lists "anionic." In chemistry, "anionic" refers to a negative ionic charge. However, in the context of semantic relations, this is almost certainly a misinterpretation of **Ionic** or **Iconic** signs. Snippet 33 contains the text "Anionic sign looks like what it represents," which is the textbook definition of an **Iconic sign** (Peirce's Icon). The snippet explicitly contrasts it with symbols that must be learned. Therefore, the missing category here is **Semiotic Relations**.

### **12.1. Peircean Semiotics**

* **Iconic:** The sign resembles the referent.  
  * *Example:* A map, a portrait, onomatopoeia.  
* **Indexical:** The sign is physically connected or causally linked to the referent.  
  * *Example:* Smoke is an index of fire; a footprint is an index of a walker.  
* **Symbolic:** The relationship is arbitrary and conventional.  
  * *Example:* The word "dog" (no resemblance to the animal).

*Correction:* If the user strictly meant the chemical definition, "Anionic" would fall under **Electrochemical Relations** (alongside Cationic and Covalent). However, given the context of "rhymes," "metaphorical," and "sounds\_like," the semiotic interpretation is the structural gap.

## ---

**13\. Kinship and Social Relations**

"Cultural" is too broad. Ontologies like the **Kinship Ontology** define specific social algebra.34

* **Consanguinity:** Blood relationship.  
* **Affinity:** Relationship by marriage.  
* **Lineage:** Direct descent (Ascending/Descending).  
* **Collateral:** Same generation/ancestor but not direct descent (e.g., Cousins).

## ---

**14\. Conclusion: Synthesizing the Missing Link**

The user's initial taxonomy provides a strong foundation in **Lexical Semantics** (WordNet) and **Frame Semantics** (FrameNet). However, to reach a "comprehensive" state, one must integrate:

1. **Discourse Relations** (RST/SDRT) to understand text flow.  
2. **Formal Spatiotemporal Logic** (Allen/RCC8) for physics and planning.  
3. **Detailed Mereology** (Winston’s taxonomy) to solve logical fallacies in composition.  
4. **Semiotic Relations** (Icon/Index) to understand non-arbitrary meaning.  
5. **Etymological Relations** to map meaning across time and languages.  
6. **Epistemic/BDI Relations** to model the minds of agents.

The integration of these "dark matter" relationships transforms a static lexicon into a dynamic ontology capable of reasoning about the physical world, social intent, and the structure of argumentation.

---

*Citations used:*.1

#### **Works cited**

1. Lexical Relations to Know for Intro to Semantics and Pragmatics \- Fiveable, accessed on February 14, 2026, [https://fiveable.me/lists/lexical-relations](https://fiveable.me/lists/lexical-relations)  
2. Lexical Semantics, accessed on February 14, 2026, [https://www.cs.mcgill.ca/\~jcheung/teaching/fall-2017/comp550/lectures/lecture13.pdf](https://www.cs.mcgill.ca/~jcheung/teaching/fall-2017/comp550/lectures/lecture13.pdf)  
3. 19 LEXICAL SEMANTICS \- Stanford University, accessed on February 14, 2026, [https://web.stanford.edu/class/linguist1/Rdgs/JM19.pdf](https://web.stanford.edu/class/linguist1/Rdgs/JM19.pdf)  
4. Metonymy \- Wikipedia, accessed on February 14, 2026, [https://en.wikipedia.org/wiki/Metonymy](https://en.wikipedia.org/wiki/Metonymy)  
5. (PDF) Making Sense of Mention, Quotation, and Autonymy. A Semantic and Pragmatic Survey of Metalinguistic Discourse \- ResearchGate, accessed on February 14, 2026, [https://www.researchgate.net/publication/36734704\_Making\_Sense\_of\_Mention\_Quotation\_and\_Autonymy\_A\_Semantic\_and\_Pragmatic\_Survey\_of\_Metalinguistic\_Discourse](https://www.researchgate.net/publication/36734704_Making_Sense_of_Mention_Quotation_and_Autonymy_A_Semantic_and_Pragmatic_Survey_of_Metalinguistic_Discourse)  
6. Understanding Semantic Relationships, accessed on February 14, 2026, [https://www.vldb.org/journal/VLDBJ2/P455.pdf](https://www.vldb.org/journal/VLDBJ2/P455.pdf)  
7. Wiktionary:Semantic relations \- Wiktionary, the free dictionary, accessed on February 14, 2026, [https://en.wiktionary.org/wiki/Wiktionary:Semantic\_relations](https://en.wiktionary.org/wiki/Wiktionary:Semantic_relations)  
8. RST \- Rhetorical Structure Theory, accessed on February 14, 2026, [https://www.sfu.ca/rst/01intro/intro.html](https://www.sfu.ca/rst/01intro/intro.html)  
9. relation definitions \- Rhetorical Structure Theory, accessed on February 14, 2026, [https://www.sfu.ca/rst/01intro/definitions.html](https://www.sfu.ca/rst/01intro/definitions.html)  
10. Theoretical Models of Discourse Relations (Chapter 2), accessed on February 14, 2026, [https://www.cambridge.org/core/books/connectives-and-discourse-relations/theoretical-models-of-discourse-relations/73EABD0A22C9E7A9876C9E034F3330CD](https://www.cambridge.org/core/books/connectives-and-discourse-relations/theoretical-models-of-discourse-relations/73EABD0A22C9E7A9876C9E034F3330CD)  
11. Rhetorical Relations, accessed on February 14, 2026, [https://philtypo3.uni-koeln.de/sites/sfb\_1252/user\_upload/Pdfs\_Publikationen/Jasinskaja\_Karagjosova\_accepted\_Rhetorical\_Relations\_draft.pdf](https://philtypo3.uni-koeln.de/sites/sfb_1252/user_upload/Pdfs_Publikationen/Jasinskaja_Karagjosova_accepted_Rhetorical_Relations_draft.pdf)  
12. Allen's Interval Algebra, accessed on February 14, 2026, [https://www.ics.uci.edu/\~alspaugh/cls/shr/allen.html](https://www.ics.uci.edu/~alspaugh/cls/shr/allen.html)  
13. Allen's interval algebra \- Wikipedia, accessed on February 14, 2026, [https://en.wikipedia.org/wiki/Allen%27s\_interval\_algebra](https://en.wikipedia.org/wiki/Allen%27s_interval_algebra)  
14. (PDF) Extensionality of the RCC8 Composition Table \- ResearchGate, accessed on February 14, 2026, [https://www.researchgate.net/publication/220443316\_Extensionality\_of\_the\_RCC8\_Composition\_Table](https://www.researchgate.net/publication/220443316_Extensionality_of_the_RCC8_Composition_Table)  
15. Qualitative Spatio-Temporal Reasoning with RCC-8 and Allen's Interval Calculus: Computational Complexity \- Foundations of Artificial Intelligence, accessed on February 14, 2026, [https://gki.informatik.uni-freiburg.de/papers/gerevini-nebel-ecai02.pdf](https://gki.informatik.uni-freiburg.de/papers/gerevini-nebel-ecai02.pdf)  
16. Thematic Roles, accessed on February 14, 2026, [https://www.sfu.ca/\~hedberg/Thematic\_Roles.pdf](https://www.sfu.ca/~hedberg/Thematic_Roles.pdf)  
17. Thematic relation \- Wikipedia, accessed on February 14, 2026, [https://en.wikipedia.org/wiki/Thematic\_relation](https://en.wikipedia.org/wiki/Thematic_relation)  
18. Automatic Discovery of Telic and Agentive Roles from Corpus Data \- ACL Anthology, accessed on February 14, 2026, [https://aclanthology.org/Y04-1012.pdf](https://aclanthology.org/Y04-1012.pdf)  
19. A Guide to Generative Lexicon Theory \- GL Tutorials, accessed on February 14, 2026, [https://gl-tutorials.org/wp-content/uploads/2015/12/GL-QualiaStructure.pdf](https://gl-tutorials.org/wp-content/uploads/2015/12/GL-QualiaStructure.pdf)  
20. The Belief-Desire-Intention Ontology for modelling mental reality and agency \- arXiv, accessed on February 14, 2026, [https://arxiv.org/html/2511.17162v1](https://arxiv.org/html/2511.17162v1)  
21. Belief & Desire The Standard Model of Intentional Action — Critique and Defence Petersson, Björn \- Lund University Publications, accessed on February 14, 2026, [https://lup.lub.lu.se/search/files/138727373/Petersson\_Belief\_Desire.pdf](https://lup.lub.lu.se/search/files/138727373/Petersson_Belief_Desire.pdf)  
22. Relations · commonsense/conceptnet5 Wiki \- GitHub, accessed on February 14, 2026, [https://github.com/commonsense/conceptnet5/wiki/relations](https://github.com/commonsense/conceptnet5/wiki/relations)  
23. Sensory Language: What Is It, and How Can It Improve Your Writing? \- Scribophile, accessed on February 14, 2026, [https://www.scribophile.com/academy/what-is-sensory-language](https://www.scribophile.com/academy/what-is-sensory-language)  
24. Consequences of Sensory Modality for Perspective-Taking: Comparing Visual, Olfactory and Gustatory Perception \- PMC, accessed on February 14, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC8415443/](https://pmc.ncbi.nlm.nih.gov/articles/PMC8415443/)  
25. Loanword \- Wikipedia, accessed on February 14, 2026, [https://en.wikipedia.org/wiki/Loanword](https://en.wikipedia.org/wiki/Loanword)  
26. Doublet (linguistics) \- Wikipedia, accessed on February 14, 2026, [https://en.wikipedia.org/wiki/Doublet\_(linguistics)](https://en.wikipedia.org/wiki/Doublet_\(linguistics\))  
27. Ontology-Driven Conceptual Modeling Acknowledgements \- Department of Computer Science, accessed on February 14, 2026, [http://www.cs.toronto.edu/caise02/cwelty.pdf](http://www.cs.toronto.edu/caise02/cwelty.pdf)  
28. OWL 2 Web Ontology Language Structural Specification and Functional-Style Syntax (Second Edition) \- W3C, accessed on February 14, 2026, [https://www.w3.org/TR/owl2-syntax/](https://www.w3.org/TR/owl2-syntax/)  
29. Adversarial Semantic Collisions \- ACL Anthology, accessed on February 14, 2026, [https://aclanthology.org/2020.emnlp-main.344/](https://aclanthology.org/2020.emnlp-main.344/)  
30. Contrasting Semantic versus Inhibitory Processing in the Angular Gyrus: An fMRI Study, accessed on February 14, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC6519692/](https://pmc.ncbi.nlm.nih.gov/articles/PMC6519692/)  
31. Accuracy and precision \- Wikipedia, accessed on February 14, 2026, [https://en.wikipedia.org/wiki/Accuracy\_and\_precision](https://en.wikipedia.org/wiki/Accuracy_and_precision)  
32. Measurement or the semantics of numerical information \- Emerald Insight, accessed on February 14, 2026, [https://www.emerald.com/md/article/39/7/583/281243/Measurement-or-the-semantics-of-numerical](https://www.emerald.com/md/article/39/7/583/281243/Measurement-or-the-semantics-of-numerical)  
33. The Theory of Semiotics: Semiotics and Medicine Term Paper \- IvyPanda, accessed on February 14, 2026, [https://ivypanda.com/essays/the-theory-of-semiotics-semiotics-and-medicine/](https://ivypanda.com/essays/the-theory-of-semiotics-semiotics-and-medicine/)  
34. An Extendible Realism-Based Ontology for Kinship \- PMC, accessed on February 14, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC11131162/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11131162/)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADwAAAAYCAYAAACmwZ5SAAADkUlEQVR4Xu2XS4jNURzHv/KIkEQkJJqNR1lgoTxSKAsWbBRKeW0sPELYjGRhwQJFeYXkWSiPlHQn5ZGVhRSpUaKUlKKQx+/T739mzj333Dt3ZpqhzKe+9b/n/O895/c7v8e5Ug89tIfepqGmXulEN9Gt6/c17TMtTSe6EQzdatpcPLfJPNN70+9IH0zfTT9NT0zL5J5MYaGDqnOhLgTHn5Xvs25OmH6YZkVjGLlebvh2lRs22fTUND4a+5tMMT0yjU0ncgw2PTC9No1M5kaZ3iRzGH6k0N8+3UAf0wVTYzKeZaLpo+mq/IsxM0xfTc9Nw4ux0aaXpvnhpX+EFfKoo4jVZIk8dzekE3KPMUe+BjCUEx8TjcWQU3MK8UxqTJOnS64W1IIQXWQaloz3Nw1KxqbKo5FDqskhVeYvG10jP/ltxefADlNJlQvCONM1ee7zu02m4/LfuGs60Ppqm1D9z5j2m56p1WiMZY1LKndgSL+aXYNNl+RV+WHx/EJ+qkdV6VlgE7nwH2A6ZmooPnOqX+RRQlT8Mp1WfXk/wnRKvj4Ofid3JkyQd5ZdxedAsIX3q5LLXza0U16dFxRjMRiMUjCUfhggFL/JI2eg/NSrpUHKdNNa0xDTY3lBCvvDeRxQWkOCwdwNqhLyd0syHk6HdpVSzeAUFm6WF7mOMlNeNJdHY/zuW1U6Lxic23MLufwFKh6OyHmrHoPD4rnQbw+EJ+FLGAORcs90S57LMW2GdK3+iyMwOPdlnMCiLB6Dxy/K0yCkSvz9daaF0WcKIbkaF8QUHFtSa4EM+Zs7CNoRbSmN1ha4nXxS5SnwfFnlBu9Wa87QvuK+HGAhvkN1X108Ly7mKDjnVF4Eqdi80xiNpRCeJbnB1BZufNSWNH8Bh3N4FXOz5eU73J0R92fyOcC9lB/G8FXy1kIVBvL7lfwUY0gL2sd5eTXeK3fMSdMNVb6/SV65iZZciwOKF/nKoVyXF6tm5esC67Nebq4uCHNOiBANxkKonOR5ChvnFEPrST+nECWHVZkeQI8l7Qh59kKfLam8Ysc0qvpcp1lpuq1yR3QEqjBhmsKmuQd8lt+ggAikc+RaJU69L4/eLoGTu6n84vXCb3C54J9XSqjGV+QRxXWR+/tG5aOFA+DSU6sAdhoKEbkZbkDthZyemw5GMNck7yTk76Ty6RYaTHfU8X20Cza9x9QvnegmyHFaVHoJ6eG/4Q8lcLKwMqs9SgAAAABJRU5ErkJggg==>

[image2]: <data:image/png;base64,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>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAO0AAAAYCAYAAAAWEnolAAAIWElEQVR4Xu2be6hcVxXGv6KCz6pRfKAlNxIi4qOKVdEYva1NNEJFVIxiYlFJ7B9VQfERqzDaSpuSaJVE0ioEW3xEAgq22laxFxVbVBClaURT2vhEQcVWCxpiXb+7zsrss+ecmTkzJ01N9gcfd+bsffZee6111l5rn7lSQUFBQUFBQcH/Cx5mfGx+cQpwD/cWnFqYxR8ebXx4frHgxADjXG18cd4wBbjny+pu4GnwWuOT8osFJxyz+sNK44Hq71R4mfFPxvsrHjQ+sdajjvXGY/K+/P2e8Qm1HicPa43v0AOzgz3UuMd4Ud7QAZuNe9WvvKvlYz4ib5gSxR9mw7z+sM74TXUM4juNfzD+3vj0rC2AMb5qvEceGRD0wYInG+/UZCfrCzjrkjoqOQMP1reMb8gbZsQZxo/JZZsXxR+6YV5/wHa7jR/OG9pATn2d8bPGfxlfWG9eBoMSRbYb/2t8f735pAP52CWmTjHmAA/bjcaL84YZ8BbjjzW7sVPMu8sGij90Q1/+8FLjIeOqvKEJzzB+wfhmeZpzQb15GS+QG+kjxqPGl9ebTyvgxL8xPitvmAHo/rDm1ydOukP97LLFH7qhL394vPGnxrflDU14nTxivsh4n0ajJpFkYHya8QZ52kH60QZqiHOMrzeelbUFuH+jmtsfIncClMFnHHJBPh6K4VoK0jTGemp2/czqeswRcuGE4+RnvjXyfk312buNPzQ+Jm+owD3cyxiM9SjjBvlOmIM26sCP5g0d8Wx5etVH/Vb8oY55/CFkydfF3E3Z1RflB5TMORYD4/lyBfzV+Klaq7RJ3o6R7lZ7/YIgH5RHnffKU79bVI/+OCkFO7Uc7V+S1x03V23gPcZPGu+Qy0b/S41vl+9KuzRcFEr/RtX/t8ZnVtdJ8TjJ+4S8Ltsin3Ob8RLjP+RryrFg/IF8pyHi8UAdMV6R9EFm2AQciTqPe39k/Lzxa/LU6S7j4vGeQzDWVIZqAfddKT/M6AMDFX8ILGh2fwhZCMgEtpAFIPNtGn1wqWnbAsBxRP3CYUMU76kDLcgHwigsqq1+oZ1Ij4EWkus4a/THiNfIlRDCkopxWrlPPicyUEvxymLJ+HfVj9BRDteRm4hPDbdavjuwK1AXgNfIIyDRmboMZcecRGAUnxf91D+/ljtErJ9xWDNjAeZd0qgjg3y3Y/x/y2X6nDzVRM4c9FuSj92GFfK6CUfMif7uNf4uu/7x5Tu7ofjDEPP4wzhZIg1uCtTs5siSZwk1oCSiCC93QwDIZxTPQha86/Lno2quX4iex+SREGCQVxtv0vAwgFNS+hBRA2fLTx9DCUSnt8qdhoi4Q8OFISPpGAonCpNyECWZi90tjVxb5TsFcyLzudV1EDtI6mzMcZXcKZ6TXCe6onBSRRA6yg0MqAHT3Y5UB+NgJNKrC9V8SMRY0a8rsBFOHQ4xL4o/OOb1h3GyxHyxxhQ8tAQt7NCKqF8AgvL0E12JcETSTVVbKCjacuCg7CR/kffZb3yXvI4AcX8uEEog8hEBUzD3f6q/gVVyw+VRLa4PsuuAHY50Kz32x0nYAVNnizGQEVkDrCu9v81IOSKaxo4xDozVptdJQG+kWjxQfaD4g6Mvf2iSJX/wU/DQErQIXq0YqK4IFEAUWJRHtdgZItId0KiDhAGOqH1bjxRkkhIC1AG5QVFummYEiFh5RATUBdQHqcz8zSMfQIGMnTpAUxozyUiBSMMw0CQw1pLGp8fMz6EGegwSzUnB2MHS68HHLd/ZDQMVfwB9+QNBMA8IbWsEE9NjJkTgVBGkCAjLwjjWD2DItvolIvKSRh2Pk71HamgkBA6kSuDzZ+SROE97QK7cdxpfqeE7sjA+xn1udU9T2pNGPu69XP4wxENG+hSIa2kagxzoJl1HYIPx6/K1cg/3xo7BXKyP2iwHjpGutQmkWa8yvikha2Xd7H7p9eBLlu+cHsUf+vUHwMOcPoSxxqZgBwjybdnLMtYar1f9pIonnbRmu+ppHY7VVr8Aot4fVTd4KGFL9RllRroIPySfi4URLekLIoqnUS6MjBFwfJSEsTAIUZXFLsjru9gNon5JZWZ9kZqs1/BVC2PermHEXGH8vprTGFKsfIfAmXCqPxufJz81TI31RvmvlVKdgnBwxuwCDL5Ho7vJPCj+0J8/BAgQuR9Qx6cPfooIxCNjrZMvDAVBagXqDUA0uVnD91GfNv6z6hd9UTaLSMFOQPr0c/mJ4H55FCT6BZ5v/KXxWvkY75Mr+2fy312urPphMORbrL4Dxv+KvO935QcUgEiOvDAdAwyMv1D93RpOdNj4Hfl4aUqEfMiPkpmDiHhQo2kMKQ8GTa/jdAO5YZGDQwjmgOwIGLZpJyXy/kTNp8rjgA0v02gQmAXFH/r3hwDzMyfjowPWkWZgKWLXbku1TxhQGlElT4sCKJutPyIJTocS08hCCoUz5w7Z1BfQH4Uxdgr6NclBP/pzXxsijdmnUTlWGX+l0V0m5Is58+9NwCEPacqfrlVA/t3yV0wPdpzu/kDWwsPIzk1g4/5I6XMwDr6ATxRMADsg6R+pUgDFkQqR5uXAGLy748HJDdgFMQ7sMg5pXFOqXdAP+vKHD8jr/o3Vd84E/qb2/wTaLN+N82BT0ACUSqq3q/r+FPkLf1KapogIqLNu0Xy73Wp5HZymcJNAfbZXzT+JLOgHffkDqT67M20L8jJop5ofSjKGb6v7/+KetsAQHOrcKn8lQJ3ET+TiAKMNKJjT4jZDjgOGI1VKTyenwaLm/51ywXj05Q9r5LU6YxCcX6Hm7IhrA/nO3NRe0DPOkx+gdMVW+U/iCk4tzOIPvCrcpvLAFhQUFBQUnCT8D+b2oZTRo2FaAAAAAElFTkSuQmCC>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABMAAAAXCAYAAADpwXTaAAAAiElEQVR4XmNgGAWjgGqAA4jTgJgHXYIcwAjErUBsjC5BLgAZ1AvELOgS5ACQ6wqAOA7KRgECQCxJIpYD4vlAPBmI+RiggBuIq4F4Fhl4BxB/BeJmIGZnoACYAPFqIJZBlyAVCAPxYiCWR5cgB2QBcQS6IDkAlGinArE0ugQ5AJQUeKH0KBhMAABVixNKp22j3QAAAABJRU5ErkJggg==>