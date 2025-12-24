from taskmind.explain import Explanation


class Rule:
    def __init__(self, condition, action, name=None):
        self.condition = condition
        self.action = action
        self.name = name or action.__name__

    def evaluate(self, context):
        return self.condition(context)


class RuleEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule: Rule):
        self.rules.append(rule)

    def run(self, context, explain=False):
        explanation = Explanation() if explain else None
        results = []

        for rule in self.rules:
            result = rule.evaluate(context)

            if explain:
                explanation.add_step(rule.name, result)

            if result:
                results.append(rule.name)

        return results, explanation
