# Chapter 2 - Flow Control
# Concept 4: while Loops

# -----------------------------------------------------------------------------
# BASIC while LOOP
# The block runs repeatedly as long as the condition is True.
# Something inside the loop must eventually make the condition False,
# or the loop will run forever.
# -----------------------------------------------------------------------------

count = 0

while count < 5:
    print('count is:', count)
    count = count + 1   # this is what makes the condition eventually False
                        # without this line, the loop would never stop

print('Loop finished. count is now:', count)

# -----------------------------------------------------------------------------
# HOW THE LOOP WORKS STEP BY STEP
# Iteration 1: count=0, 0 < 5 is True  → print, count becomes 1
# Iteration 2: count=1, 1 < 5 is True  → print, count becomes 2
# Iteration 3: count=2, 2 < 5 is True  → print, count becomes 3
# Iteration 4: count=3, 3 < 5 is True  → print, count becomes 4
# Iteration 5: count=4, 4 < 5 is True  → print, count becomes 5
# Check again: count=5, 5 < 5 is False → loop exits
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# A SHORTER WAY TO INCREMENT
# count = count + 1 is so common Python gives you a shorthand: count += 1
# These are identical. += is more Pythonic.
# Same pattern works for -=, *=, /=
# -----------------------------------------------------------------------------

count = 0
while count < 3:
    print('shorthand count:', count)
    count += 1

# -----------------------------------------------------------------------------
# while WITH A BOOLEAN FLAG
# Instead of a comparison, you can use a variable that flips to False
# when you want the loop to stop. Common pattern for "keep going until done."
# -----------------------------------------------------------------------------

game_running = True
lives = 3

while game_running:
    print('Lives remaining:', lives)
    lives -= 1
    if lives == 0:
        game_running = False   # flips the flag, loop exits on next check

print('Game over.')

# -----------------------------------------------------------------------------
# while FOR INPUT VALIDATION
# A classic use case: keep asking until the user gives a valid answer.
# We simulate user input here with a list to avoid blocking the script.
# In a real program you would use: user_input = input('Enter a number: ')
# -----------------------------------------------------------------------------

# Simulating a sequence of user attempts
responses = ['dog', 'cat', '42']   # first two are invalid, third is valid
attempt = 0

user_input = responses[attempt]

while not user_input.isdigit():
    print(f'"{user_input}" is not a number. Try again.')
    attempt += 1
    user_input = responses[attempt]

print(f'Valid number received: {user_input}')

# -----------------------------------------------------------------------------
# WHILE TRUE — intentional infinite loop with a planned exit
# Sometimes you want to loop forever BY DESIGN and break out from inside.
# We'll cover 'break' properly in Concept 6, but here's a preview of
# the pattern so the while True structure makes sense when you see it.
# -----------------------------------------------------------------------------

attempts = ['bad', 'bad', 'good']
index = 0

while True:
    response = attempts[index]
    index += 1
    if response == 'good':
        print('Got a good response, stopping.')
        break   # immediately exits the loop
