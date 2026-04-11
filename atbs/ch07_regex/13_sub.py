# Chapter 7 — Pattern Matching with Regular Expressions
# Concept 13: Substituting strings with sub()
#
# Key ideas:
#   regex.sub(replacement, string) — replaces every match with the replacement
#   Returns a new string — the original is unchanged
#   \1, \2, etc. in the replacement refer back to captured groups (backreferences)

import re

# --- Basic sub(): replace every match with a fixed string ---
names_regex = re.compile(r'Agent \w+')
result = names_regex.sub('REDACTED', 'Agent Alice gave the documents to Agent Bob.')
print('Basic sub():')
print(' ', result)
# REDACTED gave the documents to REDACTED.

print()

# --- Backreferences: rearranging captured groups ---
# \1 in the replacement string means "insert what group 1 captured"
# Match: first name then last name. Rewrite as: last, first.
name_regex = re.compile(r'(\w+) (\w+)')
result = name_regex.sub(r'\2, \1', 'Spencer Brigham')
print('Backreference (swap first/last):')
print(' ', result)
# Brigham, Spencer

print()

# --- Practical: reformat dates from MM-DD-YYYY to YYYY-MM-DD ---
date_regex = re.compile(r'(\d{2})-(\d{2})-(\d{4})')
text = 'Project start: 04-11-2026. Deadline: 12-31-2026.'
result = date_regex.sub(r'\3-\1-\2', text)
print('Date reformatting (MM-DD-YYYY -> YYYY-MM-DD):')
print(' ', result)
# Project start: 2026-04-11. Deadline: 2026-12-31.

print()

# --- Redacting sensitive data: keep first and last char of each word ---
# This preserves readability while obscuring the actual content
# Groups: group 1 = first letter, group 2 = middle, group 3 = last letter
censor_regex = re.compile(r'(\w)(\w+)(\w)')
result = censor_regex.sub(r'\1***\3', 'My password is hunter2 and my pin is secret')
print('Partial redaction:')
print(' ', result)
# M* p*d is h*r and m* p* is s*t  (varies slightly by word length)

print()

# --- sub() with re.IGNORECASE ---
# Replaces all case variants with a normalized form
normalize_regex = re.compile(r'python', re.IGNORECASE)
text = 'I use Python for scripting. PYTHON is great. python rules.'
result = normalize_regex.sub('Python', text)
print('Normalizing casing with sub() + re.IGNORECASE:')
print(' ', result)
# I use Python for scripting. Python is great. Python rules.

print()

# --- sub() returns the count of substitutions made (via subn) ---
# subn() is like sub() but returns a tuple: (new_string, count)
count_regex = re.compile(r'\bthe\b', re.IGNORECASE)
new_text, count = count_regex.subn('a', 'The cat sat on the mat by the door.')
print('subn() — substitution count:')
print(f'  Result: {new_text!r}')
print(f'  Substitutions made: {count}')
