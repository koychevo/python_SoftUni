from math import floor

days_count = int(input())
left_food_count = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input()) / 1000

needed_food = days_count * (dog_food_per_day + cat_food_per_day + turtle_food_per_day)

food_diff = floor(left_food_count - needed_food)

if food_diff < 0:
    print(f"{-food_diff} more kilos of food are needed.")
else:
    print(f"{food_diff} kilos of food left.")