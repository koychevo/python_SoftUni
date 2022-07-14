from sys import maxsize
count = int(input())
sum = 0
max_number = -maxsize

for i in range(count):
    number = int(input())
    sum += number
    if number > max_number:
        max_number = number

if sum - max_number == max_number:
    print("Yes");
    print(f"Sum = {max_number}")
else:
    print("No")
    print(f"Diff = {abs(sum - 2 * max_number) }")
