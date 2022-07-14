actor_name = input()
actor_points = float(input())
jury_count = int(input())

for i in range(jury_count):
    jury_name = input()
    jury_points = float(input())
    actor_points += len(jury_name) * jury_points / 2
    if actor_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {actor_points:.1f}!")
        break

if actor_points < 1250.5:
    print(f"Sorry, {actor_name} you need {1250.5 - actor_points:.1f} more!")