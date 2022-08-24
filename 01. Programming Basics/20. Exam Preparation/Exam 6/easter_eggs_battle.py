first_player_eggs_count = int(input())
second_player_eggs_count = int(input())

command = input()

while command != "End":
    if command == "one":
        second_player_eggs_count -= 1
        if second_player_eggs_count == 0:
            print(f"Player two is out of eggs. Player one has {first_player_eggs_count} eggs left.")
            break
    else:
        first_player_eggs_count -= 1
        if first_player_eggs_count == 0:
            print(f"Player one is out of eggs. Player two has {second_player_eggs_count} eggs left.")
            break
    command = input()

if command == "End":
    print(f"Player one has {first_player_eggs_count} eggs left.")
    print(f"Player two has {second_player_eggs_count} eggs left.")