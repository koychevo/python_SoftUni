holidays = int(input())

playing_minutes = holidays * 127 + (365 - holidays) * 63

minutes_difference = 30000 - playing_minutes

hours = abs(minutes_difference) // 60
minutes = abs(minutes_difference) % 60

if minutes_difference < 0:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")

