import pyinputplus as pyip
from datetime import datetime

# inputDatetime() validates date/time strings and returns a real datetime object.
# No manual strptime() parsing or regex needed — PyInputPlus handles it.

# --- Default behavior ---
# Accepts several common formats automatically.
# Returns a datetime object you can work with directly.

print("--- inputDatetime() default formats ---")
print("Accepted formats include: 11/12/2026, 11/12/2026 13:30:00")
dt = pyip.inputDatetime("Enter a date: ")
print(f"You entered: {dt}")
print(f"Type returned: {type(dt).__name__}")
print(f"Year: {dt.year}  Month: {dt.month}  Day: {dt.day}")

# --- Custom formats ---
# Pass a formats list to restrict exactly which formats are accepted.
# Uses the same strptime directives: %Y=year, %m=month, %d=day

print("\n--- inputDatetime() with custom format ---")
print("Only accepts: YYYY-MM-DD (e.g. 2026-04-12)")
birthday = pyip.inputDatetime("Enter your birthday (YYYY-MM-DD): ",
                              formats=["%Y-%m-%d"])
print(f"Birthday: {birthday.strftime('%B %d, %Y')}")

# --- datetime math ---
# Because the return value is a real datetime object, you can do date math.

print("\n--- datetime math ---")
print("Enter today's date (YYYY-MM-DD):")
today = pyip.inputDatetime("Today: ", formats=["%Y-%m-%d"])
print("Enter a future date (YYYY-MM-DD):")
future = pyip.inputDatetime("Future date: ", formats=["%Y-%m-%d"])
delta = future - today
print(f"Days between: {delta.days}")
