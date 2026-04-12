import pyinputplus as pyip

# limit and timeout control what happens when the user can't provide valid input.
# Without them, PyInputPlus loops forever. These give you an exit condition.

# --- limit: max number of attempts ---
# After 3 failed attempts, PyInputPlus raises RetryLimitException.
# We catch it and handle the failure explicitly.

print("--- limit (3 attempts) ---")
try:
    number = pyip.inputInt("Enter a number between 1 and 5: ", min=1, max=5, limit=3)
    print(f"You entered: {number}")
except pyip.RetryLimitException:
    print("Too many failed attempts. Moving on.")

# --- timeout: max seconds to wait ---
# If valid input is not received within 8 seconds, raises TimeoutException.
# The clock runs from the first prompt — not per attempt.

print("\n--- timeout (8 seconds) ---")
try:
    answer = pyip.inputStr("Quick! Type anything (8 seconds): ", timeout=8)
    print(f"You typed: {answer}")
except pyip.TimeoutException:
    print("Time's up! No input received.")

# --- default: fallback value instead of raising an exception ---
# When limit or timeout is hit, returns the default value silently.
# Cleaner than try/except when a fallback makes sense.

print("\n--- default with limit ---")
result = pyip.inputInt("Enter a number (3 attempts, default=0): ",
                       min=1, max=5, limit=3, default=0)
print(f"Result: {result}")
