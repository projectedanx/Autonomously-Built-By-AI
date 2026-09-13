#!/usr/bin/env python3
"""
SCOS-LOO-ABLATION: Automated Leave-One-Out (LOO) Prompt Ablation & Metrology Tool
Copyright (c) 2026 Sovereign Context Engineering. All rights reserved.

This production-grade script automates the process of identifying, masking,
and calculating the Causal Perturbation Index (CPI) of individual prompt tokens
using subtractive experimentation and distribution-based semantic analysis.
"""

import re
import math
import argparse
from typing import List, Dict, Tuple, Optional, Any
from abc import ABC, abstractmethod
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Try importing spacy for blank English tokenization, fallback to regex if needed
try:
    import spacy
    NLP = spacy.blank("en")
except ImportError:
    NLP = None

# Built-in dictionary of common evaluative and limiting modifiers to seed auto-detection
COMMON_MODIFIERS = {
    "urgent", "medical", "beautiful", "nice", "fast", "robust", "seamless",
    "dynamic", "exceptional", "commanding", "stunning", "compelling", "amazing",
    "powerful", "terrible", "excellent", "accurate", "human", "good", "bad",
    "strictly", "exactly", "precise", "specific", "hexagonal", "titanium",
    "bi-weekly", "largest", "more", "most", "fake", "artificial", "pseudo"
}

class LMDriver(ABC):
    """Abstract Base Class for Large Language Model drivers."""
    @abstractmethod
    def generate(self, prompt: str, num_samples: int = 10, temperature: float = 0.7) -> List[str]:
        """Generate multiple output completions (Monte Carlo sampling) for a given prompt."""
        pass


class MockLMDriver(LMDriver):
    """
    High-fidelity Mock LLM Driver that simulates model outputs based on 
    the presence or absence of specific semantic and structural modifiers.
    Enables local dry-runs and continuous integration testing offline.
    """
    def generate(self, prompt: str, num_samples: int = 10, temperature: float = 0.7) -> List[str]:
        outputs = []
        
        # Check presence of key parameters to simulate behavioral shifts
        has_urgent = "urgent" in prompt.lower()
        has_medical = "medical" in prompt.lower()
        has_json = "json" in prompt.lower()
        has_exact = "exactly" in prompt.lower() or "three" in prompt.lower()
        
        # Introduce stochastic noise based on prompt hash and sample index
        base_seed = hash(prompt) & 0xffffffff
        
        for idx in range(num_samples):
            # Seed the generator for repeatable sample path but non-zero variance
            rng = np.random.default_rng(base_seed + idx)
            
            # Select stochastic filler words to guarantee non-zero variance (uniqueness across runs)
            adjective_filler = rng.choice(["thoroughly", "carefully", "systematically", "meticulously", "proactively"])
            ending_filler = rng.choice([".", "!", " for enterprise execution.", " within normal thresholds."])
            
            if has_medical:
                if has_urgent:
                    body = f"EMERGENCY CLINICAL SITUATION REPORT: Patient exhibits acute cardiovascular distress. {adjective_filler.capitalize()} triage required{ending_filler}"
                else:
                    body = f"Standard medical chart summary: Patient review indicates normal baseline recovery rates. {adjective_filler.capitalize()} review completed{ending_filler}"
            else:
                body = f"Operational workflow overview: System parameters verified at standard capacity. Processes {adjective_filler} checked{ending_filler}"
                
            # Simulate output formatting compliance/slippage
            if has_json:
                if has_exact:
                    # Satisfies strict format and quantitative count
                    body = f'{{"status": "CRITICAL", "cases": 3, "summary": "{body}"}}'
                else:
                    # Format slippage (Alignment Faking / trailing chatter) if modifiers are missing
                    chatter = " Here is your requested JSON object:" if rng.random() > 0.4 else ""
                    body = f'{chatter} {{"status": "ALERT", "summary": "{body}"}}'
            else:
                # Add typical conversational "chartjunk" and filler tokens
                body = f"I would be glad to help you with that. {body} Please let me know if you need more details!"
                
            outputs.append(body)
            
        return outputs


