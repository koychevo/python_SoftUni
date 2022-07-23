n = int(input())

for row in range(n):
    line = ""
    if row == 0 or row == n - 1:

        for col in range(2 * n):
            line += "*"
        for col in range(n):
            line += " "
        for col in range(2 * n):
            line += "*"

    else:
        line += "*"
        for col in range(2 * n - 2):
            line += "/"
        line += "*"
        for col in range(n):
            if row == (n - 1) // 2:
                line += "|"
            else:
                line += " "
        line += "*"
        for col in range(2 * n - 2):
            line += "/"
        line += "*"
    print(line)