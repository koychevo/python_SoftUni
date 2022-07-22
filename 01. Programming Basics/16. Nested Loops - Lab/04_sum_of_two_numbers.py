start = int(input())
end = int(input())
number = int(input())

is_found = False
combination_count = 0
first_nuber = start
second_number = start

for x in range(start, end+1):
    for y in range(start, end + 1):
        combination_count += 1
        if x + y == number:
            is_found = True
            first_nuber = x
            second_number = y
            break
    if is_found:
        break

if is_found:
    print(f"Combination N:{combination_count} ({first_nuber} + {second_number} = {number})")
else:
    print(f"{combination_count} combinations - neither equals {number}")