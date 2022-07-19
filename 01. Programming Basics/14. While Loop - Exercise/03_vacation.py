trip_price = float(input())
available_money = float(input())

spend_days_count = 0
days_count = 0

while True:
    action = input()
    money = float(input())
    days_count += 1
    if action == "save":
        spend_days_count = 0
        available_money += money
        if available_money >= trip_price:
            print(f"You saved the money for {days_count} days.")
            break
    elif action == "spend":
        spend_days_count += 1
        if spend_days_count == 5:
            print("You can't save the money.")
            print(days_count)
            break
        available_money -= money
        if available_money < 0:
            available_money = 0