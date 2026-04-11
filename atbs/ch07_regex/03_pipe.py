# Chapter 7 — Pattern Matching with Regular Expressions
# Concept 3: The | pipe — matching multiple patterns
#
# Key idea: | means OR inside a regex.
# search() returns the first match it finds left to right.
# Combine | with groups to factor out a shared prefix.

import re

# Basic pipe usage — match either word, whichever comes first in the string
hero_regex = re.compile(r'Batman|Tina Fey')

match1 = hero_regex.search('Batman and Tina Fey.')
print('First match (both present):', match1.group())   # Batman — comes first

match2 = hero_regex.search('Tina Fey and Batman.')
print('First match (Tina first):  ', match2.group())   # Tina Fey — comes first

# Factoring out a shared prefix with a group
# The group (...) captures only the varying suffix.
# group(0) = full match, group(1) = just the suffix
bat_regex = re.compile(r'Bat(man|mobile|cave|copter)')

for word in ['Batman', 'Batmobile', 'Batcave', 'Batcopter', 'Bat']:
    match = bat_regex.search(word)
    if match:
        print(f'{word!r:<12} -> full: {match.group(0)!r:<12} suffix: {match.group(1)!r}')
    else:
        print(f'{word!r:<12} -> no match')

# Why does 'Bat' alone not match?
# The pattern requires 'Bat' followed by one of the four options.
# 'Bat' with nothing after it doesn't satisfy the group.

# Practical example: matching multiple file extensions in a path
ext_regex = re.compile(r'\.(jpg|jpeg|png|gif)')
filenames = ['photo.jpg', 'document.pdf', 'icon.png', 'animation.gif', 'notes.txt']

print()
print('Image files found:')
for name in filenames:
    match = ext_regex.search(name)
    if match:
        print(f'  {name}  (extension: {match.group(1)})')
