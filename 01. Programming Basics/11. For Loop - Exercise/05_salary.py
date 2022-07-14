tabs_count = int(input())
salary = int(input())

for i in range(tabs_count):
    tab_name = input().lower()
    if tab_name == "facebook":
        salary -= 150
    elif tab_name == "instagram":
        salary -= 100
    elif tab_name == "reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        break;

if salary > 0:
    print(salary)