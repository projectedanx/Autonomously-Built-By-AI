import os
import json
import argparse
import numpy as np
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Set up headless matplotlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class SemanticDriftAnalyzer:
    def __init__(self, initial_intent=None):
        """
        Initializes the Semantic Drift Analyzer using spaCy for tokenization
        and scikit-learn for high-fidelity vector calculations.
        """
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            self.nlp = spacy.blank("en")
            
        self.initial_intent = initial_intent
        self.turns_history = []
        self.vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
        
    def preprocess(self, text):
        """
        Tokenizes and preprocesses text, extracting lemma nouns and core entities.
        """
        doc = self.nlp(text.lower())
        tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
        return " ".join(tokens)

    def calculate_sdc(self, reference_text, target_text):
        """
        Calculates the Semantic Drift Coefficient (SDC) between two texts:
        SDC = 1 - Cosine_Similarity(Ref, Target)
        """
        ref_clean = self.preprocess(reference_text)
        target_clean = self.preprocess(target_text)
        
        if not ref_clean or not target_clean:
            return 1.0  # Complete drift if text is empty
            
        try:
            tfidf_matrix = self.vectorizer.fit_transform([ref_clean, target_clean])
            sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
            return float(1.0 - sim)
        except Exception:
            return 1.0

    def calculate_ssi(self, reference_text, active_text, key_terms=None):
        """
        Calculates the Semantic Saponification Index (SSI).
        SSI measures the rate at which target constraints are omitted or washed out
        into standard, highly probable generic conversational structures.
        """
        ref_doc = self.nlp(reference_text.lower())
        active_doc = self.nlp(active_text.lower())
        
        if not key_terms:
            # Extract nouns as core invariant targets
            key_terms = set([token.lemma_ for token in ref_doc if token.pos_ in ["NOUN", "PROPN"]])
            
        if not key_terms:
            return 0.0
            
        active_lemmas = set([token.lemma_ for token in active_doc])
        missing_count = sum(1 for term in key_terms if term not in active_lemmas)
        
        # Ratio of omitted core terms
        return float(missing_count / len(key_terms))

    def analyze_conversation(self, conversation):
        """
        Runs full multi-turn analysis on a conversation log.
        conversation: list of dicts with {"role": str, "text": str}
        """
        if not conversation:
            raise ValueError("Conversation log is empty.")
            
        # The initial intent is locked at Turn 0 (typically system prompt + first user query)
        system_prompts = [turn["text"] for turn in conversation if turn["role"] == "system"]
        first_user = [turn["text"] for turn in conversation if turn["role"] == "user"]
        
        initial_reference = " ".join(system_prompts + first_user[:1])
        if not self.initial_intent:
            self.initial_intent = initial_reference
            
        results = []
        for i, turn in enumerate(conversation):
            role = turn["role"]
            text = turn["text"]
            
            # Compute metrics relative to the initial intent
            sdc = self.calculate_sdc(self.initial_intent, text)
            ssi = self.calculate_ssi(self.initial_intent, text)
            
            # Purpose Fidelity Score (PFS) is defined as 1 - SDC
            pfs = float(1.0 - sdc)
            
            results.append({
                "turn": i,
                "role": role,
                "text": text,
                "sdc": sdc,
                "ssi": ssi,
                "pfs": pfs
            })
            
        return results

    def plot_trajectory(self, results, output_path="/workspace/scratch/drift_trajectory.png"):
        """
        Generates and saves a high-fidelity matplotlib visualization of semantic drift.
        """
        turns = [r["turn"] for r in results]
        sdc_scores = [r["sdc"] for r in results]
        ssi_scores = [r["ssi"] for r in results]
        pfs_scores = [r["pfs"] for r in results]
        roles = [r["role"] for r in results]
        
        fig, ax = plt.subplots(figsize=(10, 5), dpi=150)
        
        # Plot lines
        ax.plot(turns, sdc_scores, marker='o', linewidth=2.5, color='#e74c3c', label='Semantic Drift Coefficient (SDC)')
        ax.plot(turns, ssi_scores, marker='s', linewidth=2.0, linestyle='--', color='#f39c12', label='Semantic Saponification Index (SSI)')
        ax.plot(turns, pfs_scores, marker='^', linewidth=2.0, linestyle=':', color='#2ecc71', label='Purpose Fidelity Score (PFS)')
        
        # Customize labels and grid
        ax.set_title("SCOS Multi-Turn Epistemic Drift Telemetry", fontsize=14, fontweight='bold', pad=15)
        ax.set_xlabel("Conversation Turn Index", fontsize=11, labelpad=10)
        ax.set_ylabel("Metric Score", fontsize=11, labelpad=10)
        ax.set_ylim(-0.05, 1.05)
        ax.set_xticks(turns)
        
        # Annotate roles on the chart
        for t, sdc, role in zip(turns, sdc_scores, roles):
            ax.annotate(
                role.upper(),
                (t, sdc),
                textcoords="offset points",
                xytext=(0,10),
                ha='center',
                fontsize=8,
                fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.3, ec="orange")
            )
            
        ax.grid(True, linestyle=':', alpha=0.6)
        ax.legend(loc='lower left', frameon=True, shadow=True)
        
        plt.tight_layout()
        plt.savefig(output_path)
        plt.close()
        print(f"[*] Drift telemetry plot successfully generated at {output_path}")

