fuel_type = input().lower()
fuel_count = float(input())
club_card = input().lower()

gas_price = 0.93
diesel_price = 2.33
gasoline_price = 2.22
fuel_price = 0

if fuel_type == "gas":
    fuel_price = gas_price - 0.08 if club_card == "yes" else gas_price
elif fuel_type == "diesel":
    fuel_price = diesel_price - 0.12 if club_card == "yes" else diesel_price
elif fuel_type == "gasoline":
    fuel_price = gasoline_price - 0.18 if club_card == "yes" else gasoline_price

price = fuel_price * fuel_count

if 20 <= fuel_count <= 25:
    price *= 0.92
elif fuel_count > 25:
    price *= 0.9

print(f"{price:.2f} lv.")