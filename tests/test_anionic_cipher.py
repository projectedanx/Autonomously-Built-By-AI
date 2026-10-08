import pytest
from system_logic.anionic_cipher import AnionicCipher

def test_anionic_cipher_redaction():
    cipher = AnionicCipher()
    # [∇] Assuming it predicts category of missing token
    redacted = cipher.tokenize_absence("The secret is [REDACTED]")
    assert "CATEGORY_OMISSION" in redacted
