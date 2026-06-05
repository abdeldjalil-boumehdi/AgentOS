import subprocess

class RunnerTool:

    def run(self, command, cwd="."):

        try:
            result = subprocess.run(
                command,
                shell=True,
                cwd=cwd,
                text=True,
                capture_output=True
            )

            return {
                "stdout": result.stdout,
                "stderr": result.stderr,
                "code": result.returncode
            }

        except Exception as e:
            return {
                "stdout": "",
                "stderr": str(e),
                "code": -1
            }
