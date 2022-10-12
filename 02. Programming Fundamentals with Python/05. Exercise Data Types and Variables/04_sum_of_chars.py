lines_count = int(input())
sum = 0

for _ in range(lines_count):
    character = input()
    sum += ord(character)

print(f'The sum equals: {sum}')
    
