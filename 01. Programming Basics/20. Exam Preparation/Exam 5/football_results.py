won_games_count = 0
lost_games_count = 0
draw_games_count = 0

for i in range(3):
    score = input()
    host_goals = int(score[0])
    guest_goals = int(score[2])
    if host_goals > guest_goals:
        won_games_count += 1
    elif host_goals < guest_goals:
        lost_games_count += 1
    else:
        draw_games_count += 1

print(f"Team won {won_games_count} games.")
print(f"Team lost {lost_games_count} games.")
print(f"Drawn games: {draw_games_count}")