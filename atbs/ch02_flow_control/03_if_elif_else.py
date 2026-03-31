# Chapter 2 - Flow Control
# Concept 3: if / elif / else

# -----------------------------------------------------------------------------
# BASIC if STATEMENT
# The block indented under 'if' only runs if the condition is True.
# If it's False, Python skips that block entirely.
# -----------------------------------------------------------------------------

age = 20

if age >= 18:
    print('You are an adult.')   # this runs because 20 >= 18 is True

if age >= 100:
    print('You are a centenarian.')   # this is skipped because 20 >= 100 is False

# -----------------------------------------------------------------------------
# if / else
# 'else' is the fallback — it runs when the 'if' condition is False.
# Exactly one of the two blocks will always run.
# -----------------------------------------------------------------------------

temperature = 35

if temperature >= 30:
    print('It is hot outside.')    # runs — 35 >= 30 is True
else:
    print('It is not that hot.')   # skipped

temperature = 15

if temperature >= 30:
    print('It is hot outside.')    # skipped — 15 >= 30 is False
else:
    print('It is not that hot.')   # runs — the fallback

# -----------------------------------------------------------------------------
# if / elif / else
# 'elif' lets you check additional conditions if the first was False.
# Python checks top to bottom and STOPS at the first True condition.
# Only one block ever runs.
# -----------------------------------------------------------------------------

score = 72

if score >= 90:
    print('Grade: A')
elif score >= 80:
    print('Grade: B')
elif score >= 70:
    print('Grade: C')   # this runs — 72 >= 70 is True
elif score >= 60:
    print('Grade: D')   # skipped — Python already found a True above
else:
    print('Grade: F')   # skipped

# -----------------------------------------------------------------------------
# ORDER MATTERS — the "only one block runs" rule in action
# Both conditions below could be True, but only the FIRST True one runs.
# -----------------------------------------------------------------------------

x = 10

if x > 5:
    print('x is greater than 5')    # runs — and Python stops here
elif x > 3:
    print('x is greater than 3')    # skipped — even though it's also True!

# If you need BOTH to potentially run, use two separate if statements:
if x > 5:
    print('x is greater than 5')    # runs
if x > 3:
    print('x is greater than 3')    # also runs — independent check

# -----------------------------------------------------------------------------
# COMBINING WITH BOOLEAN OPERATORS
# Conditions in if/elif can use 'and', 'or', 'not' for complex checks.
# -----------------------------------------------------------------------------

username = 'spencer'
password = 'correct_password'

if username == 'spencer' and password == 'correct_password':
    print('Access granted.')
else:
    print('Access denied.')

# -----------------------------------------------------------------------------
# NESTED if STATEMENTS
# You can put an if inside another if. Each level gets another 4 spaces.
# Use sparingly — deep nesting gets hard to read fast.
# -----------------------------------------------------------------------------

is_raining = True
has_umbrella = False

if is_raining:
    if has_umbrella:
        print('It is raining but you have an umbrella.')
    else:
        print('It is raining and you have no umbrella. Get inside!')
else:
    print('No rain. Enjoy your day.')
