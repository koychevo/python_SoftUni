first_number = int(input())
second_number = int(input())
operator = input()

even_or_odd = ""
is_divide_by_zero = False
result = 0

if second_number == 0:
    is_divide_by_zero = True

if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/" and second_number != 0:
    result = first_number / second_number
elif operator == "%" and second_number != 0:
    result = first_number % second_number

if is_divide_by_zero:
    print(f"Cannot divide {first_number} by zero")
elif operator == "+" or operator == "-" or operator == "*":
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{first_number} {operator} {second_number} = {result} - {even_or_odd}")
elif operator == "/":
    print(f"{first_number} / {second_number} = {result:.2f}")
elif operator == "%" and second_number != 0:
    print(f"{first_number} % {second_number} = {result}")
