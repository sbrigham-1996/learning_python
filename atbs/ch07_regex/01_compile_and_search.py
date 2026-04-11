# Chapter 7 — Pattern Matching with Regular Expressions
# Concept 1: re.compile() and search()
#
# Key idea: regex is a two-step process.
#   Step 1 — compile the pattern into a Regex object (do this once)
#   Step 2 — use that object to search a string (do this as many times as you need)

import re

# Step 1: compile the pattern.
# \d matches any single digit (0-9).
# So \d\d\d-\d\d\d-\d\d\d\d means: 3 digits, a dash, 3 digits, a dash, 4 digits.
# The r"..." is a raw string — backslashes are passed literally to the regex engine.
phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# Step 2: search a string.
# .search() scans left-to-right and stops at the FIRST match.
# It returns a Match object if found, or None if not.
text = 'Call me at 415-555-4242 or 212-555-0000.'
match = phone_regex.search(text)

# Always check for None before calling .group() — if search() found nothing,
# calling .group() on None raises an AttributeError.
if match:
    print('Phone number found:', match.group())
else:
    print('No phone number found.')

# What happens when there is NO match?
no_match_text = 'There is no phone number here.'
result = phone_regex.search(no_match_text)
print('Result on non-matching string:', result)   # prints: None

# Demonstrating why raw strings matter:
# Without r"...", Python would interpret \d as an escape sequence.
# \d has no meaning as a Python escape, so it technically works here —
# but patterns like \b (word boundary) would break silently.
# Habit: always use r"..." for regex patterns.
