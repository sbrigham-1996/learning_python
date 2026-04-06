# Ch. 5 — Dictionaries & Structuring Data
# Concept 5: Pretty printing with pprint

import pprint

# A nested dict — the kind of structure where plain print() falls apart
project = {
    'name': 'Highway 54 Widening',
    'client': 'NCDOT',
    'team': ['Spencer', 'Alice', 'Bob'],
    'borings': {
        'B-1': {'depth_ft': 30, 'soil': 'sandy clay'},
        'B-2': {'depth_ft': 45, 'soil': 'silty sand'},
        'B-3': {'depth_ft': 20, 'soil': 'rock'},
    },
    'complete': False,
}

# Plain print — everything on one line, hard to read
print('--- print() ---')
print(project)

# pprint.pprint() — formatted with indentation, much easier to scan
print('\n--- pprint.pprint() ---')
pprint.pprint(project)

# pprint.pformat() — same formatting, but returns a string instead of printing
# Useful when you want to log it, write it to a file, or build it into a message
print('\n--- pprint.pformat() stored in a variable ---')
formatted = pprint.pformat(project)
print(type(formatted))   # <class 'str'>
print(formatted)
