numbers = [int(x) for x in input().split(' ')]

average = sum(numbers) / len(numbers)

result = filter(lambda x: x > average, numbers)

result = sorted(result, reverse=True)

if len(result) == 0:
    print('No')
elif len(result) > 5:
    print(' '.join(map(str, result[:5])))
else:
    print(' '.join(map(str, result)))
