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

## Dependencies

Third-party libraries installed in this project, tracked in `requirements.txt` at the repo root:

| Library | Introduced | Purpose |
|---------|------------|---------|
| `pyperclip` | Ch. 6 | Clipboard access — used in the password locker capstone |
| `PyInputPlus` | Ch. 8 | Input validation with built-in retry, timeout, and type checking |
| `send2trash` | Ch. 10 | Safe deletes — sends files/folders to the OS Trash instead of permanently deleting |

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
| Ch. 8 | Input Validation | ✅ Complete |
| Ch. 9 | Reading & Writing Files | ✅ Complete |
| Ch. 10 | Organizing Files | ✅ Complete |
| Ch. 11 | Debugging | 🔜 Next |
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

### Ch. 8 — Input Validation

- **PyInputPlus replaces the `while True` + `try/except` retry loop.** Every numeric, yes/no, choice, and format input function handles the retry loop internally. You get one-line validated input instead of ~8 lines of boilerplate.
- **`inputInt()` rejects floats — `25.5` is not a valid integer.** Use `inputFloat()` when decimals are acceptable, or `inputNum()` when you don't care which type the user provides.
- **`inputNum()` return type adapts to what was typed.** `"25"` → `int`, `"25.5"` → `float`. Useful when either type is acceptable downstream.
- **`min`/`max` are inclusive; `greaterThan`/`lessThan` are exclusive.** `min=1` allows `1`; `greaterThan=1` rejects it. Same distinction as `>=` vs `>`.
- **`limit` and `timeout` raise exceptions — always handle them.** `RetryLimitException` when attempts are exhausted, `TimeoutException` when time runs out. Use `default=` as a cleaner alternative when a fallback value makes sense.
- **`inputBool()` does NOT accept yes/no/y/n — only `True`/`False`.** For conversational yes/no prompts, use `inputYesNo()` instead. They accept different inputs and return different types.
- **`inputMenu()` auto-generates a numbered list; the user can respond by number or text.** Use it over `inputChoice()` when you want PyInputPlus to handle the display formatting.
- **Don't rely on `inputDatetime()` default formats — always pass an explicit `formats` list.** The defaults require a time component; date-only strings like `04/12/2026` are rejected. Explicit formats prevent silent surprises.
- **`inputDatetime()` returns a real `datetime` object.** Date math, `.strftime()` formatting, and attribute access (`.year`, `.month`, `.day`) are all immediately available — no manual parsing needed.
- **`mustExist=True` in `inputFilepath()` may not be reliable.** Verify filesystem existence with `os.path.exists()` as an explicit follow-up check rather than depending on PyInputPlus alone.
- **`inputCustom()` contract: raise `ValueError` on bad input, return `None` on good input.** PyInputPlus catches the `ValueError`, displays the message, and reprompts. Your function owns the rule; PyInputPlus owns the loop.
- **`inputCustom()` is where Ch. 7 regex pays off.** Any compiled regex pattern can become a validator. Compile with `re.compile()` at module level (once), then use `.search()` inside the validator function.

### Ch. 9 — Reading & Writing Files

