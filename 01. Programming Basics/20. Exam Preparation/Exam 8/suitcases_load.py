load_capacity = float(input())
load_count = 0

current_load = input()

while current_load != "End":
    current_load = float(current_load)
    load_count += 1
    if load_count % 3 == 0:
        current_load *= 1.1
    load_capacity -= current_load
    if load_capacity < 0:
        load_count -= 1
        break

    current_load = input()

if current_load == "End":
    print("Congratulations! All suitcases are loaded!")
else:
    print("No more space!")

print(f"Statistic: {load_count} suitcases loaded.")