
from llm import ask

try:
    answer = ask(
        prompt="What is Artificial Intelligence? Explain in 2 simple sentences.",
        temperature=0,
        max_tokens=100
    )

    print("\nGemini API Connection Successful!")
    print("Model Response:")
    print(answer)

except Exception as e:
    print("\nGemini API Connection Failed!")
    print("Error:", e)
