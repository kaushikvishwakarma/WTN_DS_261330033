# Data Preprocessing - Interview Questions

1. **What is Data Preprocessing?**
   *Answer*: Data preprocessing is the process of transforming and cleaning raw, often messy or incomplete data, into an understandable and structured format that is suitable for building and training machine learning models.

2. **Difference between Data Wrangling and Data Preprocessing.**
   *Answer*: 
   - **Data Preprocessing** generally refers to the specific steps taken to prepare data for a machine learning algorithm (e.g., normalization, missing value imputation, encoding).
   - **Data Wrangling** (or Data Munging) is a broader term that encompasses gathering, assessing, and restructuring "raw" data into a desired format for various downstream purposes, such as broader analytics or business intelligence, not just ML.

3. **How to handle missing values?**
   *Answer*: Missing values can be handled by:
   - **Deletion**: Dropping rows or columns with missing data (if the missingness is rare).
   - **Imputation**: Filling in the missing values with statistical measures (mean, median, mode) or predicting them using algorithms like K-Nearest Neighbors (KNN).

4. **What is Data Imputation?**
   *Answer*: Data imputation is the process of replacing missing or null data with substituted values (such as the column mean or median) to retain the rest of the data in a row, preventing the loss of valuable information that would occur if the incomplete record were simply discarded.

5. **How to handle Inappropriate Data?**
   *Answer*: Inappropriate data (such as outliers, typos, erroneous negative values for age, or inconsistent date formats) can be handled by:
   - Identifying and filtering out outliers using statistical boundaries (Z-score or IQR).
   - Correcting formatting inconsistencies (e.g., standardizing text to lowercase).
   - Replacing illogical values with nulls and then imputing them, or capping extreme values (winsorization).
