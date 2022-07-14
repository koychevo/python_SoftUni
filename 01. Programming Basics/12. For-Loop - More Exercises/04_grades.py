students_count = int(input())

average_grade = 0.0
top_students_count = 0
very_good_students_count = 0
good_students_count = 0
failed_students_count = 0


for i in range(students_count):
    grade = float(input())
    average_grade += grade
    if 2 <= grade <= 2.99:
        failed_students_count += 1
    elif grade <= 3.99:
        good_students_count += 1
    elif grade <= 4.99:
        very_good_students_count += 1
    elif grade >= 5:
        top_students_count += 1

average_grade /= students_count

print(f"Top students: {top_students_count / students_count * 100:.2f}%")
print(f"Between 4.00 and 4.99: {very_good_students_count / students_count * 100:.2f}%")
print(f"Between 3.00 and 3.99: {good_students_count / students_count * 100:.2f}%")
print(f"Fail: {failed_students_count / students_count * 100:.2f}%")
print(f"Average: {average_grade:.2f}")