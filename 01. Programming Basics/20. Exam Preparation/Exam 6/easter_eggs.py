eggs_count = int(input())

red_eggs_count = 0
orange_eggs_count = 0
blue_eggs_count = 0
green_egss_count = 0
max_eggs_count = 0
max_color = ""

for i in range(eggs_count):
    color = input()
    if color == "red":
        red_eggs_count += 1
    elif color == "orange":
        orange_eggs_count += 1
    elif color == "blue":
        blue_eggs_count += 1
    else:
        green_egss_count += 1

max_eggs_count = red_eggs_count
max_color = "red"

if orange_eggs_count > max_eggs_count:
    max_color = "orange"
    max_eggs_count = orange_eggs_count
if blue_eggs_count > max_eggs_count:
    max_color = "blue"
    max_eggs_count = blue_eggs_count
if green_egss_count > max_eggs_count:
    max_color = "green"
    max_eggs_count = green_egss_count

print(f"Red eggs: {red_eggs_count}")
print(f"Orange eggs: {orange_eggs_count}")
print(f"Blue eggs: {blue_eggs_count}")
print(f"Green eggs: {green_egss_count}")
print(f"Max eggs: {max_eggs_count} -> {max_color}")