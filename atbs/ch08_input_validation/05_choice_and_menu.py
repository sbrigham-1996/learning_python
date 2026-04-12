import pyinputplus as pyip

# inputChoice() and inputMenu() constrain input to a fixed set of options.
# Use these instead of manually checking 'if response not in valid_options'.

# --- inputChoice() ---
# User must type one of the provided options exactly.
# No menu is displayed — list the options in your prompt string.

print("--- inputChoice() ---")
direction = pyip.inputChoice(["north", "south", "east", "west"],
                             prompt="Which direction? (north/south/east/west): ")
print(f"Heading: {direction}")

# --- inputChoice() with caseSensitive=False ---
# Accepts any casing — "NORTH", "North", "north" all match.
# The returned value matches what the user typed, not the list entry.

print("\n--- inputChoice() with caseSensitive=False ---")
color = pyip.inputChoice(["red", "green", "blue"], caseSensitive=False,
                         prompt="Pick a color (red/green/blue): ")
print(f"You chose: {color}")

# --- inputMenu() ---
# Displays a numbered list automatically. User can type the option text
# or its number. Good for longer lists where you want PyInputPlus to
# handle the formatting.

print("\n--- inputMenu() ---")
meal = pyip.inputMenu(["pizza", "sushi", "tacos", "salad"],
                      prompt="What do you want for dinner?\n")
print(f"Ordering: {meal}")
