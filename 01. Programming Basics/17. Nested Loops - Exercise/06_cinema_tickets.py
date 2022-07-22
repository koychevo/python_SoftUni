movie_name = input()

standard_tickets = 0
student_tickets = 0
kid_tickets = 0


while movie_name != "Finish":
    seat_count = int(input())
    current_tickets_count = 0
    current_capacity = seat_count
    while seat_count > 0:
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1
        seat_count -= 1
        current_tickets_count += 1
    print(f"{movie_name} - {current_tickets_count / current_capacity * 100:.2f}% full.")
    movie_name = input()

tickets_count = standard_tickets + student_tickets + kid_tickets
print(f"Total tickets: {tickets_count}")
print(f"{student_tickets / tickets_count * 100:.2f}% student tickets.")
print(f"{standard_tickets / tickets_count * 100:.2f}% standard tickets.")
print(f"{kid_tickets / tickets_count * 100:.2f}% kids tickets.")