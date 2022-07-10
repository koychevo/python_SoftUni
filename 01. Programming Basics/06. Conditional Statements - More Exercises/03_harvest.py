from math import floor, ceil

area = int(input())
grape_per_square_meter = float(input())
needed_wine =int(input())
workers_count = int(input())

produced_wine = 0.4 * area * grape_per_square_meter / 2.5
wine_diff = produced_wine - needed_wine

if wine_diff < 0:
    print(f"It will be a tough winter! More {floor(-wine_diff)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {floor(produced_wine)} liters.")
    print(f"{ceil(wine_diff)} liters left -> {ceil(wine_diff / workers_count)} liters per person.")