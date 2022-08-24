balls_count = int(input())

points = 0
red_balls_count = 0
orange_balls_count = 0
yellow_balls_count = 0
white_balls_count = 0
black_balls_count = 0
other_balls_count = 0

for ball in range(balls_count):
    current_color = input()
    if current_color == "red":
        red_balls_count += 1
        points += 5
    elif current_color == "orange":
        orange_balls_count += 1
        points += 10
    elif current_color == "yellow":
        yellow_balls_count += 1
        points += 15
    elif current_color == "white":
        white_balls_count += 1
        points += 20
    elif current_color == "black":
        black_balls_count += 1
        points //= 2
    else:
        other_balls_count += 1

print(f"Total points: {points}")
print(f"Red balls: {red_balls_count}")
print(f"Orange balls: {orange_balls_count}")
print(f"Yellow balls: {yellow_balls_count}")
print(f"White balls: {white_balls_count}")
print(f"Other colors picked: {other_balls_count}")
print(f"Divides from black balls: {black_balls_count}")