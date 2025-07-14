# 📊 Electric Vehicle Trade Analysis

This project analyzes global electric vehicle (EV) trade data using Python's data analysis and visualization libraries. The goal is to extract insights on trade trends, country-wise performance, and import-export dynamics through visual exploration and statistical testing.

---

## 📁 Dataset

- **Source**: [Custom Local CSV]  
- **Filename**: `Electric vehicle dataset.csv`
- **Main Columns**:
  - `Country or Area`
  - `Year`
  - `Flow` (Import/Export)
  - `Trade (USD)`
  - `Quantity`
  - `Quantity Name`
  - `Weight (kg)`

---

## 🧹 Step 1: Data Cleaning

- Removed rows with missing `Trade (USD)` values.
- Renamed columns for ease of use:
  - `Trade (USD)` → `Trade_Value_USD`
  - `Country or Area` → `Country`
  - `Weight (kg)` → `Weight_KG`
  - `Quantity Name` → `Quantity_Unit`
  - `Quantity` → `Quantity_Value`

---

## 📊 Step 2: Data Visualization

1. **Top 10 Countries by Trade Value**  
   - Horizontal bar chart using Seaborn.
2. **Yearly Trade Trends**  
   - Line plot showing changes in trade value over years.
3. **Import vs Export Share**  
   - Pie chart representing total trade by flow type.
4. **Distribution of Trade Value**  
   - Histogram with KDE plot.
5. **Top 10 Countries by Average Quantity Traded**  
   - Bar chart showing quantity-wise performance.

---

## 📈 Step 3: Exploratory Data Analysis (EDA)

- **Boxplot**: Visualized the distribution of trade values grouped by `Flow` (Import/Export) on a logarithmic scale.

---

## 🧪 Step 4: Hypothesis Testing

### Objective:
To test if there's a statistically significant difference in trade values between **Imports** and **Exports**.

### Method:
- Applied **log transformation** to normalize skewed values.
- Performed an **Independent T-test** on log-transformed data.

### Output:
- **T-statistic** and **P-value** are printed.
- A conclusion is drawn based on `p < 0.05`.

---

## 🛠️ Libraries Used

- `pandas`  
- `numpy`  
- `matplotlib`  
- `seaborn`  
- `scipy.stats`

---

## 📌 How to Run

1. Clone the repository or download the Python script.
2. Place the CSV file at the defined path.
3. Run the script using:

```bash
python electric_vehicle_analysis.py
