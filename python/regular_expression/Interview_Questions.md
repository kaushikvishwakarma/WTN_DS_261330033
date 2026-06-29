# Regular Expression - Interview Questions

1. **Why do we need Regular expression?**
   *Answer*: Regular expressions (regex) are essential for advanced pattern matching and text manipulation. They provide a concise, flexible, and efficient means to search, extract, replace, and validate strings based on specific patterns (e.g., validating emails, finding specific formats).

2. **What is difference between match() and search() functions in Regular expression?**
   *Answer*: 
   - `re.match()` checks for a match **only at the beginning** of the string.
   - `re.search()` checks for a match **anywhere** in the string. If there are multiple matches, it returns the first one it finds.
