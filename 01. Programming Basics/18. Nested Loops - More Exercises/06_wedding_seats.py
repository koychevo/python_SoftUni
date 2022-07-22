last_sector = input()
rows_in_first_sector = int(input())
places_in_odd_row = int(input())

places_in_even_row = places_in_odd_row + 2
rows_in_sector = rows_in_first_sector - 1
places_count = 0

for sector in range(ord("A"), ord(last_sector) + 1):
    rows_in_sector += 1
    for row in range(1, rows_in_sector + 1):
        places_in_row = places_in_odd_row
        if row % 2 == 0:
            places_in_row = places_in_even_row
        for place in range(1, places_in_row + 1):
            print(f"{chr(sector)}{row}{chr(96 + place)}")
            places_count += 1

print(places_count)