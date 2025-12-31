from taskmind import RuleEngine, parse_rule

engine = RuleEngine()
engine.add_rule(parse_rule("IF age < 18 THEN DENY PRIORITY 100"))

result = engine.run({"age": 16}, explain=True)
print(result)
