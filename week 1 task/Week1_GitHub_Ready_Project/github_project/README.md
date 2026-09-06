# Week 1 — Excel & Data Cleaning (Data Analyst Course, Codec Technologies)

This repo contains my completed Week 1 practice questions and course project
for the AICTE & ICAC-approved Data Analyst internship program.

## Contents

| File | Description |
|---|---|
| `Week1_Excel_DataCleaning_Project.xlsx` | Full workbook with all tasks completed (see sheets below) |
| `data/raw_data.csv` | Raw dataset export (contains duplicates & missing values, on purpose) |
| `data/cleaned_data.csv` | Cleaned dataset after dedup + missing-value handling |

## Workbook sheets

- **README** — overview of what's where
- **Raw_Data** — the messy source data (192 rows, 12 duplicates, several blanks)
- **Cleaned_Data** — deduplicated + missing values filled, with the **Top 10 Sales**
  conditional formatting rule applied to the Sales column
- **Analysis** — pivot-style summaries and statistics, all built with live formulas
  (`SUMIF`, `AVERAGE`, `MEDIAN`, `MODE`, `COUNTA`)
- **Charts** — Category Revenue (bar), Region-wise Sales (bar), Yearly Sales Trend
  (line), Department-wise Revenue (bar)

## Practice Questions — Week 1 (Excel & Data Cleaning)

1. **Remove duplicates and handle missing values** → `Raw_Data` → `Cleaned_Data`
   (12 duplicate rows dropped; missing Customer Name filled with "Unknown Customer";
   missing Quantity/Sales filled with the column median)
2. **Pivot Table showing region-wise sales** → `Analysis` sheet, Task 2 table + chart
3. **Mean, median, mode using Excel formulas** → `Analysis` sheet, Task 3 table
4. **Conditional formatting to highlight top 10 sales** → `Cleaned_Data` sheet,
   Sales column (red highlight, Excel "Top 10" rule)
5. **Bar chart showing category-wise revenue** → `Charts` sheet

## Course Project — Pivot Table Dashboard (Sales Performance)

- Total Revenue
- Sales by Category
- Yearly Sales Trends
- Department-wise Revenue

All four are on the `Analysis` sheet with supporting charts on the `Charts` sheet.

## Note on the dataset

The course PDF links to a GitHub-hosted Global Superstore 2016 workbook. This
environment has no live network access to download that file, so a synthetic
dataset with the identical structure (Order ID, Order Date, Customer, Region,
Category, Sub-Category, Department, Quantity, Sales, Discount, Profit) was
generated to complete every task. Drop the real Superstore file into
`data/raw_data.csv` (matching column names) and every formula and chart in the
workbook recalculates automatically.

## Tools used

Microsoft Excel / LibreOffice Calc, `openpyxl`, `pandas`.
