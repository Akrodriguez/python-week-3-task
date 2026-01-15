import pandas as pd

# Step 1: Load dataset
df = pd.read_csv("sales_data.csv")

# Step 2: Display basic info
print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nShape of dataset:", df.shape)

# Step 3: Handle missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Fill missing numeric values with mean
for col in df.select_dtypes(include="number"):
    df[col].fillna(df[col].mean(), inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Step 4: Analysis (metrics)
total_sales = df["Total_Sales"].sum()
average_sales = df["Total_Sales"].mean()
max_sale = df["Total_Sales"].max()

best_product = df.groupby("Product")["Total_Sales"].sum().idxmax()

# Step 5: Final Report
print("\n--- SALES REPORT ---")
print(f"Total Revenue: ₹{total_sales:,.2f}")
print(f"Average Sale Value: ₹{average_sales:,.2f}")
print(f"Highest Single Sale: ₹{max_sale:,.2f}")
print(f"Best Selling Product: {best_product}")
