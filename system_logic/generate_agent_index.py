import os
import re
import sys

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


def _parse_yaml_frontmatter(content):
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            parsed = yaml.safe_load(parts[1])
            if isinstance(
                    parsed, dict) and (
                    'agent_name' in parsed or 'name' in parsed):
                return parsed
    return None


def _parse_yaml_blocks(content):
    yaml_blocks = re.findall(
        r'```(?:yaml|yml)\n(.*?)\n```',
        content,
        re.DOTALL | re.IGNORECASE)
    for block in yaml_blocks:
        try:
            parsed = yaml.safe_load(block)
            if isinstance(
                    parsed, dict) and (
                    'agent_name' in parsed or 'name' in parsed):
                return parsed
        except Exception:
            pass
    return None


def extract_yaml_data(content):
    """Extracts YAML data from markdown content."""
    if not HAS_YAML:
        return None
    try:
        frontmatter = _parse_yaml_frontmatter(content)
        if frontmatter:
            return frontmatter
        return _parse_yaml_blocks(content)
    except Exception as e:
        print(f"YAML parsing error: {e}", file=sys.stderr)
        return None


def _process_table_row(parts, data, key_mapping):
    if len(parts) < 2:
        return
    key_raw = re.sub(r'[*_]', '', parts[0]).lower().strip()
    val_raw = strip_markdown(parts[1])
    for k, v in key_mapping.items():
        if k in key_raw:
            data[v] = val_raw
    if 'name' in key_raw and ' — ' in strip_markdown(parts[1]):
        name_parts = strip_markdown(parts[1]).split(' — ')
        data['name'] = name_parts[0].strip()
        if len(name_parts) > 1 and 'designation' not in data:
            data['designation'] = name_parts[1].strip()


def extract_markdown_table_data(content):
    """Extracts data from a markdown table, looking for specific keys."""
    data = {}
    lines = content.split('\n')
    in_table = False
    key_mapping = {
        'agent name': 'name',
        'designation': 'designation',
        'agent specialty': 'fundamental_use_cases',
        'when to use': 'purpose',
        'description': 'description'
    }
    for line in lines:
        if line.strip().startswith('|') and '|' in line[1:]:
            in_table = True
            parts = [p.strip() for p in line.split('|')[1:-1]]
            _process_table_row(parts, data, key_mapping)
        elif in_table and not line.strip().startswith('|'):
            in_table = False
    return data if data else None


_RE_CODE_BLOCK = re.compile(r'```.*?```', flags=re.DOTALL)
_RE_INLINE_CODE = re.compile(r'`[^`]+`')
_RE_HTML_TAGS = re.compile(r'<[^>]+>')
_RE_MD_LINKS = re.compile(r'\[([^\]]+)\]\([^\)]+\)')
_RE_HEADING = re.compile(r'#+\s+')
_RE_FORMATTING = re.compile(r'[*_]')
_RE_JSON_ELEMENTS = re.compile(r'^\s*".*?":\s*.*?,?\s*$', flags=re.MULTILINE)
_RE_WHITESPACE = re.compile(r'\s+')


def _apply_markdown_code_regexes(text):
    if '`' in text:
        if '```' in text:
            text = _RE_CODE_BLOCK.sub('', text)
        text = _RE_INLINE_CODE.sub('', text)
    return text


def _apply_markdown_other_regexes(text):
    if '<' in text and '>' in text:
        text = _RE_HTML_TAGS.sub('', text)
    if '[' in text and ']' in text:
        text = _RE_MD_LINKS.sub(r'\1', text)
    if '#' in text:
        text = _RE_HEADING.sub('', text)
    if '*' in text or '_' in text:
        text = _RE_FORMATTING.sub('', text)
    if '"' in text and ':' in text:
        text = _RE_JSON_ELEMENTS.sub('', text)
    return _RE_WHITESPACE.sub(' ', text)


def _apply_markdown_regexes(text):
    text = _apply_markdown_code_regexes(text)
    return _apply_markdown_other_regexes(text)


def strip_markdown(text):
    """Removes markdown formatting from a text string."""
    if not text:
        return ""
    text = text.strip('"\'')
    text = _apply_markdown_regexes(text)
    return text.strip()


_PATTERN_CACHE = {}


def _get_section_pattern(section_keywords):
    cache_key = tuple(section_keywords)
    if cache_key not in _PATTERN_CACHE:
        keywords_pattern = '|'.join(section_keywords)
        pattern = re.compile(
            rf'(?:{keywords_pattern})[^\w\n]*\n?(.*?)(?=\n#|\n\n\*\*|\n\n\w+:|\Z)',
            re.IGNORECASE | re.DOTALL)
        _PATTERN_CACHE[cache_key] = pattern
    return _PATTERN_CACHE[cache_key]


def extract_section(content, section_keywords):
    """Extracts a specific section from markdown content based on keywords."""
    pattern = _get_section_pattern(section_keywords)
    match = pattern.search(content)

    if match:
        extracted = match.group(1).strip()
        if len(extracted) > 300:
            extracted = extracted[:297] + '...'
        return strip_markdown(extracted)
    return ""


def _apply_yaml_data(data, content):
    yaml_data = extract_yaml_data(content)
    if yaml_data and isinstance(yaml_data, dict):
        data['name'] = yaml_data.get(
            'agent_name', yaml_data.get(
                'name', 'Unknown'))
        data['designation'] = yaml_data.get('designation', 'Unknown')
        data['purpose'] = yaml_data.get('when_to_use', '')
        specialty = yaml_data.get('specialty', [])
        if isinstance(specialty, list):
            data['fundamental_use_cases'] = ', '.join(specialty)
        return True
    return False


