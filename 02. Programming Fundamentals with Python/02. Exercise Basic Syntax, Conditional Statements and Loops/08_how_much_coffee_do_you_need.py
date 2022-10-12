coffee_count = 0
while True:
    event = input()

    if event == 'END':
        break
    if event.lower() not in ['coding', 'cat', 'dog', 'movie']:
        continue

    if event.isupper():
        coffee_count += 2
    elif event.islower():
        coffee_count += 1

    if coffee_count > 5:
        print('You need extra sleep')
        break

if coffee_count < 6:
    print(f'{coffee_count}')
