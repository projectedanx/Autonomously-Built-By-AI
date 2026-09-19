from dual_helix_state import DualHelixState

def validate_trace(state: DualHelixState) -> bool:
    """Detects behavioral drift in regression suites. [∇] Flag for uncertainty."""
    if state.get("loop_count", 0) > 3:
        return False
    if not state.get("synthesized_code"):
        return False
    return True
