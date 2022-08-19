height = int(input())
width = int(input())
doors_windows_percentage = int(input())

area_to_paint = round(4 * height * width * (100 - doors_windows_percentage) / 100)

paint = input()
while paint != "Tired!":
    paint = int(paint)
    area_to_paint -= paint
    if area_to_paint <= 0:
        break
    paint = input()

if area_to_paint > 0:
    print(f"{area_to_paint} quadratic m left.")
elif area_to_paint == 0:
    print("All walls are painted! Great job, Pesho!")
else:
    print(f"All walls are painted and you have {-area_to_paint} l paint left!")