year_fee = int(input())

sneakers = 0.6 * year_fee
clothes = 0.8 * sneakers
ball = clothes / 4
accessories = ball / 5

total_costs = year_fee + sneakers + clothes + ball + accessories
print(total_costs)