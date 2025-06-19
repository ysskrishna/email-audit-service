from abc import ABC, abstractmethod
from typing import Dict

class BaseRule(ABC):
    @abstractmethod
    def evaluate(self, email_data: Dict) -> Dict:
        """
        Evaluate the email against this rule
        
        Args:
            email_data: Dictionary containing parsed email data
            
        Returns:
            {                
                "rule_name": str,
                "passed": bool,
                "score": float,
                "justification": str
            }
        """
        pass 