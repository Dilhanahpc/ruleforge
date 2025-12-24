class Explanation:
    """
    Stores step-by-step reasoning of rule evaluation.
    """

    def __init__(self):
        self.steps = []

    def add_step(self, rule_name, condition_result):
        self.steps.append({
            "rule": rule_name,
            "result": condition_result
        })

    def summary(self):
        return self.steps
