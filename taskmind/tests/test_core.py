from taskmind.core import Rule, RuleEngine

def test_rule_engine_with_explain():
    engine = RuleEngine()

    rule = Rule(
        condition=lambda ctx: ctx["age"] >= 18,
        action=lambda ctx: "ALLOW",
        name="age_check"
    )

    engine.add_rule(rule)

    results, explanation = engine.run({"age": 20}, explain=True)

    assert "age_check" in results
    assert explanation is not None
    assert explanation.summary()[0]["rule"] == "age_check"
