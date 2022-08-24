egg_size = input()
egg_color = input()
eggs_count = int(input())

price = 0

if egg_color == "Red":
    if egg_size == "Large":
        price = 16
    elif egg_size == "Medium":
        price = 13
    else:
        price = 9
elif egg_color == "Green":
    if egg_size == "Large":
        price = 12
    elif egg_size == "Medium":
        price = 9
    else:
        price = 8
else:
    if egg_size == "Large":
        price = 9
    elif egg_size == "Medium":
        price = 7
    else:
        price = 5

print(f"{0.65 * price * eggs_count :.2f} leva.")