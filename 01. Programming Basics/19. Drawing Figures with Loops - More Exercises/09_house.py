n = int(input())

middle = "*"

if n % 2 == 0:
    middle += "*"

for row in range((n + 1) // 2):
    length = len(middle)
    line = ""
    for col in range((n - length) // 2):
        line += "-"
    line += middle
    for col in range((n - length) // 2):
        line += "-"
    print(line)
    middle += "**"

for row in range( n // 2):
    line = "|"
    for col in range(n - 2):
        line += "*"
    line += "|"
    print(line)