- **A `Path` object does not require the path to exist on disk.** `Path('/some/fake/path')` is valid — it's a representation, not a connection. Existence checks (`.exists()`, `.is_file()`, `.is_dir()`) are separate, explicit calls.
- **Use `/` to join `Path` objects — never string concatenation.** `Path('/Users/spencer') / 'Desktop' / 'file.txt'` is cross-platform safe. String concatenation with `+` or `os.sep` is fragile and unnecessary.
- **`Path.cwd()` depends on where you run the script from; `Path.home()` does not.** `cwd()` shifts if you `cd` before running. `home()` always points to your user directory. Use `Path(__file__).parent` when you need a path relative to the script itself — it's stable regardless of the working directory.
- **`.name` is the full filename; `.stem` is the name without extension; `.suffix` includes the dot.** `Path('README.md').stem` → `'README'`, `.suffix` → `'.md'`. Use these to rebuild a path with a changed extension instead of slicing strings manually.
- **Always use `with open(...)` — never `f = open(...)` without a `with` block.** The `with` statement guarantees the file closes even if an exception is raised mid-read. A manually opened file left unclosed can corrupt data and hold OS locks.
- **`.readlines()` keeps the trailing `\n` on every line — always `.strip()` before using.** `['Line one\n', 'Line two\n']` is what you get. The Ch. 6 rule about stripping file lines is non-negotiable here.
- **Iterating directly over the file object is the most memory-efficient read pattern.** `for line in f:` yields one line at a time without loading the whole file. Use `.read()` or `.readlines()` only when you need the entire content at once.
- **`'w'` mode silently overwrites — there is no warning, no confirmation, no recovery.** Any existing content is gone the moment you call `open(path, 'w')`. Use `'a'` to append to an existing file. Default (no mode) is `'r'` (read-only).
- **`.write()` does NOT add `\n` automatically — you must include it in the string.** `f.write('hello')` followed by `f.write('world')` produces `'helloworld'` on one line. Always include `\n` explicitly.
- **`.write()` returns the character count as an int.** It's easy to overlook, but useful if you need to verify how much was written. Ignoring the return value is fine.
- **`'\n'.join(lines) + '\n'` is the clean pattern for writing a list of strings.** One `.write()` call beats a loop of individual writes, and the trailing `\n` keeps the file properly terminated.
- **`shelve` gives you a persistent dict backed by binary files on disk.** You interact with it exactly like a regular dict — `shelf['key'] = value`, `shelf['key']`, `del shelf['key']`, `'key' in shelf` all work. The data survives between program runs.
- **`shelve.open()` manages its own file extensions — do not add one to the path.** Pass `'mydata'`, not `'mydata.db'`. On macOS it creates `mydata.db`; on other systems it may create multiple files. The name is OS-dependent.
- **Mutating a mutable value stored in a shelf requires a read-modify-write cycle.** `shelf['score'] += 1` may silently fail on some Python versions. The safe pattern is: read the value out, modify it, assign it back: `val = shelf['key']; val.append(x); shelf['key'] = val`.
- **`pprint.pformat()` converts a Python object into a string of valid Python code.** Writing `'variable = ' + pformat(data) + '\n'` to a `.py` file creates a human-readable, hand-editable data file. This is the pattern that makes `saved_data.py` and `config.py` work.
- **Load a `pformat()`-generated file back by importing it as a module.** `import saved_data` runs the file, which executes the assignment statements. The variable is then available as `saved_data.cats`. This is a simple persistence technique that requires zero parsing.
- **`pformat()` only works for Python literal types.** Strings, ints, floats, lists, dicts, tuples, booleans, and `None` all serialize cleanly. Custom class instances, file objects, and functions cannot be represented this way — use `shelve` (which uses `pickle` internally) for those.
- **`shelve` vs `pformat()` is a tradeoff between flexibility and readability.** `shelve` handles almost any Python object but is binary and Python-only. `pformat()` files are readable in any text editor and editable by hand, but are limited to literal data types.
- **`os.path` is the legacy path API — know it to read old code, but write new code with `pathlib`.** Key translations: `os.path.join()` → `Path('/') / 'dir'`, `os.path.basename()` → `.name`, `os.path.dirname()` → `.parent`, `os.path.splitext()` → `.stem` + `.suffix`, `os.path.getsize()` → `.stat().st_size`, `os.listdir()` → `.iterdir()`.
- **`os.listdir()` returns plain strings; `Path.iterdir()` returns Path objects.** With `iterdir()` you can immediately call `.is_file()`, `.name`, `.suffix`, etc. on each item without constructing a new `Path` from a string.
- **`frequency.get(word, 0) + 1` is the canonical word-counting idiom.** It combines the Ch. 5 `get()` pattern (safe default on a missing key) with an inline increment. No `if word in frequency:` guard needed.

### Ch. 10 — Organizing Files

