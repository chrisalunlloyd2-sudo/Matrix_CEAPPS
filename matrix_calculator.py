import sys
import json
import math

class MatrixCalculator:
    """
    KAI 9000: Agent-Ready Scientific Calculator
    Exposes advanced math functions to the orchestration layer.
    """
    def calculate(self, expression):
        try:
            # Safe evaluation with a limited global namespace
            allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
            result = eval(expression, {"__builtins__": {}}, allowed_names)
            return {"status": "success", "result": result}
        except Exception as e:
            return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    calc = MatrixCalculator()
    if len(sys.argv) > 1:
        expr = " ".join(sys.argv[1:])
        print(json.dumps(calc.calculate(expr)))
    else:
        print("Usage: python3 matrix_calculator.py 'math_expression'")
