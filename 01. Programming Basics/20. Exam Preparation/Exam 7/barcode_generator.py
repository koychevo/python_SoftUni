#start_number = int(input())
#end_number = int(input())

start_in_string = input() #str(start_number)
end_in_string = input() #str(end_number)

first_a = int(start_in_string[0])
first_b = int(start_in_string[1])
first_c = int(start_in_string[2])
first_d = int(start_in_string[3])


if first_a % 2 == 0:
    first_a += 1

if first_b % 2 == 0:
    first_b += 1

if first_c % 2 == 0:
    first_c += 1

if first_d % 2 == 0:
    first_d += 1

end_a = int(end_in_string[0])
end_b = int(end_in_string[1])
end_c = int(end_in_string[2])
end_d = int(end_in_string[3])

for a in range(first_a, end_a + 1, 2):
    for b in range(first_b, end_b + 1, 2):
        for c in range(first_c, end_c + 1, 2):
            for d in range(first_d, end_d + 1, 2):
                print(1000 * a + 100 * b + 10 * c + d, end = " ")