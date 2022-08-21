best_movie = ""
score = 0

for i in range(7):
    movie_name = input()
    if movie_name == "STOP":
        break
    if i == 6:
        print("The limit is reached.")
    length = len(movie_name)
    current_score = 0
    for i in range(length):
        letter = movie_name[i]
        current_score += ord(letter)
        if 97 <= ord(letter) <= 122:
            current_score -= 2 * length
        elif 65 <= ord(letter) <= 90:
            current_score -= length
        if current_score > score:
            score = current_score
            best_movie = movie_name


print(f"The best movie for you is {best_movie} with {score} ASCII sum.")
