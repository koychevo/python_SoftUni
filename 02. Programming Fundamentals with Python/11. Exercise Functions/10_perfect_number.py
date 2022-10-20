def sum_divisors(num):
    sum = 0
    for n in range(1, num):
        if num % n == 0:
            sum += n
    return sum

def is_perfect_number(number):
    if number == sum_divisors(number):
        return True
    return False

num = int(input())

if is_perfect_number(num):
    print('We have a perfect number!')
else:
    print('It\'s not so perfect.')
