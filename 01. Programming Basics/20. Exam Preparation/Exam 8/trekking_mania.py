groups_count = int(input())

first_type_group_count = 0
second_type_group_count = 0
third_type_group_count = 0
forth_type_group_count = 0
fifth_type_group_count = 0

for group in range(groups_count):
    current_group = int(input())
    if current_group <= 5:
        first_type_group_count += current_group
    elif current_group <= 12:
        second_type_group_count += current_group
    elif current_group <= 25:
        third_type_group_count += current_group
    elif current_group <= 40:
        forth_type_group_count += current_group
    else:
        fifth_type_group_count += current_group

total_group_count = first_type_group_count + second_type_group_count + third_type_group_count + forth_type_group_count + fifth_type_group_count

print(f"{first_type_group_count / total_group_count * 100 :.2f}%")
print(f"{second_type_group_count / total_group_count * 100 :.2f}%")
print(f"{third_type_group_count / total_group_count * 100 :.2f}%")
print(f"{forth_type_group_count / total_group_count * 100 :.2f}%")
print(f"{fifth_type_group_count / total_group_count * 100 :.2f}%")