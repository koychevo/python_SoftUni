load_count = int(input())

bus_load_count = 0
truck_load_count = 0
train_load_count = 0
average_price = 0
total_load = 0

for i in range(load_count):
    current_load = int(input())
    total_load += current_load
    if current_load <= 3:
        bus_load_count += current_load
        average_price += current_load * 200
    elif current_load <= 11:
        truck_load_count += current_load
        average_price += current_load * 175
    else:
        train_load_count += current_load
        average_price += current_load * 120

average_price /= total_load

print(f"{average_price:.2f}")
print(f"{bus_load_count / total_load * 100:.2f}%")
print(f"{truck_load_count / total_load * 100:.2f}%")
print(f"{train_load_count / total_load * 100:.2f}%")