import pandas as pd

# STEP 1: Extract
df = pd.read_csv("C:\\Users\\HP\\OneDrive\\Desktop\\Eval8AI\\DATA ENGINEER\\etl_project\\data\\sales.csv")
print("Original Data:")
print(df)

# STEP 2: Transform

# Remove duplicates
df = df.drop_duplicates()

# Remove missing values
df = df.dropna()

# Convert date column
df['order_date'] = pd.to_datetime(df['order_date'])

# Create new column
df['total_price'] = df['quantity'] * df['price']

print("\nCleaned Data:")
print(df)






from sqlalchemy import create_engine

# 🔴 Replace with your actual password
engine = create_engine("postgresql://postgres:admin123@localhost:5432/sales_db")

# Load data into PostgreSQL
df.to_sql("sales_cleaned", engine, if_exists="replace", index=False)

print("Data loaded into PostgreSQL successfully!")