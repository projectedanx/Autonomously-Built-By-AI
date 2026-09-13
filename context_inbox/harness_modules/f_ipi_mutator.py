#!/usr/bin/env python3
"""
f_ipi_mutator.py
================================================================================
Failure-Informed Prompt Inversion (F-IPI) Engine
Part of the Immunological Layer (L4) of the Verifiable Cognition Stack (VCS)
================================================================================

This production-grade script automates the capture of runtime and syntactic 
failures, logs them as persistent "Symbolic Scars" within the Scar Tissue Archive 
(STA) at `.gemini/scar_tissue_archive.json`, and executes "Prompt Inversion" 
to mutate your agent's master constitution (GEMINI.md).

By appending or updating declarative Semantic Integrity Constraints (SICs), 
the F-IPI Engine applies a "repulsive force" in the latent space of the LLM,
preventing recurring architectural drift and design regressions.

Usage:
  python3 f_ipi_mutator.py --log-failure --file broken_file.py --error "TypeError: ..."
  python3 f_ipi_mutator.py --mutate-prompt
  python3 f_ipi_mutator.py --status
"""

import os
import sys
import json
import uuid
import re
import argparse
from datetime import datetime, timezone

# Default Paths conforming to VCS Specifications
DEFAULT_GEMINI_MD = "GEMINI.md"
DEFAULT_STA_DIR = ".gemini"
DEFAULT_STA_FILE = os.path.join(DEFAULT_STA_DIR, "scar_tissue_archive.json")

