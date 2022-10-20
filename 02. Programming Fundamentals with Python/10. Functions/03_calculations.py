def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a // b

def calculate(a, b, op):
    if op == 'add':
        return add(a, b)
    elif op == 'subtract':
        return subtract(a, b)
    elif op == 'multiply':
        return multiply(a, b)
    elif op == 'divide':
        return divide(a, b)

operator = input()
a = int(input())
b = int(input())

print(calculate(a, b, operator))
