food_count = int(input()) * 1000

current_food = input()

while current_food != "Adopted":
    current_food = int(current_food)
    food_count -= current_food
    current_food = input()

if food_count < 0:
    print(f"Food is not enough. You need {-food_count} grams more.")
else:
    print(f"Food is enough! Leftovers: {food_count} grams.")