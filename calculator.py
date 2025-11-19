"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math
def add(a, b): 
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    try:
       return b/a
    except ZeroDivisionError:
        print("error")

def log(a,b):
    try:
        return math.log(b,a)
    except ValueError:
        print("error")
def exp(a,b):
    return a^b


