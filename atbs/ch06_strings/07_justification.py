# Ch. 6 — String Justification: rjust(), ljust(), center()
# These methods pad a string to a specified width for aligned output.

# --- Basic Usage ---
print("hello".rjust(10))   # '     hello' — padded on the left, right-aligned
print("hello".ljust(10))   # 'hello     ' — padded on the right, left-aligned
print("hello".center(10))  # '  hello   ' — padded on both sides, centered

# Width is the TOTAL length of the result, not the amount of padding added.
print(len("hello".rjust(10)))   # 10
print(len("hello".ljust(10)))   # 10

# If the string is already as long or longer than width, nothing changes.
print("hello".rjust(3))   # 'hello' — no truncation, returned as-is

# --- Custom Fill Character ---
# Pass a second argument to use something other than a space.
print("hello".rjust(10, "-"))   # '-----hello'
print("hello".ljust(10, "."))   # 'hello.....'
print("hello".center(11, "*"))  # '***hello***'

# --- The Real Use Case: Aligned Tabular Output ---
# Without justification, columns are jagged and hard to read.
data = [
    ("Apples",   42,  1.20),
    ("Bananas",   7,  0.50),
    ("Cherries", 150, 3.99),
]

# Unaligned — hard to read
print("--- Unaligned ---")
for name, qty, price in data:
    print(name, qty, price)

# Aligned using ljust/rjust — columns line up cleanly
print("\n--- Aligned ---")
for name, qty, price in data:
    print(name.ljust(12) + str(qty).rjust(6) + str(price).rjust(8))

# --- Building a Table with a Header ---
# rjust/ljust work great for building simple text tables.
def print_table(data):
    header = ("Item", "Qty", "Price")
    print(header[0].ljust(12) + header[1].rjust(6) + header[2].rjust(8))
    print("-" * 26)
    for name, qty, price in data:
        print(name.ljust(12) + str(qty).rjust(6) + f"{price:.2f}".rjust(8))

print()
print_table(data)

# --- center() for Headings ---
title = "Sales Report"
print("\n" + title.center(40, "="))
