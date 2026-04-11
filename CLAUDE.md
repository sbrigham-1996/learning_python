# CLAUDE.md — learning_python

## About This Repo

This is Spencer's active Python learning repository. It tracks a full,
chapter-by-chapter progression through *Automate the Boring Stuff with Python*
(ATBS) by Al Sweigart. The goal is genuine proficiency — not just making code
run, but understanding *why* it works.

Each chapter gets its own folder under `atbs/`. Exercises and practice scripts
live there as they are completed.

---

## How I Work With Claude Code

- **Explain reasoning at every step.** Don't just give me the answer — walk me
  through the logic so I actually learn it.
- **Prefer step-by-step over all-at-once.** Break things into digestible pieces.
- **Call out Python best practices** when relevant (naming conventions, PEP 8
  style, Pythonic patterns).
- **Ask before refactoring.** If my code works but could be cleaner, flag it
  rather than silently rewrite it.
- **Match my level.** I have previously worked through Ch. 1–6 of ATBS, so the
  foundational concepts (variables, data types, loops, functions, lists, dicts,
  strings, basic file I/O) are familiar. I am restarting from Ch. 1 to build
  a clean, well-documented record of the full book.
- **Don't skip the fundamentals.** Even familiar chapters should be done
  thoroughly — the reps matter.

---

## Environment

- **OS:** macOS (zsh)
- **Python:** Python 3 via terminal
- **Tool:** Claude Code
- **GitHub:** sbrigham-1996/learning_python

---

## Folder Structure
```
learning_python/
├── CLAUDE.md               ← This file. Update as the repo grows.
├── README.md               ← Public-facing summary of the repo
└── atbs/                   ← All ATBS chapter work lives here
    ├── ch01_python_basics/
    ├── ch02_flow_control/
    ├── ch03_functions/
    └── ...
```

**File naming convention:**
- One folder per chapter: `ch##_topic_name/`
- Scripts inside each folder: `##_exercise_or_concept_name.py`
  - Example: `atbs/ch03_functions/01_local_scope.py`
- Keep names lowercase, words separated by underscores

---

## Progress Log

| Chapter | Topic | Status |
|---------|-------|--------|
| Ch. 1 | Python Basics | ✅ Complete |
| Ch. 2 | Flow Control | ✅ Complete |
| Ch. 3 | Functions | ✅ Complete |
| Ch. 4 | Lists | ✅ Complete |
| Ch. 5 | Dictionaries & Structuring Data | ✅ Complete |
| Ch. 6 | Manipulating Strings | ✅ Complete |
| Ch. 7 | Pattern Matching with Regex | ✅ Complete |
| Ch. 8 | Input Validation | ⬜ Not started |
| Ch. 9 | Reading & Writing Files | ⬜ Not started |
| Ch. 10 | Organizing Files | ⬜ Not started |
| Ch. 11 | Debugging | ⬜ Not started |
| Ch. 12 | Web Scraping | ⬜ Not started |
| Ch. 13 | Working with Excel Spreadsheets | ⬜ Not started |
| Ch. 14 | Working with Google Sheets | ⬜ Not started |
| Ch. 15 | Working with PDF & Word Documents | ⬜ Not started |
| Ch. 16 | Working with CSV Files & JSON Data | ⬜ Not started |
| Ch. 17 | Keeping Time, Scheduling Tasks & Launching Programs | ⬜ Not started |
| Ch. 18 | Sending Email & Text Messages | ⬜ Not started |
| Ch. 19 | Manipulating Images | ⬜ Not started |
| Ch. 20 | Controlling the Keyboard & Mouse | ⬜ Not started |

---

## Notes & Lessons Learned

### Ch. 1 — Python Basics

