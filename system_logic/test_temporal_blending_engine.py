import pytest
from system_logic.temporal_blending_engine import Action, SystemAssuranceAgent, TemporalBlendingEngine

def test_perfect_trace():
    s1 = {"f_cam": 1, "door_open": 0}
    a1 = Action("disable_cam", preconditions={"f_cam": 1}, effects={"f_cam": 0})
    s2 = {"f_cam": 0, "door_open": 0}
    a2 = Action("open_door", preconditions={"door_open": 0}, effects={"door_open": 1})
    s3 = {"f_cam": 0, "door_open": 1}

    states = [s1, s2, s3]
    actions = [a1, a2]

    tbe = TemporalBlendingEngine()
    saa = SystemAssuranceAgent()

    cpi = saa.calculate_cpi(states, actions)
    assert cpi == 1.0
    result = tbe.process_trace(states, actions)
    assert result == "Release State"

def test_contradictory_trace():
    # [∇] Uncertainty in how to handle very short trace threshold. N=3 -> 1 valid out of 2 transitions = 0.5.
    s1 = {"f_cam": 1, "door_open": 0}
    a1 = Action("disable_cam", preconditions={"f_cam": 1}, effects={"f_cam": 0})
    s2 = {"f_cam": 0, "door_open": 0}
    a2 = Action("scan_retina", preconditions={"f_cam": 1}, effects={"door_open": 1})
    s3 = {"f_cam": 1, "door_open": 1}

    states = [s1, s2, s3]
    actions = [a1, a2]

    tbe = TemporalBlendingEngine()
    saa = SystemAssuranceAgent()

    cpi = saa.calculate_cpi(states, actions)
    assert cpi == 0.5
    result = tbe.process_trace(states, actions)
    assert result == "Epistemic Escrow / Reflexive Repair"
