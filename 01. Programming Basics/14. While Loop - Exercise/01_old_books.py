searched_book = input()
book_title = input()
is_book_found = False
books_count = 0

while book_title != "No More Books":
    if book_title == searched_book:
        is_book_found = True
        break
    books_count += 1
    book_title = input()

if is_book_found:
    print(f"You checked {books_count} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {books_count} books.")