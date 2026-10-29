
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model=os.getenv("MODEL_NAME"),
    messages=[
        {
            "role": "system",
            "content": "You are a concise technical mentor."
        },
        {
            "role": "user",
            "content": "Explain what an API is in two sentences."
        }
    ],
  max_completion_tokens=150
)

print(response.choices[0].message.content)
print("Finish reason:", response.choices[0].finish_reason)

usage = response.usage
print("Input tokens:", usage.prompt_tokens)
print("Output tokens:", usage.completion_tokens)
print("Total tokens:", usage.total_tokens)
