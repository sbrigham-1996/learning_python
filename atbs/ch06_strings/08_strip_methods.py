# Ch. 6 — Stripping Whitespace: strip(), lstrip(), rstrip()
# Removes leading/trailing whitespace (or specified characters) from a string.
# Never touches whitespace in the middle of a string.

# --- Basic Usage ---
messy = "   Hello, World!   "

print(messy.strip())    # 'Hello, World!'  — both ends cleaned
print(messy.lstrip())   # 'Hello, World!   ' — left end only
print(messy.rstrip())   # '   Hello, World!' — right end only

# Middle whitespace is untouched
spaced = "   too   much   space   "
print(spaced.strip())   # 'too   much   space' — edges clean, middle unchanged

# --- The Most Common Use: Cleaning Input ---
# Users accidentally add spaces — strip() before comparing prevents silent failures.
username = input("Enter your username: ")
if username.strip().lower() == "spencer":
    print("Welcome, Spencer!")
else:
    print("Unknown user.")

# Without .strip(), "  spencer  " would not match "spencer" — an invisible bug.

# --- File Lines Always End with \n ---
# When you read lines from a file (Ch. 9), each line ends with a newline character.
# strip() is the standard way to remove it before working with the content.
line_from_file = "Spencer,Python,2026\n"
print(repr(line_from_file))          # 'Spencer,Python,2026\n' — \n is visible with repr()
print(repr(line_from_file.strip()))  # 'Spencer,Python,2026'   — \n removed

# rstrip() is also common here — strips the trailing \n without touching the left side
print(repr(line_from_file.rstrip())) # 'Spencer,Python,2026'

# --- Stripping Specific Characters ---
# Pass a string of characters to remove instead of whitespace.
# It strips any combination of those characters from the edges — not a substring.

greeting = "!!!Hello, World!!!"
print(greeting.strip("!"))      # 'Hello, World' — all leading/trailing ! removed

punctuation = "...wait, what?..."
print(punctuation.strip("."))   # 'wait, what?' — dots removed from both ends

# The argument is a SET of characters — order doesn't matter, each is stripped individually
print("xxyHelloyxx".strip("xy"))  # 'Hello' — any x or y stripped from edges

# Stripping multiple different characters
messy_value = "  ##  42  ##  "
print(messy_value.strip().strip("#").strip())  # '42' — chain strips for multiple passes

# --- Practical Example: Cleaning a List of Raw Inputs ---
raw_entries = ["  Alice  ", "Bob\n", "  CHARLIE  ", "\tDave\t"]
cleaned = [entry.strip().title() for entry in raw_entries]
print(cleaned)  # ['Alice', 'Bob', 'Charlie', 'Dave']
