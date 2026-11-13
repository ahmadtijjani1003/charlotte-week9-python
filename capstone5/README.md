# Drilling Telemetry Data Processing System

## Project description
This Week 9 Class 5 capstone reads synthetic drilling sensor records, validates each record, converts pressure to kPa and temperature to Celsius, logs rejected records, calculates average ACTIVE pressure by well, and writes three CSV files.

## Requirements
- Python 3.8 or later
- Python standard library only (`csv`, `pathlib`, `sys`, `collections`, `unittest`, etc.)
- No Pandas or NumPy

## Project structure
```text
telemetry_capstone_submission/
├── data/
│   └── drilling_telemetry_capstone.txt
├── src/
│   └── telemetry_capstone.py
├── tests/
│   └── test_telemetry_capstone.py
├── outputs/
├── README.md
└── .gitignore
```

## Run the program
From the project root directory:

```bash
python src/telemetry_capstone.py data/drilling_telemetry_capstone.txt outputs
```

The program creates:
- `outputs/cleaned_telemetry.csv`
- `outputs/rejected_records.csv`
- `outputs/well_summary.csv`

## Run the tests
From the project root directory:

```bash
python -m unittest discover -s tests -v
```

## Validation and conversion rules
- Every nonblank record must contain exactly seven pipe-separated fields.
- Timestamp and well ID cannot be blank.
- Pressure accepts `psi` and `kPa`; negative pressure is rejected.
- Temperature accepts `F` and `C`.
- Measurements must be numeric.
- Status accepts `ACTIVE` and `INACTIVE`.
- Converted values are rounded to two decimal places.
- Rejected records retain their original 1-based line number and raw text.
- Only ACTIVE accepted records contribute to well averages.
- Well summaries are sorted by well ID.

## Results for the supplied synthetic dataset
The supplied dataset contains 20 nonblank lines. Expected processing results:
- 13 accepted records
- 7 rejected records (source lines 7, 8, 9, 12, 14, 18 and 20)
- 5 well summary rows

## Safety note
All records are synthetic and intended only for education. Do not use these outputs to make operational drilling decisions.
