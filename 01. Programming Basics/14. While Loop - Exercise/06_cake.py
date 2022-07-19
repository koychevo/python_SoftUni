cake_width = int(input())
cake_length = int(input())

cake_pieces_count = cake_length * cake_width

input_line = input()

while input_line != "STOP":
    current_pieces = int(input_line)
    cake_pieces_count -= current_pieces
    if cake_pieces_count <0:
        break
    input_line = input()

if cake_pieces_count < 0:
    print(f"No more cake left! You need {-cake_pieces_count} pieces more.")
else:
    print(f"{cake_pieces_count} pieces are left.")