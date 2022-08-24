flour_price = float(input())
flour_kg_count = float(input())
sugar_kg_count = float(input())
packages_eggs_count = int(input())
packages_yeast_count = int(input())

sugar_price = 0.75 * flour_price
packages_eggs_price = 1.1 * flour_price
packages_yeast_price = 0.2 * sugar_price

costs = flour_kg_count * flour_price + sugar_kg_count * sugar_price + packages_eggs_price * packages_eggs_count + packages_yeast_price * packages_yeast_count
print(f"{costs:.2f}")