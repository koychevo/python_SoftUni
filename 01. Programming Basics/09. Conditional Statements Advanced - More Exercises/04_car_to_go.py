budget = float(input())
season = input().lower()

car_class = ""
car_type = ""
car_price = 0

if budget <= 100:
    car_class = "Economy class"
    car_type = "Cabrio" if season == "summer" else "Jeep"
    car_price = (0.35 if season == "summer" else 0.65) * budget
elif budget <= 500:
    car_class = "Compact class"
    car_type = "Cabrio" if season == "summer" else "Jeep"
    car_price = 0.45 if season == "summer" else 0.8 * budget
else:
    car_class = "Luxury class"
    car_type = "Jeep"
    car_price = 0.9 * budget

print(car_class)
print(f"{car_type} - {car_price:.2f}")