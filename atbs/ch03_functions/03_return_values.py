# 03_return_values.py
# Chapter 3 — Return Values and the return Statement
#
# A function can send a value back to the caller using return.
# That returned value can be stored, printed, passed to another function, etc.


# --- Example 1: A basic return value ---
# This function takes a number and returns its double.
# The caller decides what to do with the result.

def double(number):
    return number * 2

result = double(5)
print(result)         # 10
print(double(3) + 1)  # 7 — you can use the return value directly in expressions


# --- Example 2: None is returned when you don't use return ---
# If a function has no return statement, Python silently returns None.
# None means "no value" — it is not 0, not "", not False. It is its own thing.

def say_hello(name):
    print('Hello, ' + name)
    # no return statement here

greeting = say_hello('Spencer')  # prints "Hello, Spencer"
print(greeting)                  # prints None — nothing was returned


# --- Example 3: return exits the function immediately ---
# Any code after a return statement in the same branch will never run.
# This is useful for "early exit" — bailing out before doing more work.

def is_even(number):
    if number % 2 == 0:
        return True   # function stops here if the number is even
    return False      # only reached if the number is odd

print(is_even(4))   # True
print(is_even(7))   # False


# --- Example 4: Multiple return statements (one per branch) ---
# A function can have several return statements — Python uses whichever it hits first.
# This is common when different conditions produce different results.

def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'F'

print(grade(95))   # A
print(grade(83))   # B
print(grade(61))   # F


# --- Example 5: Returning None explicitly ---
# You can write "return None" or just "return" to exit early and signal
# that there is nothing meaningful to return.
# This is sometimes done to guard against bad input.

def safe_divide(a, b):
    if b == 0:
        print('Error: cannot divide by zero.')
        return None   # early exit, no result
    return a / b

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # prints the error message, then None
