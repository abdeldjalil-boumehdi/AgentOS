class Architect:

    def design(self, goal: str):

        goal = goal.lower()

        if "fastapi" in goal and "auth" in goal:

            return {
                "type": "web_api",
                "stack": ["fastapi", "pydantic"],
                "modules": ["auth", "users", "database"],
                "structure": [
                    "app/main.py",
                    "app/api/auth.py",
                    "app/api/users.py",
                    "app/core/security.py",
                    "app/models/user.py"
                ]
            }

        if "fastapi" in goal:

            return {
                "type": "web_api",
                "stack": ["fastapi"],
                "modules": ["core"],
                "structure": [
                    "app/main.py"
                ]
            }

        return {
            "type": "generic",
            "structure": ["main.py"]
        }
