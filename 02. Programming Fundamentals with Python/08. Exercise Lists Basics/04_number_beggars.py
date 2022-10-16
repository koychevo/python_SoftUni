nums = [int(x) for x in input(). split(', ')]
beggars_count = int(input())

if beggars_count == len(nums):
    print(nums)
    exit()

if beggars_count > len(nums):
    for _ in range(beggars_count - len(nums)):
        nums.append(0)
    print(nums)
    exit()


beggars = []

for idx in range(beggars_count):
    sum = 0
    current_idx = idx

    while current_idx < len(nums):
        sum += nums[current_idx]
        current_idx += beggars_count

    beggars.append(sum)

print(beggars)