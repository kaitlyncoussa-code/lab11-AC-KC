"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b):
    a + b

def subtract(a, b):
    a - b

def multiply(a, b):
    a * b

def divide(a, b):
    if a ==0:
        print("Whoopsies! Please enter a number that is not 0")
        return
    else:
        b / a   # raise ZeroDivisionError if a == 0

def logarithm(a, b):
    if a<=0:
        print("Whoopsies! Please enter a number that is greater than 0")
        return
    if b<=0:
        print("Whoopsies! Please enter a number that is greater than 0")
        return
    math.log(b,a)# use math library/raise ValueError

def exponent(a, b):
    a**b



