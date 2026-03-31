# Chapter 2 - Flow Control
# Concept 2: Boolean Operators (and, or, not)

# -----------------------------------------------------------------------------
# THE 'and' OPERATOR
# Both sides must be True for the result to be True.
# One False is enough to make the whole expression False.
# -----------------------------------------------------------------------------

print(True and True)    # True  — both sides are True
print(True and False)   # False — one side is False
print(False and True)   # False — one side is False
print(False and False)  # False — both sides are False

# Real-world example: a user must be logged in AND have admin rights
is_logged_in = True
is_admin = False
print(is_logged_in and is_admin)   # False — both must be True, but is_admin isn't

# -----------------------------------------------------------------------------
# THE 'or' OPERATOR
# Only one side needs to be True for the result to be True.
# Only False or False gives you False.
# -----------------------------------------------------------------------------

print(True or True)    # True  — at least one side is True
print(True or False)   # True  — at least one side is True
print(False or True)   # True  — at least one side is True
print(False or False)  # False — neither side is True

# Real-world example: accept 'quit' or 'exit' as valid ways to stop
user_input = 'quit'
print(user_input == 'quit' or user_input == 'exit')   # True

user_input = 'exit'
print(user_input == 'quit' or user_input == 'exit')   # True

user_input = 'hello'
print(user_input == 'quit' or user_input == 'exit')   # False

# -----------------------------------------------------------------------------
# THE 'not' OPERATOR
# Flips the Boolean value. True becomes False, False becomes True.
# -----------------------------------------------------------------------------

print(not True)    # False
print(not False)   # True

# Real-world example: check if a door is NOT locked
is_locked = False
print(not is_locked)   # True — the door is not locked, so we can enter

# -----------------------------------------------------------------------------
# COMBINING OPERATORS — ORDER OF OPERATIONS
# Python evaluates: not → and → or
# Parentheses always override this order and improve readability.
# -----------------------------------------------------------------------------

# Without parentheses — Python evaluates 'not' first, then 'and', then 'or'
print(not False and True or False)
# Step 1: not False → True
# Step 2: True and True → True
# Step 3: True or False → True

# With parentheses — makes the intent explicit and easier to read
age = 20
has_id = True
is_member = False

# "Must be 18+ AND have ID, OR be a member"
print((age >= 18 and has_id) or is_member)   # True — first condition is met

# "Must be 18+ AND (have ID OR be a member)"
print(age >= 18 and (has_id or is_member))   # True — has_id satisfies the 'or'

# These two expressions look similar but can produce different results
# depending on the values — parentheses make your intent unambiguous.
