stage = input()
ticket_type = input()
tickets_count = int(input())
photo = input()

price = 0
is_photo_fee = False

if stage == "Quarter final":
    if ticket_type == "Standard":
        price = 55.50
    elif ticket_type == "Premium":
        price = 105.20
    else:
        price = 118.90
elif stage == "Semi final":
    if ticket_type == "Standard":
        price = 75.88
    elif ticket_type == "Premium":
        price = 125.22
    else:
        price = 300.40
else:
    if ticket_type == "Standard":
        price = 110.10
    elif ticket_type == "Premium":
        price = 160.66
    else:
        price = 400

total_price = tickets_count * price

if (photo == "Y" and total_price > 4000) or photo == "N":
    is_photo_fee = True

if total_price > 4000:
    total_price *= 0.75
elif total_price > 2500:
    total_price *= 0.9

if not is_photo_fee:
    total_price += tickets_count * 40

print(f"{total_price:.2f}")