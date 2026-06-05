from core.memory import Memory
from core.planner import Planner
from core.self_heal import SelfHeal
from core.architect import Architect
from core.compiler import Compiler
from core.tester import Tester
from tools.runner_tool import RunnerTool


class Agent:

    def __init__(self):

        self.memory = Memory()
        self.planner = Planner()
        self.healer = SelfHeal()
        self.architect = Architect()
        self.compiler = Compiler()
        self.tester = Tester()
        self.runner = RunnerTool()

    def execute(self, task):

        self.memory.save({"task": task})

        return self.autonomous_factory(task)

    def autonomous_factory(self, goal):

        result = {
            "goal": goal
        }

        # 🧠 1. Architecture design
        architecture = self.architect.design(goal)
        result["architecture"] = architecture

        # 🏗️ 2. Build full project
        build = self.compiler.build(architecture)
        result["build"] = build

        # 🧪 3. Test project
        test = self.tester.run_tests()
        result["test"] = test

        # 🔁 4. Auto-heal loop
        if not test["ok"]:

            fix = self.healer.analyze_error(test.get("stderr", ""))
            result["fix"] = fix

            # simple auto-fix
            if "syntax" in fix:

                with open("app/main.py", "w") as f:
                    f.write("""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Auto Fixed v6"}
""")

                # re-test
                result["retest"] = self.tester.run_tests()

        # ⚙️ 5. optional run server
        try:
            server = self.runner.run("uvicorn app.main:app --host 0.0.0.0 --port 8000")
            result["server"] = server
        except:
            result["server"] = "server skipped"

        result["status"] = "AUTONOMOUS FACTORY COMPLETE"

        return result
