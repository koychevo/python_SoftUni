turns = int(input())

points = 0
numbers_0_9_count = 0
numbers_10_19_count = 0
numbers_20_29_count = 0
numbers_30_39_count = 0
numbers_40_50_count = 0
invalid_numbers_count = 0

for i in range(turns):
    number = int(input())
    if number < 0 or number > 50:
        invalid_numbers_count += 1
        points /= 2
    elif 0 <= number <= 9:
        numbers_0_9_count += 1
        points += 0.2 * number
    elif number < 20:
        numbers_10_19_count += 1
        points += 0.3 * number
    elif number < 30:
        numbers_20_29_count += 1
        points += 0.4 * number
    elif number < 40:
        numbers_30_39_count += 1
        points += 50
    else:
        numbers_40_50_count += 1
        points += 100

print(f"{points:.2f}")
print(f"From 0 to 9: {numbers_0_9_count / turns * 100:.2f}%")
print(f"From 10 to 19: {numbers_10_19_count / turns * 100:.2f}%")
print(f"From 20 to 29: {numbers_20_29_count / turns * 100:.2f}%")
print(f"From 30 to 39: {numbers_30_39_count / turns * 100:.2f}%")
print(f"From 40 to 50: {numbers_40_50_count / turns * 100:.2f}%")
print(f"Invalid numbers: {invalid_numbers_count / turns * 100:.2f}%")