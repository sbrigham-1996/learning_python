# Ch. 5 — Dictionaries & Structuring Data
# Concept 7: Capstone — Geotechnical Project Tracker

import pprint

# --- DATA STRUCTURE ---
# Nested dict: each project has metadata, a team list, and a borings dict.
# This is the kind of structure you'd build before moving data to a database.

projects = {
    'HWY-54': {
        'client': 'NCDOT',
        'complete': False,
        'team': ['Spencer', 'Alice'],
        'borings': {
            'B-1': {'depth_ft': 30, 'soil': 'sandy clay'},
            'B-2': {'depth_ft': 45, 'soil': 'silty sand'},
        },
    },
    'SITE-22': {
        'client': 'Town of Carrboro',
        'complete': True,
        'team': ['Bob'],
        'borings': {
            'B-1': {'depth_ft': 20, 'soil': 'fill'},
        },
    },
}

# --- SUMMARY REPORT ---
# .items() to loop, nested access to pull fields, get() for safe lookups
print('=== Project Summary ===')
for project_id, data in projects.items():
    boring_count = len(data['borings'])
    status = 'Complete' if data['complete'] else 'In Progress'
    # get() with a default — 'client' should always exist, but this is safe practice
    client = data.get('client', 'Unknown client')
    print(f"{project_id} | {client} | {status} | {boring_count} boring(s)")

# --- ADDING A NEW PROJECT ---
# Assigning a new key to the top-level dict creates the project
projects['BRIDGE-7'] = {
    'client': 'Durham County',
    'complete': False,
    'team': [],
    'borings': {},
}
print('\nNew project added: BRIDGE-7')

# --- ADDING A TEAM MEMBER ---
# setdefault() ensures the 'team' list exists before appending
projects['BRIDGE-7'].setdefault('team', [])
projects['BRIDGE-7']['team'].append('Spencer')
print('Team for BRIDGE-7:', projects['BRIDGE-7']['team'])

# --- ADDING A BORING TO AN EXISTING PROJECT ---
projects['BRIDGE-7']['borings']['B-1'] = {'depth_ft': 60, 'soil': 'weathered rock'}
print('Borings for BRIDGE-7:', projects['BRIDGE-7']['borings'])

# --- QUERYING ACROSS PROJECTS ---
# Find all projects Spencer is assigned to
print('\nProjects assigned to Spencer:')
for project_id, data in projects.items():
    if 'Spencer' in data['team']:
        print(f"  {project_id}")

# --- COUNTING TOTAL BORINGS ACROSS ALL PROJECTS ---
total_borings = 0
for data in projects.values():
    total_borings += len(data['borings'])
print(f'\nTotal borings across all projects: {total_borings}')

# --- FULL DATA DUMP ---
print('\n=== Full Project Data ===')
pprint.pprint(projects)
