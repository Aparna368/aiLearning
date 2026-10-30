
# Decision Log

## Decision 2: Token Handling and Cost Estimation

**Date:** 30 October 2026

**Decision 1: Token Counting**

Used the `tiktoken` library to count tokens for English text, Hindi text, Python code, and numbers.

**Decision 2: Truncation**

Implemented token-based truncation to keep text within a specified token budget.

**Decision 3: Long Document Strategy**

For long documents, prefer chunking and retrieval (RAG) instead of blindly truncating the entire document.

**Decision 4: Cost Estimation**

Implemented a cost estimation function that reads input and output token prices from environment variables.

**Decision 5: Temperature Experiment**

The experiment was not completed because the GPT-5 endpoint rejected custom temperature values and the API account had no credits. No results were assumed or fabricated.
