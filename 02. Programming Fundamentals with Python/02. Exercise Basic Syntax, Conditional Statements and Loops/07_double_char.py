while True:
    string = input()

    if string == 'End':
        break

    if string == 'SoftUni':
        continue

    double_string = ''

    for idx in range(len(string)):
        double_string += string[idx] * 2
    print(double_string)


