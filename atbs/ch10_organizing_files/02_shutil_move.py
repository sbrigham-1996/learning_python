import shutil
from pathlib import Path

sandbox = Path(__file__).parent / 'sandbox'
sandbox.mkdir(exist_ok=True)

# Create dummy files
(sandbox / 'report.txt').write_text('Quarterly report\n')
(sandbox / 'draft.txt').write_text('Work in progress\n')
(sandbox / 'old_name.txt').write_text('I need a better name\n')

archive = sandbox / 'archive'
archive.mkdir(exist_ok=True)

print('=== Setup complete ===')
print(f'sandbox: {[f.name for f in sandbox.iterdir()]}')
print()

# --- Case 1: dst is an existing directory — moves into it, keeps filename ---
shutil.move(str(sandbox / 'report.txt'), str(archive))
print('Case 1 — move into a directory:')
print(f'  archive contents: {[f.name for f in archive.iterdir()]}')
print(f'  report.txt still in sandbox? {(sandbox / "report.txt").exists()}')
print()

# --- Case 2: dst is a new file path — move and rename in one step ---
shutil.move(str(sandbox / 'old_name.txt'), str(sandbox / 'new_name.txt'))
print('Case 2 — move with rename:')
print(f'  new_name.txt exists? {(sandbox / "new_name.txt").exists()}')
print(f'  old_name.txt still exists? {(sandbox / "old_name.txt").exists()}')
print()

# --- Case 3: rename-only (same directory, different name) ---
# This is the standard rename pattern in Python — shutil.move() is all you need
(sandbox / 'draft.txt').write_text('Still drafting\n')
shutil.move(str(sandbox / 'draft.txt'), str(sandbox / 'final.txt'))
print('Case 3 — rename in place:')
print(f'  final.txt exists? {(sandbox / "final.txt").exists()}')
print(f'  draft.txt still exists? {(sandbox / "draft.txt").exists()}')
print()

# --- Sharp edge demo: dst is an existing file --- overwrites silently ---
(sandbox / 'file_a.txt').write_text('I am file A\n')
(sandbox / 'file_b.txt').write_text('I am file B\n')

print('Case 4 — overwrite warning:')
print(f'  file_b.txt before move: {(sandbox / "file_b.txt").read_text().strip()}')
shutil.move(str(sandbox / 'file_a.txt'), str(sandbox / 'file_b.txt'))
print(f'  file_b.txt after move:  {(sandbox / "file_b.txt").read_text().strip()}')
print(f'  file_a.txt still exists? {(sandbox / "file_a.txt").exists()}')
print('  file_b original content is gone — no warning was raised')
print()

shutil.rmtree(sandbox)
print('=== Sandbox cleaned up ===')