- **`shutil.copy()` is for one file; `shutil.copytree()` is for a whole folder tree.** `copytree()` requires `dst` to NOT already exist — it creates the destination fresh. Guard re-runs by removing the old copy first (`if dst.exists(): shutil.rmtree(dst)`).
- **`shutil.move()` covers move, rename, and rename-in-place all in one call.** No separate `os.rename()` needed. **Sharp edge:** if `dst` is an existing file, it is silently overwritten — same hazard as `'w'` mode in Ch. 9.
- **The three permanent-delete functions each have a specific scope.** `os.unlink()` → one file. `os.rmdir()` → one *empty* directory. `shutil.rmtree()` → directory + everything inside. None of them go to the Trash.
- **`os.rmdir()` refusing to delete a non-empty directory is a feature, not a limitation.** It is the safe, defensive choice when you *expect* a directory to be empty — it raises `OSError` if your assumption was wrong, instead of silently destroying contents the way `rmtree()` would.
- **`OSError` is the parent class** of `FileNotFoundError`, `PermissionError`, `IsADirectoryError`, etc. Catching `OSError` covers cross-platform errno variations (e.g., "directory not empty" has different numbers on macOS/Linux/Windows). Catch the specific subclass when *that's* the only error you expect.
- **`Path.unlink()` is the modern `pathlib` equivalent of `os.unlink()`.** Same operation, called as a method on the Path object. After Ch. 9, prefer this form for consistency with the rest of your `pathlib` code.
- **The dry-run safety pattern: print first, delete second — never the reverse.** When writing a deletion script, always run it once with `print(path)` and the `unlink()` call commented out. Eyeball the list. Only then uncomment the delete. This catches off-by-one filter bugs before they become permanent data loss.
- **`send2trash` is the safe alternative for "I'm not 100% sure my filter is correct" cleanup.** It moves files/folders to the OS Trash (recoverable) instead of permanent deletion. Same call signature for files and directories: `send2trash(path)`. Tradeoff: doesn't free disk space until the Trash is emptied.
- **Don't reflexively use `send2trash` for everything.** Scaffolding folders the script created itself are noise — they belong in permanent delete-land via `shutil.rmtree()`. Reserve `send2trash` for content with value.
- **`os.walk()` yields a 3-tuple per directory: `(folder_name, subfolders, filenames)`.** `subfolders` and `filenames` are bare names — NOT paths. To act on them, rebuild: `Path(folder_name) / name`. Forgetting this is a classic early bug — the script "works" but operates relative to the wrong CWD.
- **Mutating the `subfolders` list IN PLACE prunes the walk; reassigning does NOT.** `subfolders.remove('node_modules')` works. `subfolders = [s for s in subfolders if ...]` does nothing — that creates a new local variable, but `os.walk()` still has the original list. Same trick for stable traversal order: `subfolders.sort()` in place.
- **`os.walk()` does NOT guarantee alphabetical order.** Order comes from the OS/filesystem. If you need reproducible output, sort `subfolders` and `filenames` yourself.
- **Use `os.walk()` when you need tree structure or pruning; use `Path.rglob()` when you just want a flat list of matches.** `rglob('*.txt')` is shorter for "find every X anywhere underneath." `os.walk()` is the right tool when per-directory grouping or skip logic matters.
- **`zipfile.ZipFile` is a context manager — always use `with`.** Same rule as `open()` from Ch. 9. Default mode is `'r'` (read-only).
- **`ZipFile` has four modes: `r`, `w`, `a`, `x`.** `'w'` silently overwrites an existing archive. **`'x'` is the safe alternative** — it raises `FileExistsError` if the target exists, which is what you want for backup scripts that must not clobber yesterday's data.
- **`arcname` is the single most important parameter when writing ZIPs.** Without it, the file's absolute filesystem path is baked into the archive — extracting gives the recipient a deeply nested folder mirror of *your* machine. With `arcname=path.relative_to(some_root)`, the archive is clean and portable.
- **`relative_to(folder)` vs `relative_to(folder.parent)` controls whether the folder itself is in the archive.** For a "backup of folder X" archive, use `folder.parent` so entries are `X/file.txt` — extracting reconstructs the folder. Use `folder` for loose files at the root.
- **`ZIP_DEFLATED` is the default-default; `ZIP_STORED` is bundle-only.** `STORED` *increases* file size by a few bytes of header overhead — use it only for files that won't compress (already-zipped images, video). For text and code, always `DEFLATED`.
- **`.read(name)` returns `bytes`, not `str` — even for text files.** Decode with `.decode()` if you know the encoding. This lets you peek inside an archive without writing anything to disk.
- **`.extract()` and `.extractall()` default to the current working directory — always pass `path=`.** Defaulting to CWD is the kind of surprise that makes scripts hard to debug. Be explicit about the destination.
- **Appending a duplicate name to a ZIP does NOT replace the existing entry — both copies are stored.** Most extraction tools return the last one, but the duplicate sits there wasting space. To "replace" entries, recreate the archive from scratch.
- **The "loop until unused" pattern is the clean way to pick a non-clobbering output filename.** `while (output_dir / f'{name}_{n}.zip').exists(): n += 1`. Simpler and clearer than regexing existing filenames for the max number — same result.
- **`Path.resolve()` at function entry normalizes paths before using `.parent` or `.name`.** Without it, `backup_to_zip('.')` gives surprising results: `Path('.').name` is `''`, `Path('.').parent` is `Path('.')`. Resolving turns relative paths, `.`, and symlinks into a clean absolute path the rest of the function can rely on.
