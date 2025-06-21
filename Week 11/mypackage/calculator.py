import math


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    return a ** b

def root(a, n):
    if a < 0 and n % 2 == 0:
        raise ValueError("Cannot take even root of negative number")
    return a ** (1 / n)

def sine(degrees):
    radians = math.radians(degrees)
    return math.sin(radians)

def cosine(degrees):
    radians = math.radians(degrees)
    return math.cos(radians)

def tangent(degrees):
    if degrees % 180 == 90:
        raise ValueError("Tangent undefined at 90 degrees")
    radians = math.radians(degrees)
    return math.tan(radians)