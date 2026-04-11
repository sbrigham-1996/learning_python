# Chapter 7 — Pattern Matching with Regular Expressions
# Concept 5: * and + — matching repetition
#
# Key idea:
#   * = zero or more occurrences (optional AND repeatable)
#   + = one or more occurrences (required, but can repeat)
# Both apply to whatever is immediately to their left — a character or a group.

import re

# --- The * operator (zero or more) ---
bat_star = re.compile(r'Bat(wo)*man')

for word in ['Batman', 'Batwoman', 'Batwowoman', 'Batwowowoman']:
    match = bat_star.search(word)
    print(f'*  {word!r:<18} -> {match.group()!r}')

print()

# --- The + operator (one or more) ---
bat_plus = re.compile(r'Bat(wo)+man')

for word in ['Batman', 'Batwoman', 'Batwowoman']:
    match = bat_plus.search(word)
    if match:
        print(f'+  {word!r:<18} -> {match.group()!r}')
    else:
        print(f'+  {word!r:<18} -> no match')

print()

# --- Practical difference ---
# * : the group is optional (zero is fine)
# + : the group is required (zero means no match)
# 'Batman' matches Bat(wo)*man but NOT Bat(wo)+man

# --- Real-world use: matching a name with any number of middle names ---
# \w+ matches one or more word characters (letters, digits, underscore)
# We will cover \w formally in the character classes concept,
# but it is useful here to show + in a realistic context.
name_regex = re.compile(r'\w+ (\w+ )*\w+')

names = [
    'John Smith',
    'John Paul Jones',
    'Mary Lou Retton Doe',
]

print('Name matching with +')
for name in names:
    match = name_regex.search(name)
    if match:
        print(f'  {name!r} -> matched')

print()

# --- Key contrast: ? vs * vs + ---
# All three apply to the thing immediately to their left.
# ?  zero or one   — one optional occurrence
# *  zero or more  — optional and repeatable
# +  one or more   — required but repeatable
print('Contrast: ?, *, + on the same group')
for pattern, symbol in [(r'Bat(wo)?man', '?'), (r'Bat(wo)*man', '*'), (r'Bat(wo)+man', '+')]:
    regex = re.compile(pattern)
    for word in ['Batman', 'Batwoman', 'Batwowoman']:
        match = regex.search(word)
        result = match.group() if match else 'no match'
        print(f'  {symbol}  {word!r:<14} -> {result!r}')
    print()
