contract_duration = input()
contract_type = input()
with_internet = input()
months = int(input())

price = 0

if contract_type == "Small":
    if contract_duration == "one":
        price = 9.98
    else:
        price = 8.58
elif contract_type == "Middle":
    if contract_duration == "one":
        price = 18.99
    else:
        price = 17.09
elif contract_type == "Large":
    if contract_duration == "one":
        price = 25.98
    else:
        price = 23.59
else:
    if contract_duration == "one":
        price = 35.99
    else:
        price = 31.79

if with_internet == "yes":
    if price <= 10:
        price += 5.5
    elif price <= 30:
        price += 4.35
    else:
        price += 3.85

if contract_duration == "two":
    price *= (100 - 3.75) / 100

total_price = months * price
print(f"{total_price:.2f} lv.")