age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

toys_count = 0
money = 0
money_per_birthday = 10

for i in range(2, age + 1, 2):
    money += money_per_birthday - 1
    money_per_birthday += 10
    toys_count += 1

if age % 2 != 0:
    toys_count += 1

profit = money + toys_count * toy_price
money_left = profit - washing_machine_price

if money_left < 0:
    print(f"No! {-money_left:.2f}")
else:
    print(f"Yes! {money_left:.2f}")