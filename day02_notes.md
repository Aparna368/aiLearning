
# Day 2 Notes: Tokens, Context Window and Temperature

## 1. What are Tokens?
Tokens are small pieces of text processed by an AI model. A token can be a word, part of a word, number, or punctuation.

## 2. Context Window
The context window is the maximum amount of tokens a model can process in one request, including input and output.

If the context window is exceeded, some content may need to be removed or shortened.

## 3. Tokenization
Different types of text produce different token counts. English, Hindi, Python code, and numbers may tokenize differently.

## 4. Truncation
Truncation means cutting text to fit within a specified token budget.

For long documents, chunking and retrieval (RAG) can help preserve relevant information instead of simply removing content.

## 5. Temperature
Temperature controls the randomness of model responses.

- Lower temperature: generally more predictable responses.
- Higher temperature: generally more varied responses.

Experiment status: Blocked because the GPT-5 endpoint did not support the requested custom temperature setting, and the API account had no remaining credits. No experimental results were fabricated.

## 6. Cost Estimation
API cost depends on input tokens and output tokens.

Formula:

Cost = (Input Tokens × Input Price + Output Tokens × Output Price) / 1,000,000

Prices are read from the `.env` file.

## 7. Key Learning
- Learned how to count tokens using tiktoken.
- Implemented token-based truncation.
- Tested token budgets of 5, 20, and 100.
- Implemented API cost estimation.
- Understood why chunking and retrieval are useful for long documents.
