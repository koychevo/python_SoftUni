hall_rent = float(input())

cake_price = 0.2 * hall_rent
drinks_price = 0.55 * cake_price
animator_price = hall_rent / 3

total_costs = hall_rent + cake_price + drinks_price + animator_price

print(f"{total_costs:.2f}")