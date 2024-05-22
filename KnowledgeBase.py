class KnowledgeBase:
    def __init__(self):
        self.facts = {}
        self.rules = []

    def add_fact(self, key, value):
        self.facts[key] = value

    def add_rule(self, rule):
        self.rules.append(rule)

    def evaluate(self):
        for rule in self.rules:
            rule.evaluate(self.facts)
