price = 0.0
total_price = 0.0
taxes = 0.0

current_price = input()

while current_price not in ['regular', 'special']:
    current_price = float(current_price)

    if current_price <= 0:
        print('Invalid price!')
    else:
        price += current_price
    current_price = input()

taxes = 0.2 * price

total_price = price + taxes

if current_price == 'special':
    total_price *= 0.9


if total_price == 0:
    print('Invalid order!')
else:
    print('Congratulations you\'ve just bought a new computer!')
    print(f'Price without taxes: {price:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print('-----------')
    print(f'Total price: {total_price:.2f}$')