flower = input()
quantity = int(input())
budget = int(input())

price = 0

if flower == "Roses":
    price = 5 * quantity
    if quantity > 80:
        price *= 0.9
elif flower == "Dahlias":
    price = 3.8 * quantity
    if quantity > 90:
        price *= 0.85
elif flower == "Tulips":
    price = 2.8 * quantity
    if quantity > 80:
        price *= 0.85
elif flower == "Narcissus":
    price = 3 * quantity
    if quantity < 120:
        price *= 1.15
elif flower == "Gladiolus":
    price = 2.5 * quantity
    if quantity < 80:
        price *= 1.2

rest_money = budget - price

if rest_money < 0:
    print(f"Not enough money, you need {-rest_money:.2f} leva more.")
else:
    print(f"Hey, you have a great garden with {quantity} {flower} and {rest_money:.2f} leva left.")