number = int(input())

for num in range(1, number + 1):
    sum = 0
    current_num = str(num)
    for i in range(len(current_num)):
        sum += int(current_num[i])
    if sum in [5, 7, 11]:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')