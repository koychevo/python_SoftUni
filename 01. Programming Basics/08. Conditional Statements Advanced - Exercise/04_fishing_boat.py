budget = int(input())
season = input()
fishers_count = int(input())

price = 0

if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600

if fishers_count <= 6:
    price *= 0.9
elif fishers_count <= 11:
    price *= 0.85
else:
    price *= 0.75

if fishers_count % 2 == 0 and not season == "Autumn":
    price *= 0.95

money_left = budget - price

if money_left < 0:
    print(f"Not enough money! You need {-money_left:.2f} leva.")
else:
    print(f"Yes! You have {money_left:.2f} leva left.")