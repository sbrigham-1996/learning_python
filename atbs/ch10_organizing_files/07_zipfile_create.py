import shutil
import zipfile
from pathlib import Path

# --- Setup: source folder we want to archive ---
sandbox = Path(__file__).parent / 'sandbox'
sandbox.mkdir(exist_ok=True)

src = sandbox / 'project'
(src / 'docs').mkdir(parents=True, exist_ok=True)
(src / 'main.py').write_text('print("hello")\n' * 200)
(src / 'README.md').write_text('# project\n' * 100)
(src / 'docs' / 'api.md').write_text('## API\n' * 50)

print('=== Setup complete ===')
print(f'Source files:')
for path in sorted(src.rglob('*')):
    if path.is_file():
        print(f'  {path.relative_to(src)} ({path.stat().st_size} bytes)')
print()

# --- Case 1: 'w' mode + ZIP_DEFLATED — create a fresh archive of the tree ---
# arcname=path.relative_to(src) → entries inside the ZIP are
# 'main.py', 'README.md', 'docs/api.md' — not absolute filesystem paths.
archive = sandbox / 'project.zip'

with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as zf:
    for path in src.rglob('*'):
        if path.is_file():
            zf.write(path, arcname=path.relative_to(src))

print('Case 1 — created project.zip with `w` mode + ZIP_DEFLATED:')
print(f'  archive size: {archive.stat().st_size} bytes')
print()

# --- Case 2: the arcname contrast (the most important detail) ---
# Same file added two ways. Compare the entry names with namelist().
demo = sandbox / 'arcname_demo.zip'
with zipfile.ZipFile(demo, 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.write(src / 'main.py')                                  # NO arcname
    zf.write(src / 'README.md', arcname='README.md')           # WITH arcname

print('Case 2 — arcname contrast:')
with zipfile.ZipFile(demo) as zf:
    for name in zf.namelist():
        print(f'  {name}')
print('  ↑ Without arcname, the absolute filesystem path is stored.')
print('  ↑ With arcname, the entry is clean and portable.')
print()

# --- Case 3: verify the archive by reading it back ---
print('Case 3 — verify project.zip by listing its entries:')
with zipfile.ZipFile(archive) as zf:
    for name in zf.namelist():
        info = zf.getinfo(name)
        print(f'  {name}  ({info.file_size} → {info.compress_size} bytes)')
print()

# --- Case 4: 'a' mode — append a new entry to the existing archive ---
# Useful when you are growing an archive over time. WARNING: appending
# a duplicate name does NOT replace the old entry — both are stored.
new_file = src / 'CHANGELOG.md'
new_file.write_text('# changelog\n')

with zipfile.ZipFile(archive, 'a', zipfile.ZIP_DEFLATED) as zf:
    zf.write(new_file, arcname='CHANGELOG.md')

print('Case 4 — appended CHANGELOG.md with `a` mode:')
with zipfile.ZipFile(archive) as zf:
    for name in zf.namelist():
        print(f'  {name}')
print()

# --- Case 5: 'x' mode — fail if the archive already exists ---
# The safe alternative to 'w' when you do NOT want to clobber a backup.
print('Case 5 — `x` mode against an existing archive (will fail):')
try:
    with zipfile.ZipFile(archive, 'x', zipfile.ZIP_DEFLATED) as zf:
        pass   # never reached
except FileExistsError as e:
    print(f'  Caught FileExistsError as expected: {e}')
print('  (`x` mode is the guard against overwriting a real backup.)')
print()

# --- Case 6: compression-type comparison on the same file ---
# Build two single-entry archives, one STORED, one DEFLATED.
sample = src / 'main.py'

stored_zip = sandbox / 'sample_stored.zip'
deflated_zip = sandbox / 'sample_deflated.zip'

with zipfile.ZipFile(stored_zip, 'w', zipfile.ZIP_STORED) as zf:
    zf.write(sample, arcname='main.py')

with zipfile.ZipFile(deflated_zip, 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.write(sample, arcname='main.py')

print('Case 6 — STORED vs DEFLATED on the same file:')
print(f'  source main.py:        {sample.stat().st_size} bytes')
print(f'  ZIP_STORED archive:    {stored_zip.stat().st_size} bytes (no compression)')
print(f'  ZIP_DEFLATED archive:  {deflated_zip.stat().st_size} bytes (compressed)')
print('  STORED is bundle-only — same size as source plus header overhead.')
print('  DEFLATED is the format you almost always want.')
print()

# --- Cleanup ---
shutil.rmtree(sandbox)
print('=== Sandbox cleaned up ===')
