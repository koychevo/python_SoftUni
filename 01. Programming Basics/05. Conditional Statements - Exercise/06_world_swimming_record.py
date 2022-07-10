record_time = float(input())
distance = float(input())
time_per_second = float(input())

ivan_time = distance * time_per_second
ivan_time += (distance // 15) * 12.5

if ivan_time >= record_time:
    print(f"No, he failed! He was {(ivan_time - record_time):.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {ivan_time:.2f} seconds.")