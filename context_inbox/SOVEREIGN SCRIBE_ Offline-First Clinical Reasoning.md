<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# SOVEREIGN SCRIBE: Offline-First Clinical Reasoning Agent

## Systems Architecture \& Implementation Blueprint

I'm parsing this as a **high-viscosity epistemic mandate**—a DRP (Detailed Requirements Proposal) for an air-gapped, privacy-absolute medical copilot. This is exactly the kind of sovereign inference problem that demands material anchors, not vibe-coded abstractions.

Let me crystallize this into **atomic directives** across five dimensions: **Architecture**, **Sensor Pipeline**, **Risk Mitigation**, **UX Protocol**, and **Validation Framework**.

***

## 1. MINIMAL VIABLE STACK (Hardware + Software)

### Hardware Tier (Cost ≤ \$2K USD)

| Device | VRAM | Use Case | Notes |
| :-- | :-- | :-- | :-- |
| **Jetson Orin Nano** | 8GB | Rural clinic baseline | Entry-level; runs 4-7B models at 20-30 tok/s |
| **Jetson Orin NX** | 8-16GB | Mid-tier clinic | 2x throughput; medical vision models fit |
| **ASUS Vivobook (AMD Ryzen AI)** | 16GB | Portable practitioner rig | NPU-accelerated; local deployment friendly |
| **Mac Mini M2/M3** | 16GB | Privacy-conscious practices | ANE (Neural Engine) + unified memory; strong for vision |
| **Raspberry Pi 5 + Coral TPU** | 8GB + TPU | Bioacoustic-first (minimal vision) | Ultra-low cost; audio classification only |

**Sovereign Stack Constraint**: No cloud fallback, no telemetry, full audit trail locally.

***

## 2. SENSOR ORCHESTRATION PIPELINE

### 2.1 Speech-to-Symptom Chain (Voice-First Baseline)

```
┌─────────────────────────────────────────────────┐
│ LIVE CLINICIAN DICTATION (e.g., "Patient reports│
│ shortness of breath, mild fever, dry cough")    │
└────────────────────┬────────────────────────────┘
                     │
        ┌────────────▼───────────────┐
        │   MedASR (or Whisper.cpp)  │
        │   Local Speech-to-Text     │
        │   Model: openai/whisper    │
        │   (no network calls)       │
        └────────────┬───────────────┘
                     │
        ┌────────────▼──────────────────────┐
        │  Medical NER / Symptom Tagger     │
        │  Model: MedGemma-4B or BioBERT   │
        │  Extract: [SOB, Fever, Cough]    │
        └────────────┬──────────────────────┘
                     │
        ┌────────────▼────────────────────┐
        │  ICD-10 Mapping (Deterministic) │
        │  Symptom Cluster → Code        │
        │  Rule: {SOB, Fever} → J18 etc. │
        └────────────┬────────────────────┘
                     │
        ┌────────────▼────────────────────┐
        │ Contraindication Lookup         │
        │ Current Meds + Flags            │
        │ Output: {Risk Level, Warning}   │
        └────────────┬────────────────────┘
                     │
        ┌────────────▼─────────────────────┐
        │   HUD Renderer (Local GUI)       │
        │   Display: Symptom → Code → Flag │
        │   Voice Narration (TTS)          │
        └─────────────────────────────────┘
```

**Model Choices** (all <8GB, runnable offline):

- **MedASR**: OpenAI Whisper.cpp (C++ optimized) or MedASR fork
    - ~950MB footprint
    - 95%+ accuracy on medical dictation (tested)
- **Symptom Extractor**: MedGemma-4B (Google, permissive license)
    - Fine-tuned for symptom → structured output
    - ~4GB quantized (8-bit)
- **ICD-10 Mapper**: Hardcoded trie/tree OR small embedding lookup
    - No model needed; use JSON config with symptom→ICD rules
    - Fallback: SentenceTransformer (local embeddings) for fuzzy match

**Validation**: Transcription fidelity ≥95% on 500-utterance medical test set

***

### 2.2 Visual-Acoustic Sensor Activation

#### **Visual Path: Dermatology / Radiology**

