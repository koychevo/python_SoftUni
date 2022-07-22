input_line = input()
sum_prime = 0
sum_non_prime = 0


while input_line != "stop":
    number = int(input_line)
    is_prime = True
    if number < 0:
        print("Number is negative.")
        input_line = input()
        continue
    for num in range(2, number):
        if number % num == 0:
            is_prime = False
            sum_non_prime += number
            break
    if is_prime:
        sum_prime += number
    input_line = input()

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")