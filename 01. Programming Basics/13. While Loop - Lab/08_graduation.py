name = input()

average_grade = 0.0
grade_class = 1
unsuccessful_evaluation = 0

while grade_class < 13:
    evaluation = float(input())
    if evaluation < 4:
        unsuccessful_evaluation += 1
        if unsuccessful_evaluation == 2:
            break;
        continue
    average_grade += evaluation
    grade_class += 1

if unsuccessful_evaluation == 2:
    print(f"{name} has been excluded at {grade_class} grade")
else:
    print(f"{name} graduated. Average grade: {average_grade / 12:.2f}")