juniours_count = int(input())
seniors_count = int(input())
race_type = input()

costs = 0

if race_type == "trail":
    costs = juniours_count * 5.5 + seniors_count * 7
elif race_type == "cross-country":
    costs = juniours_count * 8 + seniors_count * 9.5
    if juniours_count + seniors_count >= 50:
        costs *= 0.75
elif race_type == "downhill":
    costs = juniours_count * 12.25 + seniors_count * 13.75
elif race_type == "road":
    costs = juniours_count * 20 + seniors_count * 21.5

money_after_tax = 0.95 * costs
print(f"{money_after_tax:.2f}")