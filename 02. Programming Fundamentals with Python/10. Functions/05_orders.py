coffee_price = 1.50
water_price = 1.00
coke_price = 1.40
snacks_price = 2.00

product = input()
quantity = int(input())

price = 0

if product == 'coffee':
    price = coffee_price * quantity
elif product == 'water':
    price = water_price * quantity
elif product == 'coke':
    price = coke_price * quantity
elif product == 'snacks':
    price = snacks_price * quantity

print(f'{price:.2f}')