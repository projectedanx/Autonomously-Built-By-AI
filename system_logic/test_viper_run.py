import pytest

from system_logic.viper_run import run_viper_test

def test_run_viper_test(capsys):
    """Tests that run_viper_test correctly identifies banned tokens and outputs the expected diagnostic info."""
    run_viper_test()

    captured = capsys.readouterr()

    # Check for core diagnostic output
    assert "**[DIAGNOSTIC // VIPER-GAFFER v2026.4]**" in captured.out
    assert "User_Intent_Parsed: Portrait of an old woman in a Parisian cafe." in captured.out
    assert "Tokens_Rejected:" in captured.out
    assert "HGI_Status: NON-COMPLIANT" in captured.out

    # Check for specific rejected tokens based on the hardcoded prompt
    assert "'beautiful' -> Rejected by Lattice of Refusal." in captured.out
    assert "'cinematic' -> Rejected by Lattice of Refusal." in captured.out
    assert "'masterpiece' -> Rejected by Lattice of Refusal." in captured.out
    assert "'8k' -> Rejected by Lattice of Refusal." in captured.out
