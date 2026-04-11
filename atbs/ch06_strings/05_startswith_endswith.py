# Ch. 6 — startswith() and endswith()
# Clean, readable alternatives to slicing when checking the beginning or end of a string.

# --- Basic Usage ---
filename = "report_2026.csv"

print(filename.startswith("report"))  # True
print(filename.startswith("data"))    # False
print(filename.endswith(".csv"))      # True
print(filename.endswith(".txt"))      # False

# --- Case Sensitive ---
# Like all string comparisons, these are case-sensitive.
print(filename.startswith("Report"))  # False — capital R doesn't match lowercase r
print(filename.lower().endswith(".csv"))  # True — normalize first if needed

# --- Why Not Just Slice? ---
# Both approaches work, but endswith/startswith are more readable.
url = "https://example.com"
print(url[:8] == "https://")       # True — works, but harder to read at a glance
print(url.startswith("https://"))  # True — intent is immediately clear

# --- Passing a Tuple for Multiple Options ---
# Both methods accept a tuple of strings — returns True if ANY match.
# Note: must be a tuple, not a list.

image_file = "photo.png"
print(image_file.endswith((".jpg", ".png", ".gif")))  # True — .png matches
print(image_file.endswith((".pdf", ".csv", ".txt")))  # False — no match

# Cleaner than: image_file.endswith(".jpg") or image_file.endswith(".png") or ...

# --- Practical Example: Filtering a List of Files ---
files = [
    "notes.txt",
    "photo.jpg",
    "report.csv",
    "avatar.png",
    "data.csv",
    "readme.txt",
]

# Get only text files
text_files = [f for f in files if f.endswith(".txt")]
print("Text files:", text_files)

# Get only image files (multiple extensions)
image_files = [f for f in files if f.endswith((".jpg", ".png", ".gif"))]
print("Image files:", image_files)

# --- Practical Example: Skipping Comment Lines ---
# A common pattern when reading config files or data files —
# lines that start with '#' are comments and should be ignored.
config_lines = [
    "# This is a comment",
    "username = spencer",
    "# Another comment",
    "theme = dark",
]

active_lines = [line for line in config_lines if not line.startswith("#")]
print("Active config lines:", active_lines)
