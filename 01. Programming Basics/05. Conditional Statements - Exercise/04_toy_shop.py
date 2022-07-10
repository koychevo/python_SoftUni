puzzle_price = 2.60
doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2
toys_count = 0

trip_price = float(input())
puzzles_count = int(input())
dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

toys_count = puzzles_count + dolls_count + teddy_bears_count + minions_count + trucks_count

total_price = puzzle_price * puzzles_count + dolls_count * doll_price + teddy_bear_price * teddy_bears_count + minions_count * minion_price + trucks_count * truck_price

if toys_count >= 50:
    total_price *= 0.75

money_left = 0.9 * total_price
money_left -= trip_price

if money_left < 0:
    print(f"Not enough money! {-money_left:.2f} lv needed.")
else:
    print(f"Yes! {money_left:.2f} lv left.")