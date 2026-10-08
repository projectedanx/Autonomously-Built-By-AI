import pytest
from system_logic.friction_engine import FrictionEngine

def test_friction_engine_montage_synthesis():
    engine = FrictionEngine()
    # [∇] Assuming it returns a synthesis of conflicts
    synthesis = engine.apply_montage_synthesis(["perspective A", "perspective B"])
    assert "Synthesis:" in synthesis
    assert engine.cognitive_parallax > 0.0