- **`/` always returns a float, even when it divides evenly.** `10 / 2` gives `5.0`, not `5`. Use `//` (integer division) when you need a whole number result.
- **`"42"` and `42` are completely different things.** Quotes make any value a string. You cannot use `+` to mix a string and an int — Python raises a `TypeError` rather than guessing your intent.
- **Scripts don't auto-display expressions — you must `print()`.** In the interactive REPL, typing `2 + 2` shows `4`. In a `.py` file, that expression runs silently. Always wrap output in `print()`.
- **`=` is assignment, not equality.** It puts a value into a variable. Comparing two values requires `==`. Mixing them up inside conditions is one of the most common early bugs.
- **Python silently overwrites variables.** Assigning a new value to an existing variable name replaces the old one with no warning. If you meant to make a new variable, choose a new name.
- **`input()` always returns a string.** Even if the user types `25`, you get the string `"25"`. Wrap it in `int()` (or `float()`) immediately if you need to do math with it.
- **Concatenating a number into a string requires `str()`.** You can't do `"You are " + age + " years old"` if `age` is an int — convert it first: `str(age)`.
- **String replication (`*`) requires an int, not a float.** `"Ha" * 3` works; `"Ha" * 3.0` raises a `TypeError`.
- **Spaces in string concatenation are your responsibility.** `"Hello" + "World"` gives `"HelloWorld"`. The space has to be an explicit `" "` in the join.
- **Use `snake_case` for variable names, not `camelCase`.** `user_name` is Pythonic; `userName` is not. PEP 8 is the style guide Python code follows.

### Ch. 2 — Flow Control

- **`True` and `False` are capitalized — always.** Python is case-sensitive. `true` or `TRUE` cause a `NameError` because Python reads them as undefined variable names, not Boolean values.
- **`==` compares; `=` assigns.** Writing `if x = 10:` is a syntax error in Python. The comparison operator inside conditions is always `==`.
- **String comparison is case-sensitive.** `'Alice' == 'alice'` is `False`. If you need a case-insensitive check, normalize with `.lower()` first.
- **`42 == 42.0` is `True`, but `42 == '42'` raises a `TypeError`.** Ints and floats compare fine; ints and strings do not.
- **Boolean operator precedence: `not` → `and` → `or`.** Complex conditions without parentheses evaluate in that order, which can produce surprising results. Use parentheses liberally to make intent explicit.
- **`elif` stops at the first `True` — even if later conditions are also `True`.** If you need multiple conditions to potentially all run, use separate `if` statements instead of a chain.
- **A `while` loop without a change to its condition runs forever.** Something inside the loop body must eventually make the condition `False`, or you have an infinite loop.
- **Prefer `+=` over `x = x + 1`.** The augmented assignment operators (`+=`, `-=`, `*=`, `/=`) are more concise and Pythonic for incrementing or decrementing a variable.
- **`range()` stops *before* the stop value.** `range(5)` yields `0, 1, 2, 3, 4` — five numbers, last one is `4`. To get `1` through `5` inclusive, use `range(1, 6)`.
- **Use `_` as the loop variable when you don't need the value.** `for _ in range(3):` signals to readers that the loop variable itself is intentionally unused.
- **`for` vs `while`: know when each is appropriate.** Use `for` when iterating over a known sequence. Use `while` when you don't know in advance how many iterations you need.
- **`break`, `continue`, and `sys.exit()` each exit at a different scope.** `continue` skips the rest of the current iteration. `break` exits the current loop entirely. `sys.exit()` stops the whole program — code after the loop still runs after `break`, but nothing runs after `sys.exit()`.
- **`sys.exit()` requires `import sys` first.** It is not a built-in like `print()`. Forgetting the import causes a `NameError`.

### Ch. 3 — Functions

- **Assignment inside a function always creates a local variable.** Even if a global with the same name exists, writing `x = ...` inside a function makes a new local `x`. Use the `global` statement only when you genuinely need to modify a global.
- **Every function returns something.** If there's no `return` statement, Python returns `None`. Storing the result of a print-only function is a common bug — you get `None`, not the printed value.
- **`return` exits the function immediately.** Nothing after it in the same branch runs. Use this for early exits and input guards.
- **Prefer arguments + return values over `global`.** Functions that take inputs and return outputs are easier to test, debug, and reuse. Reach for `global` only as a last resort.
- **Catch specific exceptions, not everything.** A bare `except:` hides bugs. Name the exception type (`ValueError`, `ZeroDivisionError`, etc.) so unexpected errors still surface.
- **The retry loop pattern:** `while True` + `try/except` inside + `return` on success is the standard way to keep prompting until valid input is received.

### Ch. 4 — Lists

