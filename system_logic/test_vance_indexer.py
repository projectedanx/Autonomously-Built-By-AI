import pytest
from system_logic.vance_indexer import VanceLSPMapper

def test_handle_did_change_missing_version_logs_scar():
    mapper = VanceLSPMapper()

    # Mock error payload (missing version)
    mock_error_payload = {
        "jsonrpc": "2.0",
        "method": "textDocument/didChange",
        "params": {
            "textDocument": {
                "uri": "file:///workspace/src/auth.rs"
            },
            "contentChanges": []
        }
    }

    # Initial state should have no scars
    initial_scar_count = len(mapper.nfl_scars)

    # Trigger the error path
    mapper.handle_did_change(mock_error_payload)

    # Assert a scar was logged
    assert len(mapper.nfl_scars) == initial_scar_count + 1

    # Assert the scar contents are correct
    latest_scar = mapper.nfl_scars[-1]
    assert latest_scar["trigger"] == "didChange malformed"
    assert "LSP 3.17 Violation" in latest_scar["violation"]
