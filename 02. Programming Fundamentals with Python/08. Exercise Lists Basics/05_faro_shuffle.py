cards = input().split(' ')
shuffles_count = int(input())

middle = len(cards) // 2

for _ in range(shuffles_count):
    left_side = cards[1:middle]
    right_side = cards[middle:len(cards)]
    idx = 1
    for i in range(middle - 1):
        cards[idx] = right_side[i]
        cards[idx + 1] = left_side[i]
        idx += 2

print(cards)
