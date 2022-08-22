height = int(input())

is_failed = False
jumps_count = 0
current_height = height - 30

while current_height <= height:
    for i in range(3):
        current_jump = int(input())
        jumps_count += 1
        if current_jump > current_height:
            current_height += 5
            break
        if i == 2:
            is_failed = True
    if is_failed:
        print(f"Tihomir failed at {current_height}cm after {jumps_count} jumps.")
        break

if not is_failed:
    print(f"Tihomir succeeded, he jumped over {height}cm after {jumps_count} jumps.")
