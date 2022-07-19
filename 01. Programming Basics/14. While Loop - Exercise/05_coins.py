money = int(float(input()) * 100)

coins_count = 0

while money > 0:
    if money - 200 >= 0:
        coins_count += 1
        money -= 200
    elif money - 100 >= 0:
        coins_count += 1
        money -= 100
    elif money - 50 >= 0:
        coins_count += 1
        money -= 50
    elif money - 20 >= 0:
        coins_count += 1
        money -= 20
    elif money - 10 >= 0:
        coins_count += 1
        money -= 10
    elif money - 5 >= 0:
        coins_count += 1
        money -= 5
    elif money - 2 >= 0:
        coins_count += 1
        money -= 2
    elif money - 1 >= 0:
        coins_count += 1
        money -= 1

print(coins_count)