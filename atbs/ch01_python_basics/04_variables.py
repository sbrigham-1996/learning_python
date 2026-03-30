# Chapter 1 — Variables
# A variable is a named storage location for a value.
# The = operator assigns a value to a name. It is not mathematical equality.

# --- Basic assignment ---
spam = 42
print(spam)        # 42

name = "Spencer"
print(name)        # Spencer

pi = 3.14159
print(pi)          # 3.14159

# --- Variables can be used in expressions ---
# Python looks up the value stored in the variable and substitutes it in.
eggs = 10
print(eggs + 5)    # 15
print(eggs * 2)    # 20

# --- Variables can be overwritten ---
# The old value is replaced. Python does not warn you.
spam = 42
print(spam)        # 42
spam = 99
print(spam)        # 99 — the 42 is gone

# --- Variables can be assigned the result of an expression ---
total = 10 + 5
print(total)       # 15

double = total * 2
print(double)      # 30

# --- Variables can reference other variables ---
first_name = "Spencer"
last_name = "Brigham"
full_name = first_name + " " + last_name
print(full_name)   # Spencer Brigham

# --- PEP 8 naming conventions ---
# Good: descriptive, snake_case
num_cats = 3
user_name = "spencer"
account_balance = 100.50

# Avoid: vague single letters, camelCase (not Pythonic for variables)
# n = 3
# userName = "spencer"

# --- Checking the type of a variable ---
# type() works on variables just like on raw values.
print(type(num_cats))        # <class 'int'>
print(type(user_name))       # <class 'str'>
print(type(account_balance)) # <class 'float'>
