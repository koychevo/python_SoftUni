bitcoin_count = int(input())
yuan_count = float(input())
commission = float(input())

money_in_lv = bitcoin_count * 1168 + yuan_count * 0.15 * 1.76
money_in_euro = money_in_lv / 1.95

money_left = (1 - commission / 100) * money_in_euro

print(f"{money_left:.2f}")