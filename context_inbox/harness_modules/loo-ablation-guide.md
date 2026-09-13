# Technical Implementation Guide: Automated Leave-One-Out (LOO) Ablation & Prompt Metrology

This document serves as the formal systems-engineering manual for deploying, running, and interpreting the automated **Leave-One-Out (LOO) Ablation** and **Causal Perturbation Index (CPI)** framework. 

To transition promptware engineering from an artisanal trial-and-error craft into a deterministic, auditable science, operators must systematically measure the quantitative gravitational pull of individual tokens within high-dimensional vector spaces. 

---

## 1. Architectural Foundations of LOO Ablation

In an autoregressive transformer model, natural language instructions do not act as static rules; they function as **topological deformers** that condition the residual stream, altering query-key attention matrices and shaping the predictive probability distribution. 

### The Problem of "Instruction Bloat"
Standard prompt design frequently suffers from **Prompt Bloatware**—the unproductive stacking of defensive instructions and negative constraints (e.g., *"Do not hallucinate"*, *"Write an amazing, high-quality, and robust summary"*). This creates linguistic noise, reduces the **Token-Ink Ratio**, and triggers **Linguistic Overshadowing** at the Layer 8, Head 11 bottleneck—diluting the L2 norm of primary nominal targets and causing the model to ignore critical constraints.

### The Subtractive Solution
To resolve this, we employ **Subtractive Experimentation Protocols**. By establishing a baseline and systematically executing **Leave-One-Out (LOO) Masking**, the system can mathematically isolate the precise causal weight of individual words or phrases. 

```
                          SUBTRACTIVE LOO MASKING
                          
         Original Prompt (P)                      Masked Prompt (P \ {w_i})
   "Extract [titanium] components."            "Extract [MEMBER] components."
                 │                                           │
                 ▼                                           ▼
       Monte Carlo Sampling                       Monte Carlo Sampling
   [ y_1, y_2, ... y_M ] ~ P                   [ y'_1, y'_2, ... y'_M ] ~ P'
                 │                                           │
                 ▼                                           ▼
        Embedding Centroid                          Embedding Centroid
            ( e_control )                              ( e_treatment )
                 │                                           │
                 └──────────────────► ◄──────────────────────┘
                                     │
                                     v
                       Causal Perturbation Index (CPI)
```

---

## 2. Mathematical Formulation of the Causal Perturbation Index (CPI)

The **Causal Perturbation Index (CPI)** is a granular metric that quantifies the isolated causal influence of a specific prompt element on the final output. It translates the qualitative difference between two prompt variants into a standardized statistical effect size.

### Step 1: Monte Carlo Distribution Sampling
Because LLM token generation is stochastic, a single-pass evaluation is highly susceptible to random seed variance. To map the true output probability distribution, the ablator runs $M$ independent Monte Carlo generation passes for the control prompt $P$ and the ablated treatment prompt $P \setminus \{w_i\}$:

$$\mathcal{O}_{\text{control}} = \{y_1, y_2, \dots, y_M\} \sim P(y \mid P)$$

$$\mathcal{O}_{\text{treatment}} = \{y'_1, y'_2, \dots, y'_M\} \sim P(y' \mid P \setminus \{w_i\})$$

### Step 2: Semantic Vector Mapping
Text outputs are projected into a continuous semantic vector space using a TF-IDF vectorizer (offline-native) or dense Sentence-BERT embeddings (production-grade):

$$\vec{e}_j = \text{Embedding}(y_j), \quad \vec{e}'_k = \text{Embedding}(y'_k)$$

### Step 3: Standardized Effect Size Calculation
The CPI calculates the distance between the semantic centroids normalized by the pooled standard deviation (dispersion) of both clusters:

$$\text{CPI}(w_i) = \frac{\left\| \vec{\mu}_{\text{control}} - \vec{\mu}_{\text{treatment}} \right\|_2}{\sqrt{\frac{1}{2}(\sigma^2_{\text{control}} + \sigma^2_{\text{treatment}}) + \epsilon}}$$

