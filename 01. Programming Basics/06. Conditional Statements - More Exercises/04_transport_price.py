kilometers = int(input())
day_or_night = input()

transport_price = 0

if kilometers < 20:
    transport_price = 0.7
    if day_or_night == "day":
        transport_price += kilometers * 0.79
    elif day_or_night == "night":
        transport_price += kilometers * 0.9
elif kilometers < 100:
    transport_price = kilometers * 0.09
else:
    transport_price = kilometers * 0.06

print((f"{transport_price:.2f}"))