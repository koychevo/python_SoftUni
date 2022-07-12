season = input().lower()
group_type = input()
students_count = int(input())
nights_count = int(input())

sport_type = ""
price = 0

if group_type == "boys" or group_type == "girls":
    if season == "winter":
        price = 9.6
    elif season == "spring":
        price = 7.2
    elif season == "summer":
        price = 15
elif group_type == "mixed":
    if season == "winter":
        price = 10
        sport_type = "Ski"
    elif season == "spring":
        price = 9.5
        sport_type = "Cycling"
    elif season == "summer":
        price = 20
        sport_type = "Swimming"

if group_type == "girls":
    if season == "winter":
        sport_type = "Gymnastics"
    elif season == "spring":
        sport_type = "Athletics"
    elif season == "summer":
        sport_type = "Volleyball"
elif group_type == "boys":
    if season == "winter":
        sport_type = "Judo"
    elif season == "spring":
        sport_type = "Tennis"
    elif season == "summer":
        sport_type = "Football"

price *= students_count * nights_count

if 10 <= students_count < 20:
    price *= 0.95
elif 20 <= students_count < 50:
    price *= 0.85
elif students_count >= 50:
    price *= 0.5

print(f"{sport_type} {price:.2f} lv.")