lines_count = int(input())

nums = []

for _ in range(lines_count):
    nums.append(int(input()))

command = input()

filter_nums = []

for num in nums:

    condition_command = (
            (command == "even" and num % 2 == 0) or
            (command == "odd" and num % 2 != 0) or
            (command == "positive" and num >= 0) or
            (command == "negative" and num < 0)
    )

    if condition_command:
        filter_nums.append(num)

print(filter_nums)
