destination = input()
date = input()
nights_count = int(input())

price = 0

if date == "21-23":
    if destination == "France":
        price = 30
    elif destination == "Italy":
        price = 28
    else:
        price = 32
elif date == "24-27":
    if destination == "France":
        price = 35
    elif destination == "Italy":
        price = 32
    else:
        price = 37
else:
    if destination == "France":
        price = 40
    elif destination == "Italy":
        price = 39
    else:
        price = 43

print(f"Easter trip to {destination} : {nights_count * price :.2f} leva.")