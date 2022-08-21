first_number = int(input())
second_number = int(input())
third_number = int(input())

for first in range(first_number, second_number):
    for second in range(1, third_number):
        for third in range(1, int(third_number / 2)):
            if first % 2 != 0 and (second + third + first) % 2 != 0:
                print(f"{chr(first)}-{second}{third}{first}")