def is_palindrome(number):
    number_to_string = str(number)
    for idx in range(len(number_to_string) // 2):
        if number_to_string[idx] != number_to_string[len(number_to_string) - 1 - idx]:
            return False
    return True

nums = [int(x) for x in input().split(', ')]

for num in nums:
    print(is_palindrome(num))
