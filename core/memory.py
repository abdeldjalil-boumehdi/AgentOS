import json
import os

class Memory:

    def __init__(self):
        self.path = "data/memory.json"

        if not os.path.exists("data"):
            os.makedirs("data")

        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump([], f)

    def save(self, item):

        with open(self.path, "r") as f:
            data = json.load(f)

        data.append(item)

        with open(self.path, "w") as f:
            json.dump(data, f, indent=2)

    def load(self):

        with open(self.path, "r") as f:
            return json.load(f)
