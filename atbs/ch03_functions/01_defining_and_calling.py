# Chapter 3 — Functions
# Concept 1: Defining and calling functions with def

# --- Defining a function ---
# The 'def' keyword tells Python: "I'm creating a reusable block of code
# called 'greet'. Don't run it yet — just remember it."

def greet():
    print('Hello!')
    print('How are you?')


# At this point in the script, nothing has printed yet.
# The function body is defined but hasn't executed.

# --- Calling a function ---
# Parentheses after the name is what actually triggers execution.

greet()   # first call — runs the body once
greet()   # second call — runs the same body again

# This is the core value of functions: write once, use many times.
# If you want to change the greeting, you change it in one place.


# --- A more realistic example ---
# Without functions, repetition creates maintenance problems.

def display_welcome():
    print('----------------------------')
    print('Welcome to Spencer\'s Program')
    print('----------------------------')


display_welcome()
print('Loading data...')
display_welcome()   # reuse the same formatted header anywhere you need it
