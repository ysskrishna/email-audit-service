from typing import Dict
from ruleengine.rule_base import BaseRule
from core.enums import RuleEnum
from core.types import RuleResult, EmailData

class ToneRule(BaseRule):
    def evaluate(self, email_data: EmailData) -> RuleResult:
        """
        Check if the email maintains a professional and appropriate tone
        """
        body = email_data.body.lower()
        
        # Define tone indicators
        unprofessional_words = [
            'stupid', 'dumb', 'idiot', 'hate', 'terrible',
            'awful', 'rubbish', 'crap', 'nonsense', 'ridiculous'
        ]
        
        informal_expressions = [
            'lol', 'omg', 'wtf', 'btw', 'gonna', 'wanna',
            'ya', 'sup', 'lemme', 'gimme'
        ]
        
        # Count issues
        unprofessional_count = sum(word in body for word in unprofessional_words)
        informal_count = sum(expr in body for expr in informal_expressions)
        
        # Calculate tone score
        tone_score = 1.0 - (unprofessional_count * 0.3 + informal_count * 0.2)
        tone_score = max(0.0, min(1.0, tone_score))  # Clamp between 0 and 1
        
        passed = tone_score >= 0.8
        
        # Build justification message
        issues = []
        if unprofessional_count > 0:
            issues.append(f"found {unprofessional_count} unprofessional word(s)")
        if informal_count > 0:
            issues.append(f"found {informal_count} informal expression(s)")
            
        justification = "Email maintains a professional tone." if not issues else \
            f"Tone issues: {', '.join(issues)}"
        
        return RuleResult(
            rule_name=RuleEnum.TONE.value,
            passed=passed,
            score=tone_score,
            justification=justification
        ) 