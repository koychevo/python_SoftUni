places_count = int(input())

income = 0
input_line = input()

while input_line != "Movie time!":
    people = int(input_line)
    if people > places_count:
        break
    current_income = people * 5
    if people % 3 == 0:
        current_income -= 5
    income += current_income
    places_count -= people
    input_line = input()

if input_line == "Movie time!":
    print(f"There are {places_count} seats left in the cinema.")
else:
    print("The cinema is full.")

print(f"Cinema income - {income} lv.")