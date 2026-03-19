# GEMINI.md

This file provides guidance to Gemini CLI when working with code in this repository.

## Core Mandate: E-reader Optimization (7.8 inch)

All documentation, code, and comments in this repository MUST be optimized for a 7.8-inch e-reader screen (e.g., Kobo Libra 2, Kindle Oasis).

### 1. Hard Wrapping (60 Characters)
- **Hard-wrap all prose, code, and comments at 60 characters per line.**
- This prevents horizontal scrolling and ensures readability when font sizes are increased.
- Break long expressions across multiple lines.

### 2. Code Structure
- **One statement per line:** Avoid complex one-liners.
- **Vertical spacing:** Use blank lines to separate logical blocks.
- **Descriptive naming:** Use clear variable names to minimize the need for long explanatory comments.
- **No inline comments:** Place comments on the line ABOVE the code they describe.

### 3. Documentation & Docstrings
- **Problem Statements:** Wrap at 60 characters.
- **Format:** Use clear sections (Problem, Examples, Constraints) separated by blank lines.
- **Examples:** Keep input and output on separate lines for clarity.

### 4. Markdown Formatting
- **Hierarchy:** Use `##` and `###` headers correctly.
- **No Tables:** Use bulleted lists with bold labels instead, as tables render poorly on small screens.
- **Lists:** Prefer bullet points over long numbered lists.
- **Width:** Ensure no element (including ASCII art) exceeds 60 characters in width.

## Workflow Patterns

### Running Code
Each file is a standalone Python script. Run solutions directly:
```bash
python <category>/<problem>.py
```

### Testing
To test a solution, add an `if __name__ == "__main__":` block at the bottom of the file with example inputs. Follow the 60-character wrap rule for test cases as well.

### Repository Structure
The repository is organized by LeetCode problem categories (e.g., `array_hashing/`, `two_pointer/`, `sliding_window/`).
