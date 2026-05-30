import pytest
from system_logic.mereology_check import validate_mereology

def test_validate_mereology_clean():
    dag = {
        "nodes": ["ContextA", "ContextB"],
        "edges": [
            {"source": "ContextA", "target": "ContextB", "type": "API_CALL"}
        ]
    }
    violations = validate_mereology(dag)
    assert len(violations) == 0

def test_validate_mereology_shared_db_violation():
    dag = {
        "nodes": ["ContextA", "ContextB", "ContextB_DB"],
        "edges": [
            {"source": "ContextA", "target": "ContextB_DB", "type": "DB_WRITE"},
            {"source": "ContextB", "target": "ContextB_DB", "type": "DB_READ"}
        ]
    }
    violations = validate_mereology(dag)
    assert len(violations) > 0
    assert any("Shared Database" in v for v in violations)

def test_validate_mereology_transitivity_violation():
    dag = {
        "nodes": ["Frontend", "API_Gateway", "Internal_Microservice"],
        "edges": [
            {"source": "Frontend", "target": "API_Gateway", "type": "API_CALL"},
            {"source": "Frontend", "target": "Internal_Microservice", "type": "API_CALL"} # Frontend shouldn't talk to Internal directly
        ]
    }
    violations = validate_mereology(dag)
    # Based on strict boundaries, a frontend bypassing the gateway to an internal service is a violation
    # This might require some specific business logic definition, but let's assume strict layered architecture for now.
    assert len(violations) > 0
    assert any("Transitivity Violation" in v for v in violations)
