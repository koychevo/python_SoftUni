budget = float(input())
destination = input()
season = input()
days = int(input())

price = 0

if destination == "Dubai":
    if season == "Summer":
        price = 40000
    else:
        price = 45000
    price *= 0.7
elif destination == "Sofia":
    if season == "Summer":
        price = 12500
    else:
        price = 17000
    price *= 1.25
else:
    if season == "Summer":
        price = 20250
    else:
        price = 24000

total_price = days * price

if total_price > budget:
    print(f"The director needs {total_price - budget:.2f} leva more!")
else:
    print(f"The budget for the movie is enough! We have {budget - total_price:.2f} leva left!")