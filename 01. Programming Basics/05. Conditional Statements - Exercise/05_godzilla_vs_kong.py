budget = float(input())
supernumeraries_count = int(input())
supernumerary_cloths_price = float(input())

decor_costs = 0.1 * budget
clothes_costs = supernumerary_cloths_price * supernumeraries_count

if supernumeraries_count > 150:
    clothes_costs *= 0.9

total_costs = decor_costs + clothes_costs

money_left = budget - total_costs

if money_left < 0:
    print("Not enough money!")
    print(f"Wingard needs {-money_left:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")