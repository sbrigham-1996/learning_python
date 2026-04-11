# Chapter 7 — Pattern Matching with Regular Expressions
# Concept 7: findall() — finding every match, not just the first
#
# Key idea: findall() returns ALL non-overlapping matches as a list.
# The return type depends on whether your pattern has groups:
#   No groups       -> list of strings (the full matches)
#   One group       -> list of strings (the group's content only)
#   Multiple groups -> list of tuples (one tuple per match, one element per group)

import re

text = 'Cell: 415-555-9999, Work: 212-555-0000, Home: 503-555-1234'

# --- No groups: returns a list of full match strings ---
phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
all_matches = phone_regex.findall(text)
print('No groups:', all_matches)
# ['415-555-9999', '212-555-0000', '503-555-1234']

print()

# --- One group: returns a list of the GROUP's content, not the full match ---
# Only the area codes are captured in the group
area_regex = re.compile(r'(\d\d\d)-\d\d\d-\d\d\d\d')
area_codes = area_regex.findall(text)
print('One group (area codes only):', area_codes)
# ['415', '212', '503']
# Note: the full match was '415-555-9999' etc., but findall only returned the group

print()

# --- Multiple groups: returns a list of tuples ---
# Each tuple contains one element per group
parts_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
all_parts = parts_regex.findall(text)
print('Multiple groups (tuples):')
for match_tuple in all_parts:
    print(' ', match_tuple)
# ('415', '555', '9999')
# ('212', '555', '0000')
# ('503', '555', '1234')

print()

# --- Practical example: extracting all numbers from a mixed string ---
number_regex = re.compile(r'\d+')
data = 'Order 1042: 3 items at $14 each, plus $8 shipping. Order 2019: 1 item at $99.'
numbers = number_regex.findall(data)
print('All numbers found:', numbers)

print()

# --- Contrast: search() vs findall() ---
# search() returns a Match object (or None) — stops at the first match
# findall() returns a list — always a list, even if zero or one match found
one_phone = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

search_result = one_phone.search(text)
findall_result = one_phone.findall(text)

print('search() result type:', type(search_result))   # <class 're.Match'>
print('findall() result type:', type(findall_result)) # <class 'list'>
print('search() gives you .group():', search_result.group())
print('findall() gives you a list: ', findall_result)
