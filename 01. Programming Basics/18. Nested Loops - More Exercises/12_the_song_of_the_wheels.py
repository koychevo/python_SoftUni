number = int(input())

password = 0
combination_count = 0
combinations = ""

for a in range(1, 10):
    for b in range(a + 1, 10):
        for c in range(2, 10):
            for d in range(1, c):
                if a * b + c * d == number:
                    combination_count += 1
                    combinations += str(1000 * a + 100 * b + 10 * c + d) + " "
                    if combination_count == 4:
                        password = 1000 * a + 100 * b + 10 * c + d

print(combinations)
if password > 1000:
    print(f"Password: {password}")
else:
    print("No!")
