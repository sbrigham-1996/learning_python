import pyinputplus as pyip

# Range constraints add a second layer of validation on top of type checking.
# PyInputPlus handles both in one call — no nested if/else needed.

# --- min and max (inclusive boundaries) ---
# min=1, max=10 means: 1 <= value <= 10
# The boundary values themselves are allowed.

print("--- min and max (inclusive) ---")
score = pyip.inputInt("Enter a score (1-10): ", min=1, max=10)
print(f"Score recorded: {score}")

# --- greaterThan and lessThan (exclusive boundaries) ---
# greaterThan=0 means: value > 0  (zero itself is rejected)
# lessThan=100 means: value < 100  (100 itself is rejected)

print("\n--- greaterThan and lessThan (exclusive) ---")
percentage = pyip.inputFloat("Enter a percentage (0-100, endpoints excluded): ",
                             greaterThan=0, lessThan=100)
print(f"Percentage: {percentage}%")

# --- Mixing min and lessThan ---
# You can combine them freely. Here: value >= 0 but value < 1
# Useful for things like probabilities (0.0 to just under 1.0)

print("\n--- min=0, lessThan=1 (probability range) ---")
probability = pyip.inputFloat("Enter a probability [0, 1): ", min=0, lessThan=1)
print(f"Probability: {probability}")