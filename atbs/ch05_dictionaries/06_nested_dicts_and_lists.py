# Ch. 5 — Dictionaries & Structuring Data
# Concept 6: Nested dictionaries and lists

import pprint

# A nested structure: dict of dicts, with lists inside
# Models a geotechnical boring log
borings = {
    'B-1': {
        'depth_ft': 30,
        'soil_layers': ['topsoil', 'sandy clay', 'dense sand'],
        'groundwater_ft': 12,
    },
    'B-2': {
        'depth_ft': 45,
        'soil_layers': ['topsoil', 'silty sand', 'weathered rock', 'rock'],
        'groundwater_ft': 18,
    },
    'B-3': {
        'depth_ft': 20,
        'soil_layers': ['fill', 'sandy clay'],
        'groundwater_ft': None,   # not encountered
    },
}

# --- Drilling down with chained brackets ---
# Each [] steps one level deeper into the structure
print(borings['B-1']['depth_ft'])            # 30
print(borings['B-2']['soil_layers'][1])      # silty sand (index 1 of the list)
print(borings['B-3']['groundwater_ft'])      # None

# --- Looping over a nested structure ---
# Outer loop: each boring
# Inner access: pull specific fields from each boring's dict
print('\nBoring Summary:')
for boring_id, data in borings.items():
    layer_count = len(data['soil_layers'])
    gw = data['groundwater_ft']
    gw_display = f"{gw} ft" if gw is not None else 'not encountered'
    print(f"  {boring_id}: {data['depth_ft']} ft deep, "
          f"{layer_count} layers, groundwater {gw_display}")

# --- Modifying nested data ---
# Adding a new key inside a nested dict works the same way
borings['B-1']['refusal'] = True
print('\nB-1 after update:')
pprint.pprint(borings['B-1'])

# Appending to a list inside a nested dict
borings['B-3']['soil_layers'].append('dense gravel')
print('\nB-3 soil layers after append:', borings['B-3']['soil_layers'])
