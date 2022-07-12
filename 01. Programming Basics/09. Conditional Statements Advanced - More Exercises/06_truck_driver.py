season = input().lower()
kilometers = float(input())

profit = 4

if kilometers <= 5000:
    if season == "spring" or season == "autumn":
        profit *= 0.75 * kilometers
    elif season == "summer":
        profit *= 0.9 * kilometers
    elif season == "winter":
        profit *= 1.05 * kilometers
elif kilometers <= 10000:
    if season == "spring" or season == "autumn":
        profit *= 0.95 * kilometers
    elif season == "summer":
        profit *= 1.1 * kilometers
    elif season == "winter":
        profit *= 1.25 * kilometers
elif kilometers <= 20000:
    profit *= 1.45 * kilometers

profit *= 0.9
print(f"{profit:.2f}")