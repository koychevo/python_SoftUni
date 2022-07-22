number = int(input())

special_numbers = ""

for num in range(1111, 10000):
    num_to_string = str(num)
    is_special_number = True
    for i in range(len(num_to_string)):
        if int(num_to_string[i]) == 0 or number % int(num_to_string[i]) != 0:
            is_special_number = False
            break
    if is_special_number:
        special_numbers += num_to_string + " "

print(special_numbers)