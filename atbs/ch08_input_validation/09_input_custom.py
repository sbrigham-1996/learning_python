import pyinputplus as pyip
import re

# inputCustom() lets you plug your own validation function into PyInputPlus.
# PyInputPlus owns the retry loop — your function owns the rule.
#
# Validation function contract:
#   - Takes one argument: the string the user typed
#   - Valid input:   return None (or bare return)
#   - Invalid input: raise ValueError with a descriptive message

# --- Validator 1: must be an even number ---
# A simple rule that inputInt() alone can't enforce.

def must_be_even(value):
    value = int(value)
    if value % 2 != 0:
        raise ValueError("Must be an even number.")

print("--- Custom validator: even numbers only ---")
num = pyip.inputCustom(must_be_even, prompt="Enter an even number: ")
print(f"You entered: {num}")

# --- Validator 2: regex-based product code ---
# Must match the pattern: two uppercase letters, dash, four digits.
# Example: AB-1234
# This is where Ch. 7 regex pays off directly.

PRODUCT_CODE_RE = re.compile(r'^[A-Z]{2}-\d{4}$')

def valid_product_code(value):
    if not PRODUCT_CODE_RE.search(value):
        raise ValueError("Product code must be two uppercase letters, a dash, and four digits (e.g. AB-1234).")

print("\n--- Custom validator: product code format ---")
code = pyip.inputCustom(valid_product_code, prompt="Enter a product code (e.g. AB-1234): ")
print(f"Product code: {code}")

# --- Validator 3: multiple conditions ---
# Username rules: 4-12 characters, letters and numbers only, must start with a letter.

def valid_username(value):
    if not 4 <= len(value) <= 12:
        raise ValueError("Username must be between 4 and 12 characters.")
    if not value[0].isalpha():
        raise ValueError("Username must start with a letter.")
    if not value.isalnum():
        raise ValueError("Username can only contain letters and numbers.")

print("\n--- Custom validator: username rules ---")
username = pyip.inputCustom(valid_username, prompt="Enter a username (4-12 chars, letters/numbers, start with a letter): ")
print(f"Username accepted: {username}")
