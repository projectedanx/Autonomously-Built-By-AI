#!/usr/bin/env python3
import os
import sys

def get_yaml_template():
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

def create_agent(name, designation, color, specialty, when_to_use, primary_goal, secondary_goal, forbidden, voice, primary_mode, rules, folder_name=None):
    if not folder_name:
        folder_name = name.lower().replace(" ", "_")

    folder_path = os.path.join("agent_profiles", folder_name)
    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, "profile.yaml")

    # Format list items
    specialty_str = "\n".join([f"  - {s.strip()}" for s in specialty.split(",") if s.strip()])
    forbidden_str = "\n".join([f"      - \"{f.strip()}\"" for f in forbidden.split(",") if f.strip()])
    rules_str = "\n".join([f"  - \"{r.strip()}\"" for r in rules.split("|") if r.strip()])

    # Indent when_to_use
    when_to_use_str = "  " + when_to_use.replace("\n", "\n  ")

    yaml_content = get_yaml_template().format(
        name=name,
        designation=designation,
        color=color,
        specialty=specialty_str,
        when_to_use=when_to_use_str,
        primary_goal=primary_goal,
        secondary_goal=secondary_goal,
        forbidden=forbidden_str,
        voice=voice,
        primary_mode=primary_mode,
        rules=rules_str
    )

    with open(file_path, "w") as f:
        f.write(yaml_content)

    print(f"Created agent profile for {name} at {file_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Simplistic command line support just for testing
        print("Use Python directly to call create_agent() for complex inputs.")
    else:
        print("Agent profile creator tool ready.")
