"""Tests for the map-over-functions task."""

import ast
import inspect
import unittest

from lab4.transform import map_functions


class MapFunctionsTests(unittest.TestCase):
    """Checks for :func:`map_functions`."""

    def test_each_function_mapped_over_values(self) -> None:
        """Every function is applied to the whole value list."""
        result = map_functions(
            [lambda x: x + 1, lambda x: x * 2],
            [1, 2, 3],
        )
        self.assertEqual(result, [[2, 3, 4], [2, 4, 6]])

    def test_empty_function_list(self) -> None:
        """No functions means no result rows."""
        self.assertEqual(map_functions([], [1, 2]), [])

    def test_empty_value_list(self) -> None:
        """No values means empty rows for every function."""
        result = map_functions([lambda x: x + 1, lambda x: x], [])
        self.assertEqual(result, [[], []])

    def test_inputs_are_not_modified(self) -> None:
        """The original value list stays intact."""
        values = [1, 2, 3]
        map_functions([lambda x: -x], values)
        self.assertEqual(values, [1, 2, 3])

    def test_implemented_with_map(self) -> None:
        """The body is built from map calls, not explicit loops."""
        tree = ast.parse(inspect.getsource(map_functions))
        loops = [
            node
            for node in ast.walk(tree)
            if isinstance(node, (ast.For, ast.While, ast.AsyncFor))
        ]
        self.assertEqual(loops, [])
        names = {
            node.id
            for node in ast.walk(tree)
            if isinstance(node, ast.Name)
        }
        self.assertIn("map", names)


if __name__ == "__main__":
    unittest.main()
