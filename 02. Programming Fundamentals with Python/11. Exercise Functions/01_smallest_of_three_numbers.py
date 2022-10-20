def min_number(a, b, c):
    min = a
    if min > b:
        min = b
    if min > c:
        min = c
    return min

a = int(input())
b = int(input())
c = int(input())

print(min_number(a, b, c))