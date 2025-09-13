import random

# Helper function to check if input parameters are valid. 
# Checks all given params and informs the user what specofocally should be updated
def check_input_params(min:int, max:int, quantity:int) -> bool:
    # Check if all params have the integer type
    are_params_int = isinstance(min, int) and isinstance(max, int) and isinstance(quantity, int)
    if not are_params_int:
        print("All parameters must be integers.")
        return are_params_int

    # Check if min parameter is valid. Return False if the check fails
    is_min_valid = min >=1 and min < max
    if not is_min_valid:
        print("Invalid min parameter. Please, provide number that is greater then 0 and less than max.")
        return is_min_valid
    
    # Check if max parameter is valid
    is_max_valid = max <= 1000 and max > min
    if not is_max_valid:
        print("Invalid max parameter. Please, provide number that is less then 1001 and greater than min.")
        return is_max_valid
    
     # Check if quantity parameter is valid
    is_quantity_valid = max >= quantity >= 1
    if not  is_quantity_valid:
        print("Invalid quantity parameter. Please, provide number that is more then 0 and less than or equal to max.")
        return is_quantity_valid
    
    # If all parameters are valid, return True
    return True

# Main function to generate a set of unique random numbers for lottery ticket
def get_numbers_ticket(min:int, max:int, quantity:int) -> list[int]:
    # Check if input parameters are valid. If not - stop exectiong the function
    is_params_valid = check_input_params(min, max, quantity)
    if not is_params_valid:
        return
    
    # Create an empty set to store unique numbers
    unique_numbers = set()

    # Generate unique random numbers until the set reaches the desired quantity
    while len(unique_numbers) < quantity:
        generated_number = random.randrange(min, max + 1)
        unique_numbers.add(generated_number)

    # Return a sorted list of unique numbers
    return sorted(unique_numbers)

# Test cases for the function check_format
assert check_input_params(1, 49, 6) == True
assert check_input_params('24', 36, 5) == False # min must be int
assert check_input_params(0, 49, 6) == False # min must be >= 1
assert check_input_params(1, 1001, 6) == False # max must be <= 1000
assert check_input_params(50, 49, 6) == False # min must be < max
assert check_input_params(1, 49, 50) == False # quantity must be less or equal to max

# Test cases for the function get_numbers_ticket
assert get_numbers_ticket(15, '49', 5) == None # invalid params
numbers = get_numbers_ticket(1, 10, 5)
assert isinstance(numbers, list) # valid params
assert len(numbers) == 5 # quantity of numbers in the set is correct
assert numbers == sorted(numbers) # numbers in the set are sorted
assert get_numbers_ticket(1, 10, 5)!= get_numbers_ticket(1, 10, 5) # each call returns different set of numbers
assert len(get_numbers_ticket(1, 1000, 100)) == len(set(get_numbers_ticket(1, 1000, 100))) # all numbers in the set are unique
