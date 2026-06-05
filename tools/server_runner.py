import subprocess

class ServerRunner:

    def run_server(self, cmd):

        try:
            process = subprocess.Popen(
                cmd,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            stdout, stderr = process.communicate(timeout=5)

            return {
                "stdout": stdout,
                "stderr": stderr,
                "code": process.returncode
            }

        except subprocess.TimeoutExpired:
            return {
                "stdout": "server running (timeout reached)",
                "stderr": "",
                "code": 0
            }
