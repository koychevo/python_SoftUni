first_limit = int(input())
second_limit = int(input())
third_limit = int(input())

for first_digit in range(2, first_limit + 1, 2):
    for second_digit in range(1, second_limit + 1):
        for third_digit in range(2, third_limit + 1, 2):
            if second_digit in [2, 3, 5, 7]:
                print(f"{first_digit} {second_digit} {third_digit}")

