start = int(input())
end = int(input()) + 1
magic_number = int(input())

combination_count = 0
found_combination_place = -1
first_num = second_num = 0

for first_number in range(start, end):
    if found_combination_place > 0:
        break
    for second_number in range(start, end):
        combination_count += 1
        if first_number + second_number == magic_number:
            found_combination_place = combination_count
            first_num = first_number
            second_num = second_number
            break

if found_combination_place > 0:
    print(f"Combination N:{combination_count} ({first_num} + {second_num} = {magic_number})")
else:
    print(f"{combination_count} combinations - neither equals {magic_number}")