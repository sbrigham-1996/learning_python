# 06_exception_handling.py
# Chapter 3 — Exception Handling with try and except
#
# When Python hits an error it raises an exception and crashes.
# try/except lets you catch that error and handle it gracefully instead.


# --- Example 1: The crash without handling ---
# This is what happens when you don't handle an exception.
# Python raises ZeroDivisionError and the program stops immediately.

# print(10 / 0)   # uncomment to see: ZeroDivisionError: division by zero


# --- Example 2: Catching a specific exception ---
# Wrapping risky code in try/except lets you respond to the error
# instead of crashing. Only the specific exception type listed is caught.

def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print('Error: cannot divide by zero.')
        return None

print(divide(10, 2))   # 5.0
print(divide(10, 0))   # prints the error message, returns None


# --- Example 3: Catching ValueError for bad input ---
# int() raises ValueError when you pass it something it cannot convert.
# This is extremely common when working with user input.

def parse_age(value):
    try:
        age = int(value)
        return age
    except ValueError:
        print(f'"{value}" is not a valid age.')
        return None

print(parse_age('25'))      # 25
print(parse_age('abc'))     # "abc" is not a valid age.
print(parse_age('30.5'))    # "30.5" is not a valid age. (int() won't accept a decimal string)


# --- Example 4: Catching multiple exception types ---
# You can handle different errors differently by stacking except blocks.
# Python checks them in order and runs the first one that matches.

def safe_index(a_list, index):
    try:
        return a_list[index]
    except IndexError:
        print(f'Index {index} is out of range.')
        return None
    except TypeError:
        print(f'Index must be an integer, got {type(index).__name__}.')
        return None

my_list = ['a', 'b', 'c']
print(safe_index(my_list, 1))      # b
print(safe_index(my_list, 10))     # Index 10 is out of range.
print(safe_index(my_list, 'one'))  # Index must be an integer, got str.


# --- Example 5: The else clause ---
# try/except can have an optional else block.
# else runs only if the try block succeeded — no exception was raised.
# This keeps your "success" code separate from your "risky" code.

def load_number(value):
    try:
        number = int(value)
    except ValueError:
        print(f'Could not convert "{value}" to an integer.')
    else:
        print(f'Success! The number is {number}.')   # only runs if no exception

load_number('42')    # Success! The number is 42.
load_number('oops')  # Could not convert "oops" to an integer.


# --- Example 6: Exception handling inside a loop (retry pattern) ---
# A common real-world pattern: keep asking until you get valid input.
# try/except inside a while loop lets you reject bad input and try again.

def get_positive_number():
    while True:
        raw = input('Enter a positive number: ')
        try:
            number = int(raw)
            if number <= 0:
                print('Please enter a number greater than zero.')
                continue      # go back to the top of the loop
            return number     # valid input — exit the loop and return
        except ValueError:
            print(f'"{raw}" is not a number. Try again.')

# Uncomment to run interactively:
# result = get_positive_number()
# print('You entered:', result)
