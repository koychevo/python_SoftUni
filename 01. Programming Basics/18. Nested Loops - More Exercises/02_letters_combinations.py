first_letter = input()
second_letter = input()
third_letter = input()

start = ord(first_letter)
end = ord(second_letter) + 1

combinations_count = 0;
result = ""
for first in range(start, end):
    for second in range(start, end):
        for third in range(start, end):
            if first != ord(third_letter) and second != ord(third_letter) and third != ord(third_letter):
                combinations_count += 1
                result += chr(first) + chr(second) + chr(third) + " "


print(result + str(combinations_count))
