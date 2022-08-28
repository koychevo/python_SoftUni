fruit = input()
size = input()
package_count = int(input())
price = 0

if size == "big":
    if fruit == "Watermelon":
        price = 28.7
    elif fruit == "Mango":
        price = 19.6
    elif fruit == "Pineapple":
        price = 24.8
    else:
        price = 15.2
    price *= 5
else:
    if fruit == "Watermelon":
        price = 56
    elif fruit == "Mango":
        price = 36.66
    elif fruit == "Pineapple":
        price = 42.10
    else:
        price = 20
    price *= 2

total_price = price * package_count

if 400 <= total_price <= 1000:
    total_price *= 0.85
elif total_price > 1000:
    total_price *= 0.5

print(f"{total_price:.2f} lv.")