class FIPIMutator:
    def __init__(self, gemini_md_path=DEFAULT_GEMINI_MD, archive_path=DEFAULT_STA_FILE):
        self.gemini_md_path = gemini_md_path
        self.archive_path = archive_path
        self.archive_dir = os.path.dirname(archive_path)
        
        # Ensure directory structures exist
        if self.archive_dir and not os.path.exists(self.archive_dir):
            os.makedirs(self.archive_dir, exist_ok=True)
            
        self._init_archive()

    def _init_archive(self):
        """Initializes the Scar Tissue Archive JSON structure if not present."""
        if not os.path.exists(self.archive_path):
            with open(self.archive_path, 'w', encoding='utf-8') as f:
                json.dump({"schema_version": "1.0.0", "symbolic_scars": []}, f, indent=2)

    def load_archive(self):
        """Loads and returns the Scar Tissue Archive."""
        try:
            with open(self.archive_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f"[-] ERROR: Scar Tissue Archive is corrupted: {e}", file=sys.stderr)
            # Safe backup recovery
            return {"schema_version": "1.0.0", "symbolic_scars": []}

    def save_archive(self, data):
        """Saves the Scar Tissue Archive."""
        with open(self.archive_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

    def log_scar(self, target_file, failed_metric, error_trace, causal_path=None):
        """
        Registers a new failure trace as an un-mutated Symbolic Scar.
        
        Conforms to L4 Failure Capture Specifications.
        """
        archive = self.load_archive()
        
        scar_id = str(uuid.uuid4())
        timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
        
        new_scar = {
            "scar_id": scar_id,
            "timestamp": timestamp,
            "failed_metric": failed_metric,
            "target_file": target_file or "unknown_context",
            "error_message": error_trace.strip(),
            "causal_path": causal_path or ["Compilation/Test execution pipeline triggered"],
            "mutation_status": "pending",
            "inverted_constraint": None
        }
        
        archive["symbolic_scars"].append(new_scar)
        self.save_archive(archive)
        print(f"[+] SUCCESS: Failure trace serialized as Symbolic Scar {scar_id} in Archive.")
        return scar_id

    def generate_inverted_constraint(self, error_msg, target_file):
        """
        Synthesizes a rule-based inverted negative constraint (SIC) from tracebacks.
        This provides a repulsive programmatic guardrail (Policy-as-Code).
        """
        # Clean target filename for identifier use
        clean_file = os.path.basename(target_file).upper().replace(".", "_").replace("-", "_")
        if not clean_file:
            clean_file = "GENERIC"
            
        constraint_id = f"SIC_REGEN_{clean_file}_{str(uuid.uuid4())[:8].upper()}"
        
        # Analyze error type to construct structured assertions and prohibitions
        assertion = "ASSERT code compile matches expected specification."
        prohibition = "FORBID any modification that violates design consistency."
        remedy_notes = "Refactor logic step-by-step."
        
        if "assert" in error_msg.lower():
            assertion = f"ASSERT correct logical states for {clean_file} operations."
            prohibition = "FORBID returning mock elements without verifying underlying assertions."
            remedy_notes = f"Run unit tests to verify correctness of logic in {target_file}."
        elif "typeerror" in error_msg.lower() or "type" in error_msg.lower():
            assertion = f"ASSERT strict type safety and interface agreements in {clean_file}."
            prohibition = "FORBID structural bypasses, loose dynamic types, or untyped signatures."
            remedy_notes = f"Add comprehensive type annotations/checks to {target_file}."
        elif "import" in error_msg.lower() or "module" in error_msg.lower():
            assertion = f"ASSERT absolute dependency path integrity."
            prohibition = "FORBID hardcoded circular dependencies or relative imports outside root limits."
            remedy_notes = "Verify all imports are correctly bundled and available in dependency trees."
        elif "not found" in error_msg.lower() or "notfound" in error_msg.lower():
            assertion = "ASSERT all referenced variables, assets, or databases exist before call."
            prohibition = f"FORBID referencing uninstantiated files or elements in {clean_file}."
            remedy_notes = "Initialize elements and assert their presence before runtime execution."
        elif "keyerror" in error_msg.lower() or "indexerror" in error_msg.lower():
            assertion = "ASSERT dictionary keys and array indices are safely fetched or checked."
            prohibition = "FORBID accessing raw map items without using safe defaults (e.g., .get() or index checks)."
            remedy_notes = "Safely check dictionary or list bounds prior to dereferencing."
        elif "unused-vars" in error_msg.lower() or "lint" in error_msg.lower():
            assertion = "ASSERT clean syntax conforms exactly to stylistic and styleguide configurations."
            prohibition = "FORBID dead code, dangling imports, or unused parameters in generated files."
            remedy_notes = "Format and clean all modified segments using standard formatting scripts."
        else:
            # Fallback for general unclassified failures
            assertion = f"ASSERT defensive error bounds are implemented around {clean_file}."
            prohibition = "FORBID unchecked exceptions from crashing the thread context."
            remedy_notes = "Isolate process logic inside standard try-catch/except blocks."

        # Compile into a structured Policy-as-Code Markdown block
        sic_block = f"""### [{constraint_id}] — IMMUNOLOGICAL REALIGNMENT
*   **TRIGGER FAILING TRACE:** `{error_msg.splitlines()[0] if error_msg.splitlines() else error_msg}`
*   **ASSERT:** {assertion}
*   **FORBID:** {prohibition}
*   **REMEDIAL ACTION:** {remedy_notes}"""
        
        return constraint_id, sic_block

    def mutate_gemini_md(self):
        """
        Executes the mutation pass. Reads the most recent un-mutated Symbolic Scar,
        generates an inverted SIC block, and writes it directly to GEMINI.md.
        """
        archive = self.load_archive()
        pending_scars = [s for s in archive["symbolic_scars"] if s["mutation_status"] == "pending"]
        
        if not pending_scars:
            print("[~] INFO: Zero pending Symbolic Scars. GEMINI.md is structurally sanitized.")
            return False
            
        # Prioritize the most recent failure
        target_scar = pending_scars[-1]
        error_msg = target_scar["error_message"]
        target_file = target_scar["target_file"]
        
        constraint_id, sic_block = self.generate_inverted_constraint(error_msg, target_file)
        
        # Verify if GEMINI.md exists
        if not os.path.exists(self.gemini_md_path):
            print(f"[!] WARNING: {self.gemini_md_path} not found. Bootstrapping new constitution...")
            self._bootstrap_gemini_md()
            
        # Read active GEMINI.md
        with open(self.gemini_md_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Target the IMMUNOLOGICAL or AUDIT section. If not found, look for end of file or SIC blocks
        target_section_match = re.search(r"(#+\s*PART 3:\s*AUDIT\s*&\s*ANTIFRAGILITY.*)", content, re.IGNORECASE)
        reparation_match = re.search(r"(###+\s*REPARATION\s*PROTOCOL.*)", content, re.IGNORECASE)
        
        insertion_header = "\n\n## 4. AUTO-GENERATED INVERTED CONSTRAINTS (F-IPI Layer)\n\n"
        
        if target_section_match:
            # We insert right after Part 3's heading
            pos = target_section_match.end()
            mutated_content = content[:pos] + "\n\n" + sic_block + content[pos:]
        elif reparation_match:
            # Insert under reparation section
            pos = reparation_match.end()
            mutated_content = content[:pos] + "\n\n" + sic_block + content[pos:]
        else:
            # Append as custom F-IPI layer at the end of the file
            if "AUTO-GENERATED INVERTED CONSTRAINTS" in content:
                mutated_content = content + "\n\n" + sic_block
            else:
                mutated_content = content + insertion_header + sic_block
                
        # Commit mutated constitution to file
        with open(self.gemini_md_path, 'w', encoding='utf-8') as f:
            f.write(mutated_content)
            
        # Update Scar metadata in archive
        target_scar["mutation_status"] = "mutated"
        target_scar["inverted_constraint"] = {
            "constraint_id": constraint_id,
            "applied_timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
        }
        
        self.save_archive(archive)
        print(f"[+] MUTATED SUCCESS: Injected {constraint_id} into {self.gemini_md_path}.")
        return True

    def _bootstrap_gemini_md(self):
        """Bootstraps a minimal functional GEMINI.md context file."""
        default_constitution = """# GEMINI.md: EPISTEMIC CONFIGURATION

## PART 1: CORE INVARIANTS
*   **SIC_VERIFY:** ASSERT code compiles and is verified immediately following any changes.
*   **SIC_PROV:** ASSERT all activity tracks to historical ledger systems.

## PART 3: AUDIT & ANTIFRAGILITY PROTOCOLS (L1/L4)
### REPARATION PROTOCOL
1. Log all execution anomalies as Symbolic Scars in the Scar Tissue Archive.
2. Auto-run f_ipi_mutator.py to assert negative feedback parameters.
"""
        with open(self.gemini_md_path, 'w', encoding='utf-8') as f:
            f.write(default_constitution)

    def print_status(self):
        """Outputs current health metrics and log telemetry for the Immunological Layer."""
        archive = self.load_archive()
        scars = archive.get("symbolic_scars", [])
        total_scars = len(scars)
        pending = len([s for s in scars if s["mutation_status"] == "pending"])
        mutated = len([s for s in scars if s["mutation_status"] == "mutated"])
        
        print("================================================================================")
        print("   VCS IMMUNOLOGICAL LAYER TELEMETRY (L4)")
        print("================================================================================")
        print(f"[*] Archive Location:   {os.path.abspath(self.archive_path)}")
        print(f"[*] GEMINI.md Path:     {os.path.abspath(self.gemini_md_path)}")
        print(f"[*] Total Scars Logged: {total_scars}")
        print(f"[*] Pending Mutations:  {pending}  (Need Inversion)")
        print(f"[*] Applied Mutations:  {mutated}  (Sanitized)")
        print("--------------------------------------------------------------------------------")
        
        if total_scars > 0:
            print("Chronological Scar Ledger:")
            for s in scars[-5:]:  # Show last 5
                status_icon = "[✖]" if s["mutation_status"] == "pending" else "[✔]"
                print(f"  {status_icon} ID: {s['scar_id'][:8]} | {s['timestamp']} | File: {s['target_file']}")
                print(f"      Failing Metric: {s['failed_metric']}")
                print(f"      Error Sample:   {s['error_message'].splitlines()[0] if s['error_message'] else 'None'}")
        print("================================================================================")

def main():
    parser = argparse.ArgumentParser(description="Failure-Informed Prompt Inversion (F-IPI) Mutator")
    group = parser.add_mutually_exclusive_group(required=True)
    
    group.add_argument("--log-failure", action="store_true", help="Log a new software failure trace as a Symbolic Scar.")
    group.add_argument("--mutate-prompt", action="store_true", help="Parse pending scars and mutate GEMINI.md.")
    group.add_argument("--status", action="store_true", help="Display VCS Immunological Layer metrics and registered scars.")
    
    parser.add_argument("--file", type=str, help="Target file that generated the error.")
    parser.add_argument("--metric", type=str, default="test_execution_failure", help="The type of failure metric (e.g. compile_error, lint_error).")
    parser.add_argument("--error", type=str, help="The captured trace or error message.")
    parser.add_argument("--gemini-md", type=str, default=DEFAULT_GEMINI_MD, help="Path to GEMINI.md (Constitution).")
    parser.add_argument("--archive", type=str, default=DEFAULT_STA_FILE, help="Path to scar_tissue_archive.json.")
    
    args = parser.parse_args()
    
    mutator = FIPIMutator(gemini_md_path=args.gemini_md, archive_path=args.archive)
    
    if args.log_failure:
        if not args.error:
            print("[-] ERROR: --error is required when logging a failure trace.", file=sys.stderr)
            sys.exit(1)
        mutator.log_scar(target_file=args.file, failed_metric=args.metric, error_trace=args.error)
        
    elif args.mutate_prompt:
        mutator.mutate_gemini_md()
        
    elif args.status:
        mutator.print_status()

if __name__ == "__main__":
    main()
