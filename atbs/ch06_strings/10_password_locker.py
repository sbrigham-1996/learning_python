# Ch. 6 Capstone — Multi-Password Locker
# Usage: python3 10_password_locker.py <account>
# Looks up the account in the passwords dict and copies the password to clipboard.
#
# NOTE: Storing passwords in plain text is for learning purposes only.
# Real password managers encrypt credentials — never ship something like this.

import sys
import pyperclip

passwords = {
    "gmail":    "sUp3rS3cur3Gm@il",
    "github":   "gh_t0k3nXyZ123",
    "twitter":  "Tw1tt3rP@ssw0rd",
    "linkedin": "L1nk3dInSecure!",
}

# --- Step 1: Check that an account argument was provided ---
# sys.argv is a list: [script_name, arg1, arg2, ...]
# If the user ran: python3 10_password_locker.py gmail
# then sys.argv = ['10_password_locker.py', 'gmail']
# If they ran with no argument, len(sys.argv) is 1 (only the script name).

if len(sys.argv) < 2:
    print("Usage: python3 10_password_locker.py <account>")
    print("Available accounts:", ", ".join(sorted(passwords.keys())))
    sys.exit()

# --- Step 2: Grab the account name from the command line ---
# Normalize to lowercase so "Gmail" and "GMAIL" both work.
account = sys.argv[1].lower()

# --- Step 3: Look up the account and copy the password ---
if account in passwords:
    pyperclip.copy(passwords[account])
    print(f"Password for '{account}' copied to clipboard.")
else:
    print(f"No account named '{account}' found.")
    print("Available accounts:", ", ".join(sorted(passwords.keys())))
