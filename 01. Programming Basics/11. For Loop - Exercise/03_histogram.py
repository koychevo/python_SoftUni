n = int(input())

p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0

for i in range(n):
    number = int(input())
    if number < 200:
        p1_count += 1
    elif number < 400:
        p2_count += 1
    elif number < 600:
        p3_count += 1
    elif number < 800:
        p4_count += 1
    else:
        p5_count += 1

print(f"{p1_count / n * 100 :.2f}%")
print(f"{p2_count / n * 100 :.2f}%")
print(f"{p3_count / n * 100 :.2f}%")
print(f"{p4_count / n * 100 :.2f}%")
print(f"{p5_count / n * 100 :.2f}%")