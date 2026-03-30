# Chapter 1 — A Simple Program
# This program brings together everything from Chapter 1:
# expressions, data types, string concatenation, and variables.

# --- New tools used here ---
# input(prompt) : pauses the program, displays the prompt, waits for the user
#                 to type something and press Enter. Always returns a string.
# int(value)    : converts a value to an integer. Needed because input() returns
#                 a string even if the user types a number.
# str(value)    : converts a value to a string. Needed to concatenate a number
#                 into a string with +.

# --- Get the user's name ---
name = input("What is your name? ")

# --- Get the user's age ---
# input() always returns a str, so "25" not 25.
# We wrap it in int() immediately so we can do math with it.
age = int(input("How old are you? "))

# --- Calculate approximate birth year ---
# This is an expression: 2026 minus their age gives an approximate birth year.
birth_year = 2026 - age

# --- Greet the user ---
print("Hello, " + name + "!")

# --- Report their birth year ---
# birth_year is an int, so we must convert it to str before concatenating.
print("You were born in approximately " + str(birth_year) + ".")

# --- Show their age next year ---
print("Next year you will be " + str(age + 1) + " years old.")
