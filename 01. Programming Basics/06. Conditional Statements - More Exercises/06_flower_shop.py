from math import floor

magnolia_count = int(input())
hyacinth_count = int(input())
rose_count = int(input())
cactus_count = int(input())
present_price = float(input())

profit = 0.95 * (magnolia_count * 3.25 + hyacinth_count * 4 + rose_count * 3.5 + cactus_count * 8)

money_left = floor(profit - present_price)

if money_left < 0:
    print(f"She will have to borrow {-money_left} leva.")
else:
    print(f"She is left with {money_left} leva.")