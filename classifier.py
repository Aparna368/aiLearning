
from pathlib import Path
import time

from llm import ask


# Available categories
ALLOWED_LABELS = {
    "billing",
    "technical",
    "account",
    "feature_request",
    "other"
}


# Prompt files
PROMPT_DIR = Path(__file__).parent / "prompts"

PROMPT_FILES = {
    "zero_shot": "classify_zero_shot.txt",
    "rules": "classify_rules.txt",
    "few_shot": "classify_few_shot.txt"
}


def load_prompt(variant):
    """Load the selected prompt file."""

    if variant not in PROMPT_FILES:
        raise ValueError(f"Unknown prompt variant: {variant}")

    prompt_path = PROMPT_DIR / PROMPT_FILES[variant]

    return prompt_path.read_text(encoding="utf-8")


def classify(email_text, variant="zero_shot"):
    """Classify one customer email."""

    system_prompt = load_prompt(variant)

    user_message = f"""
<email>
{email_text}
</email>
"""

    start_time = time.time()

    raw_response = ask(
        prompt=user_message,
        system=system_prompt,
        temperature=0,
        max_tokens=20
    )

    latency = time.time() - start_time

    # Clean and validate response
    label = raw_response.strip().lower()

    if label not in ALLOWED_LABELS:
        label = "invalid"

    return {
        "label": label,
        "raw_response": raw_response,
        "latency_s": round(latency, 3)
    }



if __name__ == "__main__":

    test_email = (
        "I was charged twice for my October subscription. "
        "Please refund the extra payment."
    )

    for variant in ["zero_shot", "rules", "few_shot"]:

        result = classify(test_email, variant=variant)

        print(f"\nPrompt Style: {variant}")
        print(f"Label: {result['label']}")
        print(f"Latency: {result['latency_s']} seconds")
