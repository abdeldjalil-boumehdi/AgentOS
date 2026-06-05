import os

class ProjectBuilder:

    def create_structure(self, name):

        folders = [
            name,
            f"{name}/core",
            f"{name}/api",
            f"{name}/models"
        ]

        for f in folders:
            os.makedirs(f, exist_ok=True)

        return f"Project {name} structure created"
