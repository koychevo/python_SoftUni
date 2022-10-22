def check_wagons(lift, limit):
    for idx in range(len(lift)):
        if lift[idx] < limit:
            return True
    return False

people_count = int(input())
lift_state = [int(x) for x in input().split(' ')]

limit = 4

for idx in range(len(lift_state)):
    if people_count == 0:
        break
    current_free_places = limit - lift_state[idx]

    if current_free_places > 0 and people_count < current_free_places:
        current_free_places = people_count

    lift_state[idx] += current_free_places
    people_count -= current_free_places

if people_count == 0 and check_wagons(lift_state, limit):
    print('The lift has empty spots!')
elif people_count > 0 and not check_wagons(lift_state, limit):
    print(f'There isn\'t enough space! {people_count} people in a queue!')

print(' '.join(map(str, lift_state)))
