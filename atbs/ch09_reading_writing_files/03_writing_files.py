"""
Ch. 9 — Concept 3: Writing Files with open()

The mode argument to open() controls whether you're creating,
overwriting, or appending. Getting this wrong can silently destroy data.
"""

from pathlib import Path

output_dir = Path(__file__).parent

# ------------------------------------------------------------------
# 1. Writing a new file with 'w' mode
# ------------------------------------------------------------------

write_path = output_dir / 'output.txt'

with open(write_path, 'w') as f:
    f.write('Line one\n')
    f.write('Line two\n')
    f.write('Line three\n')

print("Written to:", write_path)

# Read it back to confirm what landed on disk
with open(write_path) as f:
    print(f.read())

# ------------------------------------------------------------------
# 2. 'w' mode overwrites — the danger
# ------------------------------------------------------------------

# Opening the same file again in 'w' mode erases everything already there.
with open(write_path, 'w') as f:
    f.write('This replaced everything.\n')

print("After overwrite:")
with open(write_path) as f:
    print(f.read())

# ------------------------------------------------------------------
# 3. 'a' mode — append without erasing
# ------------------------------------------------------------------

append_path = output_dir / 'log.txt'

# Write an initial entry
with open(append_path, 'w') as f:
    f.write('Entry 1: program started\n')

# Append two more entries — existing content is preserved
with open(append_path, 'a') as f:
    f.write('Entry 2: something happened\n')

with open(append_path, 'a') as f:
    f.write('Entry 3: program finished\n')

print("Append log contents:")
with open(append_path) as f:
    print(f.read())

# ------------------------------------------------------------------
# 4. .write() returns the character count
# ------------------------------------------------------------------

# This is easy to miss — .write() returns an int (characters written).
# You can ignore it, but it's there if you need to verify output size.
with open(output_dir / 'count_demo.txt', 'w') as f:
    chars_written = f.write('Hello, file!\n')

print(f"Characters written: {chars_written}")

# ------------------------------------------------------------------
# 5. Writing multiple lines cleanly with join()
# ------------------------------------------------------------------

# Instead of calling .write() in a loop, build your content first,
# then write it in one call. Cleaner and more efficient.
lines = ['apple', 'banana', 'cherry']

with open(output_dir / 'fruits.txt', 'w') as f:
    f.write('\n'.join(lines) + '\n')  # trailing \n keeps the file tidy

print("Fruits file contents:")
with open(output_dir / 'fruits.txt') as f:
    print(f.read())