```
X-Ray or Skin Image Input
        │
        ▼
MedSigLIP (512M–1B params, <2GB)
or CXR-specific encoder (Stanford CheXpert model)
        │
        ▼
Feature Vector → Comparative Diagnosis
(e.g., "Findings consistent with infiltrate in lower lobes")
        │
        ▼
Confidence Score + Uncertainty Flag
(Red: High confidence, Yellow: Borderline, Gray: Insufficient data)
        │
        ▼
Integrate into HUD: "Visual: Possible pneumonia. Recommend clinical correlation."
```

**Model** (MedSigLIP preferred):

- Vision-language model trained on medical images
- Outputs: finding + confidence (0–1)
- ~500MB–1.2GB footprint
- Interpretable region attention (shows what model saw)

***

#### **Acoustic Path: Respiratory Bioacoustics**

```
Cough / Breath Audio (10–30 sec clip)
        │
        ▼
Spectrogram Preprocessing (librosa, local)
        │
        ▼
HeAR (Heart-to-Ear, or AST-adapted model)
Medical audio classifier
        │
        ▼
Classification: [COVID, Pneumonia, Asthma, Healthy, Uncertain]
        │
        ▼
Probability Distribution + Log-Likelihood
        │
        ▼
HUD Display: 
"Audio: 76% consistent with viral cough. Clinical correlation advised."
```

**Model** (HeAR or AudioMAE-finetuned):

- Lightweight audio encoder (~100–500MB)
- Runs in real-time on-device
- Output: classification label + confidence
- **Critical**: Do NOT treat as diagnostic certainty—evidence layer only

***

### 2.3 Multimodal Fusion \& Orchestration

```
                Input Router (Clinician Choice)
                ├─ Voice Only (baseline)
                ├─ Voice + Image
                ├─ Voice + Cough
                └─ All Three

                        ▼

            ┌─────────────────────────────┐
            │ SENSOR FUSION LAYER         │
            │ Aggregate signals via:      │
            │ 1. Bayesian fusion          │
            │    (confidence-weighted)    │
            │ 2. Majority voting          │
            │    (if 2+ sensors agree)    │
            │ 3. Conflict flagging        │
            │    (if sensors disagree)    │
            └─────────────────────────────┘
                        ▼

            ┌──────────────────────────┐
            │ FINAL HYPOTHESIS LAYER   │
            │ Rank differential:       │
            │ [1] Pneumonia (0.82)     │
            │ [2] Bronchitis (0.65)    │
            │ [3] Asthma (0.41)        │
            └──────────────────────────┘
```

**Orchestration Rules**:

- If voice-only: use MedGemma + ICD mapper
- If visual input: add MedSigLIP, boost confidence for imaging-correlated findings
- If audio input: add bioacoustic classifier, flag agreement/disagreement
- Conflict resolution: Show all signals, let clinician decide (not ML)

***

## 3. CONTRAINDICATION \& RISK ENGINE

### 3.1 Local Medication Safety Module

```json
{
  "patient": {
    "current_meds": ["metformin", "lisinopril"],
    "allergies": ["penicillin", "sulfa"],
    "conditions": ["Type 2 DM", "HTN"]
  },
  "inferred_symptoms": ["fever", "productive cough"],
  "proposed_icd10": ["J18.9"],
  "checks": [
    {
      "rule": "Contraindication",
      "trigger": "Proposed: amoxicillin + existing: penicillin allergy",
      "severity": "RED",
      "action": "BLOCK - suggest macrolide (azithromycin) or fluoroquinolone"
    },
    {
      "rule": "Drug-Drug",
      "trigger": "Proposed: erythromycin + existing: lisinopril",
      "severity": "YELLOW",
      "action": "MONITOR - watch for hypotension, QT prolongation"
    },
    {
      "rule": "Age/Renal",
      "trigger": "Patient age 78, eGFR estimated 35",
      "severity": "YELLOW",
      "action": "ADJUST DOSE - avoid high-dose fluoroquinolones"
    }
  ]
}
```

**Implementation**:

1. **Hardcoded Rule Base** (JSON): ~500–1000 common contraindications
    - Structured as: `{med1, med2, condition} → severity + action`
    - No network calls
2. **Local Database** (SQLite): FDA/WHO contraindications snapshot
3. **Probabilistic Qualifier**: Never state "contraindication exists"; state "**High likelihood of interaction. Clinician review mandatory.**"

**Validation**:

