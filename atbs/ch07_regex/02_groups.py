# Chapter 7 — Pattern Matching with Regular Expressions
# Concept 2: Grouping with parentheses
#
# Key idea: wrapping part of a pattern in (...) creates a group.
# Groups let you extract specific pieces of a match, not just the whole thing.

import re

# Parentheses divide the pattern into named sections.
# Group 1: (\d\d\d)  — area code
# Literal: -
# Group 2: (\d\d\d)  — exchange
# Literal: -
# Group 3: (\d\d\d\d) — subscriber number
phone_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')

text = 'Call me at 415-555-4242.'
match = phone_regex.search(text)

if match:
    # group(0) is always the full match — same as calling group() with no argument
    print('Full match:        ', match.group(0))

    # group(1) through group(n) are the individual groups, left to right
    print('Area code (group 1):', match.group(1))
    print('Exchange  (group 2):', match.group(2))
    print('Subscriber(group 3):', match.group(3))

    # .groups() returns ALL groups at once as a tuple — useful for unpacking
    area, exchange, subscriber = match.groups()
    print()
    print('Unpacked from .groups():')
    print(f'  Area code:   {area}')
    print(f'  Exchange:    {exchange}')
    print(f'  Subscriber:  {subscriber}')

# What if your pattern itself needs to match a literal parenthesis?
# Escape it with a backslash: \( and \)
paren_regex = re.compile(r'\((\d\d\d)\) (\d\d\d)-(\d\d\d\d)')
text2 = 'My number is (415) 555-4242.'
match2 = paren_regex.search(text2)

if match2:
    print()
    print('Matching (415) 555-4242 style:')
    print('Full match: ', match2.group())
    print('Area code:  ', match2.group(1))
    print('Exchange:   ', match2.group(2))
    print('Subscriber: ', match2.group(3))
