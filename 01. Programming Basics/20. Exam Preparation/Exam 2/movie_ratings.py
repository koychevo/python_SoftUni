from sys import maxsize

movies_count = int(input())

max_rating = -maxsize
min_rating = maxsize
average_rating = 0
max_rating_movie = ""
min_rating_movie = ""

for movie in range(movies_count):
    movie = input()
    rating = float(input())
    average_rating += rating
    if max_rating < rating:
        max_rating = rating
        max_rating_movie = movie
    if min_rating > rating:
        min_rating = rating
        min_rating_movie = movie


print(f"{max_rating_movie} is with highest rating: {max_rating:.1f}")
print(f"{min_rating_movie} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average_rating / movies_count:.1f}")