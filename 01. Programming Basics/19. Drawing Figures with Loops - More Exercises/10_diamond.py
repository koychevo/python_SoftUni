n = int(input())

middle = "*"
end = n // 2 + 1
if n % 2 == 0:
    middle += "*"
    end -= 1

if n < 3:
    print(middle)
    exit()

# upper part of the figure
for row in range(end):
    line = ""
    length = len(middle)
    for col in range((n - 1) // 2 - row):
        line += "-"
    if row == 0:
        line += middle
        line_length = len(line)
        for col in range(n - line_length):
            line += "-"
    else:
        line_length = len(line)
        line += "*"
        for col in range(n - 2 * line_length - 2):
            line += "-"
        line += "*"
        line_length = len(line)
        for col in range(n - line_length):
            line += "-"
    print(line)

# lower part of the figure
for row in range(end - 1):
    line = ""
    for col in range(row + 1):
        line += "-"
    if row == end - 2:
        line += middle
        line_length = len(line)
        for col in range(n - line_length):
            line += "-"
    else:
        line_length = len(line)
        line += "*"
        for col in range(n - 2 * line_length - 2):
            line += "-"
        line += "*"
        line_length = len(line)
        for col in range(n - line_length):
            line += "-"
    print(line)
