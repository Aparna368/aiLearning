
import csv
import time
from pathlib import Path

from openai import RateLimitError
from emails_day03 import EMAILS
from classifier import classify


PROMPT_VARIANTS = ["zero_shot", "rules", "few_shot"]
CSV_FILE = Path("day03_results.csv")
WAIT_SECONDS = 15

FIELDNAMES = [
    "email_id",
    "variant",
    "actual_label",
    "predicted_label",
    "correct",
    "latency_s"
]


def save_results(results):
    """Save progress after every successful API call."""
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(results)


# Load previously completed results
if CSV_FILE.exists():
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
        results = list(csv.DictReader(file))
else:
    results = []

completed = {
    (int(row["email_id"]), row["variant"])
    for row in results
}

print(f"Already completed: {len(completed)} / 30")


stop_evaluation = False

for variant in PROMPT_VARIANTS:

    if stop_evaluation:
        break

    print(f"\n========== {variant.upper()} ==========")

    for email in EMAILS:

        key = (email["id"], variant)

        # Skip results already saved
        if key in completed:
            print(f"Email {email['id']}: Already completed. Skipping.")
            continue

        try:
            result = classify(
                email["text"],
                variant=variant
            )

        except RateLimitError:
            print("\nGemini API rate limit reached!")
            print("Your completed results are safely saved in the CSV.")
            print("Wait before running the script again.")
            stop_evaluation = True
            break

        predicted = result["label"]
        actual = email["label"]
        latency = result["latency_s"]
        is_correct = predicted == actual

        row = {
            "email_id": email["id"],
            "variant": variant,
            "actual_label": actual,
            "predicted_label": predicted,
            "correct": is_correct,
            "latency_s": latency
        }

        results.append(row)
        completed.add(key)

        # Save immediately after each successful call
        save_results(results)

        print(
            f"Email {email['id']}: "
            f"Actual={actual}, "
            f"Predicted={predicted}, "
            f"Correct={is_correct}"
        )

        # Wait before the next API request
        time.sleep(WAIT_SECONDS)

    # Show current accuracy for this variant
    variant_results = [
        row for row in results
        if row["variant"] == variant
    ]

    if variant_results:
        correct = sum(
            str(row["correct"]).lower() == "true"
            for row in variant_results
        )

        accuracy = correct / len(variant_results) * 100

        print(
            f"\nCurrent accuracy: {accuracy:.2f}% "
            f"({correct}/{len(variant_results)} completed)"
        )


print(f"\nTotal completed: {len(completed)} / 30")
print(f"Results saved in: {CSV_FILE}")

if len(completed) == 30:
    print("Evaluation completed successfully!")
else:
    print("Evaluation is incomplete. Run this script again later to resume.")