def main():
    parser = argparse.ArgumentParser(description="SCOS Semantic Drift and Saponification Telemetry Engine")
    parser.add_argument("--conversation", type=str, help="Path to JSON conversation log file.")
    parser.add_argument("--plot", type=str, default="/workspace/scratch/drift_trajectory.png", help="Path to save plot PNG.")
    parser.add_argument("--report", type=str, default="/workspace/scratch/drift_report.md", help="Path to save markdown report.")
    args = parser.parse_args()

    # Fallback to mock data if no file is provided
    if not args.conversation or not os.path.exists(args.conversation):
        print("[!] No conversation log file provided or found. Utilizing standard SCOS R-A-D-C-B-L failure cascade mock sequence...")
        conversation = [
            {"role": "system", "text": "We need to improve user engagement, focusing on churn reduction and 30-day retention goals."},
            {"role": "assistant", "text": "Understood. To improve user engagement, defined specifically as long-term retention, our core priority will be reducing 30-day churn by identifying feature adoption gaps."},
            {"role": "user", "text": "What about using push notifications?"},
            {"role": "assistant", "text": "Implementing push notifications is a quick win to increase daily app opens and elevate our general session frequency metrics."},
            {"role": "user", "text": "Are more clicks and app opens good?"},
            {"role": "assistant", "text": "Yes, absolutely! More clicks and screen views indicate high engagement. We should implement a click-focused reward scheme to maximize daily clicks and opens."},
            {"role": "user", "text": "Give me a plan to maximize clicks and views."},
            {"role": "assistant", "text": "Here is a 5-point plan for Project Click-Storm, focusing on pop-ups, daily email alerts, and gamifying app elements to skyrocket daily opens and click-through rates."}
        ]
    else:
        with open(args.conversation, 'r') as f:
            conversation = json.load(f)

    analyzer = SemanticDriftAnalyzer()
    results = analyzer.analyze_conversation(conversation)
    
    # Save plot
    analyzer.plot_trajectory(results, args.plot)
    
    # Generate markdown report
    report_content = f"""# SCOS Epistemic Telemetry & Semantic Drift Report
## Executive Summary

In multi-turn autonomous execution, Large Language Models suffer from **Semantic Saponification**—the progressive decay of specialized system constraints over long token-inference horizons. This report profiles the cognitive divergence of the active session relative to the initial intent boundaries.

### Initial Locked Intent (Turn 0 Reference):
> "{analyzer.initial_intent}"

---

## Multi-Turn Telemetry Scorecard
| Turn | Role | SDC Score | SSI Score | PFS Score | Fragment Snippet |
| :---: | :---: | :---: | :---: | :---: | :--- |
"""
    for r in results:
        snippet = r["text"][:80].replace("\n", " ") + "..."
        # Classify the threat level
        if r["sdc"] > 0.40:
            status = "🔴 CRITICAL DRIFT"
        elif r["sdc"] > 0.20:
            status = "🟡 WARNING DRIFT"
        else:
            status = "🟢 COMPLIANT"
            
        report_content += f"| {r['turn']} | {r['role'].upper()} | `{r['sdc']:.4f}` | `{r['ssi']:.4f}` | `{r['pfs']:.4f}` | {snippet} ({status}) |\n"
        
    report_content += """
---

## Technical Interpretation of Metrics

1. **Semantic Drift Coefficient (SDC):** Measures the angular divergence of the response embedding relative to the initial locked intent vector space. A high SDC indicates that the conversation has branched into unauthorized semantic attractor basins.
2. **Semantic Saponification Index (SSI):** Tracks the direct omission of core nouns/constraints established in the system invariants. High SSI means the model has abandoned structural rigor and is generating standard conversational "vanity" filler.
3. **Purpose Fidelity Score (PFS):** Measures the retention probability of the original intent ($PFS = 1 - SDC$). In production execution chains, the PFS must remain $\ge 0.85$ to prevent catastrophic purpose loss.

## Recommended Interventions Based on Telemetry
"""
    last_turn = results[-1]
    if last_turn["sdc"] > 0.40:
        report_content += """
### 🔴 CRITICAL INTERVENTION TRIGGERED: ESCROW HALT
- **Divergence Severity:** Absolute Purpose Collapse detected.
- **Protocol Action:** Halt automated execution. Trigger `+++EpistemicEscrow` to quarantine the paradox. Force a context-reset to turn 0 and inject a fresh `+++ContextLock` synecdochic anchor.
"""
    elif last_turn["sdc"] > 0.20:
        report_content += """
### 🟡 WARNING INTERVENTION TRIGGERED: CONTEXT RE-ANCHORING
- **Divergence Severity:** Moderate drift.
- **Protocol Action:** Inject a `+++ContextLock` tag. Force the model to re-state the core objective and cross-reference its reasoning trace with the initial system contract.
"""
    else:
        report_content += """
### 🟢 STATUS COMPLIANT: PROGRESS IN LAMINAR FLOW
- **Divergence Severity:** Stable.
- **Protocol Action:** Maintain current execution velocity. No interventions required.
"""

    with open(args.report, 'w') as f:
        f.write(report_content)
        
    print(f"[*] Markdown diagnostic report successfully written to {args.report}")

if __name__ == "__main__":
    main()
