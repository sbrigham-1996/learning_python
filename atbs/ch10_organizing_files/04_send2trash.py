from pathlib import Path
import shutil
from send2trash import send2trash

# --- Setup: sandbox so we never touch real files ---
sandbox = Path(__file__).parent / 'sandbox'
sandbox.mkdir(exist_ok=True)

(sandbox / 'oops.txt').write_text('I deleted this by accident\n')
(sandbox / 'config.txt').write_text('important settings\n')

old_project = sandbox / 'old_project'
old_project.mkdir(exist_ok=True)
(old_project / 'main.py').write_text('print("legacy")\n')
(old_project / 'notes.md').write_text('# old notes\n')

print('=== Setup complete ===')
print(f'sandbox contents: {[p.name for p in sandbox.iterdir()]}')
print()

# --- Case 1: send a single file to the Trash ---
# Same call signature as os.unlink(), but recoverable from the OS Trash.
target = sandbox / 'oops.txt'
print(f'Case 1 — send a single file to Trash:')
print(f'  Before: {target.name} exists? {target.exists()}')
send2trash(target)
print(f'  After:  {target.name} exists? {target.exists()}')
print(f'  (Check ~/.Trash on macOS — oops.txt should be there.)')
print()

# --- Case 2: send a directory to the Trash ---
# No separate "rmtree" version — the same function handles files AND folders.
print(f'Case 2 — send a whole directory to Trash:')
print(f'  Before: old_project exists? {old_project.exists()}')
send2trash(old_project)
print(f'  After:  old_project exists? {old_project.exists()}')
print(f'  (Folder + everything inside it is in the Trash, recoverable.)')
print()

# --- Case 3: send2trash on a missing path raises OSError ---
# Same behavior as os.unlink() / shutil.rmtree() — the path must exist.
print(f'Case 3 — send2trash on a missing path (will fail):')
try:
    send2trash(sandbox / 'does_not_exist.txt')
except OSError as e:
    print(f'  Caught OSError as expected: {e}')
print()

# --- Case 4: the safety pattern — send2trash for "soft" cleanup ---
# Compare to Case 6 in script 03 (the dry-run pattern). With send2trash
# you can be less paranoid: even if the filter is wrong, every file is
# recoverable from the Trash. This is the right tool for "I'm not 100%
# sure my filter is correct" cleanup work.
print('Case 4 — soft cleanup (no dry-run needed):')
for path in sandbox.iterdir():
    if path.is_file() and path.suffix == '.txt':
        print(f'  Sending to Trash: {path.name}')
        send2trash(path)

print()
print(f'  sandbox contents now: {[p.name for p in sandbox.iterdir()]}')
print()

# --- Cleanup ---
# Use shutil.rmtree() here because we DO want the empty sandbox folder
# permanently gone — no point cluttering the Trash with our own scaffolding.
shutil.rmtree(sandbox)
print('=== Sandbox cleaned up (permanent, not via Trash) ===')
