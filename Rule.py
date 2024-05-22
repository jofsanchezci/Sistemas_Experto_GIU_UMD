class Rule:
    def __init__(self, condition, action):
        self.condition = condition
        self.action = action

    def evaluate(self, facts):
        if self.condition(facts):
            self.action(facts)
