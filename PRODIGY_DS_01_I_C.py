#importing Library
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the dataset
file_path = r"E:\Research\PRODIGY_DS_02\PRODIGY_DS_02\Netflix_dataset\netflix_titles.csv"  
df = pd.read_csv(file_path) 

# Previewing the data
print("Dataset Head:\n", df.head())
print("\nDataset Info:\n")
df.info()

# -------------------------------------------
# Checking for null values
# -------------------------------------------
print("\nMissing Values in Each Column:\n", df.isnull().sum())

# -------------------------------------------
# Droping duplicates
# -------------------------------------------
df = df.drop_duplicates()
print(f"\nDataset Shape After Removing Duplicates: {df.shape}")

# -------------------------------------------
# Handling missing values
# -------------------------------------------
# Replacing missing values in columns with "Unknown"
df.fillna({
    "director": "Unknown", 
    "cast": "Unknown", 
    "country": "Unknown"
}, inplace=True)
# Checking for numerical or date columns
if 'date_added' in df.columns:
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
# Standardizing column names (lowercase and underscores for consistency)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
# Handle missing values for 'date_added'
df['date_added'] = df['date_added'].fillna(pd.to_datetime("1900-01-01", errors='coerce'))
# Handle missing values for 'rating'
df['rating'] = df['rating'].fillna("Not Rated")
# Handle missing values for 'duration'
df['duration'] = df['duration'].fillna("Unknown Duration")

# -------------------------------------------
# Verify Cleaned Data
# -------------------------------------------
print("\nCleaned Dataset Info:\n")
df.info()


# -------------------------------------------
# Checking Updated Cleaned Data
# -------------------------------------------
print("\n Missing Values After Cleaning:\n", df.isnull().sum())

# -------------------------------------------
# Setting Updated Clean Data Path
# -------------------------------------------
cleaned_file_path = r"E:\Research\PRODIGY_DS_02\PRODIGY_DS_02\Netflix_dataset\cleaned_netflix_titles.csv"
df.to_csv(cleaned_file_path, index=False)
print(f"\n Cleaned dataset saved at: {cleaned_file_path}")
