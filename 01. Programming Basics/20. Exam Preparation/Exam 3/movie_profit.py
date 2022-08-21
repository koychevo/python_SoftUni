movie = input()
days = int(input())
tickets_count = int(input())
ticket_price = float(input())
cinema_percentage = int(input())

profit = days * tickets_count * ticket_price * (100 - cinema_percentage) / 100
print(f"The profit from the movie {movie} is {profit:.2f} lv.")
