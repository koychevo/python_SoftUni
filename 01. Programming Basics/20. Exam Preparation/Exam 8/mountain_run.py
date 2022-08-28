record = float(input())
distance = float(input())
time_per_meter = float(input())

time = distance * time_per_meter + (distance // 50) * 30

if time < record:
    print(f"Yes! The new record is {time:.2f} seconds.")
else:
    print(f"No! He was {(time - record):.2f} seconds slower.")

