"""
Ch. 9 — Concept 4: Saving Variables with shelve

shelve gives you a persistent dictionary backed by a binary database on disk.
You interact with it exactly like a dict, but the data survives between runs.
"""

import shelve
from pathlib import Path

# shelve.open() takes a path (without extension — it manages its own file names).
# Using __file__.parent keeps the shelf file next to this script.
shelf_path = str(Path(__file__).parent / 'mydata')

# ------------------------------------------------------------------
# 1. Saving data to a shelf
# ------------------------------------------------------------------

# The 'with' statement works just like with open() — shelf closes automatically.
with shelve.open(shelf_path) as shelf:
    shelf['cats'] = ['Zophie', 'Pooka', 'Fat-tail']
    shelf['user'] = {'name': 'Spencer', 'chapter': 9}
    shelf['score'] = 42

    print("Keys in shelf:", list(shelf.keys()))
    print("Values in shelf:", list(shelf.values()))

print("Shelf closed. Data is now on disk.")

# ------------------------------------------------------------------
# 2. Loading data back in a separate open() call
# ------------------------------------------------------------------

# This simulates a second program run — the shelf file already exists,
# and we're reading back what was saved in step 1.
with shelve.open(shelf_path) as shelf:
    print("\nLoaded from disk:")
    print("  cats  :", shelf['cats'])
    print("  user  :", shelf['user'])
    print("  score :", shelf['score'])

# ------------------------------------------------------------------
# 3. Updating a value
# ------------------------------------------------------------------

with shelve.open(shelf_path) as shelf:
    shelf['score'] = shelf['score'] + 10  # read, modify, write back

with shelve.open(shelf_path) as shelf:
    print("\nUpdated score:", shelf['score'])

# ------------------------------------------------------------------
# 4. Checking membership and deleting a key
# ------------------------------------------------------------------

with shelve.open(shelf_path) as shelf:
    print("\n'cats' in shelf:", 'cats' in shelf)
    print("'inventory' in shelf:", 'inventory' in shelf)

    del shelf['score']
    print("Deleted 'score'.")

with shelve.open(shelf_path) as shelf:
    print("Keys after delete:", list(shelf.keys()))

# ------------------------------------------------------------------
# 5. The shelf files on disk (binary — not human readable)
# ------------------------------------------------------------------

print("\nFiles created by shelve:")
for f in sorted(Path(__file__).parent.glob('mydata*')):
    print(f" {f.name} ({f.stat().st_size} bytes)")
