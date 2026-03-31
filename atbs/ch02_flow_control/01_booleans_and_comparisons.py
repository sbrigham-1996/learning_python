# Chapter 2 - Flow Control
# Concept 1: Boolean Values and Comparison Operators

# -----------------------------------------------------------------------------
# BOOLEAN VALUES
# A Boolean can only be True or False. Note the capital letters — Python is
# case-sensitive, so 'true' or 'TRUE' will cause an error.
# -----------------------------------------------------------------------------

is_raining = True
is_sunny = False

print(type(is_raining))   # <class 'bool'>
print(is_raining)         # True
print(is_sunny)           # False

# -----------------------------------------------------------------------------
# COMPARISON OPERATORS
# These evaluate two values and return a Boolean (True or False).
# Think of them as asking a yes/no question.
# -----------------------------------------------------------------------------

x = 10
y = 5

# == (equal to)
# IMPORTANT: This is NOT the same as = (assignment)
# = stores a value.   x = 10  → puts 10 into x
# == compares values. x == 10 → asks "is x equal to 10?"
print(x == 10)   # True
print(x == 99)   # False

# != (not equal to)
print(x != y)    # True  — 10 is not equal to 5
print(x != 10)   # False — 10 is equal to 10, so "not equal" is False

# < and > (less than / greater than)
print(y < x)     # True  — 5 is less than 10
print(y > x)     # False — 5 is not greater than 10

# <= and >= (less than or equal to / greater than or equal to)
print(x >= 10)   # True  — 10 is equal to 10, so >= is satisfied
print(y <= 4)    # False — 5 is not less than or equal to 4

# -----------------------------------------------------------------------------
# COMPARING STRINGS
# == works on strings too, but it is case-sensitive.
# -----------------------------------------------------------------------------

name = 'Alice'
print(name == 'Alice')   # True
print(name == 'alice')   # False — Python sees these as different strings

# -----------------------------------------------------------------------------
# COMPARING DIFFERENT TYPES
# You can compare integers and floats, but comparing int to string raises
# a TypeError. Python won't guess what you mean.
# -----------------------------------------------------------------------------

print(42 == 42.0)    # True  — int and float with same value are equal
# print(42 == '42') # would raise TypeError — don't mix int and str with ==
