import pytest
from system_logic.generate_agent_index import extract_markdown_table_data, extract_yaml_data
from unittest.mock import patch

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


def test_extract_yaml_data_frontmatter():
    content = """---
agent_name: Test Agent
designation: Tester
---
This is some content.
"""
    expected = {'agent_name': 'Test Agent', 'designation': 'Tester'}
    assert extract_yaml_data(content) == expected

def test_extract_yaml_data_code_block():
    content = """Some intro text.
```yaml
name: YAML Agent
designation: YAMLer
```
Some outro text.
"""
    expected = {'name': 'YAML Agent', 'designation': 'YAMLer'}
    assert extract_yaml_data(content) == expected

def test_extract_yaml_data_missing_keys():
    content = """---
designation: Tester
specialty: Testing
---
"""
    assert extract_yaml_data(content) is None

def test_extract_yaml_data_invalid_yaml():
    content = """---
agent_name: Test Agent
designation: [Tester
---
"""
    assert extract_yaml_data(content) is None

def test_extract_yaml_data_no_yaml():
    content = """Just plain text.
Nothing to see here.
"""
    assert extract_yaml_data(content) is None

def test_extract_yaml_data_not_dict():
    content = """---
- item 1
- item 2
---
"""
    assert extract_yaml_data(content) is None

def test_extract_yaml_data_no_yaml_module():
    with patch('system_logic.generate_agent_index.HAS_YAML', False):
        content = """---
agent_name: Test Agent
---
"""
        assert extract_yaml_data(content) is None

def test_extract_yaml_data_general_exception(capsys):
    with patch('system_logic.generate_agent_index.HAS_YAML', True),\
         patch('system_logic.generate_agent_index.yaml') as mock_yaml:
        mock_yaml.safe_load.side_effect = Exception("Mocked catastrophic failure")
        content = "---\\nagent_name: Test Agent\\n---"
        assert extract_yaml_data(content) is None
        captured = capsys.readouterr()
        assert "YAML parsing error: Mocked catastrophic failure" in captured.err
