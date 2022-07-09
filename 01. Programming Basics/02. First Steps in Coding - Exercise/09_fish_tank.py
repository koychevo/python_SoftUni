length = int(input()) / 10
width = int(input()) / 10
high = int(input()) / 10
percentage = float(input()) / 100

area = length * width * high
water = (1 - percentage) * area
print(water)
