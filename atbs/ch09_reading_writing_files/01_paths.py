"""
Ch. 9 — Concept 1: Files, Paths, and the pathlib Module

Path objects are the modern way to work with file paths in Python.
They replace fragile string concatenation and handle OS differences
(Mac/Linux use '/', Windows uses '\') automatically.
"""

from pathlib import Path

# ------------------------------------------------------------------
# 1. Creating Path objects
# ------------------------------------------------------------------

# A Path object is created by passing a string to Path().
# It does NOT have to exist on disk — it's just a representation.
p = Path('/Users/spencerbrigham/Desktop/learning_python')
print("Path object:", p)
print("Type:", type(p))

# ------------------------------------------------------------------
# 2. Joining paths with /
# ------------------------------------------------------------------

# Python overloads the / operator for Path objects.
# This is cleaner and cross-platform safe compared to string concatenation.
child = p / 'atbs' / 'ch09_reading_writing_files' / '01_paths.py'
print("\nJoined path:", child)

# ------------------------------------------------------------------
# 3. Current working directory and home directory
# ------------------------------------------------------------------

# cwd() = the folder Python is currently running from
# This changes depending on WHERE you run the script from.
print("\nCurrent working directory:", Path.cwd())

# home() = your user's home directory, regardless of where you run from
print("Home directory:", Path.home())

# ------------------------------------------------------------------
# 4. Checking path properties (existence, type)
# ------------------------------------------------------------------

# These return True/False — useful for defensive checks before opening files.
print("\nDoes the project folder exist?", p.exists())
print("Is it a directory?", p.is_dir())
print("Is it a file?", p.is_file())

# A path that doesn't exist on disk
fake = Path('/Users/spencerbrigham/fake_folder/fake_file.txt')
print("\nDoes the fake path exist?", fake.exists())

# ------------------------------------------------------------------
# 5. Path attributes — dissecting a path into its parts
# ------------------------------------------------------------------

# Each attribute gives you a specific piece of the path string.
example = Path('/Users/spencerbrigham/Desktop/learning_python/README.md')

print("\nFull path:    ", example)
print(".anchor       ", example.anchor)    # root of the filesystem ('/')
print(".parent       ", example.parent)    # everything except the final component
print(".name         ", example.name)      # final component (filename + extension)
print(".stem         ", example.stem)      # filename WITHOUT extension
print(".suffix       ", example.suffix)    # extension only (includes the dot)

# ------------------------------------------------------------------
# 6. Why .stem and .suffix matter
# ------------------------------------------------------------------

# Common pattern: rename a file by changing only the extension.
# You can rebuild the path from parts without string slicing.
new_name = example.stem + '.txt'  # 'README.txt'
new_path = example.parent / new_name
print("\nRenamed path:", new_path)
