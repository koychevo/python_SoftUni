control_mins = int(input())
control_secs = int(input())
length = float(input())
secs_per_100_meters = int(input())
control_time = control_mins * 60 + control_secs
time = length / 100 * secs_per_100_meters - length / 120 * 2.5

if time > control_time:
    print(f"No, Marin failed! He was {time - control_time:.3f} second slower.")
else:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {time:.3f}.")