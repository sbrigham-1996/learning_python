# Ch. 4 — Lists
# Concept 4: in, not in, and multiple assignment (unpacking)

fruits = ['apple', 'banana', 'cherry']

# --- in: returns True if the value exists in the list ---
print('banana' in fruits)       # True
print('grape' in fruits)        # False

# --- not in: the inverse ---
print('grape' not in fruits)    # True
print('apple' not in fruits)    # False

# Practical use: guard against acting on a value that isn't there
search = 'cherry'
if search in fruits:
    print(f'{search} is in the list.')
else:
    print(f'{search} was not found.')

# --- Multiple assignment (unpacking) ---
# Assign each item in a list to its own variable in one line.
# The number of variables must exactly match the number of items.
coordinates = [40, 73]
lat, lon = coordinates
print(lat)      # 40
print(lon)      # 73

# Works with any list — not just numbers
person = ['Spencer', 28, 'Python']
name, age, language = person
print(f'{name} is learning {language}.')

# This is also how Python lets you swap two variables without a temp variable —
# a classic Pythonic pattern:
a = 'hello'
b = 'world'
a, b = b, a     # swap
print(a)        # 'world'
print(b)        # 'hello'
