from typing import Dict
import re
from ruleengine.rule_base import BaseRule
from core.enums import RuleEnum
from core.types import RuleResult, EmailData

class GrammarRule(BaseRule):
    def evaluate(self, email_data: EmailData) -> RuleResult:
        """
        Check for basic grammar issues in the email
        """
        body = email_data.body
        
        # Basic grammar checks
        grammar_issues = []
        
        # Check for double spaces
        if "  " in body:
            grammar_issues.append("double spaces")
            
        # Check for missing capitalization after periods
        sentences = re.split(r'[.!?]+\s+', body)
        for sentence in sentences[:-1]:  # Exclude last split which might be empty
            if sentence and sentence[0].islower():
                grammar_issues.append("missing capitalization")
                break
        
        # Check for common grammar mistakes
        common_mistakes = {
            "your welcome": "you're welcome",
            "their going": "they're going",
            "its a": "it's a",
            "cant": "can't",
            "dont": "don't",
            "im ": "I'm ",
        }
        
        for mistake, correction in common_mistakes.items():
            if mistake in body.lower():
                grammar_issues.append(f"incorrect usage of '{mistake}'")
        
        # Calculate score based on issues found
        score = 1.0 - (len(grammar_issues) * 0.2)
        score = max(0.0, min(1.0, score))  # Clamp between 0 and 1
        
        passed = score >= 0.8
        
        justification = "No grammar issues found." if not grammar_issues else \
            f"Grammar issues found: {', '.join(grammar_issues)}"
        
        return RuleResult(
            rule_name=RuleEnum.GRAMMAR.value,
            passed=passed,
            score=score,
            justification=justification
        ) 