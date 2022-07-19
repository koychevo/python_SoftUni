
c_count = 0
o_count = 0
n_count = 0
text = ""
word = ""

symbol = input()

while symbol != "End":
    symbol_to_int = ord(symbol)
    if not (65 <= symbol_to_int <= 90 or 97 <= symbol_to_int <= 122):
        symbol = ""

    if symbol == "c" and c_count == 0:
        c_count += 1
        symbol = ""

    if symbol == "o" and o_count == 0:
        o_count += 1
        symbol = ""

    if symbol == "n" and n_count == 0:
        n_count += 1
        symbol = ""

    if c_count == o_count == n_count == 1:
        text += word + " "
        word = ""
        c_count = o_count = n_count = 0
    word += symbol
    symbol = input()

print(text)