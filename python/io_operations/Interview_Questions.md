# IO Operations - Interview Questions

1. **How to open a file in create mode?**
   *Answer*: You can use `open("filename.txt", "x")` to create a new file (fails if it already exists) or `open("filename.txt", "w")` to create a new file (or overwrite if it already exists).

2. **Which function reads one line at a time?**
   *Answer*: The `readline()` method of a file object reads one line at a time.

3. **Which module is required to delete files or folders?**
   *Answer*: The `os` module is required (`os.remove()` for files and `os.rmdir()` for empty folders). Alternatively, the `shutil` module can be used to delete non-empty folders (`shutil.rmtree()`).
