budget = float(input())
season = input()

destination = ""
holiday = ""
spent_money = 0
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        holiday = "Camp"
        spent_money = 0.3 * budget
    elif season == "winter":
        holiday = "Hotel"
        spent_money = 0.7 * budget
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        holiday = "Camp"
        spent_money = 0.4 * budget
    elif season == "winter":
        holiday = "Hotel"
        spent_money = 0.8 * budget
else:
    destination = "Europe"
    spent_money = 0.9 * budget
    holiday = "Hotel"

print(f"Somewhere in {destination}")
print(f"{holiday} - {spent_money:.2f}")