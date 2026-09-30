"""Tests for the timing decorator task."""

import time
import unittest

from lab4.timing import timer


class TimerTests(unittest.TestCase):
    """Checks for :func:`timer`."""

    def test_duration_covers_sleep(self) -> None:
        """A function sleeping 0.01s reports at least 0.01s."""

        @timer
        def slow() -> int:
            time.sleep(0.01)
            return 42

        self.assertEqual(slow(), 42)
        self.assertGreaterEqual(slow.last_duration, 0.01)

    def test_duration_is_non_negative_float(self) -> None:
        """A fast function reports a non-negative float."""

        @timer
        def fast(value: int) -> int:
            return value + 1

        fast(1)
        self.assertIsInstance(fast.last_duration, float)
        self.assertGreaterEqual(fast.last_duration, 0.0)

    def test_attribute_exists_before_first_call(self) -> None:
        """The attribute defaults to zero before any call."""

        @timer
        def untouched() -> None:
            return None

        self.assertEqual(untouched.last_duration, 0.0)

    def test_metadata_is_preserved(self) -> None:
        """functools.wraps keeps the original name and docstring."""

        @timer
        def documented() -> str:
            """Original docstring."""
            return "ok"

        self.assertEqual(documented.__name__, "documented")
        self.assertEqual(documented.__doc__, "Original docstring.")


if __name__ == "__main__":
    unittest.main()
