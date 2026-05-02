import shutil
import zipfile
from pathlib import Path

# --- Setup: build a sample ZIP so this script is self-contained ---
# (Sneak peek at concept 07 — writing ZIPs is covered next.)
sandbox = Path(__file__).parent / 'sandbox'
sandbox.mkdir(exist_ok=True)

# Create some source files with repetitive content so compression is visible.
src = sandbox / 'src'
(src / 'docs').mkdir(parents=True, exist_ok=True)
(src / 'hello.txt').write_text('hello world\n' * 200)
(src / 'notes.txt').write_text('these are notes\n' * 100)
(src / 'docs' / 'readme.md').write_text('# readme\n' * 50)

zip_path = sandbox / 'example.zip'

# Build the ZIP. ZIP_DEFLATED = the standard compressed format
# (default ZIP_STORED would just bundle without compressing).
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
    for path in src.rglob('*'):
        if path.is_file():
            # arcname = the path RELATIVE to src, so the archive doesn't
            # contain the absolute filesystem path. Without arcname, the
            # ZIP would store '/Users/spencer/.../src/hello.txt' literally.
            zf.write(path, arcname=path.relative_to(src))

print('=== Setup complete ===')
print(f'Created: {zip_path}')
print(f'On-disk size: {zip_path.stat().st_size} bytes')
print()

# --- Case 1: open with `with` (read mode is the default) ---
# Same context-manager rule as `with open(...)` from Ch. 9.
print('Case 1 — open the archive (read mode by default):')
with zipfile.ZipFile(zip_path) as zf:
    print(f'  Archive opened: {zip_path.name}')
print()

# --- Case 2: namelist() — every entry inside the ZIP ---
print('Case 2 — namelist():')
with zipfile.ZipFile(zip_path) as zf:
    for name in zf.namelist():
        print(f'  {name}')
print()

# --- Case 3: getinfo() — per-entry metadata, including compression ratio ---
print('Case 3 — getinfo() metadata for each file:')
with zipfile.ZipFile(zip_path) as zf:
    for name in zf.namelist():
        info = zf.getinfo(name)
        ratio = info.compress_size / info.file_size if info.file_size else 0
        print(f'  {name}')
        print(f'    original:   {info.file_size} bytes')
        print(f'    compressed: {info.compress_size} bytes')
        print(f'    ratio:      {ratio:.1%} of original')
print()

# --- Case 4: read() — get a file's contents WITHOUT extracting to disk ---
# Returns bytes. Decode if you know it's text.
print('Case 4 — read() one file in-memory (no extraction):')
with zipfile.ZipFile(zip_path) as zf:
    raw = zf.read('hello.txt')
    print(f'  type returned: {type(raw).__name__}')
    print(f'  first 40 bytes (decoded): {raw[:40].decode()!r}')
print()

# --- Case 5: extract() — pull ONE file to an explicit destination ---
# Always pass an explicit path. The default is the current working
# directory, which is rarely what you want (gotcha 1).
single_dest = sandbox / 'extracted_one'
single_dest.mkdir(exist_ok=True)

print('Case 5 — extract() a single file:')
with zipfile.ZipFile(zip_path) as zf:
    extracted_path = zf.extract('hello.txt', path=single_dest)
print(f'  extracted to: {extracted_path}')
print(f'  destination contents: {[p.name for p in single_dest.iterdir()]}')
print()

# --- Case 6: extractall() — pull EVERYTHING to an explicit destination ---
all_dest = sandbox / 'extracted_all'
all_dest.mkdir(exist_ok=True)

print('Case 6 — extractall() to an explicit destination:')
with zipfile.ZipFile(zip_path) as zf:
    zf.extractall(path=all_dest)

# Walk the result so you can see the folder structure was preserved
for path in sorted(all_dest.rglob('*')):
    indent = '  ' * len(path.relative_to(all_dest).parts)
    label = path.name + ('/' if path.is_dir() else '')
    print(f'  {indent}{label}')
print()

# --- Cleanup ---
shutil.rmtree(sandbox)
print('=== Sandbox cleaned up ===')
