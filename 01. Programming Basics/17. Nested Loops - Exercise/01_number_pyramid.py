number = int(input())

current_number = 1
row = 0

while current_number <= number:
    row += 1
    line = ""
    for col in range(row):
        line += str(current_number) + " "
        current_number += 1
        if current_number > number:
            break
    print(line)