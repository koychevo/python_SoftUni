house_height = float(input())
wall_length = float(input())
roof_height = float(input())

roof_area = 2 * (house_height * roof_height / 2 + house_height * wall_length)
red_paint_quantity = roof_area / 4.3
walls_area = 2 * (house_height ** 2 + house_height * wall_length - 1.5 ** 2) - 1.2 * 2
green_paint_quantity = walls_area / 3.4

print(f"{green_paint_quantity:.2f}")
print((f"{red_paint_quantity:.2f}"))