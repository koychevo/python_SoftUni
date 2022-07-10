from math import ceil

series_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_duration = break_duration / 8
pause_duration = break_duration / 4

time_for_series = break_duration - lunch_duration - pause_duration
rest_time = time_for_series - episode_duration

if rest_time < 0:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(-rest_time)} more minutes.")
else:
    print(f"You have enough time to watch {series_name} and left with {ceil(rest_time)} minutes free time.")