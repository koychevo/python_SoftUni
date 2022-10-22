def shoot(idx, power, lst):
    if not 0 <= idx < len(lst):
        return
    lst[idx] -= power
    if lst[idx] <= 0:
        del lst[idx]

def add(idx, power, lst):
    if not 0 <= idx < len(lst):
        print('Invalid placement!')
        return
    lst = lst[:idx] + [power] + lst[idx:]

def strike(idx, radius, lst):
    if idx - radius < 0 or idx + radius >= len(lst):
        print('Strike missed!')
        return
    del lst[idx-radius: idx+radius+1]

targets = [int(x) for x in input().split()]

line = input()

while line != 'End':
    commands = line.split()
    if commands[0] == 'Shoot':
        shoot(int(commands[1]), int(commands[2]), targets)
    elif commands[0] == 'Add':
        add(int(commands[1]), int(commands[2]), targets)
    elif commands[0] == 'Strike':
        strike(int(commands[1]), int(commands[2]), targets)
    line = input()
else:
    print('|'.join(map(str, targets)))
    exit()