guests_count = int(input())
price_per_person = float(input())
budget = float(input())

cake_price = 0.1 * budget

if 10 <= guests_count <= 15:
    price_per_person *= 0.85
elif 15 < guests_count <= 20:
    price_per_person *= 0.8
elif guests_count > 20:
    price_per_person *= 0.75

costs = guests_count * price_per_person + cake_price

if costs > budget:
    print(f"No party! {costs - budget :.2f} leva needed.")
else:
    print(f"It is party time! {budget - costs :.2f} leva left.")