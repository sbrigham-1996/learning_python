# Chapter 1 — String Concatenation and Replication
# + and * work on strings, but they mean something different than with numbers.

# --- Concatenation: joining strings with + ---
print("Hello" + " " + "World")   # Hello World
print("Spam" + "Spam" + "Spam")   # SpamSpamSpam

# The space between "Hello" and "World" has to be explicit.
# Python won't add spacing for you — what you join is exactly what you get.
print("Hello" + "World")         # HelloWorld (no space)

# --- Replication: repeating a string with * ---
print("Ha" * 3)                   # HaHaHa
print("-" * 20)                   # -------------------- (useful for visual separators)
print(3 * "Ha")                   # HaHaHa — order doesn't matter

# --- Type rules ---
# Both sides of + must be strings. This will cause a TypeError:
# print("Alice" + 42)            # uncomment to see the error

# Replication requires an int, not a float. This will also cause a TypeError:
# print("Ha" * 3.0)              # uncomment to see the error

# --- Practical example: building a simple banner ---
name = "Spencer"
print("*" * 20)
print("Hello, " + name)
print("*" * 20)
