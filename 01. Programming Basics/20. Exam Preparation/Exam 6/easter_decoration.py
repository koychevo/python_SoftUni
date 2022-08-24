customers_count = int(input())

average_bill = 0

for i in range(customers_count):
    item = input()
    price = 0
    item_count = 0
    while item != "Finish":
        item_count += 1
        if item == "basket":
            price += 1.50
        elif item == "wreath":
            price += 3.80
        else:
            price += 7
        item = input()
    if item_count % 2 == 0:
        price *= 0.8
    print(f"You purchased {item_count} items for {price:.2f} leva.")
    average_bill += price

print(f"Average bill per client is: {average_bill / customers_count :.2f} leva.")