"""Factorial computed with :func:`functools.reduce`."""

from functools import reduce
from operator import mul


def factorial(n: int) -> int:
    """Return ``n!`` for a non-negative integer ``n``.

    The value is built by :func:`functools.reduce` over the
    numbers ``1 .. n``; no explicit loop is used. By convention
    ``factorial(0) == 1``.

    Args:
        n: The non-negative argument of the factorial.

    Returns:
        The product ``1 * 2 * ... * n`` (equal to ``1`` for
        ``n == 0``).

    Raises:
        ValueError: If ``n`` is negative.
    """
    if n < 0:
        raise ValueError("n must be non-negative, got {!r}".format(n))
    return reduce(mul, range(1, n + 1), 1)
