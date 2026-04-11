# Chapter 7 — Pattern Matching with Regular Expressions
# Concept 10: Anchors — ^ and $
#
# Key ideas:
#   ^  at the start of a pattern = match must begin at the start of the string
#   $  at the end of a pattern   = match must end at the end of the string
#   ^pattern$                    = the entire string must match the pattern
#
# IMPORTANT: ^ inside [] means negation (Concept 9).
#            ^ outside [] means start anchor. Same character, different context.

import re

# --- ^ anchor: must start with this ---
starts_with_digit = re.compile(r'^\d')

print('^ anchor (must start with digit):')
for text in ['42 is the answer', 'The answer is 42', '0 degrees']:
    match = starts_with_digit.search(text)
    print(f'  {text!r:<28} -> {"match" if match else "no match"}')

print()

# --- $ anchor: must end with this ---
ends_with_period = re.compile(r'\.$')

print('$ anchor (must end with period):')
for text in ['Hello.', 'Hello!', 'Hello. Goodbye.', 'Hello']:
    match = ends_with_period.search(text)
    print(f'  {text!r:<24} -> {"match" if match else "no match"}')
# Note: 'Hello. Goodbye.' matches — $ only cares about the very end

print()

# --- Both together: entire string must match ---
# ^\d+$ means: from the start to the end, nothing but digits
whole_number = re.compile(r'^\d+$')

print('^\d+$ anchor (entire string must be digits):')
for text in ['1234567890', '123abc', '  123', '123 ', '']:
    match = whole_number.search(text)
    print(f'  {text!r:<14} -> {"match" if match else "no match"}')
# Spaces, letters, or anything else cause a no match — the whole string must qualify

print()

# --- Practical example: validating input format ---
# A simple username rule: must start with a letter, end with a letter or digit,
# and contain only word characters, between 3 and 16 characters total
username_regex = re.compile(r'^[a-zA-Z]\w{1,14}[a-zA-Z0-9]$')

usernames = ['spencer', 'a', 'valid_user1', '1invalid', '_bad', 'x' * 17, 'ok']
print('Username validation (^[a-zA-Z]\\w{1,14}[a-zA-Z0-9]$):')
for name in usernames:
    match = username_regex.search(name)
    print(f'  {name!r:<20} -> {"valid" if match else "invalid"}')
