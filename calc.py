# app/calculator.py

def calculate(operator: str, a: float, b: float) -> float:
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            raise ZeroDivisionError("division par zéro interdite.")
        return a / b
    else:
        raise ValueError(f"{operator} n'est pas un opérateur valide.")

