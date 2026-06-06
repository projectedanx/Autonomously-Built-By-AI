import pytest
from system_logic.generate_agent_index import extract_markdown_table_data

def test_extract_markdown_table_data_standard():
    content = """
Here is a table:
| Field | Value |
|---|---|
| **Agent Name** | Test Agent |
| Designation | Tester |
| Agent Specialty | Testing |
| When to use | For testing things |
| Description | A test description |
    """
    expected = {
        'name': 'Test Agent',
        'designation': 'Tester',
        'fundamental_use_cases': 'Testing',
        'purpose': 'For testing things',
        'description': 'A test description'
    }
    assert extract_markdown_table_data(content) == expected

def test_extract_markdown_table_data_combined_name_designation():
    content = """
| Field | Value |
|---|---|
| Agent Name | Combined Agent — The Combiner |
| Agent Specialty | Combining |
    """
    expected = {
        'name': 'Combined Agent',
        'designation': 'The Combiner',
        'fundamental_use_cases': 'Combining'
    }
    assert extract_markdown_table_data(content) == expected

def test_extract_markdown_table_data_combined_name_designation_existing():
    content = """
| Field | Value |
|---|---|
| Agent Name | Combined Agent — The Combiner |
| Designation | Explicit Designation |
    """
    expected = {
        'name': 'Combined Agent',
        'designation': 'Explicit Designation'
    }
    assert extract_markdown_table_data(content) == expected

def test_extract_markdown_table_data_unknown_keys():
    content = """
| Field | Value |
|---|---|
| Agent Name | Key Agent |
| Unknown Key | Should be ignored |
| Designation | Key Master |
    """
    expected = {
        'name': 'Key Agent',
        'designation': 'Key Master'
    }
    assert extract_markdown_table_data(content) == expected

def test_extract_markdown_table_data_no_table():
    content = """
This is just some text.
No table here.
    """
    assert extract_markdown_table_data(content) is None

def test_extract_markdown_table_data_no_matching_keys():
    content = """
| Foo | Bar |
|---|---|
| Baz | Qux |
    """
    assert extract_markdown_table_data(content) is None
