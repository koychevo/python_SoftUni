needed_profit = float(input())
cocktail = input()

income = 0

while cocktail != "Party!":
    cocktails_count = int(input())
    cocktail_price = len(cocktail)
    order_price = cocktail_price * cocktails_count
    if order_price % 2 != 0:
        order_price *= 0.75
    income += order_price
    if income >= needed_profit:
        break
    cocktail = input()

if cocktail == "Party!":
    print(f"We need {needed_profit - income:.2f} leva more.")
else:
    print("Target acquired.")

print(f"Club income - {income:.2f} leva.")