import os
import ast
import tempfile
import subprocess
from typing import Tuple, Dict, Any, List

class SelfHealingEngine:
    """
    A production-grade implementation of a self-healing code repair loop,
    drawing on the systems engineering designs of SWE-agent's ACI linter guardrails
    and Plandex's transactional sandbox mechanisms.
    """
    def __init__(self, filename: str, content: str):
        self.filename = filename
        # Maintain the transaction history to allow Plandex-style 'rewind' operations
        self.history: List[str] = [content]
        self.current_content = content

    def get_current_state(self) -> str:
        return self.current_content

    def rewind(self) -> bool:
        """
        Rolls back the file state to the last-known-good content version.
        """
        if len(self.history) > 1:
            self.history.pop()
            self.current_content = self.history[-1]
            return True
        return False

    def validate_code(self, candidate_code: str) -> Tuple[bool, str]:
        """
        Executes a deterministic syntax check. It first parses the Abstract Syntax Tree (AST)
        of the candidate code to locate compilation errors, and then optionally falls back 
        to running flake8 with strict SWE-agent error filters.
        """
        # Step 1: Fast, zero-dependency local AST validation
        try:
            ast.parse(candidate_code)
        except SyntaxError as e:
            # Reconstruct detailed compiler traceback
            error_msg = f"AST Syntax Error on line {e.lineno}, col {e.offset}: {e.msg}\n"
            if e.text:
                error_msg += f"Line containing error: {e.text.strip()}"
            return False, error_msg

        # Step 2: SWE-agent isolated linter command protocol (F821, F822, F831, E111, E112, E113, E999, E902)
        # We simulate this check locally on a temporary file to prevent modifying the host environment.
        with tempfile.NamedTemporaryFile(suffix=".py", mode="w+", delete=False) as tmp:
            tmp.write(candidate_code)
            tmp_path = tmp.name

        try:
            # Check if flake8 is available on the sandbox path
            flake8_codes = "F821,F822,F831,E111,E112,E113,E999,E902"
            result = subprocess.run(
                ["flake8", "--isolated", f"--select={flake8_codes}", tmp_path],
                capture_output=True,
                text=True,
                check=False
            )
            if result.returncode != 0:
                # Format output to remove the temporary file path from messages
                formatted_output = result.stdout.replace(tmp_path, self.filename)
                return False, f"Flake8 Guardrail Failure:\n{formatted_output}"
        except FileNotFoundError:
            # If flake8 is not installed, the AST check is our primary security boundary
            pass
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

        return True, "Code passed all static validation guardrails."

    def compile_feedback_payload(self, proposed_edit: str, error_msg: str, start_line: int, end_line: int) -> str:
        """
        Unifies the three critical context views required for self-correction:
        1. Explanatory linter diagnostics.
        2. The speculative view of the modified code.
        3. The baseline unmodified code state.
        This structured representation prevents the agent from getting stuck in infinite recovery loops.
        """
        original_lines = self.current_content.splitlines()
        speculative_lines = self._apply_edit_to_lines(original_lines, proposed_edit, start_line, end_line)

        # Retrieve a 10-line context window surrounding the edit block for diagnostics
        context_start = max(0, start_line - 5)
        context_end = min(len(original_lines), end_line + 5)

        speculative_snippet = "\n".join(speculative_lines[context_start:context_end + 1])
        original_snippet = "\n".join(original_lines[context_start:context_end + 1])

        feedback = (
            f"❌ [VERIFICATION FAILURE] Your proposed edit introduced syntax/linter regressions.\n"
            f"ERRORS:\n{error_msg}\n\n"
            f"--- SPECULATIVE STATE (What your edit would have looked like if applied) ---\n"
            f"[File: {self.filename}]\n"
            f"{speculative_snippet}\n"
            f"---------------------------------------------------------------------------\n\n"
            f"--- ORIGINAL UNMODIFIED FILE BASELINE ------------------------------------\n"
            f"[File: {self.filename}]\n"
            f"{original_snippet}\n"
            f"---------------------------------------------------------------------------\n"
            f"CRITICAL: Re-evaluate your line coordinates and indentation settings. Do NOT resubmit identical code."
        )
        return feedback

    def _apply_edit_to_lines(self, lines: List[str], replacement: str, start_line: int, end_line: int) -> List[str]:
        # Line numbers are 1-indexed (standard editor convention)
        start_idx = start_line - 1
        end_idx = end_line
        
        replacement_lines = replacement.splitlines()
        return lines[:start_idx] + replacement_lines + lines[end_idx:]

    def commit_transaction(self, new_content: str):
        """
        Saves the validated code state to history, updating the current content pointer.
        """
        self.current_content = new_content
        self.history.append(new_content)


