# Chapter 7 — Pattern Matching with Regular Expressions
# Concept 9: Custom character classes with []
#
# Key ideas:
#   [abc]    = match any one of: a, b, or c
#   [a-z]    = match any lowercase letter (range)
#   [a-zA-Z] = match any letter (combined ranges)
#   [^abc]   = match any character that is NOT a, b, or c (negation)
#   Inside [], most special characters lose their meaning and are treated literally.

import re

# --- Basic custom class: vowels ---
vowel_regex = re.compile(r'[aeiouAEIOU]')
text = 'RoboCop eats baby food.'
print('Vowels found:', vowel_regex.findall(text))
# ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o']

print()

# --- Ranges ---
# [a-z]  matches any single lowercase letter
# [A-Z]  matches any single uppercase letter
# [0-9]  matches any single digit (same as \d)
# [a-zA-Z0-9] matches any letter or digit (same as \w minus underscore)

lowercase_regex = re.compile(r'[a-z]+')
print('Lowercase runs:', lowercase_regex.findall('RoboCop eats BABY food'))
# ['obo', 'op', 'eats', 'food']  — uppercase letters break the run

hex_regex = re.compile(r'[0-9a-fA-F]+')
colors = ['FF5733', 'not-hex', '1a2b3c', 'ZZZZZZ', '0-9']
for c in colors:
    match = hex_regex.search(c)
    if match:
        print(f'  {c!r:<12} -> {match.group()!r}')
    else:
        print(f'  {c!r:<12} -> no match')

print()

# --- Negated class with ^ ---
# ^ as the FIRST character inside [] inverts the match
# [^aeiouAEIOU] matches any single character that is NOT a vowel
consonant_regex = re.compile(r'[^aeiouAEIOU ]+')
print('Non-vowel, non-space runs:', consonant_regex.findall('RoboCop eats baby food.'))
# ['R', 'b', 'C', 'p', 'ts', 'b', 'b', 'y', 'f', 'd.']

print()

# --- Special characters inside [] are mostly literal ---
# You do NOT need to escape . * + ? inside a character class
# They lose their special meaning there
literal_regex = re.compile(r'[.!?]+')
sentence = 'Wait... really?! Yes!'
print('Punctuation found:', literal_regex.findall(sentence))
# ['...', '?!', '!']

print()

# --- Practical example: matching a date in MM/DD/YYYY or MM-DD-YYYY format ---
# [\/\-] matches either / or -  (backslash escapes / and - to be safe here)
# Note: - at the END of a character class is treated as a literal, not a range
date_regex = re.compile(r'\d{2}[\/\-]\d{2}[\/\-]\d{4}')
dates = ['04/11/2026', '04-11-2026', '04.11.2026']
for d in dates:
    match = date_regex.search(d)
    if match:
        print(f'{d!r} -> matched: {match.group()!r}')
    else:
        print(f'{d!r} -> no match')
