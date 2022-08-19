team_name = input()
games_count = int(input())

if games_count == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    win_count = 0
    lose_count = 0
    draw_count = 0
    scores = 0

    for game in range(games_count):
        current_score = input()
        if current_score == "W":
            win_count += 1
            scores += 3
        elif current_score == "D":
            draw_count += 1
            scores += 1
        else:
            lose_count += 1

    print(f"{team_name} has won {scores} points during this season.")
    print("Total stats:")
    print(f"## W: {win_count}")
    print(f"## D: {draw_count}")
    print(f"## L: {lose_count}")
    print(f"Win rate: {win_count / games_count * 100 :.2f}%")