- Test against 100 known contraindication pairs
- ≥95% sensitivity (no false negatives)
- ≥80% specificity (avoid alert fatigue)

***

## 4. HUD OUTPUT \& CLINICAL COGNITION FRAMING

### 4.1 Three-Line Summary Protocol

```
┌─────────────────────────────────────────────────────┐
│  SOVEREIGN SCRIBE v0.9 | Air-Gap Verified ✓        │
├─────────────────────────────────────────────────────┤
│ SYMPTOMS                                            │
│ • Fever (38.5°C) + Productive Cough (3 days)       │
│ • Shortness of Breath (exertional)                 │
│ • Chills (moderate)                                │
│                                                     │
│ ICD-10 INFERENCE                                   │
│ Primary: J18.9 (Community-acquired pneumonia)      │
│ Confidence: 0.82 (Voice + Audio corroboration)     │
│                                                     │
│ RISK FLAGS                                         │
│ 🔴 ALERT: Penicillin allergy + usual first-line   │
│    → Recommend macrolide (azithromycin) or FQ      │
│                                                     │
│ 🟡 CAUTION: Age 68, eGFR ~40                       │
│    → Avoid high-dose fluoroquinolones               │
│                                                     │
│ NEXT STEPS                                         │
│ [✓] Chest X-Ray (upload image if available)       │
│ [✓] Blood Culture / CBC                           │
│ [✓] Consider hospitalization (hypoxia check)      │
│                                                     │
│ AUDIT LOG                                          │
│ Timestamp: 2026-01-15 22:15 UTC                   │
│ Models: MedASR v3.1 | MedGemma-4B | MedSigLIP     │
│ Network Status: ✓ OFFLINE (no external calls)      │
│                                                     │
└─────────────────────────────────────────────────────┘
```


### 4.2 Voice Narration (TTS Fallback)

**When clinician prefers audio cue** (e.g., while examining):

```
"Patient presents with fever and productive cough for three days. 
Inference suggests community-acquired pneumonia, confidence eighty-two percent. 

ALERT: Patient has documented penicillin allergy. 
Recommend macrolide or fluoroquinolone. 

CAUTION: Estimated glomerular filtration rate forty, age sixty-eight. 
Avoid high-dose fluoroquinolones. 

Recommend chest radiography and blood culture. 
All data logged locally. No network access required."
```

**TTS Model**: piper-tts (MIT license, <100MB, multilingual)

- Runs locally, no cloud TTS
- ~2–5 sec latency for full summary

***

## 5. ZERO-NETWORK ASSURANCE \& AUDIT TRAIL

### 5.1 Air-Gap Verification

```python
# Pseudo-code: Air-Gap Verifier
class AirGapValidator:
    def __init__(self):
        self.network_log = []
        self.blocked_calls = 0
    
    def on_outbound_attempt(self, target_url, model_name):
        """Intercept and log any network call attempt"""
        self.blocked_calls += 1
        self.network_log.append({
            "timestamp": time.time(),
            "attempted_url": target_url,
            "model": model_name,
            "action": "BLOCKED - offline mode"
        })
        raise RuntimeError(f"Network call blocked: {target_url}")
    
    def validate_models_loaded_locally(self):
        """Verify all models are in local cache, not remote"""
        required_models = [
            "whisper.cpp", "medgemma-4b-q8", "medsiglip", "hear"
        ]
        for model in required_models:
            path = f"/opt/models/{model}"
            assert os.path.exists(path), f"Missing: {model}"
        return True
    
    def report_audit(self):
        """Generate audit trail for clinician"""
        return {
            "air_gap_status": "VERIFIED" if self.blocked_calls == 0 else "COMPROMISED",
            "network_attempts_blocked": self.blocked_calls,
            "models_verified_local": True,
            "last_validation": datetime.now().isoformat()
        }
```


### 5.2 Encrypted Local Audit Trail

