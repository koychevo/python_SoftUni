bake_count = int(input())

winner = ""
winner_points = 0

for i in range(bake_count):
    name = input()
    points = 0
    current_points = input()
    while current_points != "Stop":
        current_points = int(current_points)
        points += current_points
        current_points = input()
    print(f"{name} has {points} points.")
    if points > winner_points:
        winner_points = points
        winner = name
        print(f"{name} is the new number 1!")


print(f"{winner} won competition with {winner_points} points!")