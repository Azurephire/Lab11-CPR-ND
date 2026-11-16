"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

<<<<<<< HEAD
def square_root(a):
    if a < 0:
        raise ValueError()
    else:
        return math.sqrt(a)

def hypotenuse(a, b):
    math.hypot(a, b)
=======
# First example

def square_root(a):
    try:
        if a < 0:
            raise ValueError
        return math.sqrt(a)
    except ValueError:
        raise ValueError

def hypotenuse(a, b):
    try:
        h = math.hypot(a, b)
        if h < 0:
            raise ValueError
        return h
    except ValueError:
        raise ValueError
>>>>>>> d28770415fc0069c676196a4579ded2d7c9ff452

def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    if b < 1 or a == 1 or a <= 0:
        raise ValueError
    return math.log(b, a)

def log(a,b):
    if b < 1 or a == 1 or a <= 0:
        raise ValueError
    else:
        return math.log(a, b)

def exp(a,b):
    return a ** b
