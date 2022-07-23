number = int(input())

for row in range(number):
    line = ""
    for col in range(number):
        line += "*"
    print(line)