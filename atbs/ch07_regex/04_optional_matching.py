# Chapter 7 — Pattern Matching with Regular Expressions
# Concept 4: Optional matching with ?
#
# Key idea: ? after a character or group means "zero or one times."
# The pattern matches whether that piece is present or not.

import re

# Basic example: (wo)? makes the group optional
bat_regex = re.compile(r'Bat(wo)?man')

match1 = bat_regex.search('The Adventures of Batman')
print('Without wo:', match1.group())   # Batman

match2 = bat_regex.search('The Adventures of Batwoman')
print('With wo:   ', match2.group())   # Batwoman

# What does group(1) return when the optional part is absent?
# The group still exists — it just captured nothing, so it returns None.
print('group(1) when absent: ', match1.group(1))   # None
print('group(1) when present:', match2.group(1))   # wo

# Practical example: phone number with optional area code
# The area code (\d\d\d-) is optional — some numbers are written without it
phone_regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')

for number in ['415-555-4242', '555-4242']:
    match = phone_regex.search(number)
    if match:
        print(f'{number!r} -> matched: {match.group()!r}  area code: {match.group(1)}')

# Spelling variation example: colour vs color
# The 'u' is optional
color_regex = re.compile(r'colou?r')

for word in ['color', 'colour', 'colouur']:
    match = color_regex.search(word)
    if match:
        print(f'{word!r} -> matched')
    else:
        print(f'{word!r} -> no match')

# Why does 'colouur' not match?
# ? means zero OR ONE — it does not mean "any number of u's."
# For that you would need * (zero or more) or + (one or more) — coming up next.
