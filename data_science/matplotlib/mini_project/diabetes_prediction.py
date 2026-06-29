import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def diabetes_eda():
    # Note: To run this, download 'Diabetes.csv' from Kaggle
    try:
        # 1. Load the data in the DataFrame
        df = pd.read_csv('Diabetes.csv')
        print("1. Data Loaded successfully. Shape:", df.shape)
        
        # 2. Data Pre-processing
        # Example: replacing 0s with NaN for columns where 0 is medically invalid
        cols_with_zeros = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
        for col in cols_with_zeros:
            if col in df.columns:
                df[col] = df[col].replace(0, pd.NA)
        print("2. Data Pre-processing done (medically invalid 0s replaced with NaN).")
        
        # 3. Handle the Categorical Data
        # Depending on the specific dataset, categorical data might need encoding
        cat_cols = df.select_dtypes(include=['object']).columns
        if len(cat_cols) > 0:
            df = pd.get_dummies(df, columns=cat_cols, drop_first=True)
            print("3. Categorical Data Handled (One-hot encoding applied).")
        else:
            print("3. No Categorical Data found in this dataset.")
            
        # 4. Perform Uni-variate Analysis
        print("4. Performing Uni-variate Analysis... (Displaying plot)")
        if 'Age' in df.columns:
            plt.figure(figsize=(8, 5))
            sns.histplot(df['Age'].dropna(), kde=True, color='purple')
            plt.title('Age Distribution of Patients')
            plt.xlabel('Age')
            plt.ylabel('Count')
            plt.show()
            
        # 5. Perform Bi-variate Analysis
        print("5. Performing Bi-variate Analysis... (Displaying plot)")
        if 'Glucose' in df.columns and 'Outcome' in df.columns:
            plt.figure(figsize=(8, 5))
            sns.boxplot(x='Outcome', y='Glucose', data=df, palette='Set3')
            plt.title('Glucose Level by Diabetes Outcome')
            plt.xlabel('Outcome (0: No, 1: Yes)')
            plt.ylabel('Glucose Level')
            plt.show()
            
    except FileNotFoundError:
        print("Error: 'Diabetes.csv' not found. Please download from Kaggle.")

if __name__ == "__main__":
    diabetes_eda()
