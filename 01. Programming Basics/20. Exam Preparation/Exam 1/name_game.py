name = input()

winner_name = ""
winner_score = 0

while name != "Stop":
    current_score = 0
    for i in range(len(name)):
        number = int(input())
        if number == ord(name[i]):
            current_score += 10
        else:
            current_score += 2
    if current_score >= winner_score:
        winner_score = current_score
        winner_name = name
    name = input()

print(f"The winner is {winner_name} with {winner_score} points!")