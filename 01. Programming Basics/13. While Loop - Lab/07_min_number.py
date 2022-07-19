from sys import maxsize

min_number = maxsize
line = input()

while line != "Stop":
    number = int(line)
    if number < min_number:
        min_number = number
    line = input()

print(min_number)