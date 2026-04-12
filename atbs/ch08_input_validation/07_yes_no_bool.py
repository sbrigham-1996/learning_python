import pyinputplus as pyip

# inputYesNo() and inputBool() handle yes/no prompts without manual spelling checks.
# Both accept: yes, no, y, n — in any casing.

# --- inputYesNo() ---
# Returns the string "yes" or "no", normalized regardless of what was typed.
# "Y", "YES", "y" all return "yes".

print("--- inputYesNo() ---")
response = pyip.inputYesNo("Do you want to continue? (yes/no): ")
print(f"You answered: {response}")
print(f"Type returned: {type(response).__name__}")

# --- inputBool() ---
# Returns an actual bool: True for yes, False for no.
# More useful than inputYesNo() when you need control flow.

print("\n--- inputBool() ---")
confirmed = pyip.inputBool("Are you sure? (yes/no): ")
print(f"You answered: {confirmed}")
print(f"Type returned: {type(confirmed).__name__}")

if confirmed:
    print("Proceeding...")
else:
    print("Cancelled.")
