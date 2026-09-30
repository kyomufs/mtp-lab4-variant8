"""Decorator that measures the execution time of a function."""

import functools
import time
from collections.abc import Callable
from typing import TypeVar

ResultT = TypeVar("ResultT")


def timer(func: Callable[..., ResultT]) -> Callable[..., ResultT]:
    """Measure the duration of every call of ``func``.

    The elapsed wall-clock time in seconds (measured with
    :func:`time.perf_counter`) is stored after each call in the
    ``last_duration`` attribute of the decorated function, so the
    measurement itself can be checked by tests. The attribute
    exists even before the first call and initially equals
    ``0.0``. The original arguments, the return value and the
    metadata (:func:`functools.wraps`) are passed through
    unchanged.

    Args:
        func: The function to wrap.

    Returns:
        A wrapper that runs ``func`` and records its duration
        in ``wrapper.last_duration``.
    """

    @functools.wraps(func)
    def wrapper(*args: object, **kwargs: object) -> ResultT:
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            wrapper.last_duration = time.perf_counter() - start

    wrapper.last_duration = 0.0
    return wrapper
