orders_count = int(input())
total_price = 0

for _ in range(orders_count):
    price = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if not (0.01 <= price <= 100 and 1 <= days <= 31 and 1 <= capsules_per_day <= 2000):
        continue
    current_price = price * capsules_per_day * days
    total_price += current_price
    print(f'The price for the coffee is: ${current_price:.2f}')
else:
    print(f'Total: ${total_price:.2f}')
