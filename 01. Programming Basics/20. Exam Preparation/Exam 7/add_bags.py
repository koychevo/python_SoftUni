luggage_price = float(input())
luggage_weight = float(input())
days = int(input())
luggages_count = int(input())

price = 0

if luggage_weight < 10:
    price = 0.2 * luggage_price
elif luggage_weight <= 20:
    price = 0.5 * luggage_price
else:
    price = luggage_price

if days < 7:
    price *= 1.4
elif days <= 30:
    price *= 1.15
else:
    price *= 1.1

print(f"The total price of bags is: {price * luggages_count:.2f} lv.")