factor = int(input())
count = int(input())

nums = []
num = 0

for _ in range(count):
    num += factor
    nums.append(num)

print(nums)