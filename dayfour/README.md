# Week 9 – Class 4: Raw Drilling Telemetry Parser

## Overview
This project reads synthetic pipe-delimited drilling telemetry records, validates the seven input fields, converts pressure and temperature units, and writes valid records to a cleaned CSV file. Invalid records are reported with their original source line numbers and reasons.

## Requirements
- Python 3.8 or later
- No third-party packages are required

## Files
- `student_telemetry_parser.py` – parser and log-processing program
- `test_student_telemetry_parser.py` – automated unit tests
- `drilling_telemetry_raw.txt` – synthetic practice input
- `cleaned_telemetry.csv` – generated output

## Input format
Each data row must contain seven pipe-separated fields:

`well_id|timestamp|pressure|pressure_unit|temperature|temperature_unit|status`

Header/comment lines beginning with `#` and blank lines are skipped.

Validation rules:
- Exactly seven fields
- Nonblank well ID
- ISO timestamp accepted by `datetime.fromisoformat`
- Numeric, non-negative pressure
- Numeric temperature
- Pressure unit: `psi` or `kPa`
- Temperature unit: `F` or `C`
- Status: `ACTIVE` or `OFFLINE` (case-insensitive)

## Unit conversions
- `psi` to `kPa`: multiply by `6.8947572932`
- `F` to `C`: `(F - 32) * 5 / 9`
- Converted values are rounded to two decimal places.
- Values already in kPa or C are retained and rounded to two decimals.

## Run the program
From this folder, run:

```bash
python student_telemetry_parser.py
```

Or specify input and output files:

```bash
python student_telemetry_parser.py drilling_telemetry_raw.txt -o cleaned_telemetry.csv
```

The program prints the number of valid and rejected rows and lists each rejected row's source line number and reason.

## Run tests
```bash
python -m unittest discover -v
```

The test suite covers successful psi/F conversion, successful kPa/C handling, invalid numeric pressure, missing fields, unsupported units, negative pressure, invalid status, and line-number reporting.

## Example test results
When all tests pass, unittest reports `OK` and the number of tests run. Record the actual result from your own terminal run here before submission.

## GitHub submission
```bash
git switch -c feature/class-04
git add .
git commit -m "feat: add validated telemetry parser and tests"
git push -u origin feature/class-04
```

Then open a pull request from `feature/class-04` to `main`. In the PR description, explain what the parser does, how to run it, and the actual test results. Include the PR link when submitting.

## Data note
The included input file contains synthetic examples for practice only. Replace it with the instructor-supplied raw log if one is provided. Do not invent or alter measurements from the official dataset.
