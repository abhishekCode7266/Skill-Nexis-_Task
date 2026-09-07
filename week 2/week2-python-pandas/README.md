# Week 2 – Python for Data Analysis (Pandas Practice)

Practice solutions for the Data Analyst Course, Week 2 (Python/Pandas).

## Questions Covered

1. Load a CSV/Excel file using Pandas and display basic info
2. Handle missing values and duplicates using Pandas
3. Group data by category and find total revenue
4. Sort data by multiple columns using Python
5. Create a correlation matrix for numerical columns

## Dataset

`dataset.xlsx` — 200 order records with columns:
`order_id, customer_name, order_date, category, sub_category, product_name, quantity, unit_price, total_price, region`

## How to Run

```bash
pip install -r requirements.txt
python week2_solutions.py
```

## Sample Results

**Total revenue by category**

| Category | Revenue |
|---|---|
| Furniture | 714,399 |
| Grocery | 672,147 |
| Electronics | 549,302 |
| Clothing | 484,259 |

**Correlation matrix (numeric columns)**

`quantity` and `unit_price` each show a moderate positive correlation (~0.65–0.67) with `total_price`, since `total_price = quantity × unit_price`. `order_id` shows no meaningful correlation with any other column, as expected for an identifier field.

## Project Structure

```
.
├── dataset.xlsx
├── week2_solutions.py
├── requirements.txt
└── README.md
```
