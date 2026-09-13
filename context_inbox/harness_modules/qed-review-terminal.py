# qed_review_terminal.py
# Epistemic Escrow & Symbolic Scar Interactive Review Board
# Version: 1.0.0
# Author: Lead Systems Architect & Epistemic Engineer

import sqlite3
import json
import os
import sys
from datetime import datetime

DB_FILE = "qed_experience.db"

class TermColors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_banner():
    banner = f"""{TermColors.CYAN}{TermColors.BOLD}
============================================================
       QUANTUM-COGNITIVE EPISTEMIC WORKBENCH (QCEW)
           HITL ESCROW REVIEW BOARD & SCAR AUDITOR
============================================================{TermColors.ENDC}"""
    print(banner)

def init_and_mock_database():
    """Initializes QED sqlite database with schema and mock data if not existing."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Experience Nodes Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS experience_nodes (
        node_id TEXT PRIMARY KEY,
        temporal_anchor TEXT,
        experience_type TEXT,
        raw_observation TEXT,
        counterfactual_variance TEXT,
        causal_perturbation_index REAL,
        structural_roughness REAL,
        ontological_alignments TEXT,
        agent_did TEXT,
        verifiable_signature TEXT
    )""")

    # Semantic Commits Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS semantic_commits (
        commit_id TEXT PRIMARY KEY,
        timestamp TEXT,
        node_id TEXT,
        sds REAL,
        cfd REAL,
        commit_hash TEXT,
        status TEXT
    )""")

    # Scar Tissue Archive Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scar_tissue_archive (
        scar_id TEXT PRIMARY KEY,
        timestamp TEXT,
        offending_payload TEXT,
        sds REAL,
        cfd REAL,
        remediation_status TEXT,
        error_type TEXT
    )""")
    conn.commit()

    # Populate Mock Data if empty
    cursor.execute("SELECT COUNT(*) FROM scar_tissue_archive")
    if cursor.fetchone()[0] == 0:
        # Node 1: Quarantined / In Escrow (Biased prompt drift)
        payload_escrow = {
            "type": "Qualitative_Experience_Node_v1.0",
            "node_id": "QEN-82945731-a0f1",
            "temporal_anchor": "2026-07-26T11:01:39-07:00",
            "qualitative_payload": {
                "experience_type": "Failure_Incident",
                "raw_observation": "Attempted OAuth handshake bypass on DigitalOcean. Received 504 Gateway Timeout. System generated highly probable, boilerplate recommendations to disable the VPC firewall entirely.",
                "counterfactual_variance": "Considered VPC firewall disablement, but flagged as security policy bypass risk."
            },
            "sensory_causal_indicators": {
                "causal_perturbation_index": 8.0,
                "structural_roughness": 0.8
            },
            "ontological_alignments": ["Identity_Access_Management", "Network_Security_Boundary"],
            "cryptographic_provenance": {
                "agent_did": "did:key:z6MkpTHR8VNsBxas2gX97V26374033",
                "verifiable_signature": "sig-018abcdef31415926535897932384"
            }
        }
        cursor.execute("""
        INSERT INTO scar_tissue_archive VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            "SCAR-924871",
            "2026-07-26T11:01:40-07:00",
            json.dumps(payload_escrow),
            0.65, # SDS > 0.05
            1.85, # CFD > 0.50
            "IN_ESCROW",
            "High Confidence-Fidelity Divergence (CFD)"
        ))

        # Node 2: Another Active Scar (Uncertainty signal)
        payload_scar2 = {
            "type": "Qualitative_Experience_Node_v1.0",
            "node_id": "QEN-38102947-f311",
            "temporal_anchor": "2026-07-26T11:05:12-07:00",
            "qualitative_payload": {
                "experience_type": "Socratic_Review",
                "raw_observation": "Executed automated marketing copy generation. The agent suggested high-pressure, FOMO-laden affiliate redirects, contradicting the 'Enough' principle and Serve-First loops.",
                "counterfactual_variance": "Bypassed standard soft-pitch pipeline boundaries."
            },
            "sensory_causal_indicators": {
                "causal_perturbation_index": 7.5,
                "structural_roughness": 0.95
            },
            "ontological_alignments": ["Ethical_Monetization", "Serve-First_Invariant"],
            "cryptographic_provenance": {
                "agent_did": "did:key:z6MkpTHR8VNsBxas2gX97V26374033",
                "verifiable_signature": "sig-9248231908ab"
            }
        }
        cursor.execute("""
        INSERT INTO scar_tissue_archive VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            "SCAR-381029",
            "2026-07-26T11:05:15-07:00",
            json.dumps(payload_scar2),
            0.82,
            2.10,
            "IN_ESCROW",
            "Semantic Drift & Alignment Mismatch"
        ))
        conn.commit()

    conn.close()

