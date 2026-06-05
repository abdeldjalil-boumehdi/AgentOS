import subprocess

class Tester:

    def run_tests(self):

        try:
            result = subprocess.run(
                "python -m py_compile app/main.py",
                shell=True,
                capture_output=True,
                text=True
            )

            return {
                "ok": result.returncode == 0,
                "stderr": result.stderr
            }

        except Exception as e:
            return {"ok": False, "error": str(e)}
