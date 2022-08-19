budget = float(input())
statists_count = int(input())
clothes_price = float(input())

decor_price = 0.1 * budget
clothes_costs = statists_count * clothes_price
if statists_count > 150:
    clothes_costs *= 0.9

total_costs = clothes_costs + decor_price

if total_costs > budget:
    print("Not enough money!")
    print(f"Wingard needs {total_costs - budget :.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget - total_costs:.2f} leva left.")