movie = input()
hall_type = input()
tickets_count = int(input())

ticket_price = 0

if movie == "A Star Is Born":
    if hall_type == "normal":
        ticket_price = 7.50
    elif hall_type == "luxury":
        ticket_price = 10.50
    else:
        ticket_price = 13.50
elif movie == "Bohemian Rhapsody":
    if hall_type == "normal":
        ticket_price = 7.35
    elif hall_type == "luxury":
        ticket_price = 9.45
    else:
        ticket_price = 12.75
elif movie == "Green Book":
    if hall_type == "normal":
        ticket_price = 8.15
    elif hall_type == "luxury":
        ticket_price = 10.25
    else:
        ticket_price = 13.25
else:
    if hall_type == "normal":
        ticket_price = 8.75
    elif hall_type == "luxury":
        ticket_price = 11.55
    else:
        ticket_price = 13.95

print(f"{movie} -> {tickets_count * ticket_price:.2f} lv.")