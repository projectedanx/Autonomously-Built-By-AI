import pytest
from system_logic.generate_agent_index import parse_profile

def test_parse_profile_exception_handling():
    # Pass an invalid file path that will cause an exception
    invalid_filepath = "/invalid/path/that/does/not/exist_12345.md"
    result = parse_profile(invalid_filepath)

    # Verify that the function returns None as expected
    assert result is None, f"Expected None for invalid filepath, but got {result}"
