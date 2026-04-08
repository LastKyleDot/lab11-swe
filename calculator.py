import math # [cite: 81]

def add(a, b):
    return a + b # [cite: 82]

def sub(a, b):
    return a - b # [cite: 83, 85]

def mul(a, b):
    return a * b # [cite: 86, 88]

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero") # [cite: 91]
    return b / a # [cite: 89, 91]

def log(a, b):
    # log base a of b [cite: 94]
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid input for logarithm") # [cite: 94]
    return math.log(b, a) # [cite: 94]

def exp(a, b):
    return a ** b # [cite: 95]