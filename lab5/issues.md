# Lab 5: Static Code Analysis — Issues Report

| Issue | Type | Original Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Shell command injection | Security — High | 21 | `os.system()` executes a shell command containing a supplier value, potentially allowing command injection. | Replaced shell execution with Python's `print()` function. |
| SQL injection | Security — Medium | 11 | SQL queries were constructed using string formatting, allowing input to alter the query. | Used parameterized SQL queries with placeholders. |
| Broad exception handling | Code quality — Low | 25–28 | A broad exception was silently ignored, hiding potential errors. | Removed the unnecessary exception handler. |
| Global variable usage | Maintainability | 6, 10–12 | The global `order_total` variable made state management less clear. | Calculated the total order quantity using a database query. |
| Unused parameter | Code quality | 16 | The `remarks` parameter was accepted but not used. | Stored delivery remarks in the database. |
| Non-standard function names | Style | 9, 16, 20, 31 | Function names used camelCase instead of Python's conventional snake_case. | Renamed functions and updated their callers. |
| Missing docstrings | Code quality | Multiple | Functions and the module lacked explanatory documentation. | Added a module docstring and function docstrings. |
| Formatting violations | Style | 5, 11, 12, 32 | Long lines and missing whitespace violated style rules. | Reformatted statements and added appropriate whitespace. |

## Conclusion

Pylint, Bandit, and Flake8 helped identify code-quality, security, and formatting issues. After making the changes, Bandit reported no issues, Flake8 reported no violations, and Pylint achieved a score of 9.71/10.
