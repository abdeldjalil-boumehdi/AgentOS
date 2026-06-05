class Planner:

    def create_plan(self, goal: str):

        goal = goal.lower()

        if "fastapi" in goal and "auth" in goal:

            return [
                "create project structure",
                "build authentication module",
                "create user model",
                "create API routes",
                "run project",
                "fix errors"
            ]

        if "fastapi" in goal:

            return [
                "create project structure",
                "create main API file",
                "create routes",
                "run project",
                "validate output"
            ]

        return ["analyze", "build", "validate"]
