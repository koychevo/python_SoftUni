lines_count = int(input())
tank_capacity = 255
total_water = 0

for _ in range(lines_count):
    current_water = int(input())
    if current_water + total_water > tank_capacity:
        print('Insufficient capacity!')
    else:
        total_water += current_water

print(total_water)