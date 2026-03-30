# Chapter 1 — Expressions
# An expression is any value + operator combination that Python evaluates to a result.
# Python reads each expression and "collapses" it down to a single value.

# --- Basic arithmetic ---
2 + 2        # evaluates to 4
10 - 3       # evaluates to 7
3 * 5        # evaluates to 15
22 / 7       # evaluates to 3.142857... (always returns a float)

# --- Two division operators worth knowing ---
22 // 7      # integer division: drops the decimal, returns 3
22 % 7       # modulo: returns the *remainder* only, returns 1

# --- Exponents ---
2 ** 3       # 2 to the power of 3 = 8
2 ** 8       # 2 to the power of 8 = 256

# --- Order of operations (PEMDAS applies) ---
2 + 3 * 6        # = 20, because * happens before +
(2 + 3) * 6      # = 30, parentheses force the addition first
2 ** 2 + 5       # = 9,  exponent happens before addition
2 ** (2 + 5)     # = 128, parentheses change what gets exponentiated

# --- Printing results so we can actually see them ---
# Python won't display anything unless you use print().
# In the interactive shell (REPL), expressions display automatically.
# In a .py script, you must print explicitly.

print(2 + 2)
print(22 // 7)
print(22 % 7)
print(2 ** 8)
print(2 + 3 * 6)
print((2 + 3) * 6)
