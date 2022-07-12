chrysanthemum_count = int(input())
rose_count = int(input())
tulip_count = int(input())
season = input().lower()
is_holiday = input().lower()

chrysanthemum_price = 0
rose_price = 0
tulip_price = 0

if season == "spring" or season == "summer":
    chrysanthemum_price = 2
    rose_price = 4.10
    tulip_price = 2.50
elif season == "autumn" or season == "winter":
    chrysanthemum_price = 3.75
    rose_price = 4.50
    tulip_price = 4.15

bouquet_price = chrysanthemum_count * chrysanthemum_price + rose_count * rose_price + tulip_count * tulip_price

if is_holiday == "y":
    bouquet_price *= 1.15

if tulip_count > 7 and season == "spring":
    bouquet_price *= 0.95
if rose_count >= 10 and season == "winter":
    bouquet_price *= 0.9
if chrysanthemum_count + rose_count + tulip_count > 20:
    bouquet_price *= 0.8

bouquet_price += 2

print(f"{bouquet_price:.2f}")