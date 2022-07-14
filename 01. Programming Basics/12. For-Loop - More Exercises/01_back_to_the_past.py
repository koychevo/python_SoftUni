money = float(input())
end_year = int(input())

age = 18
money_needed = 0

for year in range(1800, end_year + 1):
    if year % 2 == 0:
        money_needed += 12000
    else:
        money_needed += 12000 + 50 * age
    age += 1

money_left = money - money_needed

if money_left < 0:
    print(f"He will need {-money_left:.2f} dollars to survive.")
else:
    print(f"Yes! He will live a carefree life and will have {money_left:.2f} dollars left.")


