"""Week 9 Class 5: Drilling Telemetry Data Processing System.

Uses only Python's standard library.
"""
import csv
import sys
from collections import defaultdict
from pathlib import Path

PSI_TO_KPA = 6.8947572932

CLEAN_FIELDS = [
    "timestamp", "well_id", "pressure_kpa", "temperature_c", "status"
]
REJECTED_FIELDS = ["line_number", "reason", "raw_record"]
SUMMARY_FIELDS = ["well_id", "active_readings", "avg_pressure_kpa"]


def convert_pressure(value, unit):
    """Return pressure in kPa; reject unsupported units and negative values."""
    unit = unit.strip().upper()
    number = float(value)

    if number < 0:
        raise ValueError("Negative pressure")
    if unit == "PSI":
        return number * PSI_TO_KPA
    if unit == "KPA":
        return number
    raise ValueError(f"Unsupported pressure unit: {unit}")


def convert_temperature(value, unit):
    """Return temperature in degrees Celsius; reject unsupported units."""
    unit = unit.strip().upper()
    number = float(value)

    if unit == "F":
        return (number - 32) * 5 / 9
    if unit == "C":
        return number
    raise ValueError(f"Unsupported temperature unit: {unit}")


def parse_record(raw_line):
    """Validate, convert and return one normalized telemetry record."""
    fields = [field.strip() for field in raw_line.split("|")]
    if len(fields) != 7:
        raise ValueError(f"Expected 7 fields, found {len(fields)}")

    timestamp, well_id, pressure_value, pressure_unit, temperature_value, temperature_unit, status = fields

    if not timestamp:
        raise ValueError("Blank timestamp")
    if not well_id:
        raise ValueError("Blank well_id")

    try:
        pressure = float(pressure_value)
    except ValueError:
        raise ValueError("Nonnumeric pressure") from None

    try:
        temperature = float(temperature_value)
    except ValueError:
        raise ValueError("Nonnumeric temperature") from None

    pressure_kpa = convert_pressure(pressure, pressure_unit)
    temperature_c = convert_temperature(temperature, temperature_unit)

    normalized_status = status.upper()
    if normalized_status not in ("ACTIVE", "INACTIVE"):
        raise ValueError(f"Invalid status: {status}")

    return {
        "timestamp": timestamp,
        "well_id": well_id,
        "pressure_kpa": round(pressure_kpa, 2),
        "temperature_c": round(temperature_c, 2),
        "status": normalized_status,
    }


def process_lines(lines):
    """Return accepted and rejected records, retaining original line numbers."""
    accepted_records = []
    rejected_records = []

    for line_number, raw_line in enumerate(lines, start=1):
        if not raw_line.strip():
            continue

        try:
            accepted_records.append(parse_record(raw_line))
        except ValueError as error:
            rejected_records.append({
                "line_number": line_number,
                "reason": str(error),
                "raw_record": raw_line.rstrip("\r\n"),
            })

    return accepted_records, rejected_records


def summarize_by_well(records):
    """Average ACTIVE pressure readings per well, sorted by well ID."""
    pressures_by_well = defaultdict(list)

    for record in records:
        if record["status"] == "ACTIVE":
            pressures_by_well[record["well_id"]].append(
                record["pressure_kpa"]
            )

    summary = []
    for well_id in sorted(pressures_by_well):
        readings = pressures_by_well[well_id]
        summary.append({
            "well_id": well_id,
            "active_readings": len(readings),
            "avg_pressure_kpa": round(sum(readings) / len(readings), 2),
        })

    return summary


def write_csv(path, fieldnames, records):
    """Write records to a CSV file, including its required header row."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)


def run(input_path, output_dir):
    """Process an input file and generate the three required CSV files."""
    input_path = Path(input_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    with input_path.open("r", encoding="utf-8") as input_file:
        accepted, rejected = process_lines(input_file)

    summary = summarize_by_well(accepted)

    write_csv(output_dir / "cleaned_telemetry.csv", CLEAN_FIELDS, accepted)
    write_csv(output_dir / "rejected_records.csv", REJECTED_FIELDS, rejected)
    write_csv(output_dir / "well_summary.csv", SUMMARY_FIELDS, summary)

    return accepted, rejected, summary


def main():
    """Read the two command-line arguments and run the processing pipeline."""
    if len(sys.argv) != 3:
        print(
            "Usage: python src/telemetry_capstone.py INPUT_FILE OUTPUT_FOLDER",
            file=sys.stderr,
        )
        return 2

    input_path, output_dir = sys.argv[1], sys.argv[2]
    try:
        accepted, rejected, summary = run(input_path, output_dir)
    except OSError as error:
        print(f"File or folder error: {error}", file=sys.stderr)
        return 1

    print(f"Processing complete: {len(accepted)} accepted, "
          f"{len(rejected)} rejected.")
    print(f"Well summaries created: {len(summary)}")
    print(f"CSV files saved in: {Path(output_dir)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
