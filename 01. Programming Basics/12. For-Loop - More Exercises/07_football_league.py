capacity = int(input())
fans_count = int(input())

sector_a_count = 0
sector_b_count = 0
sector_v_count = 0
sector_g_count = 0

for i in range(fans_count):
    current_sector = input()
    if current_sector == "A":
        sector_a_count += 1
    elif current_sector == "B":
        sector_b_count += 1
    elif current_sector == "V":
        sector_v_count += 1
    elif current_sector == "G":
        sector_g_count += 1

print(f"{sector_a_count / fans_count * 100:.2f}%")
print(f"{sector_b_count / fans_count * 100:.2f}%")
print(f"{sector_v_count / fans_count * 100:.2f}%")
print(f"{sector_g_count / fans_count * 100:.2f}%")
print(f"{fans_count / capacity * 100:.2f}%")