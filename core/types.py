from dataclasses import dataclass
from typing import Literal

@dataclass
class RuleResult:
    rule_name: str
    passed: bool
    score: float  # Between 0 and 1
    justification: str