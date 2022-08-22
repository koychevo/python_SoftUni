budget = float(input())
fuel_count = float(input())
day_of_week = input()

costs = fuel_count * 2.1 + 100
if day_of_week == "Saturday":
    costs *= 0.9
elif day_of_week == "Sunday":
    costs *= 0.8

if costs > budget:
    print(f"Not enough money! Money needed: {costs - budget :.2f} lv.")
else:
    print(f"Safari time! Money left: {budget - costs :.2f} lv.")