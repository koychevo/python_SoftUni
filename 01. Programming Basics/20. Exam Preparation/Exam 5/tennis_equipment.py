from math import floor, ceil

tennis_racket_price = float(input())
tennis_rackets_count = int(input())
sneakers_count = int(input())

sneakers_price = tennis_racket_price / 6
total_price = 1.2 * (tennis_racket_price * tennis_rackets_count + sneakers_price * sneakers_count)

print(f"Price to be paid by Djokovic {floor(total_price / 8)}")
print(f"Price to be paid by sponsors {ceil(total_price * 7 / 8)}")