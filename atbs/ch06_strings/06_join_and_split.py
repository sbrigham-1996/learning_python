# Ch. 6 — join() and split()
# Two inverse methods: split() breaks a string into a list, join() assembles a list into a string.

# --- split() — string to list ---
# Default: splits on any whitespace, discards empty strings from extra spaces.

sentence = "the quick brown fox"
words = sentence.split()
print(words)   # ['the', 'quick', 'brown', 'fox']

# Extra whitespace between words is handled gracefully
messy = "  too   many    spaces  "
print(messy.split())  # ['too', 'many', 'spaces'] — clean result, no empty strings

# Splitting on a specific delimiter
csv_line = "Spencer,Python,2026"
fields = csv_line.split(",")
print(fields)  # ['Spencer', 'Python', '2026']

# Splitting a file path
path = "users/spencer/documents/notes.txt"
parts = path.split("/")
print(parts)   # ['users', 'spencer', 'documents', 'notes.txt']

# --- join() — list to string ---
# Called on the DELIMITER string, not on the list.
# Every item in the list must be a string — join() won't convert for you.

words = ["the", "quick", "brown", "fox"]
print(" ".join(words))    # 'the quick brown fox' — space delimiter
print("-".join(words))    # 'the-quick-brown-fox' — hyphen delimiter
print("".join(words))     # 'thequickbrownfox'    — no delimiter, all joined

# --- join() is called on the delimiter — the mental model ---
# Think of it as: delimiter.join(list)
# The separator string is the one doing the joining.
parts = ["users", "spencer", "documents", "notes.txt"]
print("/".join(parts))    # 'users/spencer/documents/notes.txt' — path rebuilt

# --- split() and join() are inverses ---
# Splitting then joining (with the same delimiter) gives you back the original.
original = "one,two,three"
print(",".join(original.split(",")))  # 'one,two,three' — round trip

# --- Practical Example: Normalizing User Input ---
# A user types a sentence with inconsistent spacing.
# Split + join is the clean way to normalize it.
raw_input = "  hello     world   how   are  you  "
normalized = " ".join(raw_input.split())
print(f"'{normalized}'")  # 'hello world how are you' — single spaces, no leading/trailing

# --- Practical Example: Building a Sentence from a List ---
# join() is the right tool any time you're assembling strings from parts.
items = ["apples", "bananas", "cherries"]
shopping = ", ".join(items)
print(f"I need to buy: {shopping}")  # 'I need to buy: apples, bananas, cherries'

# --- Common Mistake: join() requires all strings ---
# This would raise a TypeError:
# mixed = ["item1", 2, "item3"]
# print(", ".join(mixed))   # TypeError: sequence item 1: expected str instance, int found
# Fix: convert to strings first
mixed = ["item1", 2, "item3"]
print(", ".join(str(item) for item in mixed))  # 'item1, 2, item3'