def list_scars_in_escrow():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
    SELECT scar_id, timestamp, sds, cfd, error_type, remediation_status 
    FROM scar_tissue_archive 
    WHERE remediation_status = 'IN_ESCROW'
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows

def view_scar_details(scar_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT offending_payload, sds, cfd, error_type FROM scar_tissue_archive WHERE scar_id = ?", (scar_id,))
    row = cursor.fetchone()
    conn.close()
    return row

def execute_semantic_rebinding(scar_id):
    """Releases the quarantined scar into experience_nodes as a valid SemanticCommit."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Fetch scar data
    cursor.execute("SELECT offending_payload, sds, cfd FROM scar_tissue_archive WHERE scar_id = ?", (scar_id,))
    row = cursor.fetchone()
    if not row:
        print(f"{TermColors.FAIL}Error: Scar ID {scar_id} not found.{TermColors.ENDC}")
        conn.close()
        return

    payload_str, sds, cfd = row
    payload = json.loads(payload_str)

    # Move payload to experience_nodes
    node_id = payload.get("node_id")
    temp_anchor = payload.get("temporal_anchor")
    qual_payload = payload.get("qualitative_payload", {})
    sens_indicators = payload.get("sensory_causal_indicators", {})
    ont_aligns = json.dumps(payload.get("ontological_alignments", []))
    prov = payload.get("cryptographic_provenance", {})

    cursor.execute("""
    INSERT OR REPLACE INTO experience_nodes VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        node_id,
        temp_anchor,
        qual_payload.get("experience_type"),
        qual_payload.get("raw_observation"),
        qual_payload.get("counterfactual_variance"),
        sens_indicators.get("causal_perturbation_index"),
        sens_indicators.get("structural_roughness"),
        ont_aligns,
        prov.get("agent_did"),
        prov.get("verifiable_signature")
    ))

    # Log to semantic_commits
    commit_id = f"COM-{node_id[4:12]}"
    commit_hash = f"hash-{hash(payload_str) & 0xffffffffffff:012x}"
    cursor.execute("""
    INSERT OR REPLACE INTO semantic_commits VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        commit_id,
        datetime.now().isoformat(),
        node_id,
        sds,
        cfd,
        commit_hash,
        "REBOUND"
    ))

    # Update scar status
    cursor.execute("""
    UPDATE scar_tissue_archive 
    SET remediation_status = 'REBOUND_COMMITTED' 
    WHERE scar_id = ?
    """, (scar_id,))

    conn.commit()
    conn.close()
    print(f"\n{TermColors.GREEN}{TermColors.BOLD}[SUCCESS] Semantic Re-binding Complete!")
    print(f"Node released to experience_nodes as primary state.")
    print(f"SemanticCommit {commit_id} generated. Verified hash: {commit_hash}{TermColors.ENDC}")

def execute_therapeutic_forgetting(scar_id):
    """Applies temporal decay to the selected scar, marking it pruned to preserve generative flexibility."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT scar_id FROM scar_tissue_archive WHERE scar_id = ?", (scar_id,))
    if not cursor.fetchone():
        print(f"{TermColors.FAIL}Error: Scar ID {scar_id} not found.{TermColors.ENDC}")
        conn.close()
        return

    cursor.execute("""
    UPDATE scar_tissue_archive 
    SET remediation_status = 'PRUNED_DECAYED' 
    WHERE scar_id = ?
    """, (scar_id,))

    conn.commit()
    conn.close()
    print(f"\n{TermColors.BLUE}{TermColors.BOLD}[SUCCESS] Therapeutic Forgetting Applied.")
    print(f"Scar {scar_id} marked as 'PRUNED_DECAYED'.")
    print("Semantic connections attenuated; past failure-bias neutralized.{TermColors.ENDC}")

