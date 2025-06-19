from typing import Dict
from ruleengine.rule_base import BaseRule
from core.enums import RuleEnum
from core.types import RuleResult, EmailData

class ClarityRule(BaseRule):
    def evaluate(self, email_data: EmailData) -> RuleResult:
        """
        Check if the email is clear and concise
        """
        body = email_data.body.lower()
        
        # Check for common clarity indicators
        unclear_phrases = ['not sure if', 'maybe', 'kind of', 'sort of', 'i think', 'possibly']
        long_sentence_threshold = 30  # words
        
        # Count unclear phrases
        unclear_count = sum(phrase in body for phrase in unclear_phrases)
        
        # Check sentence length
        sentences = [s.strip() for s in body.split('.') if s.strip()]
        long_sentences = sum(len(s.split()) > long_sentence_threshold for s in sentences)
        
        # Calculate clarity score
        total_sentences = len(sentences) or 1  # Avoid division by zero
        clarity_score = 1.0 - (unclear_count * 0.2 + long_sentences/total_sentences * 0.3)
        clarity_score = max(0.0, min(1.0, clarity_score))  # Clamp between 0 and 1
        
        passed = clarity_score >= 0.7
        
        return RuleResult(
            rule_name=RuleEnum.CLARITY.value,
            passed=passed,
            score=clarity_score,
            justification=f'Email {"is" if passed else "is not"} sufficiently clear. Found {unclear_count} unclear phrases and {long_sentences} long sentences.'
        ) 