def digit_sums(num):
    sums = []
    sums.append(0)
    sums.append(0)
    while num > 0:
        digit = num % 10
        if digit % 2 != 0:
            sums[0] += digit
        else:
            sums[1] += digit
        num //= 10

    return sums

number = int(input())
sums = digit_sums(number)
print(f'Odd sum = {sums[0]}, Even sum = {sums[1]}')
