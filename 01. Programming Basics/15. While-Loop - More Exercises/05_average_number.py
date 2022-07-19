n = int(input())

average_number  = 0
count = 0

while count < n:
    number = int(input())
    average_number += number
    count += 1

print(f"{average_number / n :.2f}")
