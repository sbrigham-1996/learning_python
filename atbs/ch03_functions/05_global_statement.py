# 05_global_statement.py
# Chapter 3 — The global Statement
#
# By default, assigning to a variable inside a function creates a local variable.
# The global statement tells Python to use the global variable instead.


# --- Example 1: The problem global solves ---
# Without global, a function cannot modify a global variable by assignment.
# This is a repeat of the gotcha from concept 4 — the setup for why global exists.

lives = 3   # global

def lose_a_life_broken():
    lives = lives - 1   # Python sees assignment, creates a local — but then tries
                        # to read it before it's assigned. This crashes with UnboundLocalError.
    print(lives)

# lose_a_life_broken()   # uncomment to see: UnboundLocalError


# --- Example 2: global fixes it ---
# Declaring `global lives` tells Python: any reference to `lives` in this
# function means the global variable — do not create a local.

lives = 3

def lose_a_life():
    global lives
    lives = lives - 1   # now this reads AND writes the global
    print('Lives remaining:', lives)

lose_a_life()   # Lives remaining: 2
lose_a_life()   # Lives remaining: 1
lose_a_life()   # Lives remaining: 0
print('Final lives value:', lives)   # 0 — the global was modified each time


# --- Example 3: global is only needed for assignment ---
# If you are only READING a global variable, you do not need the global statement.
# Python finds it automatically. global is only required when you want to assign to it.

player = 'Spencer'

def print_player():
    print('Player:', player)   # reading global — no global statement needed

print_player()   # Player: Spencer


# --- Example 4: The better alternative — arguments and return values ---
# Most of the time, global can and should be avoided.
# Pass the value in as an argument, return the new value out.
# This keeps the function self-contained and easier to test and debug.

def lose_a_life_clean(current_lives):
    return current_lives - 1   # no global needed — takes a value in, sends one back

lives = 3
lives = lose_a_life_clean(lives)
lives = lose_a_life_clean(lives)
print('Lives after two losses (clean version):', lives)   # 1


# --- Example 5: Multiple globals in one function ---
# You can declare more than one global variable in a single function.
# List them on the same line, separated by commas.

high_score = 0
current_level = 1

def advance_level(points):
    global high_score, current_level
    current_level += 1
    if points > high_score:
        high_score = points
    print(f'Level: {current_level} | High score: {high_score}')

advance_level(500)    # Level: 2 | High score: 500
advance_level(300)    # Level: 3 | High score: 500  (300 did not beat it)
advance_level(800)    # Level: 4 | High score: 800

