n = int(input())
l = int(input())
line = ""

for a in range(1, n):
    for b in range(1, n):
        for c in range(97, 97 + l):
            for d in range(97, 97 + l):
                for e in range(max(a, b) + 1, n + 1):
                    line += str(a) + str(b) + chr(c) + chr(d) + str(e) + " "

print(line)
