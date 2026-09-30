"""Tests for the factorial task."""

import inspect
import unittest

from lab4.basics import factorial


class FactorialTests(unittest.TestCase):
    """Checks for :func:`factorial`."""

    def test_base_cases(self) -> None:
        """Zero and one factorials are defined as one."""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)

    def test_regular_values(self) -> None:
        """Factorials of small positive integers are correct."""
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_negative_value_rejected(self) -> None:
        """A negative argument raises ValueError."""
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            factorial(-7)

    def test_implemented_with_reduce(self) -> None:
        """The implementation goes through functools.reduce."""
        source = inspect.getsource(factorial)
        self.assertIn("reduce", source)


if __name__ == "__main__":
    unittest.main()
