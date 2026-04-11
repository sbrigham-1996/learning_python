# Ch. 6 — String Literals, Escape Characters, and Raw Strings

# --- Single vs. Double Quotes ---
# Both delimiters work identically. The practical benefit: you can
# put one type of quote *inside* a string that uses the other type.

greeting = 'Hello, world!'
also_greeting = "Hello, world!"
print(greeting == also_greeting)  # True — they are identical

# Using opposite quotes avoids needing to escape
contraction = "It's a beautiful day"
dialogue = 'She said "Python is great"'
print(contraction)
print(dialogue)

# --- Escape Characters ---
# A backslash tells Python: "the next character has a special meaning."
# \n = newline, \t = tab, \\ = literal backslash, \' and \" = literal quotes

print("First line\nSecond line")       # \n creates a line break
print("Name:\tSpencer")                # \t creates a tab indent
print("Backslash: \\")                 # \\ produces a single \
print('It\'s escaped')                 # \' lets single quote live inside single-quoted string

# Escaping vs. using opposite quotes — both work, but opposite quotes is cleaner
print("It's escaped (no backslash needed)")  # cleaner approach

# --- Multiline Strings with Triple Quotes ---
# Triple quotes let a string span multiple lines without \n.
# The newlines you type are part of the string.
# Use triple double quotes (""") or triple single quotes (''') — convention is """

poem = """Roses are red,
Violets are blue,
Python is great,
And so are you."""

print(poem)

# Triple-quoted strings are also commonly used for multiline messages or blocks of text.
# Note: leading/trailing newlines ARE included if you put them on their own line.

message = """
This message has a blank line at the start and end.
"""
print(repr(message))  # repr() shows the raw string so you can see \n characters

# --- Raw Strings ---
# Prefix with r to disable ALL escape processing.
# Every backslash is treated as a literal backslash character.

# Without raw string: \n becomes a newline, \t becomes a tab
normal = "C:\new_folder\test"
print("Normal string:", normal)   # \n and \t interpreted as escape chars!

# With raw string: backslashes stay as backslashes
raw = r"C:\new_folder\test"
print("Raw string:   ", raw)      # prints exactly as written

# Raw strings are essential for:
# 1. Windows file paths (C:\Users\name\...)
# 2. Regex patterns (covered in Ch. 7) where \ has special meaning
