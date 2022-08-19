budget = float(input())
nights = int(input())
price = float(input())
extra_costs = int(input()) / 100

if nights > 7:
    price *= 0.95

total_costs = nights * price + extra_costs * budget

if total_costs > budget:
    print(f"{total_costs - budget :.2f} leva needed.")
else:
    print(f"Ivanovi will be left with {budget - total_costs:.2f} leva after vacation.")