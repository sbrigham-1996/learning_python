# Ch. 6 — Validation Methods: isalpha(), isalnum(), isdecimal(), isspace(), istitle()
# These methods ask yes/no questions about what a string contains.
# They ALL return False for an empty string.

# --- isalpha() — letters only ---
print("hello".isalpha())     # True
print("hello2".isalpha())    # False — contains a digit
print("hello!".isalpha())    # False — contains punctuation
print("".isalpha())          # False — empty string

# --- isalnum() — letters OR digits, nothing else ---
print("hello123".isalnum())  # True
print("hello 123".isalnum()) # False — space is not a letter or digit
print("hello!".isalnum())    # False — punctuation fails

# --- isdecimal() — digits only (0-9) ---
print("12345".isdecimal())   # True
print("3.14".isdecimal())    # False — decimal point is not a digit
print("12 34".isdecimal())   # False — space fails
print("".isdecimal())        # False — empty string

# --- isspace() — whitespace only ---
print("   ".isspace())       # True — all spaces
print("\t\n".isspace())      # True — tab and newline are whitespace
print(" a ".isspace())       # False — contains a letter
print("".isspace())          # False — empty string

# --- istitle() --- title case (each word starts upper, rest lower) ---
print("Hello World".istitle())   # True
print("Hello world".istitle())   # False — 'world' starts lowercase
print("HELLO WORLD".istitle())   # False — all caps is not title case
print("It's A Test".istitle())   # True — apostrophe resets the word boundary

# --- The Key Practical Use: Safe Input Validation ---
# isdecimal() is the standard guard before calling int() on user input.
# Without it, int("abc") raises a ValueError and crashes the program.

while True:
    age_input = input("Enter your age: ")
    if age_input.isdecimal():
        age = int(age_input)    # safe to convert — we know it's all digits
        print(f"You are {age} years old.")
        break
    else:
        print("Please enter a number.")

# --- Combining Methods for Stricter Validation ---
# Real validation often requires more than one check.

while True:
    username = input("Enter a username (letters only, no spaces): ")
    if username.isalpha():
        print(f"Username '{username}' accepted.")
        break
    else:
        print("Username must contain letters only.")

# --- Checking Individual Characters ---
# These methods work on single characters too, which lets you inspect
# a string character by character when you need finer control.

sample = "Hello, World! 123"
letters = [c for c in sample if c.isalpha()]
digits  = [c for c in sample if c.isdecimal()]
spaces  = [c for c in sample if c.isspace()]

print("Letters:", letters)
print("Digits: ", digits)
print("Spaces: ", spaces)
