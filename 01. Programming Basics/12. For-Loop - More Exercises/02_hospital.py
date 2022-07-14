days = int(input())

doctors_count = 7
treated_patient_count = 0
untreated_patient_count = 0

for day in range(1, days + 1):
    patients_count = int(input())
    if day % 3 == 0 and untreated_patient_count > treated_patient_count:
        doctors_count += 1
    if patients_count > doctors_count:
        untreated_patient_count += patients_count - doctors_count
        treated_patient_count += doctors_count
    else:
        treated_patient_count += patients_count

print(f"Treated patients: {treated_patient_count}.")
print(f"Untreated patients: {untreated_patient_count}.")