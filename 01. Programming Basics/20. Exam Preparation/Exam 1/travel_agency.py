town = input()
offer_type = input()
vip_discount = input()
days = int(input())

price = 0
is_input_data_valid = ((town == "Bansko" or town == "Borovets") and (offer_type == "noEquipment" or offer_type == "withEquipment")) \
                      or ((town == "Varna" or town == "Burgas") and (offer_type == "withBreakfast" or offer_type == "noBreakfast"))

if days < 1:
    print("Days must be positive number!")
elif not is_input_data_valid:
    print("Invalid input!")
else:
    if town == "Bansko" or town == "Borovets":
        if offer_type == "noEquipment":
            price = 80 if vip_discount == "no" else 0.95 * 80
        else:
            price = 100 if vip_discount == "no" else 0.9 * 100
    elif town == "Varna" or town == "Burgas":
        if offer_type == "noBreakfast":
            price = 100 if vip_discount == "no" else 0.93 * 100
        else:
            price = 130 if vip_discount == "no" else 0.88 * 130

    total_price = price * days
    if days > 7:
        total_price -= price
    print(f"The price is {total_price:.2f}lv! Have a nice time!")



