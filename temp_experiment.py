
import csv
from llm import ask

prompt = "Explain Artificial Intelligence in simple words with an example."

results = []

for temperature in [0, 1]:
    print(f"\nTesting Temperature: {temperature}")

    for attempt in range(1, 6):
        response = ask(
            prompt,
            temperature=temperature
        )

        print(f"Attempt {attempt}:")
        print(response)
        print("-" * 40)

        results.append({
            "temperature": temperature,
            "attempt": attempt,
            "response": response
        })


# Save results in CSV
with open("temperature_results.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["temperature", "attempt", "response"]
    )

    writer.writeheader()
    writer.writerows(results)

print("\nExperiment completed!")
print("Results saved in temperature_results.csv")
