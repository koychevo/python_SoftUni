lines_count = int(input())
word = input()

strings = []

for _ in range(lines_count):
    strings.append(input())

print(strings)

for i in range(len(strings) - 1, -1, -1):
    if word not in strings[i]:
        strings.remove(strings[i])

print(strings)
