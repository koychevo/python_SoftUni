def swap(idx1, idx2, arr):
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

def multiply(idx1, idx2, arr):
    arr[idx1] = arr[idx1] * arr[idx2]

def decrease(arr):
    for idx in range(len(arr)):
        arr[idx] -= 1

array = [int(x) for x in input().split(' ')]

command = input()

while command != 'end':
    command = command.split(' ')
    if command[0] == 'swap':
        swap(int(command[1]), int(command[2]), array)
    elif command[0] == 'multiply':
        multiply(int(command[1]), int(command[2]), array)
    elif command[0] == 'decrease':
        decrease(array)
    command = input()


print(', '.join(map(str, array)))