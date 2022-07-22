first_number = int(input())
second_number = int(input())
line = ""

for num in range(first_number, second_number + 1):

    num_to_string = str(num)
    odd_sum = 0
    even_sum = 0
    for i in range(len(num_to_string)):
        if i % 2 == 0:
            even_sum += int(num_to_string[i])
        else:
            odd_sum += int(num_to_string[i])
    if odd_sum == even_sum:
        line += num_to_string + " "
if line != "":
    print(line)