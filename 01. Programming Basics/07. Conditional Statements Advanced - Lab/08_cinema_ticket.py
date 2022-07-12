day_of_the_week = input()
price = 12

if day_of_the_week == "Wednesday" or day_of_the_week == "Thursday":
    price = 14
elif day_of_the_week == "Saturday" or day_of_the_week == "Sunday":
    price = 16

print(price)