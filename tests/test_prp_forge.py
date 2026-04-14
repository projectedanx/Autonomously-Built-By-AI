import pytest
from system_logic.prp_forge import PRPForge

def test_generate_prp_structure():
    forge = PRPForge()
    raw_content = "Test content"
    source_filename = "test.txt"
    prp, prp_id = forge.generate_prp(raw_content, source_filename)

    assert isinstance(prp, dict)
    assert isinstance(prp_id, str)
    assert "prp_version" in prp
    assert "metadata" in prp
    assert "context" in prp
    assert "constraints_and_invariants" in prp
    assert "raw_intent_snippet" in prp

    metadata = prp["metadata"]
    assert "id" in metadata
    assert "author" in metadata
    assert "drp_lineage" in metadata
    assert "source_file" in metadata

def test_generate_prp_content_values():
    forge = PRPForge()
    raw_content = "Test content"
    source_filename = "test.txt"
    prp, prp_id = forge.generate_prp(raw_content, source_filename)

    assert prp["prp_version"] == "1.0"
    assert prp["metadata"]["author"] == "Meta-Prompt Designer (Automated Scaffold)"
    assert prp["metadata"]["drp_lineage"] == "DRP-CRITICAL-REQUIREMENTS-PRP-2026"
    assert prp["metadata"]["source_file"] == source_filename

def test_generate_prp_id_consistency():
    forge = PRPForge()
    raw_content = "Test content"
    source_filename = "test.txt"
    prp, prp_id = forge.generate_prp(raw_content, source_filename)

    assert prp_id == prp["metadata"]["id"]
    assert prp_id.startswith("PRP-CRITICAL-REQ-")

def test_generate_prp_snippet_truncation():
    forge = PRPForge()
    # 501 characters
    long_content = "A" * 501
    prp, _ = forge.generate_prp(long_content, "test.txt")

    expected_snippet = ("A" * 500) + "..."
    assert prp["raw_intent_snippet"] == expected_snippet
    assert len(prp["raw_intent_snippet"]) == 503

def test_generate_prp_short_content():
    forge = PRPForge()
    short_content = "Short"
    prp, _ = forge.generate_prp(short_content, "test.txt")

    # Based on: raw_content[:500] + "..."
    assert prp["raw_intent_snippet"] == "Short..."

def test_generate_prp_id_uniqueness():
    forge = PRPForge()
    raw_content = "Test content"
    source_filename = "test.txt"
    _, id1 = forge.generate_prp(raw_content, source_filename)
    _, id2 = forge.generate_prp(raw_content, source_filename)

    assert id1 != id2
