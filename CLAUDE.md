# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running Code

Each file is a standalone Python script. Run any solution directly:

```bash
python array_hashing/two_sum.py
python graph/number_of_island.py
```

No test framework is configured. To test a solution, add a `if __name__ == "__main__":` block at the bottom of the file with example inputs from the problem statement.

## Project Setup

Uses Poetry with Python 3.12+:

```bash
poetry install
poetry run python <file>
```

## Repository Structure

Each top-level directory corresponds to a LeetCode problem category:

| Directory | Topics |
|---|---|
| `array_hashing/` | Hash maps, frequency counting, encoding |
| `two_pointer/` | Two-pointer technique |
| `sliding_window/` | Variable/fixed window problems |
| `stack/` | Monotonic stack, parentheses |
| `binary_search/` | Search on sorted/rotated arrays |
| `linked_list/` | Singly linked list manipulation |
| `tree/` | Binary tree, BST, trie |
| `trie/` | Prefix tree implementations |
| `heap_priority/` | Min/max heap, priority queue |
| `back_tracking/` | Permutations, subsets, N-Queens |
| `graph/` | BFS, DFS, Union-Find, topological sort |
| `advanced_graph/` | Dijkstra, Bellman-Ford, Prim, Kruskal |
| `one_d_dynamic_programming/` | 1D DP patterns |
| `two_d_dynamic_programming/` | 2D DP / knapsack |
| `intervals/` | Interval merge/overlap problems |
| `Bit_Manipulation/` | Bitwise operations |
| `Math_&_Geometry/` | Math-based problems |

## File Conventions

- Each `.py` file solves one LeetCode problem.
- The problem statement is in the module docstring at the top.
- Solutions are plain functions or `class Solution` with a method, matching LeetCode's expected interface.
- Inline comments explain the reasoning step by step.

## Ereader Style Guide

All documentation and code comments in this repo are written to render
well on a 7.8 inch ereader (e.g. Kobo Libra 2, Kindle Oasis).
A 7.8 inch screen at typical font size fits roughly 60 characters per
line. Apply these rules consistently.

### Line length

- Hard-wrap prose at 60 characters per line.
- Hard-wrap code and comments at 60 characters per line.
- Break long expressions across multiple lines rather than
  letting them overflow.

```python
# Good — fits in 60 chars
result = some_function(
    argument_one,
    argument_two,
)

# Bad — overflows the screen
result = some_function(argument_one, argument_two)
```

### Code style

- Use one expression or statement per line.
- Avoid chained method calls on one line; break each call
  onto its own line.
- Name variables descriptively so comments stay short.
- Do not use single-letter variable names except for
  standard loop indices (`i`, `j`, `r`, `c`).

### Comments

- Place comments on the line above the code they describe,
  not inline at the end of a line.
- Keep each comment to one or two short sentences.
- Explain *why*, not *what* the code does.

```python
# Good
# Use a set for O(1) lookup.
seen = set()

# Bad
seen = set()  # O(1) lookup set for visited nodes
```

### Docstrings and problem statements

- Wrap the problem statement docstring at 60 characters.
- Separate sections with a blank line: problem, examples,
  constraints.
- Keep example input/output on separate lines.

```python
"""
Given an array nums and a target, return
the indices of two numbers that add up
to target.

Example:
  Input:  nums=[2,7,11,15], target=9
  Output: [0,1]
"""
```

### Markdown documentation

- Use `##` and `###` headings; never skip levels.
- Bullet lists only; avoid numbered lists longer than 5
  items.
- Do not use tables — use bullet lists with bold labels
  instead.
- Avoid ASCII diagrams wider than 60 characters.
- One blank line between every section.
