square_meter_price = 7.61
square_meters = float(input())
price = square_meter_price * square_meters
discount = 0.18 * price
total_price = price - discount
print(f"The final price is: {total_price} lv.")
print(f"The discount is: {discount} lv.")