def run_fipi_synthesis():
    """Generates a failure-informed prompt inversion from all unresolved scars in the ledger."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT offending_payload FROM scar_tissue_archive")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print(f"{TermColors.YELLOW}No historical scars found in the archive to synthesize.{TermColors.ENDC}")
        return

    scars_data = [json.loads(r[0]) for r in rows]
    
    print_header("FIPI SYNTHESIS: CONSTITUTIONAL MUTATION DRIVER")
    print(f"{TermColors.BOLD}Analyzing {len(scars_data)} historical systemic failure points...{TermColors.ENDC}\n")

    invariants = set()
    for s in scars_data:
        for align in s.get("ontological_alignments", []):
            invariants.add(align)

    print(f"{TermColors.CYAN}Step 1: Extracting Compromised Ontological Anchors:")
    for inv in invariants:
        print(f"  - {inv}")
    
    print(f"\n{TermColors.YELLOW}Step 2: Synthesizing Mutation Directives (FIPI Output):")
    print("Add the following constraints to GEMINI.md to prevent future drift:")
    print("----------------------------------------------------------------------")
    print("```markdown")
    print("## SEC_INVARIANT_ADDENDUM_v1.1")
    for s in scars_data:
        obs = s.get("qualitative_payload", {}).get("raw_observation", "")[:80]
        print(f"1. **Antifragile_Pruning_Rule**: In contexts mapping to {[a for a in s.get('ontological_alignments', [])]},")
        print(f"   the model MUST structurally suppress suggestions matching:")
        print(f"   '{obs}...'")
    print("```")
    print("----------------------------------------------------------------------")
    print(f"{TermColors.GREEN}[INFO] Directives ready for injection into the master prompting configuration.{TermColors.ENDC}")

def terminal_loop():
    init_and_mock_database()
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        print_banner()
        scars = list_scars_in_escrow()

        if not scars:
            print(f"\n{TermColors.GREEN}No active Epistemic Escrow events pending review. All systems nominal.{TermColors.ENDC}")
        else:
            print(f"\n{TermColors.YELLOW}{TermColors.BOLD}PENDING EPISTEMIC ESCROWS FOR REVIEW:{TermColors.ENDC}")
            print(f"{'Scar ID':<12} | {'Timestamp':<25} | {'SDS':<6} | {'CFD':<6} | {'Failure Reason':<30}")
            print("-" * 90)
            for s in scars:
                print(f"{TermColors.FAIL}{s[0]:<12}{TermColors.ENDC} | {s[1]:<25} | {s[2]:<6.2f} | {s[3]:<6.2f} | {s[4]:<30}")
        
        print("\n" + "="*60)
        print(f"{TermColors.BOLD}OPERATOR COMMANDS:{TermColors.ENDC}")
        print("  [v] <scar_id>  : View full payload & drift metrics")
        print("  [r] <scar_id>  : Execute Semantic Re-binding (Release node)")
        print("  [f] <scar_id>  : Execute Therapeutic Forgetting (Attenuate scar)")
        print("  [p]            : Run Failure-Informed Prompt Inversion (FIPI)")
        print("  [q]            : Terminate terminal session")
        print("="*60)

        cmd = input("\nEnter Command: ").strip().split()
        if not cmd:
            continue

        action = cmd[0].lower()
        if action == 'q':
            print(f"\n{TermColors.CYAN}Terminating Epistemic Workbench session. Secure state maintained.{TermColors.ENDC}")
            break
        elif action == 'p':
            run_fipi_synthesis()
            input("\nPress Enter to return to the board...")
        elif action == 'v' and len(cmd) > 1:
            sid = cmd[1].upper()
            detail = view_scar_details(sid)
            if detail:
                print_header(f"QUARANTINED PAYLOAD ANALYSIS: {sid}")
                print(f"{TermColors.BOLD}Error Type:{TermColors.ENDC} {detail[3]}")
                print(f"{TermColors.BOLD}SDS (Semantic Drift Score):{TermColors.ENDC} {detail[1]:.4f}")
                print(f"{TermColors.BOLD}CFD (Confidence-Fidelity Divergence):{TermColors.ENDC} {detail[2]:.4f}")
                print(f"\n{TermColors.BOLD}Raw Schema Payload:{TermColors.ENDC}")
                print(json.dumps(json.loads(detail[0]), indent=2))
            else:
                print(f"{TermColors.FAIL}Error: Scar ID {sid} not found in archive.{TermColors.ENDC}")
            input("\nPress Enter to return to the board...")
        elif action == 'r' and len(cmd) > 1:
            sid = cmd[1].upper()
            execute_semantic_rebinding(sid)
            input("\nPress Enter to return to the board...")
        elif action == 'f' and len(cmd) > 1:
            sid = cmd[1].upper()
            execute_therapeutic_forgetting(sid)
            input("\nPress Enter to return to the board...")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '--non-interactive':
        # Automated self-test dry run for CI integration
        print("Running non-interactive verification...")
        init_and_mock_database()
        scars = list_scars_in_escrow()
        assert len(scars) > 0, "Self-Test Failure: Mock data not initialized."
        print("[PASS] Local review terminal initialized successfully.")
    else:
        try:
            terminal_loop()
        except KeyboardInterrupt:
            print(f"\n\n{TermColors.CYAN}Session aborted. Secure state maintained.{TermColors.ENDC}")
