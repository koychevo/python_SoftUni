number = int(input())

for row in range(number):
    line = ""
    for col in range(row+1):
        line += "$ "
    print(line)