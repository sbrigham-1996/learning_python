import pyinputplus as pyip

# inputEmail() and inputFilepath() validate structural formats.
# They use built-in rules so you don't need to write the regex yourself.

# --- inputEmail() ---
# Checks that input looks like a valid email address.
# Does NOT verify the address exists — format only.

print("--- inputEmail() ---")
email = pyip.inputEmail("Enter your email address: ")
print(f"Email recorded: {email}")

# --- inputFilepath() ---
# Checks that input looks like a valid file path for your OS.
# Format check only — accepts paths that don't exist on disk.

print("\n--- inputFilepath() (format only) ---")
path = pyip.inputFilepath("Enter any file path: ")
print(f"Path recorded: {path}")

# --- inputFilepath() with mustExist=True ---
# Adds a real filesystem check — rejects paths that don't exist.
# This is the version you'd use in a real script that opens files.

print("\n--- inputFilepath() with mustExist=True ---")
print("Try a path that doesn't exist, then a real one.")
print("Hint: try /Users or /tmp as valid paths on macOS.")
real_path = pyip.inputFilepath("Enter an existing path: ", mustExist=True)
print(f"Confirmed path: {real_path}")
