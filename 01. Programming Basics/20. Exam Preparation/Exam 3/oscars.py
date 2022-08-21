actor_name = input()
points = float(input())
jury_count = int(input())

for jury_member in range(jury_count):
    jury_name = input()
    jury_points = float(input())
    current_points = len(jury_name) * jury_points / 2
    points += current_points
    if points > 1250.5:
        break

if points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {1250.5 - points :.1f} more!")
