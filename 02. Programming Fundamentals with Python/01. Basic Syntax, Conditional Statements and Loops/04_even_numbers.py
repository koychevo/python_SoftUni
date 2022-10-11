lines_count = int(input())

for _ in range(lines_count):
    number = int(input())
    if number % 2:
        print(f'{number} is odd!')
        break
else:
    print("All numbers are even.")