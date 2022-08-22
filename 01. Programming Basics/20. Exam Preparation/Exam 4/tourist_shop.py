budget = float(input())

items_count = 0
costs = 0

item_name = input()

while item_name != "Stop":
    item_price = float(input())
    items_count += 1
    if items_count % 3 == 0:
        item_price /= 2
    if item_price > budget:
        print("You don't have enough money!")
        print(f"You need {item_price - budget :.2f} leva!")
        break
    costs += item_price
    budget -= item_price
    item_name = input()

if item_name == "Stop":
    print(f"You bought {items_count} products for {costs:.2f} leva.")