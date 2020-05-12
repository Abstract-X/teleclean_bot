from dataclasses import dataclass


@dataclass()
class CleaningReport:

    chat_name: str
    chat_id: int
    amount_messages: int
