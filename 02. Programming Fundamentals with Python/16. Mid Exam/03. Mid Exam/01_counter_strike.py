energy = int(input())

battle_won_count = 0

command = input()

while command != 'End of battle':
    distance = int(command)

    if distance <= energy:
        energy -= distance
        battle_won_count += 1
    else:
        print(f'Not enough energy! Game ends with {battle_won_count} won battles and {energy} energy')
        break
    if battle_won_count % 3 == 0:
        energy += battle_won_count

    command = input()
else:
    print(f'Won battles: {battle_won_count}. Energy left: {energy}')