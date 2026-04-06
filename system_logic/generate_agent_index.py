import os
import re
import sys

# Try importing yaml, but don't fail if it's missing. We'll use a simple fallback.
try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

def extract_yaml_data(content):
    if not HAS_YAML:
        return None
    try:
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                return yaml.safe_load(parts[1])
        return yaml.safe_load(content)
    except Exception:
        return None

def strip_markdown(text):
    if not text:
        return ""
    # Remove code blocks
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    # Remove inline code
    text = re.sub(r'`[^`]+`', '', text)
    # Remove html tags
    text = re.sub(r'<[^>]+>', '', text)
    # Remove markdown links
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    # Remove heading markers
    text = re.sub(r'#+\s+', '', text)
    # Remove formatting chars (*, _, etc.)
    text = re.sub(r'[*_]', '', text)
    # Remove json-like structural elements (e.g. "key": "value",)
    text = re.sub(r'^\s*".*?":\s*.*?,?\s*$', '', text, flags=re.MULTILINE)
    # Condense whitespace
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_section(content, section_keywords):
    # This regex attempts to find keywords (e.g. "Purpose:") and captures text
    # that is EITHER inline on the same line OR on subsequent lines before the next markdown heading or EOF.
    keywords_pattern = '|'.join(section_keywords)

    # Pattern explanation:
    # (?:{keywords_pattern}) : Match the keywords
    # [^\w\n]* : Match any non-word, non-newline characters (like spaces, colons, markdown stars)
    # (.*?) : Capture the content
    # (?=\n#|\n\n\*\*|\Z) : Lookahead for the next major heading (e.g. \n#, \n\n**) or end of string

    pattern = re.compile(rf'(?:{keywords_pattern})[^\w\n]*\n?(.*?)(?=\n#|\n\n\*\*|\n\n\w+:|\Z)', re.IGNORECASE | re.DOTALL)
    match = pattern.search(content)

    if match:
        extracted = match.group(1).strip()
        # If it's too long, truncate it
        if len(extracted) > 300:
            extracted = extracted[:297] + '...'
        return strip_markdown(extracted)
    return ""

def parse_profile(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return None

    data = {
        'name': 'Unknown',
        'designation': 'Unknown',
        'purpose': '',
        'fundamental_use_cases': '',
        'strategic_use_cases': '',
        'filepath': filepath
    }

    filename = os.path.basename(filepath)

    yaml_data = extract_yaml_data(content)
    if yaml_data and isinstance(yaml_data, dict):
        data['name'] = yaml_data.get('agent_name', yaml_data.get('name', 'Unknown'))
        data['designation'] = yaml_data.get('designation', 'Unknown')
        data['purpose'] = yaml_data.get('when_to_use', '')
        specialty = yaml_data.get('specialty', [])
        if isinstance(specialty, list):
            data['fundamental_use_cases'] = ', '.join(specialty)

    # For Markdown or if YAML failed/was incomplete, try regex heuristics
    if data['name'] == 'Unknown' or not data['name']:
        name_match = re.search(r'(?:Name|Agent Name|Identity Name|AGENT_ID|Identity)[^\w\n]*([^\n]+)', content, re.IGNORECASE)
        if name_match:
            data['name'] = strip_markdown(name_match.group(1))

        if not data['name'] or data['name'] == 'Unknown':
             data['name'] = filename.replace('.md', '').replace('.yaml', '').replace('_', ' ').title()

    if data['designation'] == 'Unknown' or not data['designation']:
        desig_match = re.search(r'(?:Designation|Role|Title)[^\w\n]*([^\n]+)', content, re.IGNORECASE)
        if desig_match:
            data['designation'] = strip_markdown(desig_match.group(1))

    if not data['purpose']:
        data['purpose'] = extract_section(content, ['When to use', 'Purpose', 'Mission', 'Specialty', 'Core Mission'])
        # Ultimate fallback for purpose
        if not data['purpose']:
            data['purpose'] = strip_markdown(content[:300])

    if not data['fundamental_use_cases']:
        data['fundamental_use_cases'] = extract_section(content, ['Fundamental Use Cases', 'Capabilities', 'Features', 'Primary Objectives?', 'Key Use Cases'])

    if not data['strategic_use_cases']:
        data['strategic_use_cases'] = extract_section(content, ['Strategic Use Cases', 'Secondary Objectives?'])

    # Final cleanup
    for k in ['purpose', 'fundamental_use_cases', 'strategic_use_cases']:
        if len(data[k]) >= 300:
            data[k] = data[k][:297] + '...'

    return data

def main():
    base_dir = 'agent_profiles'
    profiles = []

    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.md') or file.endswith('.yaml') or file.endswith('.yml'):
                filepath = os.path.join(root, file)
                # Exclude the README itself
                if file.lower() == 'readme.md':
                    continue
                profile_data = parse_profile(filepath)
                if profile_data:
                    profiles.append(profile_data)

    # Sort profiles alphabetically
    profiles.sort(key=lambda x: x['name'].lower())

    with open(os.path.join(base_dir, 'README.md'), 'w', encoding='utf-8') as f:
        f.write("# Agent Profiles Index\n\n")
        f.write("This directory contains the profiles for all Sovereign agents. Below is an index of each agent, its purpose, fundamental use cases, and strategic use cases.\n\n")
        f.write("---\n\n")

        for p in profiles:
            rel_path = os.path.relpath(p['filepath'], base_dir)
            f.write(f"## [{p['name']}]({rel_path})\n")
            if p['designation'] != 'Unknown':
                f.write(f"**Designation:** {p['designation']}\n\n")
            if p['purpose']:
                f.write(f"**Purpose:** {p['purpose']}\n\n")
            if p['fundamental_use_cases']:
                f.write(f"**Fundamental Use Cases:** {p['fundamental_use_cases']}\n\n")
            if p['strategic_use_cases']:
                f.write(f"**Strategic Use Cases:** {p['strategic_use_cases']}\n\n")
            f.write("---\n\n")

    print(f"Generated index for {len(profiles)} agents at {os.path.join(base_dir, 'README.md')}")

if __name__ == "__main__":
    main()
