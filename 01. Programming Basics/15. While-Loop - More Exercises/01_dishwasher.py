bottles_count = int(input())

detergent_count = 750 * bottles_count
turns = 0
dishes_count = 0
pots_count = 0

line = input()

while line != "End":
    turns += 1
    if turns % 3 == 0:
        current_pots_count = int(line)
        pots_count += current_pots_count
        detergent_count -= current_pots_count * 15
    else:
        current_dishes_count = int(line)
        dishes_count += current_dishes_count
        detergent_count -= current_dishes_count * 5
    if detergent_count < 0:
        break
    line = input()

if detergent_count < 0:
    print(f"Not enough detergent, {-detergent_count} ml. more necessary!")
else:
    print("Detergent was enough!")
    print(f"{dishes_count} dishes and {pots_count} pots were washed.")
    print(f"Leftover detergent {detergent_count} ml.")

