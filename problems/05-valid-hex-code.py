# Create a function that determines whether a string is a valid hex code.

# A hex code must begin with a pound key # and is exactly 6 characters in
# length. Each character must be a digit from 0-9 or an alphabetic character
# from A-F. All alphabetic characters may be uppercase or lowercase.

# Write your function here.
def is_valid_hex_code(code):
    hexCode = '1234567890abcdef'
    try:
        if code[0] == '#' and len(code) == 7:
            for letter in code[1:]:
                if letter.lower() not in hexCode:
                    return False
            return True
        return False
    except:
        pass

print(is_valid_hex_code("#CD5C5C"))  #> True
print(is_valid_hex_code("#EAECEE"))  #> True
print(is_valid_hex_code("#eaecee"))  #> True

print(is_valid_hex_code("#CD5C58C"))
# Prints False
# Length exceeds 6

print(is_valid_hex_code("#CD5C5Z"))
# Prints False
# Not all alphabetic characters in A-F

print(is_valid_hex_code("#CD5C&C"))
# Prints false
# Contains unacceptable character

print(is_valid_hex_code("CD5C5C"))
# Prints False
# Missing #
