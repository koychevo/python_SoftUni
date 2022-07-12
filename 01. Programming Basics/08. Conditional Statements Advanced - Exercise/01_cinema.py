ticket_type = input()
rows = int(input())
cols = int(input())
price = 7.5

if ticket_type == "Premiere":
    price = 12
elif ticket_type == "Discount":
    price = 5

income = rows * cols * price
print(f"{income:.2f} leva")