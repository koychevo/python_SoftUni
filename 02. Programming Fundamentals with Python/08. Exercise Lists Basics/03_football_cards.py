team_a_count = 11
team_b_count = 11

team_a = []
team_b = []

cards = input().split(' ')

for i in range(len(cards)):
    if 'A' in cards[i] and cards[i] not in team_a:
        team_a_count -= 1
        team_a.append(cards[i])
    elif 'B' in cards[i] and cards[i] not in team_b:
        team_b_count -= 1
        team_b.append(cards[i])

    if team_a_count < 7 or team_b_count < 7:
        print(f'Team A - {team_a_count}; Team B - {team_b_count}')
        print('Game was terminated')
        break
else:
    print(f'Team A - {team_a_count}; Team B - {team_b_count}')


