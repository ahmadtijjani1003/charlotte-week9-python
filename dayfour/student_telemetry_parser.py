"""Validated parser for synthetic raw drilling telemetry records."""

import argparse
import csv
from datetime import datetime
from pathlib import Path

PRESSURE_TO_KPA = 6.8947572932


def parse_line(line):
    """Parse one pipe-delimited telemetry row into a cleaned dictionary.

    Raises:
        ValueError: if the row does not meet the input contract.
    """
    fields = [field.strip() for field in line.strip().split("|")]

    if len(fields) != 7:
        raise ValueError(f"expected 7 fields, found {len(fields)}")

    well_id, timestamp, pressure_text, pressure_unit, temperature_text, temperature_unit, status = fields

    if not well_id:
        raise ValueError("well_id must not be blank")

    if not timestamp:
        raise ValueError("timestamp must not be blank")
    try:
        datetime.fromisoformat(timestamp)
    except ValueError:
        raise ValueError("timestamp must be a valid ISO timestamp") from None

    try:
        pressure = float(pressure_text)
    except ValueError:
        raise ValueError("pressure must be numeric") from None

    if pressure < 0:
        raise ValueError("pressure must be non-negative")

    try:
        temperature = float(temperature_text)
    except ValueError:
        raise ValueError("temperature must be numeric") from None

    pressure_unit = pressure_unit.lower()
    temperature_unit = temperature_unit.upper()
    status = status.upper()

    if pressure_unit not in {"psi", "kpa"}:
        raise ValueError(f"unsupported pressure unit: {pressure_unit or '(blank)'}")

    if temperature_unit not in {"F", "C"}:
        raise ValueError(f"unsupported temperature unit: {temperature_unit or '(blank)'}")

    if status not in {"ACTIVE", "OFFLINE"}:
        raise ValueError(f"unsupported status: {status or '(blank)'}")

    pressure_kpa = pressure * PRESSURE_TO_KPA if pressure_unit == "psi" else pressure
    temperature_c = (temperature - 32) * 5 / 9 if temperature_unit == "F" else temperature

    return {
        "well_id": well_id,
        "timestamp": timestamp,
        "pressure_kpa": round(pressure_kpa, 2),
        "temperature_c": round(temperature_c, 2),
        "status": status,
    }


def process_log(source, output):
    """Clean a telemetry log and write valid records to a CSV file.

    Returns (accepted, rejected). Each rejected item is a dictionary containing
    the original source line number, original text, and validation reason.
    """
    accepted = []
    rejected = []

    with open(source, "r", encoding="utf-8") as input_file:
        for line_number, line in enumerate(input_file, start=1):
            stripped = line.strip()

            if not stripped or stripped.startswith("#"):
                continue

            try:
                accepted.append(parse_line(stripped))
            except ValueError as error:
                rejected.append({
                    "line_number": line_number,
                    "line": stripped,
                    "reason": str(error),
                })

    fieldnames = ["well_id", "timestamp", "pressure_kpa", "temperature_c", "status"]
    with open(output, "w", newline="", encoding="utf-8") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(accepted)

    return accepted, rejected


def main():
    parser = argparse.ArgumentParser(description="Validate and clean drilling telemetry records.")
    parser.add_argument("source", nargs="?", default="drilling_telemetry_raw.txt",
                        help="input pipe-delimited telemetry file")
    parser.add_argument("-o", "--output", default="cleaned_telemetry.csv",
                        help="output CSV filename")
    args = parser.parse_args()

    accepted, rejected = process_log(args.source, args.output)

    print(f"Valid records written: {len(accepted)}")
    print(f"Rejected records: {len(rejected)}")
    for item in rejected:
        print(f"Line {item['line_number']}: {item['reason']} | {item['line']}")
    print(f"Cleaned CSV saved to: {args.output}")


if __name__ == "__main__":
    main()
