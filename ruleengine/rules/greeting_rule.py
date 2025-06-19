from typing import Dict
from ruleengine.rule_base import BaseRule
from core.enums import RuleEnum
from core.types import RuleResult

class GreetingRule(BaseRule):
    def evaluate(self, email_data: Dict) -> RuleResult:
        """
        Check if the email contains a proper greeting
        """
        body = email_data.get('body', '').lower()
        greeting_words = ['hi', 'hello', 'dear', 'good morning', 'good afternoon', 'good evening']

        if any(word in body for word in greeting_words):
            return RuleResult(
                rule_name=RuleEnum.GREETING.value,
                passed=True,
                score=1.0,
                justification='Email contains a proper greeting'
            )
        else:
            return RuleResult(
                rule_name=RuleEnum.GREETING.value,
                passed=False,
                score=0.0,
                justification='Email does not contain a proper greeting'
            )
        