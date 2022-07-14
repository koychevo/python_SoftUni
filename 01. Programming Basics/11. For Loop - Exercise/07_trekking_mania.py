groups_count = int(input())

first_group_count = 0
second_group_count = 0
third_group_count = 0
forth_group_count = 0
fifth_group_count = 0

for i in range(groups_count):
    people = int(input())
    if people <= 5:
        first_group_count += people
    elif people <= 12:
        second_group_count += people
    elif people <= 25:
        third_group_count += people
    elif people <= 40:
        forth_group_count += people
    else:
        fifth_group_count += people

all_people_count = first_group_count + second_group_count + third_group_count + forth_group_count + fifth_group_count

print(f"{first_group_count / all_people_count * 100 :.2f}%")
print(f"{second_group_count / all_people_count * 100 :.2f}%")
print(f"{third_group_count / all_people_count * 100 :.2f}%")
print(f"{forth_group_count / all_people_count * 100 :.2f}%")
print(f"{fifth_group_count / all_people_count * 100 :.2f}%")