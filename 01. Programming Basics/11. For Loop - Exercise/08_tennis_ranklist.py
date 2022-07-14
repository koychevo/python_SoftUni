tournament_count = int(input())
points = int(input())

wins = 0
average_points = 0

for i in range(tournament_count):
    tournament_stage = input()
    if tournament_stage == "W":
        average_points += 2000
        wins += 1
    elif tournament_stage == "F":
        average_points += 1200
    elif tournament_stage == "SF":
        average_points += 720

points += average_points
average_points //= tournament_count

print(f"Final points: {points}")
print(f"Average points: {average_points}")
print(f"{wins * 100 / tournament_count:.2f}%")