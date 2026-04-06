# Ch. 5 — Dictionaries & Structuring Data
# Concept 3: keys(), values(), and items()

person = {
    'name': 'Spencer',
    'age': 29,
    'job': 'Geotechnical Engineer',
    'city': 'Chapel Hill',
}

# --- keys() ---
# Returns a view of all keys in the dictionary.
print('Keys:')
for key in person.keys():
    print(' ', key)

# --- values() ---
# Returns a view of all values in the dictionary.
print('\nValues:')
for value in person.values():
    print(' ', value)

# --- items() ---
# Returns a view of (key, value) pairs as tuples.
# Tuple unpacking in the loop header is the Pythonic way to handle this.
print('\nKey-value pairs:')
for key, value in person.items():
    print(f'  {key}: {value}')

# --- Checking membership ---
# 'in' checks keys by default when used directly on a dict.
# For values, use 'in' with .values() explicitly.
print('\n"name" in person:', 'name' in person)               # True
print('"salary" in person:', 'salary' in person)             # False
print('"Spencer" in person.values():', 'Spencer' in person.values())  # True

# --- Converting to a plain list ---
# The views returned by keys()/values()/items() are not lists.
# Wrap in list() if you need to index into them or store them.
all_keys = list(person.keys())
print('\nKeys as a list:', all_keys)
print('First key:', all_keys[0])
