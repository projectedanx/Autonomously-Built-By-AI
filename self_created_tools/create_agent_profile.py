import os
import argparse
import textwrap

def create_agent(name, alias, goal, constraints, mechanisms):
    safe_name = os.path.basename(name.lower().replace(" ", "_"))
    if not safe_name:
        raise ValueError("Invalid agent name provided")
    folder = os.path.join("agent_profiles", safe_name)
    os.makedirs(folder, exist_ok=True)

    yaml_path = os.path.join(folder, f"{safe_name}.yaml")
    with open(yaml_path, 'w') as f:
        f.write(textwrap.dedent(f"""\
            agent_name: "{name}"
            designation: "{alias}"
            build_version: "1.0.0-stable"
            color_designation: "#FF00FF"
            specialty:
              - General Purpose
            system_pdl_decorators:
              - "+++TaskScope: General"
            epistemic_matrix:
              G_GOAL_ORIENTATION:
                primary: "{goal}"
              G_NEGATIVE_ANTIGOALS:
                forbidden_lexicon:
                  - "seamless"
                  - "robust"
              C_COMMUNICATION:
                voice: "Standard"
        """))

    md_path = os.path.join(folder, "README.md")
    with open(md_path, 'w') as f:
        f.write(textwrap.dedent(f"""\
            # {name} - {alias}

            ## Mission
            You are {name}.

            ## Constraints
            {constraints}

            ## Mechanisms
            {mechanisms}
        """))
    print(f"Created agent profile for {name} in {folder}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True)
    parser.add_argument("--alias", required=True)
    parser.add_argument("--goal", required=True)
    parser.add_argument("--constraints", required=True)
    parser.add_argument("--mechanisms", required=True)
    args = parser.parse_args()
    create_agent(args.name, args.alias, args.goal, args.constraints, args.mechanisms)
