months = int(input())

electricity_costs = 0
water_costs = 20 * months
internet_costs = 15 * months
other_costs = 0
average_costs = water_costs + internet_costs

for i in range(months):
    current_electricity_costs = float(input())
    electricity_costs += current_electricity_costs
    other_costs += 1.2 * (20 + 15 + current_electricity_costs)

average_costs += electricity_costs + other_costs
average_costs /= months

print(f"Electricity: {electricity_costs:.2f} lv")
print(f"Water: {water_costs:.2f} lv")
print(f"Internet: {internet_costs:.2f} lv")
print(f"Other: {other_costs:.2f} lv")
print(f"Average: {average_costs:.2f} lv")