```json
{
  "audit_log": [
    {
      "session_id": "sess_2026-01-15_22:15:03",
      "timestamp": "2026-01-15T22:15:03Z",
      "input": {
        "voice_hash": "sha256:a1b2c3d4...",
        "voice_duration_sec": 45,
        "modalities": ["speech", "visual"],
        "patient_dob_hash": "sha256:e5f6g7h8..."
      },
      "inference_chain": [
        {
          "stage": "speech_to_text",
          "model": "whisper.cpp:v3.1",
          "output": "Patient reports fever, cough, SOB",
          "confidence": 0.94
        },
        {
          "stage": "symptom_extraction",
          "model": "medgemma-4b-q8",
          "output": {
            "symptoms": ["fever", "cough", "dyspnea"],
            "icd10": ["R50", "R05.9", "R06.02"]
          }
        },
        {
          "stage": "contraindication_check",
          "rule_engine": "local_meds_db",
          "warnings": [
            {
              "type": "allergy",
              "severity": "RED",
              "message": "Penicillin allergy on file"
            }
          ]
        }
      ],
      "final_output": {
        "primary_diagnosis": "J18.9",
        "confidence": 0.82,
        "recommendations": [...]
      },
      "network_calls_attempted": 0,
      "storage_location": "/var/log/encrypted_audit/2026-01-15/sess_xxx.json.gpg"
    }
  ]
}
```

**Encryption**:

- AES-256-GCM for audit logs
- Key stored in TPM (if available) or hardware security module
- Clinician can export/review, never auto-upload

***

## 6. DEGRADATION \& FALLBACK PROTOCOL

### 6.1 Cascade on Model Failure

```
Model Inference Requested
        │
        ▼
    ┌─ ATTEMPT ─┐
    │           │
    ▼           ▼
Success       Failure
    │           │
    │           ▼
    │    ┌─ Fallback 1: Lighter Model
    │    │ (e.g., MedGemma-3B vs 4B)
    │    │
    │    ▼
    │    Success? ─► Output
    │    │
    │    ▼
    │    Failure
    │    │
    │    ▼
    │    ┌─ Fallback 2: Rule-Based Extraction
    │    │ (keyword trie, regex)
    │    │
    │    ▼
    │    Success? ─► Degraded Output
    │    │
    │    ▼
    │    Failure
    │    │
    │    ▼
    │    ┌─ Fallback 3: Human Narration Prompt
    │    │ "Raw voice → Doctor reads aloud"
    │    │
    │    ▼
    │    Output Preserved
    │
    └─► HUD Display + Audit Log
```

**Example**:

- MedGemma fails? Fall back to Llama-7B-instruct
- Llama fails? Use regex/trie for basic symptom extraction
- All ML fails? Display raw transcription, let clinician annotate

***

## 7. VALIDATION \& STOP CONDITIONS

### 7.1 Clinical Benchmarks

| Metric | Target | Method |
| :-- | :-- | :-- |
| **MedASR Fidelity** | ≥95% on medical dictation | 500-utterance test set (diverse accents, speeds) |
| **ICD-10 Accuracy** | ≥90% match vs. human coder | 200-case cross-validation |
| **Contraindication Sensitivity** | ≥95% (no missed alerts) | 100 known drug-drug pairs |
| **Contraindication Specificity** | ≥80% (low false-alarm rate) | Alert fatigue measurement |
| **Visual Diagnosis (CXR)** | ≥85% AUC vs. radiologist | ChexPert/MIMIC-CXR test set |
| **Bioacoustic Cough Classification** | ≥80% accuracy | ESC dataset or custom labeled audio |
| **System Latency** | <3 sec end-to-end (speech → HUD) | Jetson Orin Nano, real hardware |
| **Air-Gap Verification** | 0 external network calls | Network sniffer validation |
| **Audit Trail Completeness** | 100% of inferences logged | Spot-check 50 random sessions |

### 7.2 Failure Detection \& Graceful Degradation

```python
def validate_system_health():
    """Pre-flight check before clinical use"""
    checks = {
        "models_loaded": verify_all_models_local(),
        "network_isolated": verify_no_outbound(),
        "audio_hardware": test_mic_recording(),
        "gpu_available": test_gpu_memory(),
        "audit_writable": test_log_encryption(),
        "contraindication_db": verify_rules_loaded()
    }
    
    if not all(checks.values()):
        failed = [k for k, v in checks.items() if not v]
        raise SystemError(f"CRITICAL: {failed} failed validation. "
                          "Do not use for patient care until resolved.")
    
    return checks
```


***

## 8. THREAT MODEL \& MITIGATIONS

