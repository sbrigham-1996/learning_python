# Chapter 7 — Pattern Matching with Regular Expressions
# Concept 8: Character classes — \d, \w, \s and their inverses
#
# \d  = any digit (0-9)
# \w  = any word character (letters, digits, underscore)
# \s  = any whitespace (space, tab, newline)
# \D  = anything NOT a digit
# \W  = anything NOT a word character
# \S  = anything NOT whitespace
# Lowercase = matches the type. Uppercase = matches everything EXCEPT that type.

import re

sample = 'Today is 04-11-2026, and the temp is 72 degrees.'

# --- \d: digits only ---
digit_regex = re.compile(r'\d+')
print('Digits found:    ', digit_regex.findall(sample))
# ['04', '11', '2026', '72']

# --- \D: everything that is NOT a digit ---
non_digit_regex = re.compile(r'\D+')
print('Non-digits found:', non_digit_regex.findall(sample))
# ['Today is ', '-', '-', ', and the temp is ', ' degrees.']

print()

# --- \w: word characters (letters, digits, underscore) ---
word_char_regex = re.compile(r'\w+')
print('Word tokens found:', word_char_regex.findall(sample))
# ['Today', 'is', '04', '11', '2026', 'and', 'the', 'temp', 'is', '72', 'degrees']
# Note: punctuation and spaces are excluded — \w does not match them

# --- \W: everything that is NOT a word character ---
non_word_regex = re.compile(r'\W+')
print('Non-word tokens:  ', non_word_regex.findall(sample))
# [' ', ' ', '-', '-', ', ', ' ', ' ', ' ', ' ', '.']

print()

# --- \s and \S ---
sentence = 'First\tSecond\nThird Fourth'

whitespace_regex = re.compile(r'\s+')
print('Whitespace chunks:', whitespace_regex.findall(sentence))
# ['\t', '\n', ' ']  — tab, newline, and space are all matched by \s

non_whitespace_regex = re.compile(r'\S+')
print('Non-whitespace:   ', non_whitespace_regex.findall(sentence))
# ['First', 'Second', 'Third', 'Fourth']

print()

# --- Combining character classes in one pattern ---
# \d+: one or more digits
# \s: one whitespace character
# \w+: one or more word characters
# Matches patterns like "72 degrees" or "3 items"
quantity_regex = re.compile(r'\d+\s\w+')
data = 'I have 3 cats, 12 books, and 1 dog.'
print('Quantities found:', quantity_regex.findall(data))
# ['3 cats', '12 books', '1 dog']

print()

# --- Why uppercase inverses matter ---
# Extracting only the non-numeric parts of a messy string
messy = 'abc123def456ghi'
letters_only = re.compile(r'\D+')
print('Letters from messy string:', letters_only.findall(messy))
# ['abc', 'def', 'ghi']
