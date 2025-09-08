import re
from datetime import datetime

# Helper function to check if the date string is given in the valid format
def check_format(date_string: str) -> bool:
    valid_format_regex = r'\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])'
    result = re.fullmatch(valid_format_regex, date_string)
    return result is not None

# Main function to check difference in days between given date and today
def get_days_from_today(date: str) -> int:
    try:
        is_format_valid = check_format(date)
        if not is_format_valid:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

    except ValueError:
        print(f"ValueError: {date} is not a valid date format. Please use 'YYYY-MM-DD'.")

    else:
        converted_date = datetime.strptime(date, "%Y-%m-%d")
        today_date = datetime.today()
        difference = today_date - converted_date    
        return difference.days

# Test cases for the function check_format
assert check_format('2023-10-01') == True
assert check_format('2023-20-01') == False # month must be in 1..12
assert check_format('2023-10-45') == False # day must be in 1..31
assert check_format('23-10-01') == False # year must be in 4 digits
assert check_format('03-10-2023') == False # wrong order
assert check_format('qwer-20-w1') == False # string includes letters

# Test cases for the function get_days_from_today
assert isinstance(get_days_from_today('2021-05-05'), int) # past date
assert get_days_from_today('2021-05-05') > 0
assert isinstance(get_days_from_today('2027-01-01'), int) # future date
assert get_days_from_today('2027-01-01') < 0
assert get_days_from_today('20-10-01') == None # invalid format