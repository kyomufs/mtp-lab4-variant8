"""CSV reading, filtering and averaging with map/filter."""

import csv
from collections.abc import Callable, Sequence


def read_rows(path: str) -> list[dict[str, str]]:
    """Read a CSV file with a header row into dictionaries.

    The first row provides the column names; every following
    row becomes one ``dict`` mapping a column name to its raw
    string value.

    Args:
        path: Path to the CSV file to read.

    Returns:
        One dictionary per data row, in file order; an empty
        list for a file that has only the header.
    """
    with open(path, newline="", encoding="utf-8") as source:
        return list(csv.DictReader(source))


def filter_rows(
    rows: Sequence[dict[str, str]],
    predicate: Callable[[dict[str, str]], bool],
) -> list[dict[str, str]]:
    """Keep the rows accepted by ``predicate``.

    The selection is delegated to the builtin :func:`filter`,
    so the input sequence is only read, never modified.

    Args:
        rows: Row dictionaries as returned by :func:`read_rows`.
        predicate: Predicate deciding whether a row is kept.

    Returns:
        The accepted rows in their original order.
    """
    return list(filter(predicate, rows))


def average_column(
    rows: Sequence[dict[str, str]], column: str
) -> float:
    """Return the arithmetic mean of a numeric column.

    Every value is converted with :func:`map` and the total is
    taken with the builtin :func:`sum`; the mean is the total
    divided by the number of rows.

    Args:
        rows: Non-empty row dictionaries.
        column: Name of the column to average.

    Returns:
        The mean of the column values as ``float``.

    Raises:
        ValueError: If ``rows`` is empty — there is nothing to
            average.
        KeyError: If ``column`` is missing in a row.
    """
    if not rows:
        raise ValueError("rows must not be empty")
    values = map(lambda row: float(row[column]), rows)
    return sum(values) / len(rows)
