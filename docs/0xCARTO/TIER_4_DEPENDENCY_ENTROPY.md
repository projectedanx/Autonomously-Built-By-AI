# TIER 4: Dependency Matrix & Entropy Audit

Thermodynamic Lens (L3) applied. Entropy Score: 0 = deterministic, 1 = fully chaotic.

## Build Reproducibility Index
| Dependency | Version Pin | Production? | CI Invoked? | Entropy Vector |
| :--- | :--- | :--- | :--- | :--- |
| `pytest` | Unpinned | ❌ Dev only | ⚠️ Implicit | 🔴 HIGH — Unpinned testing framework |
| `pytest-benchmark` | Unpinned | ❌ Dev only | ⚠️ Implicit | 🔴 HIGH — Unpinned benchmarking tool |
| `pyyaml` | Unpinned | ✅ Yes | ⚠️ Implicit | 🔴 HIGH — Unpinned production dependency |

## Entropy Score by Layer
| Layer | Score | Primary Source |
| :--- | :--- | :--- |
| Environment (Docker/ENV) | 0.90 | No Dockerfile or `.env` template found; assumed local Python env |
| Application Dependencies | 0.85 | All Python dependencies in `README.md` are unpinned (`pip install pytest pytest-benchmark pyyaml`) |
| CI Pipeline | 0.95 | No automated CI configurations detected (e.g., GitHub Actions) |
| Infrastructure (IaC) | 1.00 | No Infrastructure-as-Code found |
| Test Coverage | 0.20 | Unit tests exist in `tests/` |
| **Overall Repository Entropy** | **0.78** | **Target: < 0.15 (CRITICAL INTERVENTION REQUIRED)** |
