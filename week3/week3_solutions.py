import pandas as pd

# -----------------------------------------------------------
# Load the messy dataset
# -----------------------------------------------------------
df = pd.read_csv('dataset.csv')

print("=" * 60)
print("STEP 0: Raw data overview")
print("=" * 60)
print("Shape:", df.shape)
print(df.dtypes)
print(df.head())
print("\nMissing values per column:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# -----------------------------------------------------------
# STEP 1: Clean the 'Date' column
#   - Strip stray single quotes: "'2020/12/01'" -> "2020/12/01"
#   - Fix rows stored as a raw int: 20201226 -> "2020/12/26"
#   - Convert to proper datetime
# -----------------------------------------------------------
def clean_date(val):
    if pd.isna(val):
        return None
    s = str(val).strip().strip("'")
    if s.isdigit() and len(s) == 8:          # e.g. 20201226
        s = f"{s[0:4]}/{s[4:6]}/{s[6:8]}"
    return s

df['Date'] = df['Date'].apply(clean_date)
df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m/%d', errors='coerce')

# -----------------------------------------------------------
# STEP 2: Handle missing values
#   - Date: fill by inferring from the row order (day-by-day series)
#   - Calories: fill with column mean
# -----------------------------------------------------------
df['Date'] = df['Date'].interpolate()  # fills the 1 missing date using neighbours
df['Calories'] = df['Calories'].fillna(df['Calories'].mean())

# -----------------------------------------------------------
# STEP 3: Remove duplicate rows
# -----------------------------------------------------------
before = len(df)
df = df.drop_duplicates()
print(f"\nDropped {before - len(df)} duplicate row(s)")

# -----------------------------------------------------------
# STEP 4: Filter rows
#   - Remove the clear data-entry outlier (Duration = 450 -> not a
#     realistic workout duration compared to the rest of the data)
# -----------------------------------------------------------
df_filtered = df[df['Duration'] <= 120].reset_index(drop=True)
print(f"Filtered out {len(df) - len(df_filtered)} outlier row(s) with Duration > 120")
df = df_filtered

# -----------------------------------------------------------
# STEP 5: Create new columns
# -----------------------------------------------------------
df['Calories_per_Minute'] = (df['Calories'] / df['Duration']).round(2)
df['Pulse_Range'] = df['Maxpulse'] - df['Pulse']
df['Intensity'] = pd.cut(
    df['Pulse'],
    bins=[0, 100, 115, 200],
    labels=['Low', 'Moderate', 'High']
)

print("\n" + "=" * 60)
print("FINAL CLEANED DATASET")
print("=" * 60)
print(df)

print("\nSummary stats:")
print(df.describe(include='all'))

df.to_csv('cleaned_dataset.csv', index=False)
print("\nSaved cleaned data -> cleaned_dataset.csv")
