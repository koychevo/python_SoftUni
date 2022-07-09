total_pages = int(input())
pages_per_hour = int(input())
days = int(input())

hours = total_pages / pages_per_hour
hours_per_day = int(hours / days)

print(hours_per_day)