strawberry_price = float(input())
bananas_quantity = float(input())
oranges_quantity = float(input())
raspberries_quantity = float(input())
strawberries_quantity = float(input())

raspberry_price = strawberry_price / 2
orange_price = 0.6 * raspberry_price
banana_price = 0.2 * raspberry_price

costs = strawberries_quantity * strawberry_price + bananas_quantity * banana_price + oranges_quantity * orange_price + raspberries_quantity * raspberry_price
print(f"{costs:.2f}")