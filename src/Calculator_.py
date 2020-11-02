import math


def addition(a, b):
    a = int(a)
    b = int(b)
    c = a + b
    return c

def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = b - a
    return c

def multiplication(a, b):
    a = int(a)
    b = int(b)
    c = a * b
    return c


class Calculator:
    result = 0

def __init__(self):
    pass

def addit(self, a, b):
    self.result = addition(a, b)
    return self.result

def subt(self, a, b):
        self.result = subtraction(a, b)
        return self.result

def multi(self, a, b):
        self.result = multiplication(a, b)
        return self.result