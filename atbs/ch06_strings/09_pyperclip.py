# Ch. 6 — pyperclip: Reading and Writing the Clipboard
# pyperclip is a third-party module — install once with: pip3 install pyperclip
# It has two functions: copy() puts text on the clipboard, paste() reads from it.

import pyperclip

# --- copy(): Write to the Clipboard ---
pyperclip.copy("Hello from Python!")
print("Text copied to clipboard.")
print("Go paste it somewhere to verify — then come back and press Enter.")
input()  # pause so you can test the paste

# --- paste(): Read from the Clipboard ---
# Whatever is on your clipboard right now gets returned as a string.
clipboard_content = pyperclip.paste()
print(f"Clipboard contains: '{clipboard_content}'")

# --- Practical Example: Copy a Formatted Result ---
# Instead of printing output and manually copying it, put it straight on the clipboard.
words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
result = " ".join(words).title()

pyperclip.copy(result)
print(f"\nFormatted string: '{result}'")
print("(Already copied to clipboard — ready to paste.)")

# --- Practical Example: Process Clipboard Text ---
# Read from clipboard, transform it, write it back.
# Useful for quick text transformations without opening an editor.
print("\nCopy some text to your clipboard, then press Enter.")
input()

raw = pyperclip.paste()
cleaned = " ".join(raw.split())   # normalize whitespace
cleaned = cleaned.strip()

pyperclip.copy(cleaned)
print(f"Original:  '{raw[:60]}{'...' if len(raw) > 60 else ''}'")
print(f"Cleaned:   '{cleaned[:60]}{'...' if len(cleaned) > 60 else ''}'")
print("Cleaned version copied to clipboard.")
