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

def test_apply_delta_ignores_stale_version():
    from system_logic.vance_indexer import SemanticGraph
    graph = SemanticGraph()
    uri = "file:///workspace/src/test.py"

    # Apply initial delta (version 5)
    graph.apply_delta(
        uri=uri,
        version=5,
        changes=[{"text": "initial_function()"}]
    )

    # Verify initial state
    assert graph.version == 5
    assert "initial_function" in graph.nodes[uri]

    # Try to apply an older delta (version 4)
    graph.apply_delta(
        uri=uri,
        version=4,
        changes=[{"text": "stale_function()"}]
    )

    # Verify stale delta was ignored
    assert graph.version == 5
    assert "stale_function" not in graph.nodes[uri]
    assert "initial_function" in graph.nodes[uri]
