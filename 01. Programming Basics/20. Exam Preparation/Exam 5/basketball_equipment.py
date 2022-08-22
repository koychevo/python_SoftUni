year_fee = float(input())

sneakers_price = 0.6 * year_fee
clothes_price = 0.8 * sneakers_price
ball_price = clothes_price / 4
accessories_price = ball_price / 5

total_costs = year_fee + sneakers_price + clothes_price + ball_price + accessories_price
print(f"{total_costs:.2f}")