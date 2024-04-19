from dataclasses import dataclass
from typing import Optional


@dataclass
class NotificationSummary:
    id: int
    event: int
    type: str
    message: str
    read: Optional[bool]
    created: Optional[str]
    unread_count: int
    read_ids: int
    read_all: Optional[bool]
