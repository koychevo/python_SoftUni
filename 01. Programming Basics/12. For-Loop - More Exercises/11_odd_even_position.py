from sys import maxsize

n = int(input())

odd_sum = 0
even_sum = 0
odd_min = even_min = maxsize
odd_max = even_max = -maxsize

if n <= 1:
    even_min = even_max = odd_min = odd_max = "No"
    if n == 1:
        number = float(input())
        odd_min = odd_max = odd_sum = number
else:
    for i in range(1, n + 1):
        number = float(input())
        if i % 2 == 0:
            even_sum += number
            if even_min > number:
                even_min = number
            if even_max < number:
                even_max = number
        else:
            odd_sum += number
            if odd_min > number:
                odd_min= number
            if odd_max < number:
                odd_max = number

print(f"OddSum={odd_sum:.2f},")
print(f"OddMin={odd_min},") if type(odd_min) == str else print(f"OddMin={odd_min:.2f},")
print(f"OddMax={odd_max},") if type(odd_max) == str else print(f"OddMax={odd_max:.2f},")
print(f"EvenSum={even_sum:.2f},")
print(f"EvenMin={even_min},") if type(even_min) == str else print(f"EvenMin={even_min:.2f},")
print(f"EvenMax={even_max}") if type(even_max) == str else print(f"EvenMax={even_max:.2f}")