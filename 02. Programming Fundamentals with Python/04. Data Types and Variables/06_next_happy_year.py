year = int(input())

while True:
    is_happy_year = True
    year += 1
    current_year = str(year)
    for i in range(len(current_year) - 1):
        for j in range(i + 1, len(current_year)):
            if current_year[i] == current_year[j]:
                is_happy_year = False
                break
        if not is_happy_year:
            break
    if is_happy_year:
        break

print(year)