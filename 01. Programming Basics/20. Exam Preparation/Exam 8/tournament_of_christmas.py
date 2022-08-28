days = int(input())
charity_sum = 0
win_days_count = 0


for day in range(days):
    day_charity_sum = 0
    win_games = 0
    lose_games = 0
    sport = input()
    while sport != "Finish":
        score = input()
        if score == "win":
            win_games += 1
            day_charity_sum += 20
        else:
            lose_games += 1

        sport = input()
    if win_games > lose_games:
        day_charity_sum *= 1.1
        win_days_count += 1
    charity_sum += day_charity_sum

if win_days_count > days / 2:
    charity_sum *= 1.2
    print(f"You won the tournament! Total raised money: {charity_sum:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {charity_sum:.2f}")