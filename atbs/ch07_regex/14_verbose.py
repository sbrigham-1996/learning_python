# Chapter 7 — Pattern Matching with Regular Expressions
# Concept 14: re.VERBOSE — writing readable regex
#
# Key ideas:
#   re.VERBOSE lets you add whitespace and # comments to a pattern
#   The engine ignores all whitespace and comments — only the pattern counts
#   Literal spaces must be escaped as \ or written inside []
#   Combine multiple flags with | : re.IGNORECASE | re.VERBOSE

import re

# --- Same phone pattern: compact vs verbose ---
# Compact: hard to read at a glance
phone_compact = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

# Verbose: self-documenting
phone_verbose = re.compile(r'''
    (\d{3})   # area code — exactly 3 digits
    -         # separator
    (\d{3})   # exchange — exactly 3 digits
    -         # separator
    (\d{4})   # subscriber number — exactly 4 digits
''', re.VERBOSE)

# Both patterns are identical to the regex engine — test them side by side
text = 'Call 415-555-4242 for details.'
match_compact = phone_compact.search(text)
match_verbose = phone_verbose.search(text)

print('Compact result:', match_compact.group())
print('Verbose result:', match_verbose.group())
print('Patterns are equivalent:', match_compact.group() == match_verbose.group())

print()

# --- Verbose pattern for a date: MM/DD/YYYY or MM-DD-YYYY ---
date_regex = re.compile(r'''
    (\d{2})       # month — exactly 2 digits
    [\/\-]        # separator: / or -
    (\d{2})       # day — exactly 2 digits
    [\/\-]        # separator: / or -
    (\d{4})       # year — exactly 4 digits
''', re.VERBOSE)

dates = ['04/11/2026', '12-31-2026', '1-1-2026']
print('Date matching (verbose):')
for d in dates:
    match = date_regex.search(d)
    if match:
        month, day, year = match.groups()
        print(f'  {d!r:<14} -> month={month} day={day} year={year}')
    else:
        print(f'  {d!r:<14} -> no match')

print()

# --- Combining flags with | ---
# re.VERBOSE for readability + re.IGNORECASE for case flexibility
keyword_regex = re.compile(r'''
    \b        # word boundary — match whole words only
    python    # the keyword we are looking for
    \b        # word boundary
''', re.VERBOSE | re.IGNORECASE)

posts = ['I love Python!', 'learning python daily', 'PYTHON is great', 'monty pythons']
print('Combined flags (VERBOSE | IGNORECASE):')
for post in posts:
    match = keyword_regex.search(post)
    print(f'  {"match" if match else "no match":<8} {post!r}')

print()

# --- The literal space rule ---
# re.VERBOSE ignores plain spaces in the pattern.
# To match an actual space, escape it with \ or use [ ]
space_regex = re.compile(r'''
    hello   # first word
    \ +     # one or more literal spaces (escaped with \)
    world   # second word
''', re.VERBOSE)

for text in ['hello world', 'hello   world', 'helloworld']:
    match = space_regex.search(text)
    print(f'  {text!r:<18} -> {"match" if match else "no match"}')
