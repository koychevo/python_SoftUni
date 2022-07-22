destination = input()
budget = 0

while destination != 'End':
    budget = float(input())
    deposit = 0
    while deposit < budget:
        current_deposit = float(input())
        deposit += current_deposit
    print(f"Going to {destination}!")
    destination = input()