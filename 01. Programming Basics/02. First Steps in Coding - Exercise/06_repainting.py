nylon_price = 1.50
paint_price = 14.50
paint_thinner_price = 5.00

nylon_count = int(input()) + 2
paint_count = int(input())
paint_thinner_count = int(input())
working_hours = int(input())

paint_count *= 1.1

materials_costs = 0.40 + nylon_count * nylon_price + paint_count * paint_price + paint_thinner_count * paint_thinner_price
workers_costs = 0.3 * materials_costs * working_hours
total_costs = materials_costs + workers_costs

print(total_costs)