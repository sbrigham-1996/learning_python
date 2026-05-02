import os
import shutil
from pathlib import Path

# --- Setup: sandbox so we never touch real files ---
sandbox = Path(__file__).parent / 'sandbox'
sandbox.mkdir(exist_ok=True)

# A few loose files
(sandbox / 'temp1.txt').write_text('throwaway 1\n')
(sandbox / 'temp2.txt').write_text('throwaway 2\n')
(sandbox / 'keeper.txt').write_text('I survive the script\n')

# An empty directory (for rmdir success)
(sandbox / 'empty_dir').mkdir(exist_ok=True)

# A non-empty directory (for rmdir failure + rmtree success)
populated = sandbox / 'populated_dir'
populated.mkdir(exist_ok=True)
(populated / 'inside_a.txt').write_text('inside A\n')
(populated / 'inside_b.txt').write_text('inside B\n')
(populated / 'nested').mkdir(exist_ok=True)
(populated / 'nested' / 'deep.txt').write_text('deeply nested\n')

print('=== Setup complete ===')
print(f'sandbox contents: {[p.name for p in sandbox.iterdir()]}')
print(f'populated_dir contents: {[p.name for p in populated.iterdir()]}')
print()

# --- os.unlink(path) — delete a single file ---
# Note: os.unlink() takes a string, but accepts a Path object too.
# Trying to unlink a directory raises IsADirectoryError (PermissionError on Windows).
os.unlink(sandbox / 'temp1.txt')
print('Case 1 — os.unlink() on a single file:')
print(f'  temp1.txt still exists? {(sandbox / "temp1.txt").exists()}')
print()

# --- os.rmdir(path) — delete a SINGLE EMPTY directory ---
os.rmdir(sandbox / 'empty_dir')
print('Case 2 — os.rmdir() on an empty directory:')
print(f'  empty_dir still exists? {(sandbox / "empty_dir").exists()}')
print()

# --- os.rmdir() FAILS on a non-empty directory — that is the safety feature ---
print('Case 3 — os.rmdir() on a non-empty directory (will fail):')
try:
    os.rmdir(populated)
except OSError as e:
    # OSError is the parent class — the actual exception on macOS is
    # OSError: [Errno 66] Directory not empty. Catching OSError covers
    # the platform variations (different errno on Windows/Linux).
    print(f'  Caught OSError as expected: {e}')
print(f'  populated_dir still exists? {populated.exists()}')
print()

# --- shutil.rmtree(path) — recursively delete a directory and everything in it ---
# This is the dangerous one. No prompt, no Trash, no recovery.
shutil.rmtree(populated)
print('Case 4 — shutil.rmtree() on a populated directory:')
print(f'  populated_dir still exists? {populated.exists()}')
print()

# --- Path.unlink() — modern pathlib equivalent of os.unlink() ---
# Same operation, just called as a method on the Path object.
(sandbox / 'temp2.txt').unlink()
print('Case 5 — Path.unlink() (pathlib equivalent):')
print(f'  temp2.txt still exists? {(sandbox / "temp2.txt").exists()}')
print()

# --- The dry-run safety pattern ---
# When writing a real deletion script, ALWAYS run it in "print mode" first
# to verify the list of targets before letting it actually delete anything.
# Below: pretend we want to delete every .txt file in the sandbox.

print('Case 6 — dry-run pattern (prints what WOULD be deleted):')
for path in sandbox.iterdir():
    if path.is_file() and path.suffix == '.txt':
        print(f'  WOULD DELETE: {path}')
        # path.unlink()   # ← commented out until the dry-run output looks right

print()
print(f'  keeper.txt still exists? {(sandbox / "keeper.txt").exists()}')
print('  (Nothing was actually deleted — the unlink() call is commented out.)')
print()

# --- Cleanup ---
shutil.rmtree(sandbox)
print('=== Sandbox cleaned up ===')