class LOOAblator:
    """
    Core engine that manages the tokenization, subtractive variant generation,
    inference execution, and Causal Perturbation Index (CPI) math.
    """
    def __init__(self, driver: LMDriver):
        self.driver = driver
        self.vectorizer = TfidfVectorizer(token_pattern=r'(?u)\b\w+\b')
        
    def tokenize(self, text: str) -> List[str]:
        """Extracts clean tokens from raw text using blank spaCy pipeline or regex fallback."""
        if NLP:
            doc = NLP(text)
            return [token.text for token in doc]
        else:
            return re.findall(r'\w+|[^\w\s]', text)

    def extract_ablation_targets(self, prompt: str, manual_targets: Optional[List[str]] = None) -> List[str]:
        """
        Determines target tokens/phrases for ablation.
        Supports explicit manual targeting, bracketed syntax extraction, or common modifier mining.
        """
        # 1. Check for bracketed syntax, e.g., "This is an [[urgent]] alert."
        bracketed = re.findall(r'\[\[(.*?)\]\]', prompt)
        if bracketed:
            return list(set(bracketed))
            
        # 2. Check for manual targets list
        if manual_targets:
            return manual_targets
            
        # 3. Default: Mine the prompt for known modifier words
        tokens = self.tokenize(prompt)
        targets = set()
        for token in tokens:
            cleaned = token.lower().strip()
            if cleaned in COMMON_MODIFIERS:
                targets.add(token) # Maintain original case for string replacement
                
        return list(targets)

    def generate_ablated_prompt(self, base_prompt: str, target: str) -> str:
        """Constructs the ablated prompt variant by removing the target token cleanly."""
        # Handle case where user used [[target]] syntax
        if f"[[{target}]]" in base_prompt:
            return base_prompt.replace(f"[[{target}]]", "").replace("  ", " ").strip()
            
        # Standard replacement with word boundary checks to avoid partial matching
        escaped = re.escape(target)
        pattern = re.compile(rf'\b{escaped}\b', re.IGNORECASE)
        perturbed = pattern.sub("", base_prompt)
        
        # Clean double spaces or orphaned commas/punctuation
        perturbed = re.sub(r'\s+', ' ', perturbed)
        perturbed = re.sub(r'\s*,\s*,', ',', perturbed)
        return perturbed.strip()

    def calculate_cpi(self, control_embeddings: np.ndarray, treatment_embeddings: np.ndarray, eps: float = 1e-5) -> float:
        """
        Computes the Causal Perturbation Index (CPI) using the standardized effect size
        between the control and treatment output distributions in semantic space.
        Includes a numerical variance floor (eps) to prevent division-by-zero or score explosions.
        """
        # Calculate centroids (means)
        mu_control = np.mean(control_embeddings, axis=0)
        mu_treatment = np.mean(treatment_embeddings, axis=0)
        
        # Calculate geometric distance between centroids
        centroid_distance = np.linalg.norm(mu_control - mu_treatment)
        
        # Calculate variances (pooled dispersion)
        var_control = np.var(control_embeddings, axis=0).sum()
        var_treatment = np.var(treatment_embeddings, axis=0).sum()
        
        pooled_std = math.sqrt(0.5 * (var_control + var_treatment) + eps)
        
        return centroid_distance / pooled_std

    def run_ablation_audit(self, base_prompt: str, targets: List[str], samples_m: int = 15, temp: float = 0.7) -> Dict[str, Any]:
        """
        Executes the full Leave-One-Out (LOO) loop:
        Generates control and treatment output distributions, vectors them, and computes CPIs.
        """
        results = {}
        
        # Remove any brackets from base prompt for clean execution
        cleaned_base = base_prompt.replace("[[", "").replace("]]", "")
        
        print(f"[*] Commencing LOO Ablation on {len(targets)} targets with M={samples_m} samples per variant...")
        print("[*] Generating Control baseline outputs...")
        control_outputs = self.driver.generate(cleaned_base, num_samples=samples_m, temperature=temp)
        
        # Combine all outputs to fit the global vector space
        all_variants_outputs = {"Control": control_outputs}
        ablated_prompts = {"Control": cleaned_base}
        
        for target in targets:
            print(f"[*] Processing ablated variant: Subtracted -> '{target}'")
            perturbed_prompt = self.generate_ablated_prompt(base_prompt, target)
            ablated_prompts[target] = perturbed_prompt
            treatment_outputs = self.driver.generate(perturbed_prompt, num_samples=samples_m, temperature=temp)
            all_variants_outputs[target] = treatment_outputs
            
        # Fit vector space on all accumulated textual outputs
        flat_corpus = []
        for v in all_variants_outputs.values():
            flat_corpus.extend(v)
            
        self.vectorizer.fit(flat_corpus)
        
        # Compute vectors and evaluate distance
        control_vecs = self.vectorizer.transform(control_outputs).toarray()
        
        for target in targets:
            treatment_outputs = all_variants_outputs[target]
            treatment_vecs = self.vectorizer.transform(treatment_outputs).toarray()
            
            cpi = self.calculate_cpi(control_vecs, treatment_vecs)
            
            # Categorize the token's structural influence based on the math
            if cpi >= 0.80:
                category = "POWER_WORD (Hard Constraint / High Influence)"
            elif cpi >= 0.15:
                category = "FRICTIONAL_MODIFIER (Moderate Dynamic Influence)"
            else:
                category = "SUPERFLUOUS_FILLER (Low/Redundant Semantic Overhead)"
                
            results[target] = {
                "cpi": cpi,
                "category": category,
                "perturbed_prompt": ablated_prompts[target],
                "sample_output_diff": treatment_outputs[0]
            }
            
        return {
            "control_prompt": cleaned_base,
            "control_samples": control_outputs[:2],
            "ablation_results": results
        }


