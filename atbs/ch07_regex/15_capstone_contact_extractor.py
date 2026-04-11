# Chapter 7 Capstone — Contact Sheet Extractor & Cleaner
#
# Given a messy block of text, this script:
#   1. Extracts all phone numbers (handles multiple formats)
#   2. Extracts all email addresses
#   3. Reformats all dates from MM-DD-YYYY to YYYY-MM-DD
#   4. Redacts phone numbers in the original text
#   5. Prints a clean summary report
#
# Concepts used: compile, groups, findall, ?, [], \d \w \s, ^$, IGNORECASE, sub, VERBOSE

import re

# --- The raw text we are working with ---
# Intentionally messy: mixed phone formats, inconsistent date styles, mixed casing
raw_text = """
Team Contact Sheet — Updated 04-11-2026

Spencer Brigham    spencer@example.com        415-555-4242
Maria Santos       maria.santos@workplace.org  (212) 555-0198
Dev Team           devteam@COMPANY.COM         503.555.8811
Bob Lee            bob_lee@sub.domain.net      212-555-3344
No Phone User      nophone@example.com
Bad email          notanemail@               555-867-5309

Project kickoff: 01-15-2026
Phase 1 deadline: 03-30-2026
Final delivery:   12-31-2026
"""

# -------------------------------------------------------------------------
# PATTERN 1: Phone numbers
# Handles three formats:
#   415-555-4242
#   (415) 555-4242
#   415.555.4242
# Area code is optional in all formats.
# Uses re.VERBOSE for readability.
# -------------------------------------------------------------------------
phone_regex = re.compile(r'''
    (\(?\d{3}\)?   # optional opening paren, 3 digits, optional closing paren
    [\s\-\.]       # separator: space, dash, or dot
    \d{3}          # exchange: 3 digits
    [\-\.]         # separator: dash or dot
    \d{4})         # subscriber: 4 digits
''', re.VERBOSE)

# -------------------------------------------------------------------------
# PATTERN 2: Email addresses
# \b             word boundary — don't grab partial words
# [\w\.\-]+      one or more word chars, dots, or hyphens (local part)
# @              literal @
# [\w\-]+        domain name
# (\.\w+)+       one or more .extension parts (.com, .co.uk, etc.)
# Uses re.IGNORECASE so COMPANY.COM matches.
# -------------------------------------------------------------------------
email_regex = re.compile(r'''
    \b
    ([\w\.\-]+     # local part: letters, digits, dots, hyphens
    @              # @ symbol
    [\w\-]+        # domain name
    (\.\w+)+)      # one or more extensions: .com, .org, .net, etc.
    \b
''', re.VERBOSE | re.IGNORECASE)

# -------------------------------------------------------------------------
# PATTERN 3: Dates in MM-DD-YYYY format
# Three groups so we can rearrange them in sub()
# -------------------------------------------------------------------------
date_regex = re.compile(r'''
    (\d{2})    # month
    -          # separator
    (\d{2})    # day
    -          # separator
    (\d{4})    # year
''', re.VERBOSE)


# -------------------------------------------------------------------------
# EXTRACT
# -------------------------------------------------------------------------

# findall() with multiple groups returns a list of tuples —
# email_regex has two groups (full email + the extension sub-group).
# We only want the full match (group 1), so we pull index [0] from each tuple.
phones = phone_regex.findall(raw_text)
email_tuples = email_regex.findall(raw_text)
emails = [t[0] for t in email_tuples]
dates = date_regex.findall(raw_text)

# -------------------------------------------------------------------------
# TRANSFORM: reformat dates and redact phones in the original text
# -------------------------------------------------------------------------
reformatted = date_regex.sub(r'\3-\1-\2', raw_text)       # MM-DD-YYYY -> YYYY-MM-DD
redacted, phone_count = phone_regex.subn('[PHONE]', reformatted)  # replace phones


# -------------------------------------------------------------------------
# REPORT
# -------------------------------------------------------------------------
print('=' * 50)
print('EXTRACTION REPORT')
print('=' * 50)

print(f'\nPhone numbers found ({len(phones)}):')
for phone in phones:
    print(f'  {phone}')

print(f'\nEmail addresses found ({len(emails)}):')
for email in emails:
    print(f'  {email}')

print(f'\nDates found ({len(dates)}):')
for month, day, year in dates:
    print(f'  {month}-{day}-{year}  ->  {year}-{month}-{day}')

print(f'\nPhone numbers redacted: {phone_count}')

print('\n' + '=' * 50)
print('CLEANED TEXT')
print('=' * 50)
print(redacted)
