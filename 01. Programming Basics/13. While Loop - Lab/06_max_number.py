from sys import maxsize

max_number = -maxsize

number = input()

while number != "Stop":
    number = int(number)
    if number > max_number:
        max_number = number
    number = input()

print(max_number)