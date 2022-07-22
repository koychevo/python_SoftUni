floor_count = int(input())
room_count = int(input())

for floor in range(floor_count, 0, -1):
    line = ""
    start = "A"
    if floor == floor_count:
        start = "L"
    elif floor % 2 == 0:
        start = "O"
    for room in range(0, room_count):
        line += start + str(floor) + str(room) + " "
    print(line)