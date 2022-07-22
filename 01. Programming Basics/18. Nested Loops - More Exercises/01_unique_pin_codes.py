first_digit_limit = int(input())
second_digit_limit = int(input())
third_digit_limit = int(input())

isPrime = True;

if second_digit_limit > 7:
    second_digit_limit = 7

for first_digit in range(2, first_digit_limit + 1, 2):
    for second_digit in range(2, second_digit_limit + 1):
        for digit in range(2, second_digit):
            isPrime = True
            if second_digit % digit == 0:
                isPrime = False
                break
        for third_digit in range(2, third_digit_limit + 1, 2):
            if isPrime:
                print(f"{first_digit} {second_digit} {third_digit}")