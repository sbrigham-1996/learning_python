"""
Ch. 9 — Concept 5: Saving Variables with pprint.pformat()

pformat() converts a Python object into a formatted string of valid Python code.
Writing that string to a .py file gives you a human-readable, editable data file
that you can load back by importing it like a module.
"""

import pprint
from pathlib import Path

output_dir = Path(__file__).parent

# ------------------------------------------------------------------
# 1. What pformat() returns
# ------------------------------------------------------------------

# pprint() prints to the terminal. pformat() returns the same thing as a string.
cats = [
    {'name': 'Zophie', 'age': 7},
    {'name': 'Pooka', 'age': 3},
    {'name': 'Fat-tail', 'age': 5},
]

formatted = pprint.pformat(cats)
print("pformat() output:")
print(formatted)
print("\nType:", type(formatted))  # it's just a string

# ------------------------------------------------------------------
# 2. Writing the formatted data to a .py file
# ------------------------------------------------------------------

# We wrap it in an assignment statement so the file is valid Python.
# When imported, 'cats' becomes a variable in that module's namespace.
save_path = output_dir / 'saved_data.py'

with open(save_path, 'w') as f:
    f.write('cats = ' + pprint.pformat(cats) + '\n')

print("\nSaved to:", save_path)

# Read it back as plain text to see what the file looks like on disk
with open(save_path) as f:
    print("\nContents of saved_data.py:")
    print(f.read())

# ------------------------------------------------------------------
# 3. Loading it back by importing the file as a module
# ------------------------------------------------------------------

# import saved_data makes Python execute saved_data.py, which runs the
# assignment 'cats = [...]' and makes saved_data.cats available to us.
import saved_data

print("Loaded cats from saved_data module:")
for cat in saved_data.cats:
    print(f"  {cat['name']}, age {cat['age']}")

# You access it via the module name, just like any other import.
print("\nFirst cat's name:", saved_data.cats[0]['name'])

# ------------------------------------------------------------------
# 4. Saving multiple variables — one assignment per variable
# ------------------------------------------------------------------

user = {'name': 'Spencer', 'chapter': 9}
scores = [95, 87, 92, 100]

config_path = output_dir / 'config.py'

with open(config_path, 'w') as f:
    f.write('user = ' + pprint.pformat(user) + '\n')
    f.write('scores = ' + pprint.pformat(scores) + '\n')

print("\nContents of config.py:")
with open(config_path) as f:
    print(f.read())

# ------------------------------------------------------------------
# 5. pformat() vs shelve — the key tradeoff
# ------------------------------------------------------------------

# pformat() files:
#   + Human readable — open in any text editor
#   + Editable by hand — change a value, it loads the new value next run
#   + Works with any tool that reads Python
#   - Only works for data that has a valid Python literal representation
#     (strings, ints, floats, lists, dicts, tuples, booleans, None)
#   - Custom class instances can't be serialized this way

# shelve files:
#   + Handles almost any Python object (via pickle)
#   + Dict-like interface — familiar and convenient
#   - Binary, not human readable
#   - Python-only format
