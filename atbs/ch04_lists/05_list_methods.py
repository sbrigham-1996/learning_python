# Ch. 4 — Lists
# Concept 5: List methods — index(), sort(), reverse()

# --- index() — find the position of a value ---
# Returns the index of the FIRST matching item.
# Raises ValueError if the value isn't in the list.
animals = ['cat', 'dog', 'bird', 'dog']
print(animals.index('dog'))     # 1 — finds the first 'dog', not the second
print(animals.index('bird'))    # 2

# Useful pattern: find where something is before acting on it
if 'cat' in animals:
    i = animals.index('cat')
    print(f"'cat' is at index {i}.")

# --- sort() — sorts the list IN PLACE, returns None ---
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(numbers)      # [1, 1, 2, 3, 4, 5, 6, 9]

# Sort in reverse order with the keyword argument reverse=True
numbers.sort(reverse=True)
print(numbers)      # [9, 6, 5, 4, 3, 2, 1, 1]

# Sort strings — alphabetical by default (uppercase sorts before lowercase)
words = ['banana', 'Apple', 'cherry', 'date']
words.sort()
print(words)        # ['Apple', 'banana', 'cherry', 'date']

# For case-insensitive sorting, use the key argument
words.sort(key=str.lower)
print(words)        # ['Apple', 'banana', 'cherry', 'date'] — truly alphabetical

# Cannot sort a list that mixes strings and numbers — Python can't compare them
# mixed = [1, 'apple', 3]
# mixed.sort()      # raises TypeError

# --- sorted() — returns a NEW sorted list, original is unchanged ---
original = [5, 2, 8, 1]
new_sorted = sorted(original)
print(original)     # [5, 2, 8, 1]  — untouched
print(new_sorted)   # [1, 2, 5, 8]  — new list

# --- reverse() — reverses the list IN PLACE, returns None ---
# This is NOT the same as sorting in reverse — it just flips the order as-is
letters = ['a', 'b', 'c', 'd']
letters.reverse()
print(letters)      # ['d', 'c', 'b', 'a']
