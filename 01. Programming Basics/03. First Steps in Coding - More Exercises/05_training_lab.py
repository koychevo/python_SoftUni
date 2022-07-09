length = float(input()) * 100
width = float(input()) * 100
corridor_width = 100
working_station_length = 70
working_station_width = 120

rows_in_hall = length // working_station_width
working_station_in_row = (width - corridor_width) // working_station_length


working_stations = int(working_station_in_row * rows_in_hall) - 3
print(working_stations)

