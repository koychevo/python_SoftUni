def add_in_the_middle(lst, count):
    elem = '-' + str(count) + 'a'
    middle = len(lst) // 2
    return lst[:middle] + [elem, elem] + lst[middle:]

def is_indexed_valid(lst, length):
    if lst[0] == lst[1]:
        return False
    if lst[0] < 0 or lst[1] < 0:
        return False
    if lst[0] >= length or lst[1] >= length:
        return  False
    return True

sequence = input().split(' ')
line = input()

move_count = 0

while line != 'end':
    indexes = [int(x) for x in line.split(' ')]
    move_count += 1

    if not is_indexed_valid(indexes, len(sequence)):
        sequence = add_in_the_middle(sequence, move_count)
        print('Invalid input! Adding additional elements to the board')
    elif sequence[indexes[0]] != sequence[indexes[1]]:
        print('Try again!')
    elif sequence[indexes[0]] == sequence[indexes[1]]:
        print(f'Congrats! You have found matching elements - {sequence[indexes[0]]}!')
        sequence.pop(min(indexes))
        sequence.pop(max(indexes) - 1)
    if len(sequence) == 0:
        print(f'You have won in {move_count} turns!')
        break
    line = input()
else:
    print('Sorry you lose :(')
    print(' '.join(sequence))

