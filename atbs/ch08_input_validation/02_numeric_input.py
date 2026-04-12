import pyinputplus as pyip

# PyInputPlus numeric functions handle type conversion AND the retry loop.
# You never need to write while True + try/except for basic number input again.

# --- inputInt() ---
# Only accepts whole numbers. Reprompts on floats, letters, symbols, blank.
# Returns an actual int — no int() conversion needed on your end.

print("--- inputInt() ---")
age = pyip.inputInt("Enter your age: ")
print(f"In ten years you will be {age + 10}.")

# --- inputFloat() ---
# Accepts decimals AND whole numbers. Returns a float either way.
# Use this when precision matters — prices, measurements, percentages.

print("\n--- inputFloat() ---")
price = pyip.inputFloat("Enter a price: ")
print(f"With 10% tax: ${price * 1.10:.2f}")

# --- inputNum() ---
# The flexible option. Accepts both ints and floats.
# Returns an int if the input is whole (e.g. "4"), float if decimal (e.g. "4.5").
# Use when you don't care which type the user gives you.

print("\n--- inputNum() ---")
num = pyip.inputNum("Enter any number: ")
print(f"You entered: {num}  (type: {type(num).__name__})")
