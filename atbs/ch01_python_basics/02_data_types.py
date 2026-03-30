# Chapter 1 — Data Types
# Python categorizes every value into a "type."
# The type determines what operations are valid and how they behave.

# --- Integers (int) ---
# Whole numbers, positive or negative, no decimal point.
print(type(42))        # <class 'int'>
print(type(-7))        # <class 'int'>
print(type(0))         # <class 'int'>

# --- Floats (float) ---
# Numbers with a decimal point. Python stores them differently from ints.
print(type(3.14))      # <class 'float'>
print(type(-0.5))      # <class 'float'>
print(type(1.0))       # <class 'float'> — note: 1.0 is NOT an int, even though it looks like one

# --- Strings (str) ---
# Any text wrapped in quotes. Single or double quotes both work.
print(type("hello"))   # <class 'str'>
print(type('world'))   # <class 'str'>
print(type("42"))      # <class 'str'> — looks like a number, but the quotes make it a string

# --- Why the distinction between 42 and "42" matters ---
# This works fine:
print(42 + 8)          # 50  — math on two ints

# This causes a TypeError — you cannot add a string and an int:
# print("42" + 8)      # uncomment this line to see the error

# --- Floats and ints can mix in math ---
# When you combine an int and a float, Python promotes the result to a float.
print(3 + 1.5)         # 4.5  — int + float = float
print(10 / 2)          # 5.0  — division always returns a float, even when it divides evenly
print(10 // 2)         # 5    — integer division returns an int
