tournament = input()

wons_count = 0
losts_counts = 0

while tournament != "End of tournaments":
    games_count = int(input())
    for game in range(1, games_count + 1):
        our_points = int(input())
        opponent_points = int(input())
        if our_points > opponent_points:
            print(f"Game {game} of tournament {tournament}: win with {our_points - opponent_points} points.")
            wons_count += 1
        else:
            print(f"Game {game} of tournament {tournament}: lost with {opponent_points - our_points} points.")
            losts_counts += 1
    tournament = input()

print(f"{wons_count / (wons_count + losts_counts) * 100 :.2f}% matches win")
print(f"{losts_counts / (wons_count + losts_counts) * 100 :.2f}% matches lost")