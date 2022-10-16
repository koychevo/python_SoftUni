meercat = []

for _ in range(3):
    meercat.append(input())

meercat[0], meercat[2] = meercat[2], meercat[0]

print(meercat)
