# https://github.com/Azurephire/Lab11-CPR-ND
# Partner 1: Nicholas Di Grazia
# Partner 2: Camila Perez Ramirez

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

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
