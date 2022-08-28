walk_mins = int(input())
walks_count = int(input())
calories = int(input())

burned_calories = walks_count * walk_mins * 5

if burned_calories >= calories / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")