tank_type = input().lower()
tank_count = float(input())

if tank_type != "diesel" and tank_type != "gasoline" and tank_type != "gas":
    print("Invalid fuel!")
else:
    if tank_count < 25:
        print(f"Fill your tank with {tank_type}!")
    else:
        print(f"You have enough {tank_type}.")