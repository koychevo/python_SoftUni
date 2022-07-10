number = int(input())
bonus_score = 0
if number <= 100:
    bonus_score += 5
elif number > 1000:
    bonus_score = 0.1 * number
else:
    bonus_score = 0.2 * number

if number % 2 == 0:
    bonus_score += 1
elif number % 10 == 5:
    bonus_score += 2

print(bonus_score)
print(number + bonus_score)