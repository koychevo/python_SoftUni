width = int(input())
length = int(input())
height = int(input())

volume = width * length * height

line = input()

while line != "Done":
    volume -= int(line)
    if volume < 0:
        break
    line = input()

if volume < 0:
    print(f"No more free space! You need {-volume} Cubic meters more.")
else:
    print(f"{volume} Cubic meters left.")