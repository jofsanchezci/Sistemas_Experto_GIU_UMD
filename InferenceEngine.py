class InferenceEngine:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def run(self):
        self.knowledge_base.evaluate()
