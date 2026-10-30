
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()


def ask(
    prompt: str,
    system: str = "You are a helpful and concise AI assistant.",
    max_tokens: int = 150,
    temperature: float = 1
) -> str:

    response = client.chat.completions.create(
        model=os.getenv("MODEL_NAME"),
        messages=[
            {
                "role": "system",
                "content": system
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_completion_tokens=max_tokens
    )

    return response.choices[0].message.content or ""
