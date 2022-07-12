exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time_in_minutes = 60 * exam_hour + exam_minutes
arrival_time_in_minutes = 60 * arrival_hour + arrival_minutes

time_difference = exam_time_in_minutes - arrival_time_in_minutes

mins_diff = abs(time_difference) % 60
hours_diff = abs(time_difference) // 60

if time_difference > 30:
    print("Early")
    if hours_diff > 0:
        if mins_diff < 10:
            mins_diff = "0" + str(mins_diff)
        print(f"{hours_diff}:{mins_diff} hours before the start")
    else:
        print(f"{mins_diff} minutes before the start")
elif time_difference > 0:
    print("On time")
    print(f"{mins_diff} minutes before the start")
elif time_difference == 0:
    print("On time")
else:
    print("Late")
    if hours_diff > 0:
        if mins_diff < 10:
            mins_diff = "0" + str(mins_diff)
        print(f"{hours_diff}:{mins_diff} hours after the start")
    else:
        print(f"{mins_diff} minutes after the start")

