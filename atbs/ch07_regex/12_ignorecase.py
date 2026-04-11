# Chapter 7 — Pattern Matching with Regular Expressions
# Concept 12: Case-insensitive matching with re.IGNORECASE
#
# Key idea: by default regex is case-sensitive.
# Passing re.IGNORECASE (or re.I) as the second argument to re.compile()
# makes the pattern treat uppercase and lowercase as equivalent.

import re

# --- Default behavior: case-sensitive ---
case_sensitive = re.compile(r'hello')
print('Case-sensitive matches:')
for text in ['hello world', 'Hello world', 'HELLO WORLD']:
    match = case_sensitive.search(text)
    print(f'  {text!r:<16} -> {"match" if match else "no match"}')

print()

# --- re.IGNORECASE: case-insensitive ---
case_insensitive = re.compile(r'hello', re.IGNORECASE)
print('Case-insensitive matches (re.IGNORECASE):')
for text in ['hello world', 'Hello world', 'HELLO WORLD', 'hElLo WoRlD']:
    match = case_insensitive.search(text)
    print(f'  {text!r:<16} -> {"match" if match else "no match"}')

print()

# --- re.I is the shorthand ---
# re.I and re.IGNORECASE are identical — use whichever reads more clearly to you
robocop = re.compile(r'robocop', re.I)
print('re.I shorthand:')
for text in ['RoboCop', 'ROBOCOP', 'robocop', 'Robocop']:
    match = robocop.search(text)
    print(f'  {text!r:<10} -> {"match" if match else "no match"}')

print()

# --- Practical example: keyword search in user-generated text ---
# Users might type "Python", "python", "PYTHON" — all should count
keyword_regex = re.compile(r'\bpython\b', re.IGNORECASE)
# \b is a word boundary — ensures we match the whole word, not 'python' inside 'pythons'
posts = [
    'I love Python!',
    'Learning PYTHON is fun.',
    'Is python hard to learn?',
    'My boa constrictor is a python.',  # lowercase, different meaning — still matches
    'java is not python',
]
print('Keyword search (case-insensitive):')
for post in posts:
    match = keyword_regex.search(post)
    print(f'  {"match" if match else "no match":<8} {post!r}')

print()

# --- re.IGNORECASE with findall() ---
text = 'Run run RUN running Runner'
run_regex = re.compile(r'run\w*', re.IGNORECASE)
print('findall() with re.IGNORECASE:')
print(' ', run_regex.findall(text))
# ['Run', 'run', 'RUN', 'running', 'Runner']
# The matched text preserves the ORIGINAL casing — the flag affects matching only
