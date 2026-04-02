# 04_local_and_global_scope.py
# Chapter 3 — Local and Global Scope
#
# Scope determines where a variable is visible and how long it lives.
# Local variables exist only inside the function that created them.
# Global variables exist at the top level and last the entire program.


# --- Example 1: Local variables are invisible outside their function ---
# The variable `x` below only exists while inside_function() is running.
# Trying to access it from outside raises a NameError.

def inside_function():
    x = 100          # local variable — only lives inside this function
    print(x)         # works fine here

inside_function()    # prints 100
# print(x)          # would crash: NameError — x is not defined here


# --- Example 2: Global variables are readable inside functions ---
# A function can read a global variable without any special syntax.

player_name = 'Spencer'   # global variable

def greet_player():
    print('Welcome, ' + player_name)   # reading the global — this is fine

greet_player()   # Welcome, Spencer


# --- Example 3: Assigning inside a function creates a LOCAL variable ---
# This is the big gotcha. If you assign to a name inside a function,
# Python creates a brand-new local variable — it does NOT touch the global.

score = 0   # global

def reset_score():
    score = 999   # this creates a LOCAL variable named score — the global is untouched
    print('Inside function, score =', score)

reset_score()
print('Outside function, score =', score)   # still 0 — the global was never changed


# --- Example 4: Two functions can share a variable name without conflict ---
# Local scopes are completely isolated from each other.
# Each function call gets its own private workspace.

def function_a():
    value = 'I am in function A'
    print(value)

def function_b():
    value = 'I am in function B'   # totally separate variable, same name — no conflict
    print(value)

function_a()   # I am in function A
function_b()   # I am in function B


# --- Example 5: Local variables do not persist between calls ---
# Each time you call a function, its local variables start fresh.
# They are not saved from one call to the next.

def count_up():
    counter = 0       # starts at 0 every single call
    counter += 1
    print('counter =', counter)

count_up()   # counter = 1
count_up()   # counter = 1  (not 2 — it reset)
count_up()   # counter = 1  (resets every time)
