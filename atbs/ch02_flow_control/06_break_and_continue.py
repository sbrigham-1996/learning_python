# Chapter 2 - Flow Control
# Concept 6: break and continue

# -----------------------------------------------------------------------------
# break — EXIT THE LOOP ENTIRELY
# When Python hits 'break', it immediately jumps out of the loop.
# Nothing else in the loop body runs, and no more iterations happen.
# -----------------------------------------------------------------------------

# Example: find the first even number in a list and stop
numbers = [1, 3, 7, 4, 9, 2, 6]

for number in numbers:
    if number % 2 == 0:
        print('First even number found:', number)
        break   # no point checking the rest
    print('Checking:', number)   # this only prints for numbers before the break

# Output:
# Checking: 1
# Checking: 3
# Checking: 7
# First even number found: 4   ← loop exits here, 9/2/6 are never checked

# -----------------------------------------------------------------------------
# break IN A while LOOP
# This is the 'while True' pattern previewed in Concept 4.
# The loop runs indefinitely BY DESIGN — break is the planned exit.
# -----------------------------------------------------------------------------

# Simulated user input (in real code, you'd use input())
responses = ['wrong', 'wrong', 'correct']
index = 0

while True:
    answer = responses[index]
    index += 1
    print('Answer given:', answer)
    if answer == 'correct':
        print('You got it!')
        break   # exits the while True loop

# -----------------------------------------------------------------------------
# continue — SKIP THE REST OF THIS ITERATION
# When Python hits 'continue', it jumps back to the top of the loop.
# The loop keeps running — only the current pass is cut short.
# -----------------------------------------------------------------------------

# Example: print only odd numbers, skip evens
print('Odd numbers from 1 to 10:')
for i in range(1, 11):
    if i % 2 == 0:
        continue   # skip the print below for even numbers
    print(i)

# Even numbers hit 'continue' and never reach the print statement.
# Odd numbers skip past the if block and print normally.

# -----------------------------------------------------------------------------
# continue IN A while LOOP
# Same idea — skip processing for certain values, keep looping.
# -----------------------------------------------------------------------------

count = 0
print('Skipping multiples of 3:')
while count < 10:
    count += 1
    if count % 3 == 0:
        continue   # skip the print for 3, 6, 9
    print(count)

# -----------------------------------------------------------------------------
# break vs continue — SIDE BY SIDE
# Same loop, same condition — different behavior.
# -----------------------------------------------------------------------------

print('--- break version ---')
for i in range(1, 6):
    if i == 3:
        break      # stops at 3, never reaches 4 or 5
    print(i)
# prints: 1, 2

print('--- continue version ---')
for i in range(1, 6):
    if i == 3:
        continue   # skips 3, but keeps going to 4 and 5
    print(i)
# prints: 1, 2, 4, 5

# -----------------------------------------------------------------------------
# PRACTICAL EXAMPLE — searching with break, filtering with continue
# -----------------------------------------------------------------------------

students = [
    {'name': 'Alice', 'grade': 91},
    {'name': 'Bob',   'grade': 54},
    {'name': 'Carol', 'grade': 78},
    {'name': 'Dave',  'grade': 43},
    {'name': 'Eve',   'grade': 88},
]

# Use continue to skip failing students, print passing ones
print('Passing students:')
for student in students:
    if student['grade'] < 60:
        continue   # skip failing grades
    print(f"{student['name']}: {student['grade']}")

# Use break to find the first failing student and stop
print('First failing student:')
for student in students:
    if student['grade'] < 60:
        print(f"{student['name']}: {student['grade']}")
        break
