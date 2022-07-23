number = int(input())

for row in range(number + 1):
    line = ""
    for col in range(number - row):
        line += " "
    for col in range(row):
        line += "*"
    line += " | "
    for col in range(row):
        line += "*"
    print(line)