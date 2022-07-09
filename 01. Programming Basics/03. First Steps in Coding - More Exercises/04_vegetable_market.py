vegetables_price = float(input())
fruits_price = float(input())
vegetables_kilos = int(input())
fruits_kilos = int(input())

income_lv = vegetables_price * vegetables_kilos + fruits_price * fruits_kilos
income_euro = income_lv / 1.94

print(f"{income_euro:.2f}")