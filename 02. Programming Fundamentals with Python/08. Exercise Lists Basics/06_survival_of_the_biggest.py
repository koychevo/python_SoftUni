from sys import maxsize

numbers = [int(x) for x in input().split(' ')]
count = int(input())

for _ in range(count):
    min_num = maxsize
    for num in numbers:
        if min_num > num:
            min_num = num
    numbers.remove(min_num)

print(', '.join([str(num) for num in numbers]))
