def manipulate_targets(idx, lst):
    for i in range(len(lst)):
        if lst[i] != -1 and i != idx:
            if lst[i] > lst[idx]:
                lst[i] -= lst[idx]
            else:
                lst[i] += lst[idx]

targets = [int(x) for x in input().split()]

targets_count = 0

line = input()

while line != 'End':
    idx = int(line)

    if 0 <= idx < len(targets) and targets[idx] != -1:
        manipulate_targets(idx, targets)
        targets_count += 1
        targets[idx] = -1

    line = input()

print(f'Shot targets: {targets_count} -> {" ".join(map(str, targets))}')