def contains_only_digit_or_letter(pwd):
    for ch in pwd:
        if not 48 <= ord(ch) <= 57 and not 97 <= ord(ch.lower()) <= 122:
            return False
    return True

def count_digits(pwd):
    count = 0
    for ch in pwd:
        if 48 <= ord(ch) <= 57:
            count += 1
    return count

def is_pasword_valid(pwd):
    is_valid = True

    if len(pwd) < 6 or len(pwd) > 10:
        print('Password must be between 6 and 10 characters')
        is_valid = False

    if not contains_only_digit_or_letter(pwd):
        print('Password must consist only of letters and digits')
        is_valid = False

    if count_digits(pwd) < 2:
        print('Password must have at least 2 digits')
        is_valid = False

    if is_valid:
        print('Password is valid')

password = input()
is_pasword_valid(password)