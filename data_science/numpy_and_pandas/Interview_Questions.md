# Numpy and Pandas - Interview Questions

1. **Differentiate between Python Array and Numpy Array?**
   *Answer*: Python lists (arrays) can hold elements of different data types, whereas Numpy arrays require all elements to be of the same type. This homogeneity makes Numpy arrays more memory-efficient and significantly faster for mathematical operations. Numpy also provides many built-in functions for vectorized operations that Python lists lack.

2. **What is Numpy?**
   *Answer*: NumPy (Numerical Python) is a core open-source library in Python for scientific computing. It provides a high-performance multidimensional array object (`ndarray`) and a comprehensive collection of mathematical functions to operate on these arrays.

3. **What are mathematical operations supported by Numpy?**
   *Answer*: NumPy supports a vast array of mathematical operations, including:
   - Basic arithmetic (addition, subtraction, multiplication, division)
   - Exponentiation and logarithms
   - Trigonometric functions (sin, cos, tan)
   - Statistical operations (mean, median, standard deviation, variance)
   - Matrix operations and linear algebra (dot product, cross product, eigenvalue decomposition)

4. **How to detect the outliers using IQR?**
   *Answer*: IQR (Interquartile Range) is calculated by subtracting the first quartile ($Q1$, 25th percentile) from the third quartile ($Q3$, 75th percentile). Outliers are detected as any data points that fall below the lower bound ($Q1 - 1.5 \times IQR$) or above the upper bound ($Q3 + 1.5 \times IQR$).

5. **Why Pandas is used?**
   *Answer*: Pandas is widely used for data manipulation, cleaning, and analysis in Python. It introduces powerful data structures like DataFrames (2D tables) and Series (1D arrays) that make working with structured (tabular) data intuitive. It offers built-in tools for merging, reshaping, filtering, and dealing with missing data.

6. **What is Series in Pandas?**
   *Answer*: A Series is a one-dimensional labeled array in Pandas capable of holding data of any type (integer, string, float, python objects, etc.). The axis labels are collectively called the index. It can be thought of as a single column in an Excel spreadsheet or an SQL table.
