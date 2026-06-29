# Exception Handling - Interview Questions

1. **What will be the output for print(5-'A')?**
   *Answer*: It will raise a `TypeError: unsupported operand type(s) for -: 'int' and 'str'` because Python does not allow subtracting a string from an integer.

2. **Which block is always executed irrespective of the exception?**
   *Answer*: The `finally` block is always executed, whether an exception is thrown or not.

3. **Which block is executed when there is no exception?**
   *Answer*: The `else` block (used within a `try-except-else-finally` structure) is executed only if the `try` block succeeds without raising any exceptions.

4. **Which is the base class for all the exception classes?**
   *Answer*: `BaseException` is the root base class. However, `Exception` is the base class for all built-in, non-system-exiting exceptions that you typically catch.

5. **Do we need any module to implement exception handling?**
   *Answer*: No, exception handling in Python uses built-in keywords (`try`, `except`, `else`, `finally`) and does not require importing any external or standard modules.
