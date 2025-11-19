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


def add(a, b):
    a + b

def subtract(a, b):
    a - b

def multiply(a, b):
    a * b



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




