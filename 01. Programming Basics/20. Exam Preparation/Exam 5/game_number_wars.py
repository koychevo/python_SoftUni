name_first_player = input()
name_second_player = input()

score_first_player = 0
score_second_player = 0
is_number_wars = False

input_line = input()

while input_line != "End of game":
    card_first_player = int(input_line)
    card_second_player = int(input())
    if card_first_player > card_second_player:
        if is_number_wars:
            print(f"{name_first_player} is winner with {score_first_player} points")
            break
        score_first_player += card_first_player - card_second_player
    elif card_first_player < card_second_player:
        if is_number_wars:
            print(f"{name_second_player} is winner with {score_second_player} points")
            break
        score_second_player += card_second_player - card_first_player
    else:
        print("Number wars!")
        is_number_wars = True
    input_line = input()

if input_line == "End of game":
    print(f"{name_first_player} has {score_first_player} points")
    print(f"{name_second_player} has {score_second_player} points")