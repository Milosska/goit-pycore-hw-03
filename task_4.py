from datetime import datetime, timedelta

# Helper function to move weekend birthdays to Monday
def process_weekend_birthday(birthday_date: datetime) -> datetime:
    day_of_week = birthday_date.weekday()

    if day_of_week == 5:  
        one_day_interval = timedelta(days=2)
        birthday_date += one_day_interval
    elif day_of_week == 6:
        two_days_interval = timedelta(days=1)
        birthday_date += two_days_interval
    
    return birthday_date

# Main function to get upcoming birthdays
def get_upcoming_birthdays(users: list) -> list:
    # Create a list to store the processed data
    upcoming_birthdays = []

    # Get the current date
    current_date = datetime.today().date()

    for user in users:
        # Check is user's birthday already passed this year
        current_user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        current_user_birthday_this_year = datetime(year=current_date.year, month=current_user_birthday.month, day=current_user_birthday.day).date()
        is_birthday_this_year_passed = current_user_birthday_this_year < current_date
        
         # Check user's birthday has already passed, set the birthday to next year
        if is_birthday_this_year_passed:
             current_user_birthday_this_year = datetime(year=current_date.year + 1, month=current_user_birthday.month, day=current_user_birthday.day).date()

        # Process only users with birthdays in the next 7 days
        days_until_birthday  = (current_user_birthday_this_year - current_date).days
        if days_until_birthday <= 7:
           # If birthday falls on Saturday or Sunday, move it to Monday
           current_user_birthday_this_year = process_weekend_birthday(current_user_birthday_this_year)

           # Update the list with the processed data
           upcoming_birthdays.append({"name": user["name"], "congratulation_date" : datetime.strftime(current_user_birthday_this_year, "%Y.%m.%d")})   

    return upcoming_birthdays


# Test cases for the function process_weekend_birthday
assert process_weekend_birthday(datetime.strptime("2025.09.13", "%Y.%m.%d")) == datetime.strptime("2025.09.15", "%Y.%m.%d")
assert process_weekend_birthday(datetime.strptime("2025.09.12", "%Y.%m.%d")) == datetime.strptime("2025.09.12", "%Y.%m.%d")

# Test cases for the function get_upcoming_birthdays (as for 2025-09-14)
users = [
    {"name": "John Doe", "birthday": "1985.01.23"}, 
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Ray Charles", "birthday": "1965.09.11"},
    {"name": "Tom Hiddleston", "birthday": "1989.09.14"},
    {"name": "Hanna Montana", "birthday": "1999.09.20"},
    {"name": "Harry Potter", "birthday": "1987.09.18"},
    {"name": "Ron Weasley", "birthday": "1988.09.19"},
    {"name": "Hermione Granger", "birthday": "1989.09.21"},
]
upcoming_birthdays_test = get_upcoming_birthdays(users)
assert upcoming_birthdays_test == [{'name': 'Tom Hiddleston', 'congratulation_date': '2025.09.15'}, {'name': 'Hanna Montana', 'congratulation_date': '2025.09.22'}, {'name': 'Harry Potter', 'congratulation_date': '2025.09.18'}, {'name': 'Ron Weasley', 'congratulation_date': '2025.09.19'}, {'name': 'Hermione Granger', 'congratulation_date': '2025.09.22'}]
