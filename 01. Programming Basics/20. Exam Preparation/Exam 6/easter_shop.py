eggs_count = int(input())

sold_eggs_count = 0

command = input()

while command != "Close":
    current_eggs_count  = int(input())
    if command == "Fill":
        eggs_count += current_eggs_count
    else:
        if eggs_count < current_eggs_count:
            print("Not enough eggs in store!")
            print(f"You can buy only {eggs_count}.")
            break
        eggs_count -= current_eggs_count
        sold_eggs_count += current_eggs_count
    command = input()

if command == "Close":
    print("Store is closed!")
    print(f"{sold_eggs_count} eggs sold.")