tickets_count = 0
student_tickets_count = 0
standard_tickets_count = 0
kid_tickets_count = 0

movie = input()

while movie != "Finish":
    free_places_count = int(input())
    current_movie_tickets_count = 0

    while current_movie_tickets_count < free_places_count:
        ticket_type = input()
        if ticket_type == "End":
            break
        if ticket_type == "student":
            student_tickets_count += 1
        elif ticket_type == "standard":
            standard_tickets_count += 1
        elif ticket_type == "kid":
            kid_tickets_count += 1
        current_movie_tickets_count += 1
    tickets_count += current_movie_tickets_count
    print(f"{movie} - {current_movie_tickets_count / free_places_count *100:.2f}% full.")
    movie = input()

print(f"Total tickets: {tickets_count}")
print(f"{student_tickets_count / tickets_count * 100:.2f}% student tickets.")
print(f"{standard_tickets_count / tickets_count * 100:.2f}% standard tickets.")
print(f"{kid_tickets_count / tickets_count * 100:.2f}% kids tickets.")