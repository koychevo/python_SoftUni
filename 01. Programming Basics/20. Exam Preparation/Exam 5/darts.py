player_name = input()

points = 301
successful_shots = 0
unsuccessful_shots = 0


while points != 0:
    field = input()
    if field == "Retire":
        break
    current_points = int(input())
    if field == "Double":
        current_points *= 2
    elif field == "Triple":
        current_points *= 3
    if current_points <= points:
        points -= current_points
        successful_shots += 1
    else:
        unsuccessful_shots += 1

if points > 0:
    print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")
else:
    print(f"{player_name} won the leg with {successful_shots} shots.")