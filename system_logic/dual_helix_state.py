from typing import TypedDict, List, Dict, Any

class DualHelixState(TypedDict):
    task_request: str
    linguistic_scaffold: Dict[str, Any]
    synthesized_code: str
    evaluation_status: str
    verbal_critiques: List[str]
    skill_primitive: str
    epistemic_marker: str
    loop_count: int
