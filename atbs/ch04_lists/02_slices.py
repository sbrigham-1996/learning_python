# Ch. 4 — Lists
# Concept 2: Slices — grabbing a range of items

animals = ['cat', 'dog', 'bird', 'fish', 'rabbit']
#  index:    0       1      2       3        4

# --- Basic slice: list[start:end] ---
# start is included, end is NOT included
print(animals[1:3])     # ['dog', 'bird']  — indexes 1 and 2
print(animals[0:2])     # ['cat', 'dog']   — indexes 0 and 1

# --- Omitting start defaults to 0 ---
print(animals[:3])      # ['cat', 'dog', 'bird']  — from beginning up to index 3

# --- Omitting end defaults to the end of the list ---
print(animals[2:])      # ['bird', 'fish', 'rabbit']  — from index 2 to the end

# --- Omitting both gives you a full copy of the list ---
print(animals[:])       # ['cat', 'dog', 'bird', 'fish', 'rabbit']

# --- Slices work with negative indexes too ---
print(animals[-3:])     # ['bird', 'fish', 'rabbit']  — last 3 items
print(animals[:-1])     # ['cat', 'dog', 'bird', 'fish']  — everything except the last

# --- A slice always returns a list, even if it contains one item ---
print(animals[1:2])     # ['dog']   — a list with one item
print(animals[1])       # 'dog'     — the string itself (no brackets)
# These look similar but are different types — one is a list, one is a string.
