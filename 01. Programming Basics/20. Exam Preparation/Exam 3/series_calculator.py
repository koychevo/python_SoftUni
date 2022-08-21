from math import floor
series_name = input()
seasons_count = int(input())
episodes_count = int(input())
episode_duration = float(input())

time = seasons_count * (10 + episodes_count * 1.2 * episode_duration)
print(f"Total time needed to watch the {series_name} series is {floor(time)} minutes.")
