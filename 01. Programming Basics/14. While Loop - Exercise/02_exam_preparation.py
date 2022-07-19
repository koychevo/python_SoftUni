max_failed_score_count = int(input())
task_name = input()
average_score = 0
task_count = 0
failed_score_count = 0
last_task = ""

while task_name != "Enough":
    task_score = int(input())
    task_count += 1
    average_score += task_score
    if task_score <= 4:
        failed_score_count += 1
    if failed_score_count == max_failed_score_count:
        break
    last_task = task_name
    task_name = input()

if failed_score_count == max_failed_score_count:
    print(f"You need a break, {failed_score_count} poor grades.")
else:
    print(f"Average score: {average_score / task_count:.2f}")
    print(f"Number of problems: {task_count}")
    print(f"Last problem: {last_task}")