- **Indexes start at 0, not 1.** A list with `n` items has valid indexes `0` through `n-1`. The last valid index is always `len(list) - 1`.
- **Negative indexes count from the end.** `-1` is the last item, `-2` is second-to-last. Cleaner than calculating `len(list) - 1` manually.
- **Slices: start is inclusive, end is exclusive.** `list[1:4]` gives you items at indexes 1, 2, and 3 — same logic as `range()`.
- **A slice always returns a list, even with one item.** `list[1:2]` is a list; `list[1]` is the item itself. Different types.
- **`sort()` and `reverse()` modify in place and return `None`.** Never do `x = my_list.sort()` — `x` will be `None`. Use `sorted()` if you need a new list without touching the original.
- **`remove()` removes by value; `del` removes by index.** `remove()` raises `ValueError` if the value isn't found. `remove()` only removes the first match if duplicates exist.
- **Unpacking requires an exact variable count match.** `a, b = [1, 2, 3]` raises `ValueError: too many values to unpack`.
- **`join()` is called on the delimiter, not the list.** `' '.join(words)` — the string owns the method. This surprises everyone at first.
- **Assignment does NOT copy a list — it copies the reference.** `b = a` means both `a` and `b` point to the same list. Changing one changes both.
- **Use `[:]` or `copy.copy()` for a shallow copy; `copy.deepcopy()` for nested lists.** Shallow copies still share inner list references — only `deepcopy()` is fully independent.

### Ch. 5 — Dictionaries & Structuring Data

- **Dictionaries store data by label, not position.** `person['age']` is self-documenting; `person[1]` is not. When you'd want to label your list items, that's a signal to use a dict instead.
- **Accessing a missing key raises `KeyError`.** Unlike a list's `IndexError`, there's no "out of bounds" — the key either exists or it doesn't. Use `get()` for safe lookups.
- **`get(key, default)` never raises `KeyError`.** It returns the default (or `None`) if the key is missing. It never modifies the dict. Use it any time a missing key is a valid, expected state.
- **`setdefault(key, default)` inserts on a miss; `get()` does not.** Use `setdefault()` when you need to guarantee a key exists before working with it — especially for initializing lists or counters inside a dict.
- **Looping: `.keys()`, `.values()`, `.items()` make intent explicit.** `for k in my_dict:` loops over keys by default, but spelling it out is clearer. `.items()` with tuple unpacking (`for k, v in d.items()`) is the standard Pythonic pattern for key-value iteration.
- **`in` checks keys by default.** `'name' in person` checks keys. To check values, you must use `'Spencer' in person.values()` explicitly.
- **The views returned by `.keys()`, `.values()`, `.items()` are not lists.** They are live views of the dict. Wrap in `list()` to index into them or store a snapshot.
- **Use `pprint.pprint()` for nested data.** Plain `print()` dumps everything on one line. `pprint` indents and sorts keys, making nested structures readable at a glance. Use `pformat()` when you need the formatted string rather than printed output.
- **Nest dicts and lists together to model real data.** Dict of dicts for labeled records; lists inside dicts for ordered collections within a record. Chain `[]` brackets to drill down: `data['B-1']['soil_layers'][0]`.
- **Use `is None`, not `== None`.** When checking for the absence of a value, `is None` is the correct Pythonic form. PEP 8 requires it and it signals intent more clearly than `==`.

### Ch. 7 — Pattern Matching with Regular Expressions

