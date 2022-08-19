drink_type = input()
sugar = input()
drinks_count = int(input())

price = 0

if sugar == "Without":
    if drink_type == "Espresso":
        price = 0.9
    elif drink_type == "Cappuccino":
        price = 1
    else:
        price = 0.5
    price *= 0.65
elif sugar == "Normal":
    if drink_type == "Espresso":
        price = 1
    elif drink_type == "Cappuccino":
        price = 1.2
    else:
        price = 0.6
else:
    if drink_type == "Espresso":
        price = 1.2
    elif drink_type == "Cappuccino":
        price = 1.6
    else:
        price = 0.7

total_price = drinks_count * price

if drinks_count >= 5 and drink_type == "Espresso":
    total_price *= 0.75

if total_price > 15:
    total_price *= 0.8

print(f"You bought {drinks_count} cups of {drink_type} for {total_price:.2f} lv.")