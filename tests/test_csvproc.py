"""Tests for the CSV processing task."""

import os
import tempfile
import unittest

from lab4.csvproc import average_column, filter_rows, read_rows


class CsvProcessingTests(unittest.TestCase):
    """Checks for the CSV helpers."""

    def setUp(self) -> None:
        """Create a temporary CSV file with three data rows."""
        handle = tempfile.NamedTemporaryFile(
            "w",
            suffix=".csv",
            delete=False,
            encoding="utf-8",
            newline="",
        )
        with handle:
            handle.write("name,score\n")
            handle.write("alice,90\n")
            handle.write("bob,60\n")
            handle.write("carol,75\n")
        self.path = handle.name

    def tearDown(self) -> None:
        """Remove the temporary CSV file."""
        os.unlink(self.path)

    def test_read_rows_returns_dicts(self) -> None:
        """Every CSV line becomes a dictionary of strings."""
        rows = read_rows(self.path)
        self.assertEqual(len(rows), 3)
        self.assertEqual(
            rows[0],
            {"name": "alice", "score": "90"},
        )

    def test_filter_rows_keeps_matching_rows(self) -> None:
        """filter_rows applies the predicate via filter."""
        rows = read_rows(self.path)
        strong = filter_rows(
            rows,
            lambda row: int(row["score"]) >= 70,
        )
        self.assertEqual(
            [row["name"] for row in strong],
            ["alice", "carol"],
        )

    def test_filter_rows_accepts_everything(self) -> None:
        """A predicate that always passes keeps all rows."""
        rows = read_rows(self.path)
        self.assertEqual(len(filter_rows(rows, lambda row: True)), 3)

    def test_average_column(self) -> None:
        """The mean over score is computed with map and sum."""
        rows = read_rows(self.path)
        self.assertAlmostEqual(average_column(rows, "score"), 75.0)

    def test_empty_rows_rejected(self) -> None:
        """An empty row set raises ValueError."""
        with self.assertRaises(ValueError):
            average_column([], "score")


if __name__ == "__main__":
    unittest.main()
