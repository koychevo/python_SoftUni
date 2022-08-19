voucher = float(input())

tickets_count = 0
purchase_count = 0

purchase = input()

while purchase != "End":
    price = 0
    is_ticket = False

    if len(purchase) > 8:
        price = ord(purchase[0]) + ord(purchase[1])
        is_ticket =True
    else:
        price = ord(purchase[0])

    if price > voucher:
        break
    voucher -= price
    if is_ticket:
        tickets_count += 1
    else:
        purchase_count += 1
    purchase = input()

print(tickets_count)
print(purchase_count)