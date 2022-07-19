step_count = 0

while True:
    line = input()
    if line == "Going home":
        step_count += int(input())
        break
    current_steps = int(line)
    step_count += current_steps
    if step_count >= 10000:
        break

if step_count < 10000:
    print(f"{10000 - step_count} more steps to reach goal.")
else:
    print("Goal reached! Good job!")
    print(f"{step_count - 10000} steps over the goal!")