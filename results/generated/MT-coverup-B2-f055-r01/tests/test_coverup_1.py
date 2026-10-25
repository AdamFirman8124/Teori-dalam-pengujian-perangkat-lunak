# file: project/f055/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5], [5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5], [5, 6], [5, 7]]}

import pytest

from f055 import fib


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (7, 13),
    ],
)
def test_fib_base_and_recursive_cases(n: int, expected: int) -> None:
    assert fib(n) == expected
