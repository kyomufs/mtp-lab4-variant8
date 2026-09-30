"""Tests for the function composition task."""

import unittest

from lab4.composition import compose


def _inc(value: int) -> int:
    """Return ``value + 1``."""
    return value + 1


def _square(value: int) -> int:
    """Return ``value * value``."""
    return value * value


class ComposeTests(unittest.TestCase):
    """Checks for :func:`compose`."""

    def test_numbers_applied_right_to_left(self) -> None:
        """compose(f, g, h)(x) equals f(g(h(x))) for numbers."""
        result = compose(_inc, _square, _inc)
        self.assertEqual(result(2), _inc(_square(_inc(2))))
        self.assertEqual(result(2), 10)

    def test_single_function(self) -> None:
        """A one-function composition is that function."""
        self.assertEqual(compose(_square)(5), 25)

    def test_identity_for_empty_composition(self) -> None:
        """compose() with no arguments is the identity."""
        self.assertEqual(compose()(42), 42)
        self.assertEqual(compose()("text"), "text")

    def test_strings(self) -> None:
        """Composition works on strings as well."""
        shout = compose(str.upper, str.strip)
        self.assertEqual(shout("  hi  "), "HI")

    def test_chain_of_string_functions(self) -> None:
        """Three-function chain matches the explicit nesting."""
        joiner = compose(",".join, sorted, str.split)
        self.assertEqual(
            joiner("c b a"),
            ",".join(sorted(str.split("c b a"))),
        )


if __name__ == "__main__":
    unittest.main()