# ─── Mock Agent Loop Simulation ───────────────────────────────────────
def simulate_self_healing_repair_loop():
    print("🚀 Initializing Self-Healing Loop Simulation...\n")

    # Initial broken code that needs to be refactored
    initial_code = (
        "def calculate_metrics(data):\n"
        "    total = sum(data)\n"
        "    count = len(data)\n"
        "    # Placeholder for calculation\n"
        "    pass\n"
    )

    # Instantiate our engine with the initial code
    engine = SelfHealingEngine(filename="metrics.py", content=initial_code)

    # Let's simulate a Coder sub-agent's first, malformed editing attempt
    # The sub-agent attempts to add a division operation but accidentally introduces a syntax error (missing parenthesis)
    bad_edit = (
        "    if count == 0:\n"
        "        return 0\n"
        "    return total / (count  # Oops! Missing closing parenthesis!"
    )
    start_line, end_line = 4, 5

    print("Step 1: Agent proposes edit with syntax regression...")
    print(f"Proposed replacement lines:\n{bad_edit}\n")

    # Reconstruct the speculative code state to validate it
    original_lines = engine.get_current_state().splitlines()
    speculative_lines = engine._apply_edit_to_lines(original_lines, bad_edit, start_line, end_line)
    speculative_code = "\n".join(speculative_lines)

    # Pass the code through the linter gate
    is_valid, linter_feedback = engine.validate_code(speculative_code)

    if not is_valid:
        print("🛡️ [LINTER GATE INTRUSION ALERT] Syntactic anomalies detected! Initiating rollback...")
        # Compile the 3-part feedback payload to drive self-healing retries
        feedback_payload = engine.compile_feedback_payload(bad_edit, linter_feedback, start_line, end_line)
        print("\nGenerated Feedback Payload passed back to LLM context:\n")
        print(feedback_payload)
        print("\n" + "="*80 + "\n")
    else:
        engine.commit_transaction(speculative_code)
        print("✅ Edit transaction committed successfully.")

    # Let's simulate the second "self-healed" attempt where the agent processes the feedback and fixes the syntax
    good_edit = (
        "    if count == 0:\n"
        "        return 0\n"
        "    return total / count"
    )

    print("Step 2: Agent processes feedback payload and proposes corrected edit...")
    print(f"Corrected replacement lines:\n{good_edit}\n")

    # Reconstruct the speculative code state again
    speculative_lines = engine._apply_edit_to_lines(original_lines, good_edit, start_line, end_line)
    speculative_code = "\n".join(speculative_lines)

    is_valid, linter_feedback = engine.validate_code(speculative_code)

    if is_valid:
        engine.commit_transaction(speculative_code)
        print("🛡️ [LINTER GATE PASSED] Code verified as syntactically clean!")
        print("🔒 Transaction committed to history partition successfully.")
        print("\nFinal Self-Healed Code State:")
        print(engine.get_current_state())
    else:
        print(f"❌ Verification failed: {linter_feedback}")

if __name__ == "__main__":
    simulate_self_healing_repair_loop()
