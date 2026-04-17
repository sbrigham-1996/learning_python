"""
Ch. 9 — Concept 6: os.path (Legacy Path Manipulation)

os.path predates pathlib and is common in older codebases.
This script shows each os.path function alongside its pathlib equivalent
so you can read legacy code and translate it to modern style.
"""

import os
import os.path
from pathlib import Path

# We'll use this script's own path as our example throughout.
example = Path(__file__)

print("Working with path:", example)
print("=" * 55)

# ------------------------------------------------------------------
# 1. Joining paths
# ------------------------------------------------------------------

# Legacy: os.path.join() — strings only, uses OS-correct separator
joined_legacy = os.path.join('/Users/spencerbrigham', 'Desktop', 'learning_python')
print("\nos.path.join()  :", joined_legacy)

# Modern: Path / operator
joined_modern = Path('/Users/spencerbrigham') / 'Desktop' / 'learning_python'
print("Path() / /      :", joined_modern)

# ------------------------------------------------------------------
# 2. Absolute path
# ------------------------------------------------------------------

# Legacy: os.path.abspath() resolves relative paths to absolute
print("\nos.path.abspath('.')   :", os.path.abspath('.'))

# Modern: Path.resolve() does the same
print("Path('.').resolve()   :", Path('.').resolve())

# ------------------------------------------------------------------
# 3. Dissecting a path
# ------------------------------------------------------------------

p = str(example)  # os.path functions expect strings

print("\n--- Dissecting a path ---")
print("os.path.basename()  :", os.path.basename(p))   # filename + ext
print("Path.name           :", example.name)

print("os.path.dirname()   :", os.path.dirname(p))    # everything except filename
print("Path.parent         :", example.parent)

# os.path.split() returns (dirname, basename) as a tuple in one call
print("os.path.split()     :", os.path.split(p))
print("Path equivalent     :", (example.parent, example.name))

# os.path.splitext() returns (root, extension) — note: extension includes the dot
print("os.path.splitext()  :", os.path.splitext(p))
print("Path equivalent     :", (example.stem, example.suffix))

# ------------------------------------------------------------------
# 4. Existence and type checks
# ------------------------------------------------------------------

print("\n--- Existence and type checks ---")
print("os.path.exists()    :", os.path.exists(p))
print("Path.exists()       :", example.exists())

print("os.path.isfile()    :", os.path.isfile(p))
print("Path.is_file()      :", example.is_file())

print("os.path.isdir()     :", os.path.isdir(p))
print("Path.is_dir()       :", example.is_dir())

# ------------------------------------------------------------------
# 5. File size
# ------------------------------------------------------------------

print("\n--- File size ---")
print("os.path.getsize()   :", os.path.getsize(p), "bytes")
print("Path.stat().st_size :", example.stat().st_size, "bytes")

# ------------------------------------------------------------------
# 6. Listing directory contents
# ------------------------------------------------------------------

chapter_dir = str(example.parent)

print("\n--- Directory listing ---")
print("os.listdir() (strings):")
for name in sorted(os.listdir(chapter_dir)):
    print(f"  {name}")

print("\nPath.iterdir() (Path objects):")
for item in sorted(example.parent.iterdir()):
    kind = 'dir' if item.is_dir() else 'file'
    print(f"  {item.name:35s}  [{kind}]")
