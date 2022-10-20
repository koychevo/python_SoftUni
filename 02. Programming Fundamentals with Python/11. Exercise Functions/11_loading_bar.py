def loading_bar(num):
    if num == 100:
        print(f'{num}% Complete!')
        print(f'[{"%" * (num // 10)}]')
    else:
        print(f'{num}% [{"%" * (num // 10)}{"." * ((100 - num) // 10)}]')
        print('Still loading...')

number = int(input())

loading_bar(number)