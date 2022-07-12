product = input()
town = input()
quantity = float(input())
product_price = 0

if town == "Sofia":
    if product == "coffee":
        product_price = 0.5
    elif product == "water":
        product_price = 0.8
    elif product == "beer":
        product_price = 1.2
    elif product == "sweets":
        product_price = 1.45
    elif product == "peanuts":
        product_price = 1.6
elif town == "Plovdiv":
    if product == "coffee":
        product_price = 0.4
    elif product == "water":
        product_price = 0.7
    elif product == "beer":
        product_price = 1.15
    elif product == "sweets":
        product_price = 1.3
    elif product == "peanuts":
        product_price = 1.5
elif town == "Varna":
    if product == "coffee":
        product_price = 0.45
    elif product == "water":
        product_price = 0.7
    elif product == "beer":
        product_price = 1.1
    elif product == "sweets":
        product_price = 1.35
    elif product == "peanuts":
        product_price = 1.55


print(quantity * product_price)
