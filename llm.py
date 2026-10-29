
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()


def ask(prompt: str) -> str:
    response = client.chat.completions.create(
        model=os.getenv("MODEL_NAME"),
        messages=[
            {
                "role": "system",
                "content": "You are a helpful and concise AI assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_completion_tokens=150
    )

    return response.choices[0].message.content or ""
