import subprocess

class ShellTool:

    def run(self, cmd):

        try:

            result = subprocess.run(
                cmd,
                shell=True,
                capture_output=True,
                text=True
            )

            return result.stdout

        except Exception as e:
            return str(e)
