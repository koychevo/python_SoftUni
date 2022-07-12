budget = float(input())
ticket_type = input()
people = int(input())

transport = 0
ticket_price = 0

if ticket_type == "VIP":
    ticket_price = 499.99
elif ticket_type == "Normal":
    ticket_price = 249.99

if 1 <= people <= 4:
    transport = 0.75 * budget
elif people <= 9:
    transport = 0.6 * budget
elif people <= 24:
    transport = 0.5 * budget
elif people <= 49:
    transport = 0.4 * budget
elif people >= 50:
    transport = 0.25 * budget

costs = people * ticket_price + transport
money_left = budget - costs

if money_left < 0:
    print(f"Not enough money! You need {-money_left:.2f} leva.")
else:
    print(f"Yes! You have {money_left:.2f} leva left.")
