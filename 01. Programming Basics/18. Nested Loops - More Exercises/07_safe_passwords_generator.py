a = int(input())
b = int(input())
password_count = int(input())

combination_count = 0
is_max_password = False
result = ""
first = 35
second = 64

for x in range(1, a + 1):
    if is_max_password:
        break
    for y in range(1, b + 1):
        combination_count += 1
        if combination_count > password_count:
            is_max_password = True
            break
        result += chr(first) + chr(second) + str(x) + str(y) + chr(second) + chr(first) + "|"
        first += 1
        second += 1
        if first > 55:
            first = 35
        if second > 96:
            second = 64

print(result)
