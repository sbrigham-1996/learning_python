# Ch. 4 — Lists
# Concept 1: The list data type and accessing items by index

# A list is an ordered collection of values under one variable name.
# Square brackets define the list; items are separated by commas.
fruits = ['apple', 'banana', 'cherry']
print(fruits)           # The whole list
print(type(fruits))     # <class 'list'>

# --- Positive indexes (counting from the front, starting at 0) ---
print(fruits[0])        # 'apple'   — first item
print(fruits[1])        # 'banana'  — second item
print(fruits[2])        # 'cherry'  — third (and last) item

# This would cause an IndexError — there is no item at position 3:
# print(fruits[3])

# --- Negative indexes (counting from the back, starting at -1) ---
print(fruits[-1])       # 'cherry'  — last item
print(fruits[-2])       # 'banana'  — second-to-last
print(fruits[-3])       # 'apple'   — same as fruits[0]

# --- len() tells you how many items are in the list ---
print(len(fruits))      # 3

# The last valid positive index is always len(list) - 1.
# Negative indexes: -1 through -len(list)
last_index = len(fruits) - 1
print(fruits[last_index])   # 'cherry' — same as fruits[-1]

# --- Lists can hold any data type, and can mix types ---
mixed = [42, 'hello', 3.14, True]
print(mixed[1])         # 'hello'

# --- A list can even contain other lists (nested lists) ---
nested = [['a', 'b'], ['c', 'd']]
print(nested[0])        # ['a', 'b']   — first inner list
print(nested[0][1])     # 'b'          — second item of the first inner list
