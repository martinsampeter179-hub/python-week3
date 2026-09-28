# PLP Python Week 3: Grade Reporter & Bug Hunt

This repository contains the solutions for the Week 3 Python assignment focusing on conditional statements (`if` / `elif` / `else`), loop execution (`for` and `while`), and code debugging.

## Files Included

* `grade_reporter.py` - Processes a list of student test scores, prints letter grades for each score, tracks pass/fail counts, and calculates the overall average score rounded to one decimal place.
* `bug_hunt.py` - A corrected script that calculates the sum of numbers from 1 to 5, including `# BUG:` comments documenting the fix for each identified issue.

## Reflection Question

The hardest bug to locate in Part B was the logical error in the `while` loop condition (`count < 5`). Unlike the syntax and type errors, this bug caused no error message or program crash—it ran smoothly but produced an incorrect answer of `10` instead of `15`. I knew something was wrong because the prompt specified that the correct sum of 1 through 5 is 15. By tracing the loop steps manually, I realized `count < 5` stopped execution before adding `5`, which required changing the condition to `count <= 5`.
