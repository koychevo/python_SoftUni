budget = float(input())

name = input()

while name != "ACTION":
    reward = 0
    if len(name) > 15:
        reward = 0.2 * budget
    else:
        reward = float(input())
    budget -= reward
    if budget < 0:
        break
    name = input()

if budget < 0:
    print(f"We need {-budget:.2f} leva for our actors.")
else:
    print(f"We are left with {budget:.2f} leva.")
