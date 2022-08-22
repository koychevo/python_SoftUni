customers_count = int(input())

back_count = 0
chest_count = 0
legs_count = 0
abs_count = 0
protein_shake_count = 0
protein_bar_count = 0

for i in range(customers_count):
    program_type = input()
    if program_type == "Back":
        back_count += 1
    elif program_type == "Chest":
        chest_count += 1
    elif program_type == "Legs":
        legs_count += 1
    elif program_type == "Abs":
        abs_count += 1
    elif program_type == "Protein shake":
        protein_shake_count += 1
    else:
        protein_bar_count += 1

print(f"{back_count} - back")
print(f"{chest_count} - chest")
print(f"{legs_count} - legs")
print(f"{abs_count} - abs")
print(f"{protein_shake_count} - protein shake")
print(f"{protein_bar_count} - protein bar")
print(f"{(back_count + chest_count + legs_count + abs_count) / customers_count * 100:.2f}% - work out")
print(f"{(protein_shake_count + protein_bar_count) / customers_count * 100 :.2f}% - protein")