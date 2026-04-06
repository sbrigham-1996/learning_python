# Ch. 5 — Dictionaries & Structuring Data
# Concept 1: Creating dictionaries and accessing values by key

# A dictionary maps keys to values using curly braces and colons.
# Unlike a list (where you use an index like [0]), you look up values
# by the key you defined — making the code self-documenting.

person = {
    'name': 'Spencer',
    'age': 29,
    'job': 'Geotechnical Engineer',
}

# Access a value by its key
print(person['name'])   # Spencer
print(person['age'])    # 30
print(person['job'])    # Geotechnical Engineer

# You can also store the result in a variable
greeting = 'Hello, ' + person['name'] + '!'
print(greeting)         # Hello, Spencer!

# Keys must be unique — assigning to an existing key overwrites it
person['age'] = 30
print(person['age'])    # 30 (was 29)

# Adding a brand-new key is the same syntax as updating one
person['city'] = 'Chapel Hill'
print(person)           # now has four keys

# Accessing a key that doesn't exist raises a KeyError
# Uncomment the line below to see the error:
# print(person['salary'])
