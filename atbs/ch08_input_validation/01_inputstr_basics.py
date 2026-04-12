import pyinputplus as pyip

# inputStr() is the simplest PyInputPlus function.
# It works like input() but rejects blank input by default.
# If the user presses Enter without typing anything, it reprompts.

print("--- Basic inputStr() ---")
name = pyip.inputStr("Enter your name: ")
print(f"Hello, {name}!")

# You can still pass a blank string if you explicitly allow it.
# The 'blank' keyword overrides the default reject-blank behavior.
print("\n--- inputStr() with blank=True ---")
nickname = pyip.inputStr("Enter a nickname (or press Enter to skip): ", blank=True)

if nickname == "":
    print("No nickname given.")
else:
    print(f"Nickname: {nickname}")
