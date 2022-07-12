days = int(input())
room_type = input()
evaluation = input()

one_person_room_price = 18
apartment_price = 25
president_apartment_price = 35

price = 0

if days < 10:
    if room_type == "room for one person":
        price = (days - 1) * one_person_room_price
    elif room_type == "apartment":
        price = 0.7 * (days - 1) * apartment_price
    elif room_type == "president apartment":
        price = 0.9 * (days - 1) * president_apartment_price
elif days <= 15:
    if room_type == "room for one person":
        price = (days - 1) * one_person_room_price
    elif room_type == "apartment":
        price = 0.65 * (days - 1) * apartment_price
    elif room_type == "president apartment":
        price = 0.85 * (days - 1) * president_apartment_price
else:
    if room_type == "room for one person":
        price = (days - 1) * one_person_room_price
    elif room_type == "apartment":
        price = 0.5 * (days - 1) * apartment_price
    elif room_type == "president apartment":
        price = 0.8 * (days - 1) * president_apartment_price

if evaluation == "positive":
    price *= 1.25
elif evaluation == "negative":
    price *= 0.9

print(f"{price:.2f}")