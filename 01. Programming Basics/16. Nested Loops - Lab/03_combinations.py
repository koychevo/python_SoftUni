number = int(input())
combinations_count = 0

for x in range(number + 1):
    for y in range(number + 1):
        for z in range(number + 1):
            if x + y + z == number:
                combinations_count += 1

print(combinations_count)