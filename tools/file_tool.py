import os

class FileTool:

    def create(self, file):

        with open(file, "w") as f:
            f.write("")

        return f"created {file}"

    def write(self, file, content):

        with open(file, "w") as f:
            f.write(content)

        return f"written {file}"

    def read(self, file):

        if not os.path.exists(file):
            return "not found"

        with open(file) as f:
            return f.read()
