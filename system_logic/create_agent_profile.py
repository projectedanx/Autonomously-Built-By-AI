#!/usr/bin/env python3
import os
import sys
from dataclasses import dataclass
from typing import Optional

@dataclass
class AgentProfile:
    name: str
    designation: str
    color: str
    specialty: str
    when_to_use: str
    primary_goal: str
    secondary_goal: str
    forbidden: str
    voice: str
    primary_mode: str
    rules: str
    folder_name: Optional[str] = None


def get_yaml_template():
    """Returns the YAML template string for creating agent profiles.

    Returns:
        str: The YAML template string.
    """
    return """agent_name: "{name}"
designation: "{designation}"
build_version: "1.0.0"
color_designation: "{color}"
specialty:
{specialty}

when_to_use: >
{when_to_use}

epistemic_matrix:
  G_GOAL_ORIENTATION:
    primary: "{primary_goal}"
    secondary: "{secondary_goal}"
  G_NEGATIVE_ANTIGOALS:
    forbidden_practices:
{forbidden}
  C_COMMUNICATION:
    voice: "{voice}"
  T_TASK_EXECUTION:
    primary_mode: "{primary_mode}"

critical_rules:
{rules}
"""

def create_agent(profile: AgentProfile):
    """Creates an agent profile YAML file based on the provided profile.

    Args:
        profile (AgentProfile): The profile parameters.

    Raises:
        ValueError: If the folder name is invalid.
    """
    folder_name = profile.folder_name
    if not folder_name:
        folder_name = profile.name.lower().replace(" ", "_")

    # Sanitize folder_name to prevent path traversal
    folder_name = os.path.basename(folder_name)
    if not folder_name or folder_name in (os.curdir, os.pardir):
        raise ValueError(f"Invalid folder name: {folder_name}")

    folder_path = os.path.join("agent_profiles", folder_name)
    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, "profile.yaml")

    # Format list items
    specialty_str = "\n".join([f"  - {s.strip()}" for s in profile.specialty.split(",") if s.strip()])
    forbidden_str = "\n".join([f"      - \"{f.strip()}\"" for f in profile.forbidden.split(",") if f.strip()])
    rules_str = "\n".join([f"  - \"{r.strip()}\"" for r in profile.rules.split("|") if r.strip()])

    # Indent when_to_use
    when_to_use_str = "  " + profile.when_to_use.replace("\n", "\n  ")

    yaml_content = get_yaml_template().format(
        name=profile.name,
        designation=profile.designation,
        color=profile.color,
        specialty=specialty_str,
        when_to_use=when_to_use_str,
        primary_goal=profile.primary_goal,
        secondary_goal=profile.secondary_goal,
        forbidden=forbidden_str,
        voice=profile.voice,
        primary_mode=profile.primary_mode,
        rules=rules_str
    )

    with open(file_path, "w") as f:
        f.write(yaml_content)

    print(f"Created agent profile for {profile.name} at {file_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Simplistic command line support just for testing
        print("Use Python directly to call create_agent() for complex inputs.")
    else:
        print("Agent profile creator tool ready.")
