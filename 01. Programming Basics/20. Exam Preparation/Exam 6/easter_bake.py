from math import ceil

bake_count = int(input())

max_flour = 0
max_sugar = 0
flour_count = 0
sugar_count = 0

for i in range(bake_count):
    current_sugar = int(input())
    current_flour = int(input())
    if current_sugar > max_sugar:
        max_sugar = current_sugar
    if current_flour > max_flour:
        max_flour = current_flour
    flour_count += current_flour
    sugar_count += current_sugar

print(f"Sugar: {ceil(sugar_count / 950)}")
print(f"Flour: {ceil(flour_count / 750)}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")