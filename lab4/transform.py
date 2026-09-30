"""Applying several functions to one list via :func:`map`."""

from collections.abc import Callable, Sequence


def map_functions(
    functions: Sequence[Callable[[int], int]],
    values: Sequence[int],
) -> list[list[int]]:
    """Apply every function to every value using :func:`map`.

    For each function in ``functions`` the whole ``values``
    sequence is mapped, so the result contains one list of
    integers per function, in the same order as ``functions``.
    Both inputs are read-only: the function is pure and never
    mutates its arguments. The implementation is built solely
    from nested :func:`map` calls, without explicit loops.

    Args:
        functions: Functions taking and returning an integer.
        values: The integers to feed into each function.

    Returns:
        A list of per-function result lists; an empty outer
        list for an empty ``functions`` sequence.
    """
    return list(
        map(lambda function: list(map(function, values)), functions)
    )
