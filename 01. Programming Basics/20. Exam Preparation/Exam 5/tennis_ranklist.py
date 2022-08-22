tournaments_count = int(input())
points = int(input())

won_tournaments_count = 0
average_points = 0

for i in range(tournaments_count):
    stage = input()
    if stage == "W":
        average_points += 2000
        won_tournaments_count += 1
    elif stage == "F":
        average_points += 1200
    else:
        average_points += 720

print(f"Final points: {points + average_points}")
print(f"Average points: {average_points // tournaments_count}")
print(f"{won_tournaments_count / tournaments_count * 100 :.2f}%")