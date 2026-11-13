from datetime import date
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator


class EmailFacts(BaseModel):
    model_config = ConfigDict(extra="forbid")

    category: Literal[
        "billing",
        "technical",
        "account",
        "feature_request",
        "other"
    ]

    urgency: Literal["low", "medium", "high"]

    sender_intent: str = Field(
        min_length=5,
        max_length=200,
        description="One sentence stating what the sender wants"
    )

    dates: list[str] = Field(
        description="Dates mentioned or implied, each as YYYY-MM-DD; empty list if none"
    )

    action_items: list[str] = Field(
        description="Short imperative tasks for our team; empty list if none"
    )

    @field_validator("dates")
    @classmethod
    def dates_must_be_iso(cls, values):
        for value in values:
            date.fromisoformat(value)
        return values

    @field_validator("action_items")
    @classmethod
    def items_not_empty(cls, values):
        if any(not item.strip() for item in values):
            raise ValueError("Action item must not be empty")
        return values