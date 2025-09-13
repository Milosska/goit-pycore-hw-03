import re

# Function that normalizes Ukrainian phone numbers to the format +380XXXXXXXXX
def normalize_phone(phone_number: str) -> str:
    # Remove all non-numeric characters except the leading '+'
    pattern = r"\+|\d+"
    matches = re.findall(pattern, phone_number)
    cleaned_number = ''.join(matches)

    # Ccheck the number begining and add missing parts
    if not cleaned_number.startswith('+'):
        cleaned_number = '+' + cleaned_number

    if cleaned_number.find('3') != 1:
        cleaned_number = cleaned_number.replace('+', '+3', 1)

    if cleaned_number.find('8') != 2:
        cleaned_number = cleaned_number.replace('+3', '+38', 1)

    return cleaned_number

# Test cases for the function normalize_phone
assert normalize_phone("067\t123 4567") == "+380671234567"
assert normalize_phone("(095) 234-5678\n") == "+380952345678"
assert normalize_phone("+380 44 123 4567") == "+380441234567"
assert normalize_phone("380501234567") == "+380501234567"
assert normalize_phone("    +38(050)123-32-34") == "+380501233234"
assert normalize_phone("     0503451234") == "+380503451234"
assert normalize_phone("(050)8889900") == "+380508889900"
assert normalize_phone("38050-111-22-22") == "+380501112222"
assert normalize_phone("38050 111 22 11   ") == "+380501112211"
assert normalize_phone("     +0503451234") == "+380503451234"