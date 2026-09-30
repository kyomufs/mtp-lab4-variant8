"""Demo entry point: run ``python -m lab4``."""

import os
import tempfile
import time
from collections.abc import Callable

from lab4.basics import factorial
from lab4.composition import compose
from lab4.csvproc import average_column, filter_rows, read_rows
from lab4.timing import timer
from lab4.transform import map_functions


def main() -> None:
    """Print results of every variant task."""
    print("Medium tasks")

    print("factorial(10) ->", factorial(10))
    try:
        factorial(-1)
    except ValueError as error:
        print("factorial(-1) -> ValueError:", error)

    @timer
    def slow_square(value: int) -> int:
        time.sleep(0.01)
        return value * value

    slow_square(7)
    print("slow_square(7) ->", slow_square(7))
    print(
        "slow_square.last_duration >= 0.01 ->",
        slow_square.last_duration >= 0.01,
    )

    values = [1, 2, 3]
    functions: list[Callable[[int], int]] = [
        lambda x: x + 1,
        lambda x: x * 2,
    ]
    print(
        "map_functions([+1, *2], [1, 2, 3]) ->",
        map_functions(functions, values),
    )

    print("Advanced tasks")

    def inc(value: int) -> int:
        return value + 1

    def square(value: int) -> int:
        return value * value

    print("compose(square, inc)(5) ->", compose(square, inc)(5))
    print("compose()(42) ->", compose()(42))
    shout = compose(str.upper, str.strip)
    print('compose(str.upper, str.strip)("  hi  ") ->', shout("  hi  "))

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
    try:
        rows = read_rows(handle.name)
        print("read_rows ->", rows)
        strong = filter_rows(
            rows,
            lambda row: int(row["score"]) >= 70,
        )
        print(
            "filter(score >= 70) ->",
            [row["name"] for row in strong],
        )
        print("average_column(score) ->", average_column(rows, "score"))
    finally:
        os.unlink(handle.name)


if __name__ == "__main__":
    main()
