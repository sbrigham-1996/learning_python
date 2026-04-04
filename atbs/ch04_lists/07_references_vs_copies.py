# Ch. 4 — Lists
# Concept 7: References vs. Copies

import copy

# --- Integers are copied on assignment ---
a = 10
b = a
b = 99
print(a)        # 10 — unchanged, b got its own independent copy

# --- Lists are NOT copied on assignment — both variables point to the same list ---
list_a = [1, 2, 3]
list_b = list_a         # list_b is NOT a new list — it's a second reference to the same list
list_b[0] = 99
print(list_a)   # [99, 2, 3] — list_a was affected because list_a and list_b are the same list
print(list_b)   # [99, 2, 3]

# You can confirm they point to the same object with the `is` operator
print(list_a is list_b)     # True — same object in memory

# --- Making a shallow copy ---
# A shallow copy creates a NEW list with the same items.
# Changes to the copy don't affect the original — for flat lists.

# Method 1: slice with no start or end
list_c = [1, 2, 3]
list_d = list_c[:]
list_d[0] = 99
print(list_c)   # [1, 2, 3] — unchanged
print(list_d)   # [99, 2, 3]
print(list_c is list_d)     # False — different objects

# Method 2: copy.copy()
list_e = [1, 2, 3]
list_f = copy.copy(list_e)
list_f[0] = 99
print(list_e)   # [1, 2, 3] — unchanged
print(list_f)   # [99, 2, 3]

# --- The shallow copy limitation: nested lists ---
# A shallow copy copies the outer list, but inner lists are still shared references.
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
shallow[0][0] = 99          # modifying an inner list
print(original)     # [[99, 2], [3, 4]] — original was still affected!
print(shallow)      # [[99, 2], [3, 4]]

# --- deepcopy() solves this ---
# copy.deepcopy() copies the list AND everything inside it, all the way down.
original2 = [[1, 2], [3, 4]]
deep = copy.deepcopy(original2)
deep[0][0] = 99
print(original2)    # [[1, 2], [3, 4]] — completely untouched
print(deep)         # [[99, 2], [3, 4]]
