import math # [cite: 81]

#<<<<<<< HEAD
def square_root(a): math.sqrt(a)# raise ValueError if a < 0
def hypotenuse(a, b): math.hypot(a, b) # can have negative nums

def add(a, b): a + b
#=======
def add(a, b):
    return a + b # [cite: 82]
#>>>>>>> 6ab68f7e6d9f54edd08bab06b922f0fb69f2bbf9

def subtract(a, b):
    return a - b # [cite: 83, 85]

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

#<<<<<<< HEAD

#=======
def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid input for logarithm")
    return math.log(b, a)

def exp(a, b):
    return a ** b