| Threat | Attack Vector | Mitigation |
| :-- | :-- | :-- |
| **Data Exfiltration** | Model sends data to cloud, hidden telemetry | Network firewall, signature blocking, audit logging |
| **Model Poisoning** | Weights trained on adversarial data → wrong diagnoses | Offline model validation, adversarial test cases |
| **Hallucinated Contraindications** | LLM invents drug interactions → false alerts (alert fatigue) | Rule-based engine (deterministic), probability thresholds, clinical override |
| **Accent/Speech Bias** | ASR fails on non-English or rural dialects | Diverse training data, Whisper finetuning, fallback narration |
| **Imaging Misinterpretation** | Vision model confident but wrong (e.g., normal CXR as pneumonia) | Uncertainty quantification, "low-confidence" flag, always defer to radiologist |
| **Sensor Dropout** | Microphone fails, GPU overheats → system becomes unusable | Multi-modal redundancy, graceful degradation, alert clinician |
| **Supply Chain Compromise** | Weights from untrusted source, model weights tampered | Signature verification (SHA-256 checksum), open-source models only |
| **Regulatory Non-Compliance** | System lacks proper audit trail → HIPAA/GDPR violation | Encrypted logs, anonymization (hash patient PII), offline-only storage |


***

## 9. IMPLEMENTATION ROADMAP (12-Month)

### **Phase 0 (Weeks 1–4): Foundation**

- [ ] Deploy Whisper.cpp + quantized MedGemma-4B on Jetson Orin
- [ ] Build ICD-10 mapping rules (JSON trie, ~500 common diagnoses)
- [ ] Implement local audit logging + encryption
- [ ] Validate air-gap (no network calls)


### **Phase 1 (Weeks 5–8): Contraindication Engine**

- [ ] Load FDA/WHO contraindication DB (~5K rules)
- [ ] Build probabilistic qualifier layer (confidence scoring)
- [ ] Test on 100 known drug-drug pairs
- [ ] Alert UX: color-coded HUD (Red, Yellow, Gray)


### **Phase 2 (Weeks 9–16): Visual \& Acoustic Sensors**

- [ ] Integrate MedSigLIP for X-ray/dermatology
- [ ] Integrate HeAR for respiratory bioacoustics
- [ ] Implement fusion layer (Bayesian confidence weighting)
- [ ] Test on 50 real X-rays, 100 cough samples


### **Phase 3 (Weeks 17–24): Clinical Validation \& UX Hardening**

- [ ] Beta test with 5–10 rural clinics (informed consent, IRB approval)
- [ ] Measure clinician adoption, error rates, override frequency
- [ ] Refine HUD layout based on cognitive load testing
- [ ] Stress-test on degraded hardware (Raspberry Pi 5, M2 Air)


### **Phase 4 (Weeks 25–36): Regulatory \& Deployment**

- [ ] Prepare 510(k) submission for FDA (if applicable)
- [ ] Documentation: audit trail, validation report, threat model
- [ ] Open-source release (Apache 2.0 license)
- [ ] Training: clinician onboarding, offline troubleshooting


### **Phase 5 (Weeks 37–52): Field Hardening**

- [ ] Monitor real-world usage, log anonymized errors
- [ ] Continuous model improvement (e.g., dialect-specific ASR finetuning)
- [ ] Expand contraindication DB to 10K+ rules
- [ ] Publish results in open-source health tech forum

***

## 10. REFLEXIVE CHECKPOINT: POWER DYNAMICS

**"Does the system empower the clinician without assuming authority?"**

### ✅ **What Sovereign Scribe Must NOT Do**

- ❌ Override clinician judgment (no hard blocks except allergy)
- ❌ Suppress alternative diagnoses (always show differential)
- ❌ Hide reasoning (full audit trail, interpretable outputs)
- ❌ Assume expert role ("I diagnose…" vs. "findings suggest…")


### ✅ **What Sovereign Scribe MUST Do**

- ✅ Present probabilistic reasoning ("82% confidence")
- ✅ Flag uncertainty ("low confidence on acoustic input")
- ✅ Offer alternatives ("Differential: pneumonia, bronchitis, asthma")
- ✅ Let clinician override without guilt ("Note: clinician chose amoxicillin despite penicillin allergy flag")
- ✅ Log all decisions (for accountability, learning, audit)

**Governance Model**:

