import pytest
from system_logic.co_mind_triad import CoMindTriad

def test_co_mind_triad_execution():
    triad = CoMindTriad()
    # [∇] Assuming the Planner -> Linguist -> Crone pipeline processes a string task
    result = triad.execute_task("Analyze cognitive architecture")
    assert "Planner:" in result
    assert "Linguist:" in result
    assert "Crone:" in result
    assert triad.state == "COMPLETED"