def _apply_table_data(data, content):
    table_data = extract_markdown_table_data(content)
    if not table_data:
        return
    if 'name' in table_data:
        data['name'] = table_data['name']
    if 'designation' in table_data:
        data['designation'] = table_data['designation']
    if 'purpose' in table_data:
        data['purpose'] = table_data['purpose']
    if 'fundamental_use_cases' in table_data:
        data['fundamental_use_cases'] = table_data['fundamental_use_cases']
    if not data['purpose'] and 'description' in table_data:
        data['purpose'] = table_data['description']


def _apply_name_heuristics(data, content, filename):
    if data['name'] == 'Unknown' or not data['name']:
        name_match = re.search(
            r'(?:Agent Name|Identity Name|AGENT_ID|agent_name|DRP_NAME):\s*([^\n]+)',
            content,
            re.IGNORECASE)
        if name_match:
            data['name'] = strip_markdown(name_match.group(1))
        if not data['name'] or data['name'] == 'Unknown':
            data['name'] = filename.replace(
                '.md',
                '').replace(
                '.yaml',
                '').replace(
                '_',
                ' ').title()


def _apply_designation_heuristics(data, content):
    if data['designation'] == 'Unknown' or not data['designation']:
        desig_match = re.search(
            r'(?:Designation|Role|Title|designation):?\s*([^\n]+)',
            content,
            re.IGNORECASE)
        if desig_match:
            data['designation'] = strip_markdown(desig_match.group(1))


def _apply_purpose_heuristics(data, content):
    if not data['purpose']:
        data['purpose'] = extract_section(
            content, ['When to use', 'Purpose', 'Mission', 'Specialty', 'Core Mission'])
        if not data['purpose']:
            data['purpose'] = strip_markdown(content[:300])


def _apply_use_case_heuristics(data, content):
    if not data['fundamental_use_cases']:
        data['fundamental_use_cases'] = extract_section(
            content, [
                'Fundamental Use Cases', 'Capabilities', 'Features', 'Primary Objectives?', 'Key Use Cases'])
    if not data['strategic_use_cases']:
        data['strategic_use_cases'] = extract_section(
            content, ['Strategic Use Cases', 'Secondary Objectives?'])


def _apply_regex_heuristics(data, content, filename):
    _apply_name_heuristics(data, content, filename)
    _apply_designation_heuristics(data, content)
    _apply_purpose_heuristics(data, content)
    _apply_use_case_heuristics(data, content)


def _finalize_profile_data(data):
    data['name'] = data['name'].strip('"' + "'")
    data['designation'] = data['designation'].strip('"' + "'")
    for k in ['purpose', 'fundamental_use_cases', 'strategic_use_cases']:
        if len(data[k]) >= 300:
            data[k] = data[k][:297] + '...'
    return data


def _read_profile_content(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception:
        return None


def _create_initial_data(filepath):
    return {
        'name': 'Unknown',
        'designation': 'Unknown',
        'purpose': '',
        'fundamental_use_cases': '',
        'strategic_use_cases': '',
        'filepath': filepath
    }


def _parse_profile_logic(filepath, content):
    data = _create_initial_data(filepath)
    if not _apply_yaml_data(data, content):
        _apply_table_data(data, content)
    _apply_regex_heuristics(data, content, os.path.basename(filepath))
    return _finalize_profile_data(data)


def parse_profile(filepath):
    """Parses an agent profile file (markdown or YAML) to extract key information."""
    content = _read_profile_content(filepath)
    if content is None:
        return None
    return _parse_profile_logic(filepath, content)


def _write_index_file(base_dir, profiles):
    with open(os.path.join(base_dir, 'README.md'), 'w', encoding='utf-8') as f:
        f.write("# Agent Profiles Index\n\n")
        f.write("This directory contains the profiles for all Sovereign agents. "
                "Below is an index of each agent, its purpose, fundamental use cases, "
                "and strategic use cases.\n\n")
        f.write("---\n\n")
        for p in profiles:
            rel_path = os.path.relpath(p['filepath'], base_dir)
            f.write(f"## [{p['name']}]({rel_path})\n")
            if p['designation'] != 'Unknown':
                f.write(f"**Designation:** {p['designation']}\n\n")
            if p['purpose']:
                f.write(f"**Purpose:** {p['purpose']}\n\n")
            if p['fundamental_use_cases']:
                f.write(
                    f"**Fundamental Use Cases:** {p['fundamental_use_cases']}\n\n")
            if p['strategic_use_cases']:
                f.write(
                    f"**Strategic Use Cases:** {p['strategic_use_cases']}\n\n")
            f.write("---\n\n")


def _collect_profiles(base_dir):
    profiles = []
    valid_ext = ('.md', '.yaml', '.yml')
    for root, _, files in os.walk(base_dir):
        valid_files = [f for f in files if f.endswith(
            valid_ext) and f.lower() != 'readme.md']
        for file in valid_files:
            filepath = os.path.join(root, file)
            profile_data = parse_profile(filepath)
            if profile_data:
                profiles.append(profile_data)
    return profiles


def main():
    """Main entry point to scan for agent profiles and generate an index README."""
    base_dir = 'agent_profiles'
    profiles = _collect_profiles(base_dir)
    profiles.sort(key=lambda x: x['name'].lower())
    _write_index_file(base_dir, profiles)
    print(
        f"Generated index for {
            len(profiles)} agents at {
            os.path.join(
                base_dir,
                'README.md')}")


if __name__ == "__main__":
    main()
