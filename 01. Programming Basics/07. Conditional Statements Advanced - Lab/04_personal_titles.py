age = float(input())
gender = input()
personal_title = ""

if gender == "m":
    personal_title = "Master" if age < 16 else "Mr."
else:
    personal_title = "Miss" if age < 16 else "Ms."

print(personal_title)