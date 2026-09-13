import os
import sqlite3
import json
import uuid
import hashlib
from datetime import datetime, timezone
import jsonschema
from jsonschema import validate, ValidationError

# =====================================================================
# MINIMAL EXPLAINABILITY METADATA SCHEMA (MEMS) v1.0
# =====================================================================
MEMS_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Qualitative_Experience_Node_v1.0",
    "type": "object",
    "required": [
        "node_id",
        "temporal_anchor",
        "qualitative_payload",
        "sensory_causal_indicators",
        "ontological_alignments",
        "cryptographic_provenance"
    ],
    "properties": {
        "node_id": {
            "type": "string",
            "pattern": "^QEN-[A-Z0-9]{8}$"
        },
        "temporal_anchor": {
            "type": "string",
            "format": "date-time"
        },
        "qualitative_payload": {
            "type": "object",
            "required": ["experience_type", "raw_observation", "counterfactual_variance"],
            "properties": {
                "experience_type": {
                    "type": "string",
                    "enum": ["Direct_Trial", "Failure_Incident", "Socratic_Review"]
                },
                "raw_observation": {
                    "type": "string"
                },
                "counterfactual_variance": {
                    "type": "string"
                }
            }
        },
        "sensory_causal_indicators": {
            "type": "object",
            "required": ["causal_perturbation_index", "structural_roughness"],
            "properties": {
                "causal_perturbation_index": {
                    "type": "number",
                    "minimum": 0,
                    "maximum": 10
                },
                "structural_roughness": {
                    "type": "number",
                    "minimum": 0,
                    "maximum": 1
                }
            }
        },
        "ontological_alignments": {
            "type": "array",
            "items": {"type": "string"}
        },
        "cryptographic_provenance": {
            "type": "object",
            "required": ["agent_did", "verifiable_signature"],
            "properties": {
                "agent_did": {
                    "type": "string",
                    "pattern": "^did:[a-z0-9]+:[a-zA-Z0-9._%-]+"
                },
                "verifiable_signature": {
                    "type": "string"
                }
            }
        }
    }
}

