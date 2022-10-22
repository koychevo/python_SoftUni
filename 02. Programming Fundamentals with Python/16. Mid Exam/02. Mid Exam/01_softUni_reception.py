first = int(input())
second = int(input())
third = int(input())
students_count = int(input())

time = 0

while students_count > 0:
    time += 1
    if time % 4 != 0:
        students_count -= first + second + third

print(f'Time needed: {time}h.')