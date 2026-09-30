"""Right-to-left function composition."""

from collections.abc import Callable
from typing import Any


def compose(*functions: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """Compose functions mathematically, from right to left.

    ``compose(f, g, h)(x)`` equals ``f(g(h(x)))``: the last
    argument is applied to the value first. Calling ``compose``
    with no arguments returns the identity function, so
    ``compose()(x)`` equals ``x``. The original functions are
    never modified; the returned callable accepts any value
    that the composed chain can process.

    Args:
        *functions: Functions of one argument, applied from the
            last one to the first.

    Returns:
        A callable evaluating the whole chain right to left, or
        the identity function when ``functions`` is empty.

    Example:
        >>> compose(str.upper, str.strip)("  hi  ")
        'HI'
    """

    def identity(value: Any) -> Any:
        return value

    if not functions:
        return identity

    def composed(value: Any) -> Any:
        result = value
        for function in reversed(functions):
            result = function(result)
        return result

    return composed
