numbers_count = int(input())

p1_count = 0
p2_count = 0
p3_count = 0

for i in range(numbers_count):
    number = int(input())
    if number % 2 == 0:
        p1_count += 1
    if number % 3 == 0:
        p2_count += 1
    if number % 4 == 0:
        p3_count += 1

print(f"{p1_count / numbers_count * 100 :.2f}%")
print(f"{p2_count / numbers_count * 100 :.2f}%")
print(f"{p3_count / numbers_count * 100 :.2f}%")