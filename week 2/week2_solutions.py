import pandas as pd

# -----------------------------------------------------------
# Q1: Load a CSV file using Pandas and display basic info
# -----------------------------------------------------------
df = pd.read_excel('DOC-20260907-WA0001.xlsx')   # (loaded from the shared dataset)

print("=" * 60)
print("Q1: Basic Info")
print("=" * 60)
print("Shape:", df.shape)
print("\nColumn info:")
print(df.info())
print("\nFirst 5 rows:")
print(df.head())

# -----------------------------------------------------------
# Q2: Handle missing values and duplicates using Pandas
# -----------------------------------------------------------
print("\n" + "=" * 60)
print("Q2: Missing Values & Duplicates")
print("=" * 60)
print("Missing values per column:\n", df.isnull().sum())
print("\nNumber of duplicate rows:", df.duplicated().sum())

# Drop exact duplicate rows (if any)
df = df.drop_duplicates()

# Fill missing numeric values with the column mean, categorical with mode
for col in df.columns:
    if df[col].isnull().sum() > 0:
        if df[col].dtype in ['int64', 'float64']:
            df[col] = df[col].fillna(df[col].mean())
        else:
            df[col] = df[col].fillna(df[col].mode()[0])

print("\nAfter cleaning -> missing values:\n", df.isnull().sum().sum())
print("After cleaning -> duplicate rows:", df.duplicated().sum())

# -----------------------------------------------------------
# Q3: Group data by category and find total revenue
# -----------------------------------------------------------
print("\n" + "=" * 60)
print("Q3: Total Revenue by Category")
print("=" * 60)
revenue_by_category = df.groupby('category')['total_price'].sum().sort_values(ascending=False)
print(revenue_by_category)

# -----------------------------------------------------------
# Q4: Sort data by multiple columns using Python
# -----------------------------------------------------------
print("\n" + "=" * 60)
print("Q4: Sort by Category (asc) then Total Price (desc)")
print("=" * 60)
sorted_df = df.sort_values(by=['category', 'total_price'], ascending=[True, False])
print(sorted_df[['order_id', 'category', 'product_name', 'total_price']].head(10))

# -----------------------------------------------------------
# Q5: Create a correlation matrix for numerical columns
# -----------------------------------------------------------
print("\n" + "=" * 60)
print("Q5: Correlation Matrix (numeric columns)")
print("=" * 60)
numeric_df = df.select_dtypes(include='number')
corr_matrix = numeric_df.corr()
print(corr_matrix)
