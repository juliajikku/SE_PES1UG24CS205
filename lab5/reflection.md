# Lab 5: Static Code Analysis — Reflection

### 1. What is static code analysis?

Static code analysis examines source code without executing it to identify potential bugs, security vulnerabilities, and coding-style violations.

### 2. What are the differences between Pylint, Bandit, and Flake8?

Pylint checks code quality, naming conventions, documentation, and potential programming problems. Bandit identifies common security vulnerabilities. Flake8 checks Python formatting and compliance with style guidelines.

### 3. What issues were identified and how were they fixed?

The original program contained a potential SQL injection vulnerability, unsafe shell execution, broad exception handling, global state, an unused parameter, and formatting issues. These were addressed through parameterized queries, safer notification handling, improved state management, meaningful parameter usage, and consistent Python formatting.

### 4. How did static analysis improve the program?

Static analysis helped improve the program's security, readability, maintainability, and consistency. The final code achieved a Pylint score of 9.71/10, with no issues reported by Bandit and no violations reported by Flake8.
