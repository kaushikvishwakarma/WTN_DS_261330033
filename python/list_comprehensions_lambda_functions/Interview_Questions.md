# List Comprehensions and Lambda Functions - Interview Questions

1. **Is List comprehension faster than for loop?**
   *Answer*: Yes, list comprehensions are generally faster than traditional `for` loops in Python because they are optimized for the CPython interpreter to construct lists directly in C rather than executing loop instructions in Python.

2. **Is List iterator or iterables?**
   *Answer*: A list is an **iterable**, not an iterator. You can loop over it, but it does not maintain state like an iterator does. You can, however, create an iterator from a list by passing it to the built-in `iter()` function.

3. **Is Lambda keyword must in lambda funcations?**
   *Answer*: Yes, the `lambda` keyword is mandatory when defining anonymous functions (lambda functions) in Python.
