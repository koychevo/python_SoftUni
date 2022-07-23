number = int(input())

for row in range(number):
    line = ""
    for col in range(number - row - 1):
        line += " "
    line += "*"
    for col in range(row):
        line += " *"
    print(line)

for row in range(number - 1):
    line = ""
    for col in range(row):
        line += " "
    for col in range(number - row - 1):
        line += " *"


    print(line)