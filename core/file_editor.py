import os

class FileEditor:

    def create_file(self, filename):

        with open(filename, "w") as f:
            f.write("")

        return f"Created {filename}"

    def read_file(self, filename):

        if not os.path.exists(filename):
            return "File not found"

        with open(filename, "r") as f:
            return f.read()

    def delete_file(self, filename):

        if not os.path.exists(filename):
            return "File not found"

        os.remove(filename)

        return f"Deleted {filename}"
