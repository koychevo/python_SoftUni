days_count = int(input())
hours_per_day = int(input())

sum = 0

for day in range(1, days_count + 1):
    day_sum = 0
    for hour in range(1, hours_per_day + 1):
        if day % 2 == 0 and hour % 2 != 0:
            day_sum += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            day_sum += 1.25
        else:
            day_sum += 1
    print(f"Day: {day} - {day_sum:.2f} leva")
    sum += day_sum

print(f"Total: {sum:.2f} leva")