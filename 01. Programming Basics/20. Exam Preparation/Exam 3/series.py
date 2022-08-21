budget = float(input())
series_count = int(input())

for i in range(series_count):
    name = input()
    price = float(input())
    if name == "Thrones":
        price *= 0.5
    elif name == "Lucifer":
        price *= 0.6
    elif name == "Protector":
        price *= 0.7
    elif name == "TotalDrama":
        price *= 0.8
    elif name == "Area":
        price *= 0.9
    budget -= price

if budget < 0:
    print(f"You need {-budget:.2f} lv. more to buy the series!")
else:
    print(f"You bought all the series and left with {budget:.2f} lv.")