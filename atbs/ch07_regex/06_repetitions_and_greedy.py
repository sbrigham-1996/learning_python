# Chapter 7 — Pattern Matching with Regular Expressions
# Concept 6: {n} and {n,m} — specific repetitions, greedy vs. non-greedy
#
# Key ideas:
#   {n}    = exactly n repetitions
#   {n,m}  = between n and m repetitions (inclusive)
#   {n,}   = n or more
#   {,m}   = zero up to m
#   By default, repetition operators are GREEDY — they grab as much as possible.
#   Adding ? after them makes them NON-GREEDY — they grab as little as possible.

import re

# --- Exact repetitions with {n} ---
# Much cleaner than writing \d\d\d\d\d\d\d\d\d\d
ha_regex = re.compile(r'(Ha){3}')
match = ha_regex.search('HaHaHa')
print('Exact {3}:', match.group())    # HaHaHa

no_match = ha_regex.search('HaHa')
print('Only two Ha:', no_match)        # None — must be exactly 3

print()

# --- Range repetitions with {n,m} ---
digit_regex = re.compile(r'\d{3,5}')

for text in ['12', '123', '1234', '12345', '123456']:
    match = digit_regex.search(text)
    if match:
        print(f'{text!r:<10} -> matched: {match.group()!r}')
    else:
        print(f'{text!r:<10} -> no match')

print()

# --- Greedy matching (default behavior) ---
# The regex engine tries to match as MANY characters as possible.
# <.*> matches an opening <, then .* grabs everything it can, then >
# Given '<To serve man> for dinner>', .* will grab as much as possible
# before finding the LAST > in the string.
greedy_regex = re.compile(r'<.*>')
text = '<To serve man> for dinner>'
match = greedy_regex.search(text)
print('Greedy  <.*> :', match.group())   # <To serve man> for dinner>

# --- Non-greedy matching ---
# Adding ? after .* makes it grab as FEW characters as possible.
# It stops at the FIRST > it encounters.
non_greedy_regex = re.compile(r'<.*?>')
match = non_greedy_regex.search(text)
print('Non-greedy <.*?> :', match.group())   # <To serve man>

print()

# --- Why this matters ---
# Greedy is the default because it is often what you want for structured data.
# Non-greedy is essential when your pattern has a repeated delimiter —
# like HTML tags, quoted strings, or bracketed content —
# where you want to stop at the FIRST closing marker, not the last.

# Another example: extracting a quoted string
quoted = re.compile(r'".*?"')    # non-greedy: stop at first closing quote
text2 = '"first" and "second"'
match = quoted.search(text2)
print('Non-greedy quoted string:', match.group())   # "first"

greedy_quoted = re.compile(r'".*"')   # greedy: runs to the last quote
match = greedy_quoted.search(text2)
print('Greedy quoted string:    ', match.group())   # "first" and "second"
