import json

def run_viper_test():
    """Runs a test of the VIPER-GAFFER system to check prompts against banned aesthetic evaluators."""
    prompt = "I want a nostalgic, beautiful portrait of an old woman in a Parisian cafe, very cinematic and emotional, masterpiece quality, 8k"
    banned_tokens = [
        "masterpiece", "epic", "stunning", "beautiful", "hyper-realistic",
        "trending on artstation", "8k", "4k", "ultra HD", "cinematic vibes",
        "moody", "ethereal", "perfect", "flawless", "amazing", "breathtaking",
        "gorgeous", "cinematic"
    ]

    rejected = [token for token in banned_tokens if token in prompt.lower()]

    if rejected:
        print("**[DIAGNOSTIC // VIPER-GAFFER v2026.4]**")
        print(f"User_Intent_Parsed: Portrait of an old woman in a Parisian cafe.")
        print("Tokens_Rejected:")
        for token in rejected:
            print(f"  '{token}' -> Rejected by Lattice of Refusal.")
        print("HGI_Status: NON-COMPLIANT")
        print("\nHALT: Cannot generate Optical State Matrix. User must provide physical specifications, not aesthetic evaluators.")
    else:
        print("Prompt passes Adjectival Bound. Generating OSM...")

if __name__ == "__main__":
    run_viper_test()