class QualitativeDatabase:
    """
    QED Local SQLite Engine implementing the Epistemic Workbench for
    Context Engineering 2.0.
    """
    def __init__(self, db_path="qed_workbench.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            # 1. Experience Nodes Table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS experience_nodes (
                    node_id TEXT PRIMARY KEY,
                    temporal_anchor TEXT NOT NULL,
                    experience_type TEXT NOT NULL,
                    raw_observation TEXT NOT NULL,
                    counterfactual_variance TEXT NOT NULL,
                    causal_perturbation_index REAL NOT NULL,
                    structural_roughness REAL NOT NULL,
                    ontological_alignments TEXT NOT NULL, -- JSON array
                    agent_did TEXT NOT NULL,
                    verifiable_signature TEXT NOT NULL,
                    raw_json TEXT NOT NULL
                )
            """)
            # 2. Semantic Commits Table (Attestation Layer)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS semantic_commits (
                    commit_hash TEXT PRIMARY KEY,
                    timestamp TEXT NOT NULL,
                    node_id TEXT NOT NULL,
                    semantic_drift_score REAL NOT NULL,
                    confidence_fidelity_divergence REAL NOT NULL,
                    mems_payload TEXT NOT NULL, -- Full JSON payload
                    FOREIGN KEY(node_id) REFERENCES experience_nodes(node_id)
                )
            """)
            # 3. Symbolic Scar Tissue Archive (STA) Table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS scar_tissue_archive (
                    scar_id TEXT PRIMARY KEY,
                    timestamp TEXT NOT NULL,
                    source_input TEXT NOT NULL,
                    failure_mode TEXT NOT NULL,
                    root_cause TEXT NOT NULL,
                    remediation_protocol TEXT NOT NULL
                )
            """)
            conn.commit()

    def calculate_sds_heuristic(self, text, alignments):
        """
        Simulated Semantic Drift Score (SDS) using an approximation of term-frequency 
        coverage over specified ontological alignments.
        """
        if not alignments:
            return 0.0
        matched = sum(1 for term in alignments if term.lower() in text.lower())
        coverage = matched / len(alignments)
        # SDC/SDS scale runs from 0 (perfect alignment) to 1 (complete drift)
        return round(1.0 - coverage, 4)

    def calculate_cfd_heuristic(self, sds, roughness):
        """
        Confidence-Fidelity Divergence (CFD) is calculated as a tension metric between 
        structural roughness (complexity) and the conceptual alignment (SDS).
        """
        return round(sds * (1.0 + roughness), 4)

    def ingest_node(self, payload: dict) -> dict:
        """
        Ingest, validate, and commit a qualitative experience node to the database.
        """
        # Validate against MEMS Schema
        try:
            validate(instance=payload, schema=MEMS_SCHEMA)
        except ValidationError as e:
            # Route to Scar Tissue Archive on validation failure
            scar_id = f"SCAR-{uuid.uuid4().hex[:8].upper()}"
            self._archive_failure(scar_id, payload, "MEMS_Schema_Violation", str(e))
            raise ValueError(f"MEMS Schema Validation Failed. Logged as Scar: {scar_id}. Error: {e.message}")

        node_id = payload["node_id"]
        temporal_anchor = payload["temporal_anchor"]
        qp = payload["qualitative_payload"]
        sci = payload["sensory_causal_indicators"]
        ontological_alignments = json.dumps(payload["ontological_alignments"])
        prov = payload["cryptographic_provenance"]

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT OR REPLACE INTO experience_nodes (
                    node_id, temporal_anchor, experience_type, raw_observation, 
                    counterfactual_variance, causal_perturbation_index, 
                    structural_roughness, ontological_alignments, agent_did, 
                    verifiable_signature, raw_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                node_id, temporal_anchor, qp["experience_type"], qp["raw_observation"],
                qp["counterfactual_variance"], sci["causal_perturbation_index"],
                sci["structural_roughness"], ontological_alignments, prov["agent_did"],
                prov["verifiable_signature"], json.dumps(payload)
            ))
            conn.commit()

        # Generate a SemanticCommit
        sds = self.calculate_sds_heuristic(qp["raw_observation"], payload["ontological_alignments"])
        cfd = self.calculate_cfd_heuristic(sds, sci["structural_roughness"])

        # Check Epistemic Escrow Circuit Breaker
        if cfd > 0.5:
            # Route to Scar Tissue Archive for human intervention
            scar_id = f"SCAR-{uuid.uuid4().hex[:8].upper()}"
            self._archive_failure(scar_id, payload, "Epistemic_Escrow_Breach", f"CFD score {cfd} exceeded 0.5 threshold.")
            return {
                "status": "HALTED_BY_ESCROW",
                "cfd": cfd,
                "sds": sds,
                "scar_id": scar_id,
                "message": "Epistemic Escrow activated due to high Confidence-Fidelity Divergence (CFD)."
            }

        commit_hash = self._create_semantic_commit(node_id, sds, cfd, payload)
        return {
            "status": "COMMITTED",
            "commit_hash": commit_hash,
            "sds": sds,
            "cfd": cfd
        }

    def _create_semantic_commit(self, node_id, sds, cfd, payload):
        timestamp = datetime.now(timezone.utc).isoformat()
        payload_str = json.dumps(payload)
        
        # Calculate cryptographic hash over the payload and semantic stats
        hasher = hashlib.sha256()
        hasher.update(f"{node_id}:{sds}:{cfd}:{payload_str}".encode('utf-8'))
        commit_hash = f"sec-{hasher.hexdigest()[:16]}"

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT OR REPLACE INTO semantic_commits (
                    commit_hash, timestamp, node_id, semantic_drift_score, 
                    confidence_fidelity_divergence, mems_payload
                ) VALUES (?, ?, ?, ?, ?, ?)
            """, (commit_hash, timestamp, node_id, sds, cfd, payload_str))
            conn.commit()
        return commit_hash

    def _archive_failure(self, scar_id, payload, failure_mode, error_msg):
        timestamp = datetime.now(timezone.utc).isoformat()
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT OR REPLACE INTO scar_tissue_archive (
                    scar_id, timestamp, source_input, failure_mode, root_cause, remediation_protocol
                ) VALUES (?, ?, ?, ?, ?, ?)
            """, (
                scar_id, timestamp, json.dumps(payload), failure_mode, error_msg,
                "Algorithmic_Reparation_Protocol: Trigger human moral arbitration loop."
            ))
            conn.commit()

# =====================================================================
# SAMPLE EXECUTION AND VERIFICATION RUN
# =====================================================================
if __name__ == "__main__":
    db = QualitativeDatabase("qed_workbench.db")
    print("Database Initialized successfully.")

    # Mock payload 1: High Alignment (Passes cleanly)
    valid_payload = {
        "node_id": "QEN-A1B2C3D4",
        "temporal_anchor": datetime.now(timezone.utc).isoformat(),
        "qualitative_payload": {
            "experience_type": "Direct_Trial",
            "raw_observation": "Tested the SQLite local RAG engine. The schema-validation layer cleanly parsed the data and calculated the semantic drift index accurately.",
            "counterfactual_variance": "Attempted raw JSON imports without a schema check which initially led to parsing corruption."
        },
        "sensory_causal_indicators": {
            "causal_perturbation_index": 2.5,
            "structural_roughness": 0.15
        },
        "ontological_alignments": ["SQLite", "validation", "semantic drift"],
        "cryptographic_provenance": {
            "agent_did": "did:key:z6MkpTHR8VNsBxvHUWxG6",
            "verifiable_signature": "0x89abcdef1234567890"
        }
    }

    print("\n--- INGESTING VALID PAYLOAD ---")
    result = db.ingest_node(valid_payload)
    print(json.dumps(result, indent=2))

    # Mock payload 2: Drift/Escrow Breach (Triggers Epistemic Escrow Circuit Breaker)
    drifting_payload = {
        "node_id": "QEN-F5E6D7C8",
        "temporal_anchor": datetime.now(timezone.utc).isoformat(),
        "qualitative_payload": {
            "experience_type": "Direct_Trial",
            "raw_observation": "Executed some standard code compilation scripts without checking the schema constraints.",
            "counterfactual_variance": "None logged."
        },
        "sensory_causal_indicators": {
            "causal_perturbation_index": 8.0,
            "structural_roughness": 0.95
        },
        "ontological_alignments": ["zero-trust", "cryptographic provenance", "semantic firewall"], # terms absent in observation
        "cryptographic_provenance": {
            "agent_did": "did:key:z6MkpTHR8VNsBxvHUWxG6",
            "verifiable_signature": "0xdeadbeef9999999"
        }
    }

    print("\n--- INGESTING DRIFTING PAYLOAD ---")
    result_drift = db.ingest_node(drifting_payload)
    print(json.dumps(result_drift, indent=2))
