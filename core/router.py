from core.agent import Agent

class AgentRouter:

    def __init__(self):
        self.agent = Agent()

    def handle(self, task):
        return self.agent.execute(task)
