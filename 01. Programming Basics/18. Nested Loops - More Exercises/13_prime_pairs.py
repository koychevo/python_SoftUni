first_pair_start = int(input())
second_pair_start = int(input())
first_pair_diff = int(input())
second_pair_diff = int(input())

for first_pair in range(first_pair_start, first_pair_start + first_pair_diff + 1):
    is_first_pair_prime = True
    for i in range(2, first_pair):
        if first_pair % i == 0:
            is_first_pair_prime = False
            break
    if not is_first_pair_prime:
        continue

    for second_pair in range(second_pair_start, second_pair_start + second_pair_diff + 1):
        is_second_pair_prime = True
        for i in range(2, second_pair):
            if second_pair % i == 0:
                is_second_pair_prime = False
                break
        if not is_second_pair_prime:
            continue
        if is_first_pair_prime and is_second_pair_prime:
            print(f"{first_pair}{second_pair}")
