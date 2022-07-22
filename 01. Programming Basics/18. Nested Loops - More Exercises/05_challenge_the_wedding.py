men_count = int(input())
women_count = int(input())
tables_count = int(input())

is_free_tables = True
combinations_count = 0
result = ""

for man in range(1, men_count + 1):
    if not is_free_tables:
        break
    for woman in range(1, women_count + 1):
        combinations_count += 1
        if combinations_count > tables_count:
            is_free_tables = False
            break
        result += "(" + str(man) + " <-> " + str(woman) + ") "

print(result)