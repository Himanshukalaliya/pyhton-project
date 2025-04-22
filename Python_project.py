import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
# import warnings

# warnings.filterwarnings('ignore')
# sns.set(style='whitegrid')

# Correct local file path
file_path = "/Users/himanshuyadav/Desktop/python/Electric vehicle dataset.csv"

# Load the dataset
df = pd.read_csv(file_path)

# Preview the data
print("First few rows of the dataset:")
print(df.head())

# Check available columns
print("\nColumns in the dataset:")
print(df.columns)

###1. DATA CLEANING


# Drop rows where 'Trade (USD)' is missing
df_cleaned = df.dropna(subset=['Trade (USD)'])

# Rename columns for convenience
df_cleaned = df_cleaned.rename(columns={
    'Country or Area': 'Country',
    'Trade (USD)': 'Trade_Value_USD',
    'Weight (kg)': 'Weight_KG',
    'Quantity Name': 'Quantity_Unit',
    'Quantity': 'Quantity_Value'
})

# Display cleaned data info
print("\nCleaned dataset info:")
df_cleaned.info()

# Optional: Check for remaining missing values
print("\nMissing values after cleaning:")
print(df_cleaned.isnull().sum())


### 2. Visualizations using Matplotlib and Seaborn

# Top 10 Countries by Total Trade Value
top_countries = df_cleaned.groupby('Country')['Trade_Value_USD'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_countries.values, y=top_countries.index, palette="viridis")
plt.title("Top 10 Countries by Total Trade Value (USD)")
plt.xlabel("Total Trade Value (USD)")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

#Year-wise Trade Trend (All Countries Combined)
yearly_trade = df_cleaned.groupby('Year')['Trade_Value_USD'].sum().reset_index()

plt.figure(figsize=(10, 5))
sns.lineplot(data=yearly_trade, x='Year', y='Trade_Value_USD', marker='o')
plt.title("Total Electric Vehicle Trade Value Over Years")
plt.xlabel("Year")
plt.ylabel("Total Trade Value (USD)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Import vs Export Trade Share (Pie Chart)
flow_data = df_cleaned.groupby('Flow')['Trade_Value_USD'].sum()

plt.figure(figsize=(6, 6))
plt.pie(flow_data, labels=flow_data.index, autopct='%1.1f%%', startangle=140, colors=['#66b3ff', '#ff9999'])
plt.title("Import vs Export Share by Trade Value")
plt.axis('equal')
plt.show()

# Distribution of Trade Value (Histogram)
plt.figure(figsize=(10, 5))
sns.histplot(df_cleaned['Trade_Value_USD'], bins=50, kde=True, color='skyblue')
plt.title("Distribution of Trade Value")
plt.xlabel("Trade Value (USD)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Country vs Average Quantity Traded
avg_quantity = df_cleaned.groupby('Country')['Quantity_Value'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=avg_quantity.values, y=avg_quantity.index, palette="magma")
plt.title("Top 10 Countries by Avg Quantity Traded")
plt.xlabel("Average Quantity")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

### 3. Exploratory Data Analysis (EDA)

# Boxplot of Trade Value by Flow (Import vs Export)
plt.figure(figsize=(8, 5))
sns.boxplot(data=df_cleaned, x='Flow', y='Trade_Value_USD', palette='Set2')
plt.title('Distribution of Trade Value by Flow Type')
plt.ylabel('Trade Value (USD)')
plt.xlabel('Flow Type')
plt.yscale('log')  # Log scale for better visualization
plt.tight_layout()
plt.show()


### 4. Hypothesis Testing: Compare Import vs Export Trade Values

# Extract trade values for Import and Export
import_values = df_cleaned[df_cleaned['Flow'] == 'Import']['Trade_Value_USD']
export_values = df_cleaned[df_cleaned['Flow'] == 'Export']['Trade_Value_USD']
# Apply log transformation to reduce skewness 
import_log = np.log1p(import_values)
export_log = np.log1p(export_values)
# Perform independent t-test
t_stat, p_val = stats.ttest_ind(import_log, export_log, nan_policy='omit')
# Print results
print(f'T-statistic: {t_stat:.4f}, P-value: {p_val:.4f}')
if p_val < 0.05:
    print('Result: Statistically significant difference in trade values between Imports and Exports.')
else:
    print('Result: No statistically significant difference in trade values between Imports and Exports.')