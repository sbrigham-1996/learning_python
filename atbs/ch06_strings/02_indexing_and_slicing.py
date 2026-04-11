# Ch. 6 — String Indexing and Slicing
# Same rules as lists (Ch. 4), applied to strings.
# Key difference: strings are IMMUTABLE — you can read by index, not write.

name = "Spencer"

# --- Basic Indexing ---
print(name[0])    # 'S' — first character
print(name[1])    # 'p'
print(name[-1])   # 'r' — last character (negative counts from the end)
print(name[-2])   # 'e' — second to last

# --- len() ---
print(len(name))  # 7 — number of characters

# The last valid index is always len(s) - 1
print(name[len(name) - 1])  # 'r' — same as name[-1], but the long way

# --- Slicing ---
# s[start:end] — includes start, excludes end (same as range() and list slicing)
print(name[0:3])  # 'Spe' — indexes 0, 1, 2
print(name[3:])   # 'ncer' — from index 3 to the end
print(name[:4])   # 'Spen' — from start up to (not including) index 4
print(name[:])    # 'Spencer' — full copy of the string

# --- Negative Indexes in Slices ---
print(name[-4:])  # 'ncer' — last 4 characters
print(name[:-2])  # 'Spenc' — everything except the last 2

# --- Practical Example: extracting parts of a string ---
date = "2026-04-06"
year  = date[:4]    # '2026'
month = date[5:7]   # '04'
day   = date[8:]    # '06'
print(f"Year: {year}, Month: {month}, Day: {day}")

# --- Iterating Over a String ---
# Because strings are sequences, you can loop over them just like lists.
for char in "hello":
    print(char)

# --- Immutability Demo ---
# This is the key difference from lists. You CANNOT assign to an index.
# Uncommenting the line below raises: TypeError: 'str' object does not support item assignment
# name[0] = 's'

# To get a modified version, you build a NEW string.
# Common pattern: slice around the part you want to change, then concatenate.
lowercased_first = name[0].lower() + name[1:]
print(lowercased_first)  # 'spencer' — new string, original 'name' is unchanged
print(name)              # 'Spencer' — still the original
