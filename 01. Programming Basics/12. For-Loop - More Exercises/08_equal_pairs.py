couple_numbers_count = int(input())

sum = 0
max_diff = 0

for i in range(couple_numbers_count):
    first_number = int(input())
    second_number = int(input())
    current_sum = first_number + second_number
    if i != 0 and abs(sum - current_sum) > max_diff:
        max_diff = abs(sum - current_sum)
    sum = current_sum

if max_diff != 0:
    print(f"No, maxdiff={max_diff}")
else:
    print(f"Yes, value={sum}")
