"""Unit tests for student_telemetry_parser.py."""

import csv
import tempfile
import unittest
from pathlib import Path

from student_telemetry_parser import parse_line, process_log


class TestParseLine(unittest.TestCase):

    def test_successful_psi_and_fahrenheit(self):
        result = parse_line("WELL-01|2026-11-15T10:30:00|100|psi|212|F|ACTIVE")
        self.assertEqual(result["well_id"], "WELL-01")
        self.assertEqual(result["pressure_kpa"], 689.48)
        self.assertEqual(result["temperature_c"], 100.0)
        self.assertEqual(result["status"], "ACTIVE")

    def test_successful_kpa_and_celsius(self):
        result = parse_line("WELL-02|2026-11-15T11:00:00|250|kPa|35|C|offline")
        self.assertEqual(result["pressure_kpa"], 250.0)
        self.assertEqual(result["temperature_c"], 35.0)
        self.assertEqual(result["status"], "OFFLINE")

    def test_bad_numeric_pressure(self):
        with self.assertRaisesRegex(ValueError, "pressure must be numeric"):
            parse_line("WELL-03|2026-11-15T11:00:00|high|psi|30|C|ACTIVE")

    def test_missing_field(self):
        with self.assertRaisesRegex(ValueError, "expected 7 fields"):
            parse_line("WELL-04|2026-11-15T11:00:00|100|psi|30|C")

    def test_unsupported_pressure_unit(self):
        with self.assertRaisesRegex(ValueError, "unsupported pressure unit"):
            parse_line("WELL-05|2026-11-15T11:00:00|100|bar|30|C|ACTIVE")

    def test_negative_pressure_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "non-negative"):
            parse_line("WELL-06|2026-11-15T11:00:00|-1|psi|30|C|ACTIVE")

    def test_invalid_status_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "unsupported status"):
            parse_line("WELL-07|2026-11-15T11:00:00|100|psi|30|C|RUNNING")

    def test_process_log_skips_comments_and_reports_line_numbers(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source = Path(temp_dir) / "input.txt"
            output = Path(temp_dir) / "output.csv"
            source.write_text(
                "# sample log\n"
                "\n"
                "WELL-01|2026-11-15T10:30:00|100|psi|212|F|ACTIVE\n"
                "WELL-02|2026-11-15T11:00:00|bad|psi|30|C|ACTIVE\n",
                encoding="utf-8",
            )

            accepted, rejected = process_log(source, output)

            self.assertEqual(len(accepted), 1)
            self.assertEqual(len(rejected), 1)
            self.assertEqual(rejected[0]["line_number"], 4)

            with output.open(newline="", encoding="utf-8") as csv_file:
                reader = csv.DictReader(csv_file)
                self.assertEqual(
                    reader.fieldnames,
                    ["well_id", "timestamp", "pressure_kpa", "temperature_c", "status"],
                )
                rows = list(reader)
                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0]["well_id"], "WELL-01")


if __name__ == "__main__":
    unittest.main()
