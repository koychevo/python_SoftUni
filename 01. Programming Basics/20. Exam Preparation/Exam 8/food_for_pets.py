days = int(input())
food_count = float(input())

dog_food = 0
cat_food = 0
biscuits_count = 0
eaten_food = 0

for day in range(1, days + 1):
    day_dog_food = int(input())
    day_cat_food = int(input())
    dog_food += day_dog_food
    cat_food += day_cat_food
    if day % 3 == 0:
        biscuits_count += 0.1 * (day_dog_food + day_cat_food)

eaten_food = dog_food + cat_food

print(f"Total eaten biscuits: {round(biscuits_count)}gr.")
print(f"{eaten_food / food_count * 100 :.2f}% of the food has been eaten.")
print(f"{dog_food / eaten_food * 100 :.2f}% eaten from the dog.")
print(f"{cat_food / eaten_food * 100 :.2f}% eaten from the cat.")
