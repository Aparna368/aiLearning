
import os
import tiktoken
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# -----------------------------------
# 1. Tokenizer Setup
# -----------------------------------

MODEL_NAME = os.getenv("MODEL_NAME", "")

try:
    ENCODING = tiktoken.encoding_for_model(MODEL_NAME)
except KeyError:
    ENCODING = tiktoken.get_encoding("cl100k_base")


# -----------------------------------
# 2. Token Counter
# -----------------------------------

def count_tokens(text: str) -> int:
    tokens = ENCODING.encode(text)
    return len(tokens)


# -----------------------------------
# 3. Truncation Function
# -----------------------------------

def truncate(text: str, max_tokens: int) -> str:

    if max_tokens < 0:
        raise ValueError("max_tokens cannot be negative")

    tokens = ENCODING.encode(text)

    if len(tokens) <= max_tokens:
        return text

    cut = ENCODING.decode(tokens[:max_tokens]).rstrip("\ufffd")

    # Avoid cutting in the middle of a word
    next_char = text[len(cut):len(cut) + 1]

    if next_char and not next_char.isspace() and " " in cut:
        cut = cut.rsplit(None, 1)[0]

    return cut.rstrip()


# -----------------------------------
# 4. Cost Estimation
# -----------------------------------

def estimate_cost(input_tokens: int, output_tokens: int) -> float:

    p_in = float(os.getenv("PRICE_IN_PER_M", "0"))
    p_out = float(os.getenv("PRICE_OUT_PER_M", "0"))

    cost = (
        input_tokens * p_in +
        output_tokens * p_out
    ) / 1_000_000

    return cost


# -----------------------------------
# 5. Run Tests
# -----------------------------------

if __name__ == "__main__":

    samples = {
        "Short English": "Hello, how are you today?",
        "Long English": (
            "Retrieval-Augmented Generation reduces "
            "hallucinations by grounding answers in documents. "
        ) * 5,
        "Python Code": "def add(a, b):\n    return a + b\n",
        "Hindi": "मुझे कृत्रिम बुद्धिमत्ता सीखनी है",
        "Numbers and IDs": "Invoice INV-2026-004517 total 1,234,567.89 INR"
    }

    print("\n========== TOKEN COUNTER ==========\n")

    print(f"{'Text':<20}{'Characters':>12}{'Tokens':>10}")

    for name, sample in samples.items():
        token_count = count_tokens(sample)

        print(
            f"{name:<20}"
            f"{len(sample):>12}"
            f"{token_count:>10}"
        )

    # -----------------------------------
    # Truncation Tests
    # -----------------------------------

    print("\n========== TRUNCATION TEST ==========\n")

    long_text = "The quick brown fox jumps over the lazy dog. " * 200

    for budget in (5, 20, 100):

        output = truncate(long_text, budget)

        assert count_tokens(output) <= budget
        assert not output.endswith("qui")

        print(
            budget,
            "->",
            count_tokens(output),
            "tokens |",
            output[-30:]
        )

    assert truncate("short text", 100) == "short text"

    print("\nAll truncation tests passed!")

    # -----------------------------------
    # Cost Estimation Test
    # -----------------------------------

    print("\n========== COST ESTIMATION ==========\n")

    test_cost = estimate_cost(
        input_tokens=1_000_000,
        output_tokens=0
    )

    print("Cost for 1 million input tokens:", test_cost)

    print("\nDay 2 token tests completed!")
