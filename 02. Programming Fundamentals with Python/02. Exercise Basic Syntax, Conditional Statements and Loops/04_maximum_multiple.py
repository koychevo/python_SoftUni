divisor = int(input())
boundary = int(input())
max_num = 1

for num in range(divisor, boundary + 1):
    if num % divisor == 0:
        max_num = num

print(max_num)