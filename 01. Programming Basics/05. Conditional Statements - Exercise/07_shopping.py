budget = float(input())
videocards_count = int(input())
processors_count = int(input())
ram_memories_count = int(input())

videocard_price = 250
videocards_expenses = videocard_price * videocards_count
processors_price = 0.35 * videocards_expenses
processors_expenses = processors_price * processors_count
ram_memory_price = 0.1 * videocards_expenses
ram_memory_expenses = ram_memory_price * ram_memories_count

total_expenses = videocards_expenses + processors_expenses + ram_memory_expenses

if processors_count < videocards_count:
    total_expenses *= 0.85

money_left = budget - total_expenses

if money_left < 0:
    print(f"Not enough money! You need {-money_left:.2f} leva more!")
else:
    print(f"You have {money_left:.2f} leva left!")