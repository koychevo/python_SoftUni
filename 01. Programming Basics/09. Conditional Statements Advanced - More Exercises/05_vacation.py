budget = float(input())
season = input().lower()

location = ""
place = ""
price = 0

if season == "summer":
    location = "Alaska"
elif season == "winter":
    location = "Morocco"

if budget <= 1000:
    place = "Camp"
    price = (0.65 if season == "summer" else 0.45) * budget
elif budget <= 3000:
    place = "Hut"
    price = (0.8 if season == "summer" else 0.6) * budget
else:
    place = "Hotel"
    price = 0.9 * budget


print(f"{location} - {place} - {price:.2f}")
