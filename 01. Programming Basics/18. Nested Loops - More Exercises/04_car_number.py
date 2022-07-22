start = int(input())
end = int(input()) + 1

result = ""

for first in range(start, end):
    for second in range(start, end):
        for third in range(start, end):
            for forth in range(start, first):
                if (second + third) % 2 == 0 and ((first % 2 == 0 and forth % 2 != 0) or (first % 2 != 0 and forth % 2 == 0)):
                    result += str(first) + str(second) + str(third) + str(forth) + " "

print(result)