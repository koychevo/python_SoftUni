from sys import maxsize

n = int(input())
min_number = maxsize
max_number = -maxsize

for i in range(n):
    number = int(input())
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
