from abc import ABC, abstractmethod
from typing import Dict
from core.types import RuleResult, EmailData

class BaseRule(ABC):
    @abstractmethod
    def evaluate(self, email_data: EmailData) -> RuleResult:
        """
        Evaluate the email against this rule
        
        Args:
            email_data: Dictionary containing parsed email data
            
        Returns:
            RuleResult object containing:
                - rule_name: str
                - passed: bool
                - score: float between 0 and 1
                - justification: str
        """
        pass 