def even_number(num):
    if num % 2 == 0:
        return True
    return False

nums = [int(x) for x in input().split(' ')]
nums = list(filter(even_number, nums))

print(nums)