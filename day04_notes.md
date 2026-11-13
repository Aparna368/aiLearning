# Day 4 - Structured Output and Email Extraction

## Objective
Build an email fact extraction pipeline using Gemini
and validate structured JSON output using Pydantic.

## What I learned
- Structured JSON output
- JSON mode
- Pydantic model validation
- JSONL file processing
- Error logging
- First-try validity measurement
- API latency measurement

## Dataset
Total emails processed: 20

## Results

| Metric | Result |
|---|---:|
| Total emails | 20 |
| Valid results | 17 |
| Failed results | 3 |
| First-try validity | 85% |
| Average latency | 10.86 seconds |

## Files created
- extract.py
- data/emails.jsonl
- results_day04.jsonl
- failures.md
- models.py

## Challenges
Gemini API returned 429 errors for some requests
because of rate limiting.

## Learning
Valid JSON does not automatically mean semantically
correct data. Pydantic validates structure and rules,
while manual review checks extraction quality.

## Next Step
Day 5 - Error Handling, Retries and Backoff.
## Decision 4 - Structured Output

Used Gemini JSON mode with Pydantic validation
to extract structured facts from emails.

Reason:
Structured output makes extracted data easier
to validate and use in applications.

Result:
Achieved 85% first-try validity on 20 emails.