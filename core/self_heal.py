class SelfHeal:

    def analyze_error(self, error_text: str):

        error_text = error_text.lower()

        # Syntax errors
        if "syntax error" in error_text:
            return "fix syntax"

        # Module errors
        if "no module named" in error_text:
            return "install missing dependency"

        # Import errors
        if "importerror" in error_text:
            return "fix import structure"

        # FastAPI specific
        if "uvicorn" in error_text or "address already in use" in error_text:
            return "fix server runtime issue"

        return "unknown runtime issue"
