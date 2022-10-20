def sum_numbers(a, b):
    return a + b

def subtract(a, b):
    return a - b

def add_and_subtract(a, b, c):
    return subtract(sum_numbers(a, b), c)

first = int(input())
second = int(input())
third = int(input())

print(add_and_subtract(first, second, third))