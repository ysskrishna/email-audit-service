from typing import List, Dict
from core.types import EmailData, RuleResult
from core.enums import RuleEnum
from ruleengine.rule_base import BaseRule
from ruleengine.rules.greeting_rule import GreetingRule
from ruleengine.rules.clarity_rule import ClarityRule
from ruleengine.rules.grammar_rule import GrammarRule
from ruleengine.rules.tone_rule import ToneRule


RULE_MAP: Dict[RuleEnum, BaseRule] = {
    RuleEnum.GREETING: GreetingRule(),
    RuleEnum.CLARITY: ClarityRule(),
    RuleEnum.GRAMMAR: GrammarRule(),
    RuleEnum.TONE: ToneRule(),
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

    @staticmethod
    def print_output(email_path: str, output: Dict):
        print("-" * 50)
        print(f"🔎 Audit Result for {email_path}: ")
        print(f"Overall Score: {output['overall_score']}%")
        print(f"Passed: {output['passed']}/{output['total_rules']}")
        print(f"Strengths: {output['strengths']}")
        print(f"Areas to Improve: {output['areas_to_improve']}")
        print(f"Results: {output['results']}")
        print("-" * 50)