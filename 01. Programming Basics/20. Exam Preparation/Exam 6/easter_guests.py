from math import ceil
guests_count = int(input())
budget = float(input())

eggs_count = guests_count * 2
easter_bread_count = ceil(guests_count / 3)

costs = eggs_count * 0.45 + easter_bread_count * 4

if costs > budget:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {costs - budget :.2f} lv. more.")
else:
    print(f"Lyubo bought {easter_bread_count} Easter bread and {eggs_count} eggs.")
    print(f"He has {budget - costs :.2f} lv. left.")