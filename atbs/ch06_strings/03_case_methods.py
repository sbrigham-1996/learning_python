# Ch. 6 — Case Methods: upper(), lower(), isupper(), islower()

# --- Transformation Methods ---
# upper() and lower() return a NEW string — they don't modify the original.

name = "Spencer"
print(name.upper())   # 'SPENCER'
print(name.lower())   # 'spencer'
print(name)           # 'Spencer' — original is unchanged (strings are immutable)

# You can chain method calls — lower() returns a string, so you can call upper() on it
print("hello".upper().lower())  # 'hello' — upper then lower, ends up lowercase

# --- The Key Practical Use: Normalizing Input for Comparison ---
# Without normalization, "yes", "YES", "Yes" would all fail an equality check.

response = input("Continue? (yes/no): ")

if response.lower() == "yes":
    print("Continuing...")
else:
    print("Stopping.")

# .lower() on the input means the user can type Yes, YES, yes, YeS — all work.
# This is the single most common reason to use lower() in real code.

# --- Testing Methods ---
# isupper() and islower() ask a yes/no question about the string's case.
# They return True only if ALL cased characters match — and there's at least one.

print("HELLO".isupper())    # True
print("hello".islower())    # True
print("Hello".isupper())    # False — 'H' is upper but 'ello' is not all upper
print("Hello".islower())    # False — 'H' is uppercase
print("".isupper())         # False — no cased characters at all

# --- The Subtle Rule: Numbers and Punctuation Don't Count ---
# Non-letter characters have no case, so they're ignored by isupper()/islower().

print("HELLO123".isupper())   # True — digits are ignored, all letters are upper
print("hello!!!".islower())   # True — punctuation is ignored, all letters are lower
print("123".isupper())        # False — no cased characters at all

# --- Combining Transformation and Testing ---
# A common pattern: transform first, then test — or test to decide how to transform.

word = "Python"
if word[0].isupper():
    print(f"'{word}' starts with a capital letter")

# Building a simple title-case check manually (before we learn istitle()):
words = ["the", "quick", "Brown", "fox"]
capitalized = [w[0].upper() + w[1:].lower() for w in words]
print(capitalized)  # ['The', 'Quick', 'Brown', 'Fox']
