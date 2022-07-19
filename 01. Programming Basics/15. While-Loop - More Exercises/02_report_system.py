needed_sum = int(input())
line = input()

transactions_count = 0
average_cs = 0
average_cc = 0
average_cs_count = 0
average_cc_count = 0

while line != "End":
    current_sum = int(line)
    transactions_count += 1
    if (transactions_count % 2 == 0 and current_sum < 10) or (transactions_count % 2 != 0 and current_sum > 100):
        print("Error in transaction!");
        line = input()
        continue
    if transactions_count % 2 == 0:
        average_cc += current_sum
        average_cc_count += 1
    else:
        average_cs += current_sum
        average_cs_count += 1
    print("Product sold!")
    if average_cc + average_cs >= needed_sum:
        break
    line = input()

if line == "End":
    print("Failed to collect required money for charity.")
else:
    print(f"Average CS: {average_cs / average_cs_count:.2f}")
    print(f"Average CC: {average_cc / average_cc_count:.2f}")
