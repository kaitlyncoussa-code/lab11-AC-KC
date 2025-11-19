"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
""" 
https://github.com/kaitlyncoussa-code/lab11-AC-KC.git
Partner 1: Angelina Coutsoukes
Partner2: Kaitlyn Coussa

"""
# First example
import math

def square_root(a):
    try:
        math.sqrt(a)
    except Exception as e:
        print("Whoopsies! Please try a valid input")
def hypotenuse(a, b):
    try:
        math.hypot(a, b)
    except Exception as e:
        print("Whoopsies! Please try a valid input")


def add(a, b):
    return a+b
def subtract(a, b):
    return a - b
def mul(a,b):
    return a*b
def div(a,b):
    try:
       return b/a
    except ZeroDivisionError:
        print("error")

def logarithm(a, b):
    try:
        math.log(b,a)# use math library/raise ValueError
    except ValueError:
        print("Whoopsies! Please try a valid input")


def exp(a,b):
    return a^b









