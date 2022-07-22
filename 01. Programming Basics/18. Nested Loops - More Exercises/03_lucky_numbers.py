number = int(input())

result = ""

for first in range(1, 10):
    for second in range(1, 10):
        for third in range(1, 10):
            for forth in range(1, 10):
                if first + second == third + forth and number % (first + second) == 0:
                    result += str(first) + str(second) + str(third) + str(forth) + " "

print(result)