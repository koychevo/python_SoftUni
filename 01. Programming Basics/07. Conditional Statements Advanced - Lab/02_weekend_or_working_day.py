day = input()

if day == "Saturday" or day == "Sunday":
    print("Weekend")
elif day == "Monday" or \
        day == "Tuesday" or \
        day == "Wednesday" or \
        day == "Thursday" or \
        day == "Friday":
    print("Working day")
else:
    print("Error")


# if day in ["Saturday", "Sunday"]:
#     print("Weekend")
# elif day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
#     print("Working day")
# else:
#     print("Error")