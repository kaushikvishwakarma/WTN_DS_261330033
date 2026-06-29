import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def predict_sales():
    # Dataset: Advertising.csv
    try:
        # 1. Load the data
        df = pd.read_csv('Advertising.csv')
        
        # 2. Perform Data Preprocessing
        if 'Unnamed: 0' in df.columns:
            df.drop('Unnamed: 0', axis=1, inplace=True)
            
        print("Data loaded and preprocessed. Shape:", df.shape)
        
        # 3. Handle Categorical Data (if any exist, though Advertising is usually all numeric)
        cat_cols = df.select_dtypes(include=['object']).columns
        if len(cat_cols) > 0:
            df = pd.get_dummies(df, columns=cat_cols, drop_first=True)
            
        # 4. Perform Exploratory Data Analysis (Skipped visualization here for brevity)
        print("EDA Step: Statistical Summary")
        print(df.describe())
        
        # Features & Target
        # Assuming 'Sales' is the target column
        if 'Sales' in df.columns:
            X = df.drop('Sales', axis=1)
            y = df['Sales']
            
            # Train test split
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            # 5. Build the model using Multiple Linear Regression
            model = LinearRegression()
            model.fit(X_train, y_train)
            
            # 6. Use the appropriate evaluation metrics
            predictions = model.predict(X_test)
            print("\nMultiple Linear Regression Results:")
            print(f"Mean Squared Error (MSE): {mean_squared_error(y_test, predictions):.2f}")
            print(f"R-squared Score: {r2_score(y_test, predictions):.2f}")
        else:
            print("Target column 'Sales' not found in dataset.")
            
    except FileNotFoundError:
        print("Error: 'Advertising.csv' not found. Please download from Kaggle.")

if __name__ == "__main__":
    predict_sales()