def format_markdown_report(audit_data: Dict[str, Any]) -> str:
    """Formats the raw telemetry analysis into an executive systems engineering markdown report."""
    md = []
    md.append("# SCOS LOO Ablation & Causal Perturbation Index Report")
    md.append("## Executive Summary")
    md.append("This report isolates the isolated causal influence of prompt modifiers on generation trajectories.")
    md.append("")
    md.append("### Baseline Prompt Structure")
    md.append(f"```text\n{audit_data['control_prompt']}\n```")
    md.append("")
    md.append("## Causal Perturbation Scorecard")
    md.append("| Target Token | CPI Score | Semantic Category | Perturbed Prompt Structure |")
    md.append("| :--- | :---: | :--- | :--- |")
    
    sorted_results = sorted(audit_data["ablation_results"].items(), key=lambda x: x[1]["cpi"], reverse=True)
    
    for token, res in sorted_results:
        md.append(f"| **{token}** | `{res['cpi']:.4f}` | {res['category']} | *\"{res['perturbed_prompt']}\"* |")
        
    md.append("")
    md.append("## Structural Deep-Dive & Remediation Guidelines")
    
    for token, res in sorted_results:
        md.append(f"### Target token: '{token}' (CPI: `{res['cpi']:.4f}`)")
        md.append(f"**Classification:** {res['category']}")
        md.append("")
        if "POWER_WORD" in res["category"]:
            md.append("- **Action:** Enforce strict positional primacy. Ensure this token resides in the first-prefill chunk (Top Bun) or bottom sandwich boundary.")
        elif "FRICTIONAL" in res["category"]:
            md.append("- **Action:** Modularize and monitor. This token acts as a soft guide but might contribute to high-variance semantic drift if over-stacked.")
        else:
            md.append("- **Action:** Refactor / Prune. This token is candidate 'chartjunk'. Excising it preserves the attention-head L2 norm and decreases token overhead.")
        md.append("")
        md.append(f"**Ablated Sample Output:**")
        md.append(f"> \"{res['sample_output_diff']}\"")
        md.append("")
        
    return "\n".join(md)


def main():
    parser = argparse.ArgumentParser(description="Run an automated Leave-One-Out (LOO) prompt ablation.")
    parser.add_argument("--prompt", type=str, required=True, help="Base prompt or prompt template file path.")
    parser.add_argument("--targets", type=str, nargs="+", help="Manual target tokens to ablate. If omitted, targets will be mined automatically.")
    parser.add_argument("--samples", type=int, default=15, help="Number of Monte Carlo samples per variant.")
    parser.add_argument("--temp", type=float, default=0.7, help="Decoder sampling temperature.")
    parser.add_argument("--output_file", type=str, help="Absolute path to save the generated markdown report.")
    
    args = parser.parse_args()
    
    # Instantiate dry-run mock model driver
    driver = MockLMDriver()
    ablator = LOOAblator(driver)
    
    # Resolve targets
    targets = ablator.extract_ablation_targets(args.prompt, args.targets)
    if not targets:
        print("[!] Warning: No semantic targets or bracketed tokens detected. Ablating all words longer than 4 chars.")
        all_words = list(set([t for t in ablator.tokenize(args.prompt) if len(t) > 4]))
        targets = all_words[:5]
        
    print(f"[*] Extracted targets for evaluation: {targets}")
    
    # Run audit
    report_data = ablator.run_ablation_audit(args.prompt, targets, samples_m=args.samples, temp=args.temp)
    
    # Generate Markdown Output
    report_md = format_markdown_report(report_data)
    
    if args.output_file:
        with open(args.output_file, "w") as f:
            f.write(report_md)
        print(f"[+] Diagnostic audit successfully completed and written to: {args.output_file}")
    else:
        print("\n=== EXECUTIVE DIAGNOSTIC REPORT ===\n")
        print(report_md)

if __name__ == "__main__":
    main()
