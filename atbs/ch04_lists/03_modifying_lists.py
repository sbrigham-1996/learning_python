# Ch. 4 — Lists
# Concept 3: Modifying lists — changing, adding, and removing values

animals = ['cat', 'dog', 'bird']

# --- Changing a value by index ---
# Assign directly to an index, just like a variable
animals[1] = 'fish'
print(animals)      # ['cat', 'fish', 'bird']

# --- append() — adds one item to the END of the list ---
# This is the most common way to build up a list over time
animals.append('rabbit')
print(animals)      # ['cat', 'fish', 'bird', 'rabbit']

# --- insert() — adds an item at a SPECIFIC position ---
# insert(index, value): everything at that index and after shifts right
animals.insert(1, 'dog')
print(animals)      # ['cat', 'dog', 'fish', 'bird', 'rabbit']

# --- remove() — removes the FIRST matching value ---
# Searches by value, not index. Raises ValueError if the value isn't found.
animals.remove('fish')
print(animals)      # ['cat', 'dog', 'bird', 'rabbit']

# If a value appears more than once, only the first occurrence is removed.
duplicates = ['a', 'b', 'a', 'c']
duplicates.remove('a')
print(duplicates)   # ['b', 'a', 'c'] — only the first 'a' was removed

# --- del — removes an item by INDEX ---
# del is a statement, not a method — notice there are no parentheses
del animals[0]
print(animals)      # ['dog', 'bird', 'rabbit']

# del also works on slices — removes a range of items at once
del animals[0:2]
print(animals)      # ['rabbit']
