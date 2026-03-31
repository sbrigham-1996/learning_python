# Chapter 2 - Flow Control
# Concept 7: sys.exit()

# sys is a built-in module — we need to import it before we can use it.
# 'import' loads the module so its functions become available.
import sys

# -----------------------------------------------------------------------------
# BASIC sys.exit()
# Everything after sys.exit() is unreachable — Python stops immediately.
# Uncomment the lines below to see it in action.
# -----------------------------------------------------------------------------

# sys.exit()
# print('This line will never run.')   # never reached

# -----------------------------------------------------------------------------
# sys.exit() WITH A MESSAGE
# Pass a string to print a message before exiting.
# Useful for telling the user (or yourself) why the program stopped.
# An exit code of 0 means success. Any other value signals an error.
# -----------------------------------------------------------------------------

# sys.exit('Exiting with a message.')   # uncomment to test

# -----------------------------------------------------------------------------
# PRACTICAL USE CASE 1 — guard clause at startup
# Check a required condition before doing any real work.
# If the condition isn't met, exit immediately with a clear message.
# This pattern is called a "guard clause."
# -----------------------------------------------------------------------------

minimum_age = 18
user_age = 15

if user_age < minimum_age:
    print('You must be 18 or older to use this program.')
    # sys.exit()   # uncomment to actually exit — commented so script keeps running

print('Welcome! Continuing with the program...')

# -----------------------------------------------------------------------------
# PRACTICAL USE CASE 2 — exit inside a loop
# sys.exit() works anywhere — inside loops, inside if blocks, anywhere.
# Unlike break (exits the loop), sys.exit() exits the ENTIRE program.
# -----------------------------------------------------------------------------

passwords = ['wrong', 'wrong', 'wrong']   # simulated attempts, none correct
max_attempts = 3
attempts = 0

for password in passwords:
    attempts += 1
    print(f'Attempt {attempts}: {password}')
    if password == 'correct':
        print('Access granted.')
        break
    if attempts == max_attempts:
        print('Too many failed attempts. Exiting.')
        # sys.exit('Access denied.')   # uncomment to actually exit

print('Script completed.')   # reaches here because sys.exit() is commented out

# -----------------------------------------------------------------------------
# break vs sys.exit() — THE KEY DISTINCTION
# -----------------------------------------------------------------------------

# break:     exits the current loop only. Code after the loop still runs.
# sys.exit(): exits the entire program. Nothing else runs at all.

for i in range(5):
    if i == 2:
        break        # exits the loop
    print('loop i:', i)

print('This runs after the loop.')   # still runs after break

# If that had been sys.exit() instead of break:
# print('This runs after the loop.') would NEVER execute.

# -----------------------------------------------------------------------------
# SUMMARY — when to use each exit tool
# break      → exit a loop, continue the rest of the program
# continue   → skip this iteration, keep looping
# sys.exit() → stop the entire program immediately
# -----------------------------------------------------------------------------