Where:
*   **$\vec{\mu}_{\text{control}}$** and **$\vec{\mu}_{\text{treatment}}$** are the centroid vectors of the respective output sets.
*   **$\sigma^2_{\text{control}}$** and **$\sigma^2_{\text{treatment}}$** represent the summed variance of the vectors along each dimension.
*   **$\epsilon$** is a numerical stability floor ($10^{-5}$) to prevent division-by-zero or score explosions under zero-entropy deterministic execution.

### Influence Categorization
*   **$\text{CPI} \ge 0.80$ (Power Words):** Critical instructions or core constraints that heavily deform the latent manifold. These must be locked into top or bottom sandwich positions.
*   **$0.15 < \text{CPI} < 0.80$ (Frictional Modifiers):** Contextual or stylistic elements that softly shape the trajectory. These must be structured with explicit delimiters.
*   **$\text{CPI} \le 0.15$ (Superfluous Filler):** "Chartjunk" or redundant tokens that fail to guide the model, prime candidates for immediate pruning.

---

## 3. Production-Ready Python Implementation

The complete, self-contained Python script is provided below. It features a mock LLM driver for instant offline verification, blank spaCy tokenization, TF-IDF semantic vector mapping, robust CPI calculation, and automatic Markdown report formatting.

```python
#!/usr/bin/env python3
"""
SCOS-LOO-ABLATION: Automated Leave-One-Out (LOO) Prompt Ablation & Metrology Tool
Copyright (c) 2026 Sovereign Context Engineering. All rights reserved.
"""

import re
import math
import argparse
from typing import List, Dict, Tuple, Optional, Any
from abc import ABC, abstractmethod
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

try:
    import spacy
    NLP = spacy.blank("en")
except ImportError:
    NLP = None

COMMON_MODIFIERS = {
    "urgent", "medical", "beautiful", "nice", "fast", "robust", "seamless",
    "dynamic", "exceptional", "commanding", "stunning", "compelling", "amazing",
    "powerful", "terrible", "excellent", "accurate", "human", "good", "bad",
    "strictly", "exactly", "precise", "specific", "hexagonal", "titanium",
    "bi-weekly", "largest", "more", "most", "fake", "artificial", "pseudo"
}

class LMDriver(ABC):
    @abstractmethod
    def generate(self, prompt: str, num_samples: int = 10, temperature: float = 0.7) -> List[str]:
        pass

class MockLMDriver(LMDriver):
    def generate(self, prompt: str, num_samples: int = 10, temperature: float = 0.7) -> List[str]:
        outputs = []
        has_urgent = "urgent" in prompt.lower()
        has_medical = "medical" in prompt.lower()
        has_json = "json" in prompt.lower()
        has_exact = "exactly" in prompt.lower() or "three" in prompt.lower()
        base_seed = hash(prompt) & 0xffffffff
        
        for idx in range(num_samples):
            rng = np.random.default_rng(base_seed + idx)
            adjective_filler = rng.choice(["thoroughly", "carefully", "systematically", "meticulously", "proactively"])
            ending_filler = rng.choice([".", "!", " for enterprise execution.", " within normal thresholds."])
            
            if has_medical:
                if has_urgent:
                    body = f"EMERGENCY CLINICAL SITUATION REPORT: Patient exhibits acute cardiovascular distress. {adjective_filler.capitalize()} triage required{ending_filler}"
                else:
                    body = f"Standard medical chart summary: Patient review indicates normal baseline recovery rates. {adjective_filler.capitalize()} review completed{ending_filler}"
            else:
                body = f"Operational workflow overview: System parameters verified at standard capacity. Processes {adjective_filler} checked{ending_filler}"
                
            if has_json:
                if has_exact:
                    body = f'{{"status": "CRITICAL", "cases": 3, "summary": "{body}"}}'
                else:
                    chatter = " Here is your requested JSON object:" if rng.random() > 0.4 else ""
                    body = f'{chatter} {{"status": "ALERT", "summary": "{body}"}}'
            else:
                body = f"I would be glad to help you with that. {body} Please let me know if you need more details!"
                
            outputs.append(body)
        return outputs

class LOOAblator:
    def __init__(self, driver: LMDriver):
        self.driver = driver
        self.vectorizer = TfidfVectorizer(token_pattern=r'(?u)\b\w+\b')
        
    def tokenize(self, text: str) -> List[str]:
        if NLP:
            doc = NLP(text)
            return [token.text for token in doc]
        else:
            return re.findall(r'\w+|[^\w\s]', text)

    def extract_ablation_targets(self, prompt: str, manual_targets: Optional[List[str]] = None) -> List[str]:
        bracketed = re.findall(r'\[\[(.*?)\]\]', prompt)
        if bracketed:
            return list(set(bracketed))
        if manual_targets:
            return manual_targets
        tokens = self.tokenize(prompt)
        targets = set()
        for token in tokens:
            cleaned = token.lower().strip()
            if cleaned in COMMON_MODIFIERS:
                targets.add(token)
        return list(targets)

    def generate_ablated_prompt(self, base_prompt: str, target: str) -> str:
        if f"[[{target}]]" in base_prompt:
            return base_prompt.replace(f"[[{target}]]", "").replace("  ", " ").strip()
        escaped = re.escape(target)
        pattern = re.compile(rf'\b{escaped}\b', re.IGNORECASE)
        perturbed = pattern.sub("", base_prompt)
        perturbed = re.sub(r'\s+', ' ', perturbed)
        perturbed = re.sub(r'\s*,\s*,', ',', perturbed)
        return perturbed.strip()

    def calculate_cpi(self, control_embeddings: np.ndarray, treatment_embeddings: np.ndarray, eps: float = 1e-5) -> float:
        mu_control = np.mean(control_embeddings, axis=0)
        mu_treatment = np.mean(treatment_embeddings, axis=0)
        centroid_distance = np.linalg.norm(mu_control - mu_treatment)
        var_control = np.var(control_embeddings, axis=0).sum()
        var_treatment = np.var(treatment_embeddings, axis=0).sum()
        pooled_std = math.sqrt(0.5 * (var_control + var_treatment) + eps)
        return centroid_distance / pooled_std

    def run_ablation_audit(self, base_prompt: str, targets: List[str], samples_m: int = 15, temp: float = 0.7) -> Dict[str, Any]:
        results = {}
        cleaned_base = base_prompt.replace("[[", "").replace("]]", "")
        
        print(f"[*] Commencing LOO Ablation on {len(targets)} targets with M={samples_m} samples per variant...")
        print("[*] Generating Control baseline outputs...")
        control_outputs = self.driver.generate(cleaned_base, num_samples=samples_m, temperature=temp)
        
        all_variants_outputs = {"Control": control_outputs}
        ablated_prompts = {"Control": cleaned_base}
        
        for target in targets:
            print(f"[*] Processing ablated variant: Subtracted -> '{target}'")
            perturbed_prompt = self.generate_ablated_prompt(base_prompt, target)
            ablated_prompts[target] = perturbed_prompt
            treatment_outputs = self.driver.generate(perturbed_prompt, num_samples=samples_m, temperature=temp)
            all_variants_outputs[target] = treatment_outputs
            
        flat_corpus = []
        for v in all_variants_outputs.values():
            flat_corpus.extend(v)
            
        self.vectorizer.fit(flat_corpus)
        control_vecs = self.vectorizer.transform(control_outputs).toarray()
        
        for target in targets:
            treatment_outputs = all_variants_outputs[target]
            treatment_vecs = self.vectorizer.transform(treatment_outputs).toarray()
            cpi = self.calculate_cpi(control_vecs, treatment_vecs)
            
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
    md = [
        "# SCOS LOO Ablation & Causal Perturbation Index Report",
        "## Executive Summary",
        "This report isolates the isolated causal influence of prompt modifiers on generation trajectories.",
        "",
        "### Baseline Prompt Structure",
        f"```text\n{audit_data['control_prompt']}\n```",
        "",
        "## Causal Perturbation Scorecard",
        "| Target Token | CPI Score | Semantic Category | Perturbed Prompt Structure |",
        "| :--- | :---: | :--- | :--- |"
    ]
    
    sorted_results = sorted(audit_data["ablation_results"].items(), key=lambda x: x[1]["cpi"], reverse=True)
    for token, res in sorted_results:
        md.append(f"| **{token}** | `{res['cpi']:.4f}` | {res['category']} | *\"{res['perturbed_prompt']}\"* |")
        
    md.append("\n## Structural Deep-Dive & Remediation Guidelines")
    for token, res in sorted_results:
        md.append(f"### Target token: '{token}' (CPI: `{res['cpi']:.4f}`)")
        md.append(f"**Classification:** {res['category']}\n")
        if "POWER_WORD" in res["category"]:
            md.append("- **Action:** Enforce strict positional primacy. Ensure this token resides in the first-prefill chunk (Top Bun) or bottom sandwich boundary.")
        elif "FRICTIONAL" in res["category"]:
            md.append("- **Action:** Modularize and monitor. This token acts as a soft guide but might contribute to high-variance semantic drift if over-stacked.")
        else:
            md.append("- **Action:** Refactor / Prune. This token is candidate 'chartjunk'. Excising it preserves the attention-head L2 norm and decreases token overhead.")
        md.append(f"\n**Ablated Sample Output:**\n> \"{res['sample_output_diff']}\"\n")
        
    return "\n".join(md)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run an automated Leave-One-Out (LOO) prompt ablation.")
    parser.add_argument("--prompt", type=str, required=True, help="Base prompt or prompt template.")
    parser.add_argument("--targets", type=str, nargs="+", help="Manual target tokens to ablate.")
    parser.add_argument("--samples", type=int, default=15, help="Number of Monte Carlo samples.")
    parser.add_argument("--temp", type=float, default=0.7, help="Decoder temperature.")
    parser.add_argument("--output_file", type=str, help="Absolute path to save report.")
    args = parser.parse_args()
    
    driver = MockLMDriver()
    ablator = LOOAblator(driver)
    targets = ablator.extract_ablation_targets(args.prompt, args.targets)
    
    report_data = ablator.run_ablation_audit(args.prompt, targets, samples_m=args.samples, temp=args.temp)
    report_md = format_markdown_report(report_data)
    
    if args.output_file:
        with open(args.output_file, "w") as f:
            f.write(report_md)
        print(f"[+] Diagnostic audit successfully written to: {args.output_file}")
    else:
        print("\n=== EXECUTIVE DIAGNOSTIC REPORT ===\n")
        print(report_md)
```

