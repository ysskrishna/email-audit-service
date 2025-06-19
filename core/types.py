from dataclasses import dataclass
from typing import Literal, List, Optional

@dataclass
class RuleResult:
    rule_name: str
    passed: bool
    score: float  # Between 0 and 1
    justification: str

@dataclass
class EmailData:
    subject: Optional[str]
    from_: Optional[str]
    to: Optional[str]
    date: Optional[str]
    message_id: Optional[str]
    content_type: Optional[str]
    body: str
    attachments: List[str]
    sender: Optional[str]