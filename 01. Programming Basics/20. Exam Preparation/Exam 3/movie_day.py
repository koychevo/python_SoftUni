time = int(input())
scenes_count = int(input())
scene_duration = int(input())

time_for_shooting = scene_duration * scenes_count + 0.15 * time

if time_for_shooting > time:
    print(f"Time is up! To complete the movie you need {round(time_for_shooting - time)} minutes.")
else:
    print(f"You managed to finish the movie on time! You have {round(time - time_for_shooting)} minutes left!")