---

## 4. How to Execute the Script

### Running a Diagnostic Dry-Run
Run the script passing the base prompt. You can mark target words to evaluate by surrounding them with double brackets `[[token]]` for explicit focus:

```bash
python3 /workspace/scratch/loo_ablation.py \
  --prompt "Write a strictly [[JSON]] object representing a [[medical]] case containing [[exactly]] three parameters." \
  --samples 15 \
  --temp 0.7
```

### Auto-Mining Mode
If you omit the target tokens, the script automatically parses the prompt and targets common evaluative, descriptive, and limiting adjectives from our built-in linguistic typology:

```bash
python3 /workspace/scratch/loo_ablation.py \
  --prompt "Write an urgent, medical summary of this beautiful and robust titanium dataset." \
  --samples 15
```

### Saving the Report to Disk
Export the mathematical analysis scorecard directly to a production markdown file:

```bash
python3 /workspace/scratch/loo_ablation.py \
  --prompt "Write a strictly [[JSON]] object representing a [[medical]] case." \
  --output_file "/workspace/scratch/audit_report.md"
```

---

## 5. Integrating with Production APIs

To run this in a production workspace with live APIs, implement a custom subclass of `LMDriver` connecting to your API provider (e.g., OpenAI, Anthropic, or Gemini):

```python
import openai

class ProductionLMDriver(LMDriver):
    def __init__(self, api_key: str, model_name: str = "gpt-4o"):
        self.client = openai.OpenAI(api_key=api_key)
        self.model_name = model_name

    def generate(self, prompt: str, num_samples: int = 15, temperature: float = 0.7) -> List[str]:
        completions = []
        for _ in range(num_samples):
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature
            )
            completions.append(response.choices[0].message.content)
        return completions
```
This is fully compatible with the existing `LOOAblator` logic, allowing you to seamlessly swap out the mock testing engine for production telemetry gathering.
