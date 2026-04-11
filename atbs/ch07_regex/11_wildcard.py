# Chapter 7 — Pattern Matching with Regular Expressions
# Concept 11: The wildcard . and the .* pattern
#
# Key ideas:
#   .     = any single character EXCEPT newline
#   .*    = any characters, any number of times (greedy — grabs as much as possible)
#   .*?   = any characters, as few as possible (non-greedy — stops at first opportunity)
#   re.DOTALL makes . match newlines too

import re

# --- Basic . wildcard ---
# .at matches any single character followed by 'at'
at_regex = re.compile(r'.at')
print('. wildcard:')
print(at_regex.findall('The cat sat on the flat mat.'))
# ['cat', 'sat', 'lat', 'mat'] — the space before 'flat' is also a valid . match
# Note: 'flat' contributes 'lat' not 'flat' — . matches one character

print()

# --- .* greedy: grab everything between two markers ---
# Matches 'First Name:' then grabs everything up to 'Last Name:'
name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
match = name_regex.search('First Name: Spencer Last Name: Brigham')
if match:
    print('Greedy .* groups:')
    print('  First:', match.group(1))
    print('  Last: ', match.group(2))

print()

# --- .*? non-greedy: stop at the first opportunity ---
# Revisiting the HTML tag example from Concept 6
html = '<div>first</div><div>second</div>'

greedy = re.compile(r'<div>(.*)</div>')
non_greedy = re.compile(r'<div>(.*?)</div>')

greedy_match = greedy.search(html)
non_greedy_match = non_greedy.search(html)

print('Greedy     <div>(.*)</div> :', greedy_match.group(1))
# first</div><div>second  — ran to the LAST </div>

print('Non-greedy <div>(.*?)</div>:', non_greedy_match.group(1))
# first  — stopped at the FIRST </div>

print()

# --- . does NOT match newlines by default ---
multi_line = 'First line\nSecond line'

no_dotall = re.compile(r'First.*Second')
dotall = re.compile(r'First.*Second', re.DOTALL)

print('Without re.DOTALL:', no_dotall.search(multi_line))   # None
print('With re.DOTALL:   ', dotall.search(multi_line).group())
# First line\nSecond  — . now matches the \n

print()

# --- Practical example: flexible separator matching ---
# Date could be 04/11/2026 or 04-11-2026 or 04.11.2026
# Using . instead of a character class: quick but imprecise — accepts ANY separator
loose_date = re.compile(r'\d{2}.\d{2}.\d{4}')
strict_date = re.compile(r'\d{2}[\/\-\.]\d{2}[\/\-\.]\d{4}')

test_dates = ['04/11/2026', '04-11-2026', '04.11.2026', '04X11X2026']
print('Loose (.) vs strict ([/-.]) date matching:')
for d in test_dates:
    loose = loose_date.search(d)
    strict = strict_date.search(d)
    print(f'  {d!r:<14} loose: {"match" if loose else "no match":<8} strict: {"match" if strict else "no match"}')

# The lesson: . is convenient but imprecise — it accepts characters you probably
# didn't intend. Use [] when you know exactly what separators are valid.
