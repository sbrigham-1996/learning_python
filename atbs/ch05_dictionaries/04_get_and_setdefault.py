# Ch. 5 — Dictionaries & Structuring Data
# Concept 4: get() and setdefault()

person = {
    'name': 'Spencer',
    'age': 29,
    'job': 'Geotechnical Engineer',
}

# --- get() ---
# Safe lookup: returns the value if the key exists,
# or a fallback default if it doesn't. Never raises KeyError.

print(person.get('name', 'Unknown'))     # Spencer — key exists
print(person.get('salary', 0))          # 0 — key missing, returns default
print(person.get('city'))               # None — no default given, missing key → None

# Without get(), you'd have to write this manually every time:
# if 'salary' in person:
#     print(person['salary'])
# else:
#     print(0)
# get() replaces that whole block with one line.

# --- setdefault() ---
# Like get(), but also INSERTS the key with the default if it's missing.
# Use this when you want to guarantee a key exists before working with it.

# Key already exists — setdefault does nothing, returns current value
result = person.setdefault('name', 'No name')
print(result)          # Spencer — unchanged
print(person['name'])  # Spencer — dict not modified

# Key does NOT exist — setdefault inserts it and returns the default
result = person.setdefault('city', 'Chapel Hill')
print(result)          # Chapel Hill — inserted
print(person['city'])  # Chapel Hill — now in the dict

# --- A practical pattern: building a dict of lists ---
# Count how many times each letter appears in a word.
# The first time we see a letter, we need to initialize its list.
# setdefault() handles that initialization in one step.

word = 'geotechnical'
letter_positions = {}

for index, letter in enumerate(word):
    letter_positions.setdefault(letter, [])   # init list if needed
    letter_positions[letter].append(index)    # always safe to append now

print(letter_positions)
# Each letter maps to a list of indexes where it appears in the word
