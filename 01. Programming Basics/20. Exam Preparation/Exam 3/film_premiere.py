movie = input()
consumption = input()
tickets_count = int(input())
price = 0

if movie == "John Wick":
    if consumption == "Drink":
        price = 12
    elif consumption == "Popcorn":
        price = 15
    else:
        price = 19
elif movie == "Star Wars":
    if consumption == "Drink":
        price = 18
    elif consumption == "Popcorn":
        price = 25
    else:
        price = 30
    if tickets_count >= 4:
        price *= 0.7
else:
    if consumption == "Drink":
        price = 9
    elif consumption == "Popcorn":
        price = 11
    else:
        price = 14
    if tickets_count == 2:
        price *= 0.85

total_price = tickets_count * price
print(f"Your bill is {total_price:.2f} leva.")