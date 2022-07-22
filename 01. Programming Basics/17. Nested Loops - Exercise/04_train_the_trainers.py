jury_count = int(input())

presentation_name = input()
presentations_count = 0
final_assessment = 0

while presentation_name != "Finish":
    average_note = 0
    presentations_count += 1
    for notes_count in range(jury_count):
        note = float(input())
        average_note += note
    average_note /= jury_count
    print(f"{presentation_name} - {average_note:.2f}.")
    final_assessment += average_note
    presentation_name = input()

final_assessment /= presentations_count
print(f"Student's final assessment is {final_assessment:.2f}.")
