import shutil
from pathlib import Path

# --- Setup: create a sandbox directory so we never touch real files ---
sandbox = Path(__file__).parent / 'sandbox'
src_dir = sandbox / 'source'
src_dir.mkdir(parents=True, exist_ok=True)

# Create a couple of dummy files to work with
(src_dir / 'hello.txt').write_text('Hello from hello.txt\n')
(src_dir / 'notes.txt').write_text('Some notes here\n')

print('=== Setup complete ===')
print(f'Source dir: {src_dir}')
print(f'Files created: {[f.name for f in src_dir.iterdir()]}')
print()

# --- shutil.copy(src, dst) ---

# Case 1: dst is a directory — copies the file into that folder, same name
dest_dir = sandbox / 'dest_dir'
dest_dir.mkdir(exist_ok=True)

result = shutil.copy(src_dir / 'hello.txt', dest_dir)
print(f'Case 1 — copy into a directory:')
print(f'  Copied to: {result}')
print(f'  dest_dir contents: {[f.name for f in dest_dir.iterdir()]}')
print()

# Case 2: dst is a file path — copies and renames in one step
result = shutil.copy(src_dir / 'hello.txt', sandbox / 'hello_backup.txt')
print(f'Case 2 — copy with rename:')
print(f'  Copied to: {result}')
print()

# --- shutil.copytree(src, dst) ---
# dst must NOT already exist — copytree creates it fresh
tree_dest = sandbox / 'source_backup'

# Guard against re-running: remove old backup if it exists
if tree_dest.exists():
    shutil.rmtree(tree_dest)

shutil.copytree(src_dir, tree_dest)
print(f'Case 3 — copytree (entire folder):')
print(f'  Copied tree to: {tree_dest}')
print(f'  tree_dest contents: {[f.name for f in tree_dest.iterdir()]}')
print()

# --- Cleanup ---
shutil.rmtree(sandbox)
print('=== Sandbox cleaned up ===')