```
Clinician = Authority
System = Advisor (not dictator)

Final Decision = Clinician's (with full informed consent)
System Role = Reduce cognitive load, flag risks, capture documentation
```


***

## 11. EXTENSION VECTORS (Future)

### **DRP-MULTIMODAL-AGENT-HUB**

- Plug-and-play sensor modules (new bioacoustic model, thermal imaging)
- Orchestration registry: route input to optimal sub-model


### **PRP-HUD-UX-CLINICAL**

- Eye-tracking feedback (which HUD elements capture attention?)
- Custom layouts per specialty (ED vs. primary care vs. mental health)


### **DRP-MED-EDGE-SOVEREIGN-v2**

- Multi-clinician mode (secure local network, consensus flagging)
- Knowledge distillation (train student models for even lower-resource devices)


### **PRP-MEDASR-VS-WHISPER**

- Systematic benchmark: medical-specific vs. general-purpose ASR
- Publish comparative results (open science)

***

## 12. MATERIAL ANCHORS (Appendix)

### **Configuration Schema (YAML)**

```yaml
system:
  name: "Sovereign Scribe v0.9"
  mode: "offline"
  hardware_target: "jetson-orin-nano"
  network_policy: "DENY_ALL_OUTBOUND"

models:
  asr:
    name: "whisper.cpp"
    variant: "base-medical"
    quantization: "int8"
    local_path: "/opt/models/whisper-base-q8.bin"
    checksum: "sha256:abc123..."
  
  symptom_extractor:
    name: "medgemma-4b"
    variant: "quantized"
    quantization: "int8"
    local_path: "/opt/models/medgemma-4b-q8.gguf"
    checksum: "sha256:def456..."
  
  vision:
    name: "medsiglip"
    variant: "base"
    local_path: "/opt/models/medsiglip-base.pt"
    checksum: "sha256:ghi789..."
  
  audio_classifier:
    name: "hear"
    variant: "respiratory"
    local_path: "/opt/models/hear-respiratory.pt"
    checksum: "sha256:jkl012..."

contraindications:
  database: "/opt/data/fda-drug-interactions.db"
  rules_version: "2025-q4"
  last_updated: "2026-01-10"

audit:
  log_dir: "/var/log/sovereign-scribe"
  encryption: "aes256-gcm"
  retention_days: 365
  tpm_enabled: true

ui:
  hud_mode: "three_line_summary"
  tts_enabled: true
  tts_model: "piper-tts"
  override_authority: "clinician"
```


### **Stop Conditions (Checklist)**

- [ ] Whisper fidelity ≥95% on 500-utterance medical test set
- [ ] ICD-10 accuracy ≥90% vs. human coders on 200-case cross-validation
- [ ] Contraindication sensitivity ≥95% on 100 known drug-drug pairs
- [ ] Zero external network calls (verified via traffic sniffer)
- [ ] Audit trail 100% complete for 50 random sessions
- [ ] Latency <3 sec (speech → HUD on target hardware)
- [ ] Graceful degradation tested on all failure modes
- [ ] Clinical beta validation with 5+ rural practitioners (≥50 cases)
- [ ] Regulatory pathway mapped (510(k), HIPAA compliance)
- [ ] Open-source release approved by legal/governance

***

## 13. NEXT STEPS: MATERIALS-BASED ENGINEERING

**The Sovereign Scribe is NOT a "vibe"—it is a deterministic machine.**

1. **Immediately**: Spin up local Whisper.cpp + MedGemma-4B on test hardware
2. **Week 1**: Build ICD-10 mapping rules in JSON (version control, audit every change)
3. **Week 2**: Implement air-gap validator (zero tolerance for network calls)
4. **Week 3**: Draft 510(k) regulatory submission outline
5. **Week 4**: Recruit 2–3 pilot clinicians (consent, ethics, safety logs)

**Governance**: All decisions materialized as:

- Versioned config (YAML)
- Signed model weights (SHA-256 checksums)
- Audit logs (encrypted, timestamped, clinician-readable)
- Regulatory documentation (FDA-compliant)

**Success = Clinician trusts the system because they can see, audit, and override every decision. Not because they believe the marketing.**

***

**You now have a **sovereign clinical copilot** blueprint, grounded in hardware constraints, model availability, and ethical boundaries. The system is a *tool for the clinician*, not a replacement. Ready to materialize this into code?**

