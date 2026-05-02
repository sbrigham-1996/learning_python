import os
import shutil
import zipfile
from pathlib import Path


def backup_to_zip(folder, output_dir=None):
    """Back up `folder` into a numbered ZIP next to it (or in `output_dir`).

    Filename pattern: <folder_name>_N.zip, where N is the next unused number.
    Returns the Path of the created archive.
    """
    folder = Path(folder).resolve()
    if not folder.is_dir():
        raise NotADirectoryError(f'Not a directory: {folder}')

    output_dir = Path(output_dir) if output_dir else folder.parent

    # 1. Pick the next available number — loop until the candidate is free.
    number = 1
    while True:
        archive_path = output_dir / f'{folder.name}_{number}.zip'
        if not archive_path.exists():
            break
        number += 1

    print(f'  Creating {archive_path.name}...')

    # 2. Walk the tree and add each file with a clean arcname.
    # arcname is relative to folder.parent so the archive contains
    # `<folder_name>/...` as its top-level entries — extracting gives
    # back the folder itself, not loose files.
    with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for folder_name, subfolders, filenames in os.walk(folder):
            for name in filenames:
                full_path = Path(folder_name) / name
                arcname = full_path.relative_to(folder.parent)
                print(f'    adding {arcname}')
                zf.write(full_path, arcname=arcname)

    print(f'  Done — {archive_path.stat().st_size} bytes')
    return archive_path


# --- Setup: build a sample project to back up ---
sandbox = Path(__file__).parent / 'sandbox'
sandbox.mkdir(exist_ok=True)

project = sandbox / 'my_project'
(project / 'src' / 'utils').mkdir(parents=True, exist_ok=True)
(project / 'docs').mkdir(parents=True, exist_ok=True)

(project / 'README.md').write_text('# my_project\n' * 20)
(project / 'src' / 'main.py').write_text('print("hi")\n' * 100)
(project / 'src' / 'utils' / 'helpers.py').write_text('def help(): pass\n' * 50)
(project / 'docs' / 'api.md').write_text('## API\n' * 30)

print('=== Setup complete ===')
print(f'Backing up: {project}')
print(f'Source files:')
for path in sorted(project.rglob('*')):
    if path.is_file():
        print(f'  {path.relative_to(project)}')
print()

# --- Run the backup three times — show the numbering increments ---
print('--- Run 1 ---')
backup_to_zip(project)
print()

print('--- Run 2 ---')
backup_to_zip(project)
print()

print('--- Run 3 ---')
third_archive = backup_to_zip(project)
print()

# Show the resulting backup files in the sandbox
print('Backups produced:')
for archive in sorted(sandbox.glob('my_project_*.zip')):
    print(f'  {archive.name}  ({archive.stat().st_size} bytes)')
print()

# --- Verify the third archive — open read-only and list its contents ---
print('Verifying my_project_3.zip:')
with zipfile.ZipFile(third_archive) as zf:
    for name in zf.namelist():
        print(f'  {name}')
print()
print('  Note: every entry is prefixed with "my_project/" — extracting')
print('  this archive gives back the folder itself, not loose files.')
print()

# --- Cleanup ---
shutil.rmtree(sandbox)
print('=== Sandbox cleaned up ===')
