import json
import os

class TaskManager:

    def __init__(self):

        self.path = "data/tasks.json"

        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump([], f)

    def add(self, task):

        with open(self.path) as f:
            data = json.load(f)

        data.append(task)

        with open(self.path, "w") as f:
            json.dump(data, f, indent=2)
