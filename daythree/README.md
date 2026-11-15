
# Week 9 Class 3 Student Lab
## Control Flow and Functions

### Project Description
This project demonstrates Python control flow and functions using synthetic multi-well pressure observations. It covers decision-making, loops, functions, pressure conversion, filtering and summary calculations.

### Learning Objectives
1. Implement pressure classification using if, elif and else.
2. Use loops to process multiple pressure observations.
3. Create reusable functions.
4. Convert pressure from PSI to kPa.
5. Filter invalid and inactive readings using continue.
6. Calculate average pressure for each eligible well.

### Files in This Project
- student_control_flow_lab.py: Contains the Python implementation.
- well_readings.csv: Contains ten synthetic pressure observations.
- README.md: Provides project information and instructions.

### Pressure Classification
| Pressure (PSI) | Classification |
|---|---|
| None or below 0 | Invalid |
| 3500 and above | High |
| 2500 to 3499 | Normal |
| Below 2500 | Low |

### Results

Total observations: 10

Valid readings: 6

Skipped readings: 4

Average pressure by well:

- WELL-07: 3180.00 PSI
- WELL-08: 2795.00 PSI
- WELL-10: 3497.50 PSI

### Pressure Conversion
The program converts PSI to kPa using:

PSI × 6.8947572932

3150 PSI = 21718.49 kPa

### Skipped Records
The program skips records from inactive sensors and records with invalid pressure values, such as missing or negative readings. This leaves six valid observations and four skipped observations.

### Return Values
A return value is the result a function sends back to the code that called it. The returned value can be stored, displayed or used in another calculation.

### How to Run the Program

1. Install Python 3.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

python student_control_flow_lab.py

### Technologies Used
- Python 3
- Visual Studio Code
- Git and GitHub

### Important Note
All pressure observations and classification thresholds are synthetic classroom examples. They must not be used for actual equipment or field safety decisions.
