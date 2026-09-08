# Week 3 – Python & Data Wrangling (Pandas)

Practice solution for the Data Analyst Course, Week 3 assignment.

## Assignment

Clean a messy dataset in Pandas — handle missing values, filter rows, create new columns.

## Dataset

`dataset.csv` — a fitness-log dataset (32 rows) with columns:
`Duration, Date, Pulse, Maxpulse, Calories`

Issues found in the raw data:
- 1 duplicate row
- 1 missing `Date`, 2 missing `Calories` values
- Inconsistent `Date` formatting — some values wrapped in quotes (`'2020/12/01'`), one stored as a raw integer (`20201226`)
- 1 outlier row (`Duration = 450`, far outside the normal range of the rest of the data)

## What the script does

1. **Load** the CSV with Pandas
2. **Clean `Date`** — strips stray quotes, reformats the integer-style date, converts to real `datetime`
3. **Handle missing values** — interpolates the missing date from its neighbours, fills missing `Calories` with the column mean
4. **Remove duplicates** — drops the exact duplicate row
5. **Filter rows** — removes the `Duration = 450` outlier
6. **Create new columns**:
   - `Calories_per_Minute` = Calories / Duration
   - `Pulse_Range` = Maxpulse − Pulse
   - `Intensity` = Low / Moderate / High, binned from `Pulse`
7. Saves the result to `cleaned_dataset.csv`

## How to Run

```bash
pip install -r requirements.txt
python week3_solutions.py
```

## Project Structure

```
.
├── dataset.csv
├── week3_solutions.py
├── cleaned_dataset.csv   (generated after running the script)
├── requirements.txt
└── README.md
```
