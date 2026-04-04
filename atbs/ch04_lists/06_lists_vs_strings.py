# Ch. 4 — Lists
# Concept 6: Lists vs. Strings

# --- Both support indexing and slicing ---
my_list = ['a', 'b', 'c', 'd']
my_str = 'abcd'

print(my_list[1])       # 'b'
print(my_str[1])        # 'b'

print(my_list[1:3])     # ['b', 'c']
print(my_str[1:3])      # 'bc'

# --- The key difference: mutability ---
# Lists can be changed in place. Strings cannot.
my_list[0] = 'z'
print(my_list)          # ['z', 'b', 'c', 'd']

# This raises a TypeError — strings don't allow item assignment:
# my_str[0] = 'z'

# To "change" a string, you must create a new one entirely.
my_str = 'z' + my_str[1:]
print(my_str)           # 'zbcd' — a brand new string, not a modification

# --- Converting a string to a list with list() ---
# Breaks the string into individual characters
chars = list('hello')
print(chars)            # ['h', 'e', 'l', 'l', 'o']

# --- Splitting a string into words with split() ---
# split() breaks on whitespace by default, returns a list of strings
sentence = 'the quick brown fox'
words = sentence.split()
print(words)            # ['the', 'quick', 'brown', 'fox']

# You can split on any delimiter
csv = 'red,green,blue'
colors = csv.split(',')
print(colors)           # ['red', 'green', 'blue']

# --- Joining a list back into a string with join() ---
# join() is called on the DELIMITER string, not the list — this surprises people
print(' '.join(words))          # 'the quick brown fox'
print(', '.join(colors))        # 'red, green, blue'
print(''.join(chars))           # 'hello' — no delimiter, just concatenate

# --- Both support in/not in ---
print('b' in my_list)           # True
print('b' in my_str)            # True — works on substrings too
print('zb' in my_str)           # True — 'zb' is a substring of 'zbcd'
