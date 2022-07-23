number = int(input())

for row in range(number):
    line = ""
    for col in range(number):
        if col == 0 or col == number - 1:
            if row == 0 or row == number - 1:
                line += "+ "
            else:
                line += "| "
        else:
            line += "- "
    print(line)