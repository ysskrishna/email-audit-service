from typing import List, Dict
from core.types import EmailData, RuleResult
from core.enums import RuleEnum
from ruleengine.rule_base import BaseRule
from ruleengine.rules.greeting_rule import GreetingRule


RULE_MAP: Dict[RuleEnum, BaseRule] = {
    RuleEnum.GREETING: GreetingRule(),
}

class RuleEngine:
    def run(self, email_data: EmailData, selected_rules: List[RuleEnum]) -> List[RuleResult]:
        results = []
        total_score = 0.0

        for selected_rule in selected_rules:
            rule = RULE_MAP[selected_rule]
            if not rule:
                raise ValueError(f"Rule {selected_rule} not found")
            
            result = rule.evaluate(email_data)
            total_score += result.score
            results.append(result)


        overall_score = total_score / len(results) if results else 0
        output = {
            "overall_score": round(overall_score * 100, 2),
            "passed": sum(1 for r in results if r.passed),
            "total_rules": len(results),
            "strengths": [r.rule_name for r in results if r.passed],
            "areas_to_improve": [r.rule_name for r in results if not r.passed],
            "results": results
        }
        return output 