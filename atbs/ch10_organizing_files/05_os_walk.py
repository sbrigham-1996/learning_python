import os
import shutil
from pathlib import Path

# --- Setup: build a small nested tree in the sandbox ---
sandbox = Path(__file__).parent / 'sandbox'
sandbox.mkdir(exist_ok=True)

# project/
# ├── readme.md
# ├── src/
# │   ├── main.py
# │   ├── notes.txt
# │   ├── __pycache__/
# │   │   └── main.cpython-311.pyc
# │   └── utils/
# │       ├── helpers.py
# │       └── helpers.txt
# └── docs/
#     └── api.txt

project = sandbox / 'project'
src = project / 'src'
utils = src / 'utils'
pycache = src / '__pycache__'
docs = project / 'docs'

for d in (project, src, utils, pycache, docs):
    d.mkdir(parents=True, exist_ok=True)

(project / 'readme.md').write_text('# project\n')
(src / 'main.py').write_text('print("hi")\n')
(src / 'notes.txt').write_text('src notes\n')
(pycache / 'main.cpython-311.pyc').write_text('binary-ish\n')
(utils / 'helpers.py').write_text('def help(): pass\n')
(utils / 'helpers.txt').write_text('helpers notes\n')
(docs / 'api.txt').write_text('api docs\n')

print('=== Setup complete ===')
print()

# --- Case 1: basic os.walk() — see the 3-tuple shape verbatim ---
print('Case 1 — basic walk (top-down, raw 3-tuple per directory):')
for folder_name, subfolders, filenames in os.walk(project):
    print(f'  folder:     {folder_name}')
    print(f'  subfolders: {subfolders}')
    print(f'  filenames:  {filenames}')
    print()

# --- Case 2: rebuild full paths — the gotcha 1 fix ---
# subfolders and filenames are BARE NAMES, not paths. To act on them,
# join with folder_name (or wrap folder_name in a Path).
print('Case 2 — rebuild full paths from (folder_name, filename):')
for folder_name, subfolders, filenames in os.walk(project):
    for name in filenames:
        full_path = Path(folder_name) / name
        print(f'  {full_path}')
print()

# --- Case 3: filter — find every .txt file anywhere in the tree ---
print('Case 3 — find every .txt file in the tree:')
txt_files = []
for folder_name, subfolders, filenames in os.walk(project):
    for name in filenames:
        if name.endswith('.txt'):
            txt_files.append(Path(folder_name) / name)

for path in txt_files:
    print(f'  {path}')
print(f'  ({len(txt_files)} .txt files found)')
print()

# --- Case 4: prune __pycache__ — gotcha 2 in action ---
# Mutate subfolders IN PLACE to stop os.walk() from descending into it.
# Reassigning (subfolders = [...]) would NOT work — must mutate.
print('Case 4 — walk while pruning __pycache__:')
for folder_name, subfolders, filenames in os.walk(project):
    if '__pycache__' in subfolders:
        subfolders.remove('__pycache__')   # ← in-place mutation
    print(f'  visiting: {folder_name}')
    for name in filenames:
        print(f'    file: {name}')
print()
print('  Notice: __pycache__ never appears as a "visiting" line.')
print('  Its file (main.cpython-311.pyc) is also not listed.')
print()

# --- Case 5: contrast with Path.rglob() — same result, flatter shape ---
# rglob() yields every matching Path in one stream. No per-directory
# grouping, no pruning hook — but for "find me every X under here"
# it is shorter than os.walk().
print('Case 5 — Path.rglob("*.txt") (the pathlib equivalent):')
for path in project.rglob('*.txt'):
    print(f'  {path}')
print()
print('  Same files as Case 3, but no manual joining or filtering loop.')
print('  Use os.walk() when you need tree structure or pruning.')
print('  Use rglob() when you just want a flat list of matches.')
print()

# --- Cleanup ---
shutil.rmtree(sandbox)
print('=== Sandbox cleaned up ===')
