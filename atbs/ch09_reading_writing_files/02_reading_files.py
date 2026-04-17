"""
Ch. 9 — Concept 2: Reading Files with open()

open() opens a connection to a file on disk.
The 'with' statement ensures the file is always closed when we're done,
even if something goes wrong mid-read.
"""

from pathlib import Path

# Build the path to our sample file relative to this script's location.
# __file__ is a built-in variable — it holds the path to the current script.
# .parent gives us the folder the script lives in.
# This way, the path works regardless of where you run the script from.
sample_path = Path(__file__).parent / 'sample.txt'

print("Reading from:", sample_path)
print("=" * 50)

# ------------------------------------------------------------------
# 1. .read() — entire file as one string
# ------------------------------------------------------------------

with open(sample_path) as f:
    contents = f.read()

print("\n--- .read() ---")
print(repr(contents))   # repr() reveals the \n characters explicitly
print(contents)         # plain print renders the newlines as actual line breaks

# ------------------------------------------------------------------
# 2. .readlines() — list of strings, one per line
# ------------------------------------------------------------------

with open(sample_path) as f:
    lines = f.readlines()

print("--- .readlines() ---")
print(lines)            # shows the list with \n still attached to each string

# The \n at the end of each line is often unwanted.
# Strip it off before working with the lines:
print("\nLines after stripping \\n:")
for line in lines:
    print(repr(line.strip()))

# ------------------------------------------------------------------
# 3. Iterating directly over the file object
# ------------------------------------------------------------------

# You can also loop over the file object itself — Python yields one line
# at a time without loading everything into memory first.
# This is the most memory-efficient pattern for large files.

print("\n--- Iterating over file object ---")
with open(sample_path) as f:
    for line in f:
        print(line.strip())   # strip() removes the trailing \n

# ------------------------------------------------------------------
# 4. What happens if the file doesn't exist
# ------------------------------------------------------------------

missing = Path(__file__).parent / 'does_not_exist.txt'

print("\n--- Handling a missing file ---")
if missing.exists():
    with open(missing) as f:
        print(f.read())
else:
    print(f"File not found: {missing.name}")

# Always check .exists() before opening a file you're not certain about.
# Letting open() raise FileNotFoundError is valid too, but the explicit
# check makes the failure mode obvious in the code.
