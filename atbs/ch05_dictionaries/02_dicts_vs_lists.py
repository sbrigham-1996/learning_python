# Ch. 5 — Dictionaries & Structuring Data
# Concept 2: Dictionaries vs. Lists

# --- LISTS: use when order and position matter ---

# A list of scores — the position (index) is what matters
scores = [95, 87, 72, 91]
print(scores[0])    # 95 — first score
print(scores[-1])   # 91 — last score

# But what does index 2 mean? You have to remember the convention.
# Lists are fragile when used to represent structured records.

# --- DICTS: use when labels matter more than order ---

# A dict of scores — the key (name) is what matters
score_map = {
    'Spencer': 95,
    'Alice': 87,
    'Bob': 72,
}
print(score_map['Spencer'])   # 95 — no need to remember position
print(score_map['Bob'])       # 72

# --- INTEGER KEYS ---
# Keys don't have to be strings. Integers are valid too.
# This is useful when your data is sparse (has gaps).

# A list requires every index to exist:
# timeline = []
# timeline[2025] = 'graduated'  # IndexError — list isn't that long

# A dict with integer keys handles gaps naturally:
timeline = {
    2020: 'started college',
    2024: 'graduated',
    2026: 'first promotion',
}
print(timeline[2024])   # graduated
print(timeline[2026])   # first promotion
# timeline[2025] would raise KeyError — that year wasn't added

# --- THE CORE RULE ---
# List  → ordered sequence of similar items, accessed by position
# Dict  → labeled data about one thing, accessed by key
