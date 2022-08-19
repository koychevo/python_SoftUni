from math import ceil

people = int(input())
ticket_price = float(input())
sunbed_price = float(input())
umbrella_price = float(input())

sunbed_count = ceil(0.75 * people)
umbrella_count = ceil(people / 2)

total_costs = people * ticket_price + sunbed_price * sunbed_count + umbrella_price * umbrella_count
print((f"{total_costs:.2f} lv."))