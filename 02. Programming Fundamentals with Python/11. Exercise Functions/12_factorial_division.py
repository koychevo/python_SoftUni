    def factorial(num):
        fact = 1
        for n in range(2, num + 1):
            fact *= n
        return fact

    def division(a, b):
        return factorial(a) / factorial(b)

    first = int(input())
    second = int(input())

    print(f'{division(first, second) :.2f}')
