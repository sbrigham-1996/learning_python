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
| Ch. 4 | Lists | 🔜 Next |
| Ch. 5 | Dictionaries & Structuring Data | ⬜ Not started |
| Ch. 6 | Manipulating Strings | ⬜ Not started |
| Ch. 7 | Pattern Matching with Regex | ⬜ Not started |
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