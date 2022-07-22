one_lv_count = int(input())
two_lv_count = int(input())
five_lv_count = int(input())
sum = int(input())

for one_coin in range(one_lv_count + 1):
    for two_coin in range(two_lv_count + 1):
        for five_banknote in range(five_lv_count + 1):
            if one_coin * 1 + two_coin * 2 + five_banknote * 5 == sum:
                print(f"{one_coin} * 1 lv. + {two_coin} * 2 lv. + {five_banknote} * 5 lv. = {sum} lv.")