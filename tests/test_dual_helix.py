import unittest
from dual_helix_state import DualHelixState
from golden_trace_validator import validate_trace

class TestDualHelix(unittest.TestCase):
    def test_validate_trace_valid(self):
        # [∇] Assuming state model holds these fields
        state = DualHelixState(
            task_request="test",
            linguistic_scaffold={},
            synthesized_code="def f(): pass",
            evaluation_status="pass",
            verbal_critiques=[],
            skill_primitive="f_skill",
            epistemic_marker="[∇]",
            loop_count=1
        )
        self.assertTrue(validate_trace(state))

    def test_validate_trace_invalid(self):
        state = DualHelixState(
            task_request="test",
            linguistic_scaffold={},
            synthesized_code="",
            evaluation_status="pass",
            verbal_critiques=[],
            skill_primitive="",
            epistemic_marker="[∇]",
            loop_count=4
        )
        self.assertFalse(validate_trace(state))
