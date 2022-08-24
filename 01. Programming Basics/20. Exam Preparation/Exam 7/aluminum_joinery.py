joinery_count = int(input())
joinery_type = input()
delivery = input()

price = 0

if joinery_count < 10:
    print("Invalid order")
    exit()

if joinery_type == "90X130":
    price = 110
    if joinery_count > 60:
        price *= 0.92
    elif joinery_count > 30:
        price *= 0.95
elif joinery_type == "100X150":
    price = 140
    if joinery_count > 80:
        price *= 0.9
    elif joinery_count > 40:
        price *= 0.94
elif joinery_type == "130X180":
    price = 190
    if joinery_count > 50:
        price *= 0.88
    elif joinery_count > 20:
        price *= 0.93
else:
    price = 250
    if joinery_count > 50:
        price *= 0.86
    elif joinery_count > 25:
        price *= 0.91

total_price = price * joinery_count

if delivery == "With delivery":
    total_price += 60

if joinery_count > 99:
    total_price *= 0.96

print(f"{total_price:.2f} BGN")