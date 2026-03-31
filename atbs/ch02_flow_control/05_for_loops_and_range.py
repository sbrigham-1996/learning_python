# Chapter 2 - Flow Control
# Concept 5: for Loops and range()

# -----------------------------------------------------------------------------
# BASIC for LOOP OVER A LIST
# Python pulls each item from the list one at a time, assigns it to the
# loop variable, and runs the block. No index management, no condition.
# -----------------------------------------------------------------------------

fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)

# apple
# banana
# cherry

# -----------------------------------------------------------------------------
# for LOOP OVER A STRING
# Strings are sequences too — you can iterate over each character.
# -----------------------------------------------------------------------------

for letter in 'hello':
    print(letter)

# h, e, l, l, o — one per line

# -----------------------------------------------------------------------------
# range() — GENERATING A SEQUENCE OF NUMBERS
# range(stop)         → 0 up to (but not including) stop
# range(start, stop)  → start up to (but not including) stop
# range(start, stop, step) → start up to stop, counting by step
# -----------------------------------------------------------------------------

# range(5) → 0, 1, 2, 3, 4
print('range(5):')
for i in range(5):
    print(i)

# range(2, 8) → 2, 3, 4, 5, 6, 7
print('range(2, 8):')
for i in range(2, 8):
    print(i)

# range(0, 10, 2) → 0, 2, 4, 6, 8  (step of 2)
print('range(0, 10, 2):')
for i in range(0, 10, 2):
    print(i)

# range can count backwards with a negative step
print('range(5, 0, -1):')
for i in range(5, 0, -1):
    print(i)   # 5, 4, 3, 2, 1

# -----------------------------------------------------------------------------
# THE "STOPS BEFORE" RULE
# range(5) gives you 0–4, not 0–5. Five total numbers, last one is 4.
# This is consistent with how Python handles indexing everywhere.
# If you want 1 through 5 inclusive, use range(1, 6).
# -----------------------------------------------------------------------------

print('1 through 5 inclusive:')
for i in range(1, 6):
    print(i)   # 1, 2, 3, 4, 5

# -----------------------------------------------------------------------------
# REPEAT SOMETHING N TIMES
# When you just need to repeat a block and don't care about the number itself,
# the convention is to name the loop variable _ (underscore).
# _ means "I need a loop variable but I'm not going to use it."
# -----------------------------------------------------------------------------

for _ in range(3):
    print('This prints exactly 3 times.')

# -----------------------------------------------------------------------------
# for vs while — REWRITING THE SAME LOOP
# Anything a for loop can do, a while loop can do too — but for is cleaner
# when you're iterating over a known sequence.
# -----------------------------------------------------------------------------

# while version
i = 0
while i < 5:
    print('while:', i)
    i += 1

# for version — same result, less to manage
for i in range(5):
    print('for:', i)

# The for version has no manual increment, no condition to maintain.
# Use for when you know the sequence. Use while when you don't.

# -----------------------------------------------------------------------------
# PRACTICAL EXAMPLE — summing numbers
# -----------------------------------------------------------------------------

total = 0
for number in range(1, 11):   # 1 through 10 inclusive
    total += number

print('Sum of 1 through 10:', total)   # 55