- **Regex is a two-step process: compile once, search many times.** `re.compile()` builds the Regex object. `.search()`, `.findall()`, and `.sub()` use it. Compiling once and reusing is more efficient than recompiling inside a loop.
- **Always use raw strings `r"..."` for regex patterns.** Backslashes have special meaning in both Python strings and regex. Raw strings pass them straight to the regex engine and prevent silent bugs.
- **`search()` returns a Match object or `None` — always check before calling `.group()`.** A bare `match.group()` on `None` raises `AttributeError`. The standard guard is `if match:`.
- **`group(0)` is the full match; `group(1)`, `group(2)`, etc. are captured groups.** Groups are numbered left to right by opening parenthesis. An optional group that didn't participate returns `None`, not an empty string.
- **`findall()` return type depends on how many groups your pattern has.** No groups → list of strings. One group → list of strings (group content only). Multiple groups → list of tuples. This is a frequent source of bugs.
- **`?`, `*`, `+` apply to the thing immediately to their left — a character or a group.** `?` = 0 or 1. `*` = 0 or more. `+` = 1 or more. `{n,m}` gives you precise control.
- **Repetition operators are greedy by default — they grab as much as possible.** Add `?` after them (`*?`, `+?`, `{n,m}?`) to make them non-greedy. Non-greedy stops at the first valid match; greedy runs to the last.
- **`^` has two completely different meanings depending on context.** Inside `[]`: negation (`[^aeiou]` = not a vowel). Outside `[]` at pattern start: anchor (`^\d` = starts with a digit). Same character, different job.
- **`^pattern$` together is the standard input validation idiom.** Without both anchors, stray characters before or after the pattern can sneak through undetected.
- **`.` matches any character except newline.** Use `re.DOTALL` to make it match newlines too. Prefer `[]` over `.` when you know what characters are valid — `.` is convenient but imprecise.
- **`re.IGNORECASE` affects matching only — returned text preserves original casing.** Combine multiple flags with `|`: `re.IGNORECASE | re.VERBOSE`.
- **`sub()` returns a new string; `subn()` returns `(new_string, count)`.** Use `subn()` when you need to know whether any replacements were made.
- **Backreferences in `sub()` replacement strings (`\1`, `\2`) must use a raw string.** Without `r"..."`, `\1` is misread as a Python escape sequence.
- **`re.VERBOSE` makes complex patterns maintainable.** Whitespace and `#` comments are ignored by the engine. Literal spaces must be escaped as `\ ` or written as `[ ]`.

### Ch. 6 — Manipulating Strings

- **Strings are immutable — you can read by index, but not write.** `name[0] = 's'` raises a `TypeError`. To get a modified version, build a new string: `name[0].lower() + name[1:]`.
- **Use opposite quote types to avoid escaping.** `"It's fine"` and `'She said "hello"'` are cleaner than escaping. Reserve `\'` and `\"` for when you have no other choice.
- **`repr()` reveals invisible characters.** When a string looks right but isn't behaving right, wrap it in `repr()` — it shows `\n`, `\t`, and spaces explicitly. Essential for debugging whitespace bugs.
- **Raw strings (`r"..."`) disable all escape processing.** Use them for Windows file paths and regex patterns (Ch. 7) where backslashes should be treated literally, not as escape sequences.
- **`upper()` and `lower()` return new strings — they don't modify in place.** Same immutability rule as slicing. The original string is always unchanged.
- **Normalize with `.lower()` before comparing strings you didn't write.** User input, file data, and API responses can have any casing. Normalizing first prevents silent equality failures.
- **`isdecimal()` before `int()` is the clean guard against crashes.** It's the Pythonic alternative to wrapping every conversion in `try/except` when you expect a whole number.
- **`split()` with no argument is smarter than `split(" ")`.** It handles all whitespace, collapses multiples, and strips leading/trailing — always prefer it for natural text input.
- **`join()` is called on the delimiter, not the list.** `" ".join(words)` — the separator string owns the method. Every item in the list must already be a string.
- **`" ".join(text.split())` is the one-liner for normalizing whitespace.** Split on any whitespace (cleans edges and multiples), then rejoin with single spaces. Use it constantly.
- **`strip()` on input and file lines is non-negotiable.** Every line read from a file has a trailing `\n`. Every user input may have accidental spaces. Strip before using.
- **`rjust()`/`ljust()` width is the total output length, not the padding amount.** If your longest item is 10 chars and you call `ljust(12)`, all rows get 2 spaces of padding — regardless of their individual length.
- **`startswith()`/`endswith()` accept a tuple for multiple options.** `filename.endswith((".jpg", ".png"))` is cleaner than chaining `or`. Must be a tuple, not a list.
- **`sys.argv` is a list of command-line arguments.** `sys.argv[0]` is always the script name. Check `len(sys.argv)` before accessing `sys.argv[1]` to avoid an `IndexError`.
- **`pyperclip.copy()` turns a script into a tool.** Any script that produces a final string result should consider copying it to the clipboard automatically — skips the manual copy step entirely.