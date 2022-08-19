word = input()

powerful_word = ""
score = 0

while word != "End of words":
    current_score = 0
    first_letter = word[0].lower()
    for i in range(len(word)):
        current_score += ord(word[i])
    if first_letter == "a" or first_letter == "e" or \
    first_letter == "i" or first_letter == "o" or \
    first_letter == "u" or first_letter == "y":
        current_score *= len(word)
    else:
        current_score //= len(word)
    if current_score > score:
        score = current_score
        powerful_word = word
    word = input()

print(f"The most powerful word is {powerful_word} - {score}")
