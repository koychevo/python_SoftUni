def characters(a, b):
    string = ''
    for ch in range(ord(a) + 1, ord(b)):
        string += chr(ch) + ' '

    return string

first = input()
second = input()

print(characters(first, second))